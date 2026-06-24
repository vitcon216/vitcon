class QuizApp {
    constructor() {
        this.database = null;
        this.currentMode = null; // 'revision' | 'mock'
        this.questions = [];
        this.currentQuestionIndex = 0;
        this.userAnswers = {}; // { questionIndex: selectedOptionString }
        this.timerInterval = null;
        this.timeLeft = 3600; // 60 mins default for mock

        this.init();
    }

    async init() {
        try {
            const response = await fetch('database.json');
            this.database = await response.json();
            this.updateChapterCounts();
            if (typeof feather !== 'undefined') feather.replace();
        } catch (error) {
            console.error("Failed to load database.json", error);
            alert("Lỗi tải dữ liệu. Hãy đảm bảo bạn đang chạy qua một web server (VD: Live Server).");
        }
    }

    updateChapterCounts() {
        if (!this.database || !this.database.revision) return;
        let counts = {1: 0, 2: 0, 3: 0, 4: 0};
        let total = 0;
        this.database.revision.forEach(q => {
            if (counts[q.chapter] !== undefined) {
                counts[q.chapter]++;
                total++;
            }
        });
        
        const select = document.getElementById('chapter-select');
        if (select && select.options.length >= 5) {
            select.options[0].text = `Tất cả các chương (${total} câu)`;
            select.options[1].text = `Chương 1: Tổng quan (${counts[1]} câu)`;
            select.options[2].text = `Chương 2: Các kiến trúc cơ bản (${counts[2]} câu)`;
            select.options[3].text = `Chương 3: Thiết kế kiến trúc phần mềm (${counts[3]} câu)`;
            select.options[4].text = `Chương 4: Thiết kế mẫu (Design Patterns) (${counts[4]} câu)`;
        }
    }

    // --- Navigation ---
    switchScreen(screenId) {
        document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
        document.getElementById(screenId).classList.add('active');
        if (typeof feather !== 'undefined') feather.replace();
    }

    showHome() {
        this.resetState();
        this.switchScreen('home-screen');
    }

    showRevisionSetup() {
        this.switchScreen('revision-setup-screen');
    }

    // --- Start Modes ---
    startRevision() {
        if (!this.database) return;
        
        const selectVal = document.getElementById('chapter-select').value;
        let selectedChaps = [];
        if (selectVal === 'all') {
            selectedChaps = [1, 2, 3, 4];
        } else {
            selectedChaps = [parseInt(selectVal)];
        }

        if (selectedChaps.length === 0) {
            alert("Vui lòng chọn ít nhất 1 chương để ôn tập.");
            return;
        }

        this.currentMode = 'revision';
        this.questions = this.database.revision.filter(q => selectedChaps.includes(q.chapter));
        
        // Xáo trộn câu hỏi
        this.questions = this.questions.sort(() => Math.random() - 0.5);

        if (this.questions.length === 0) {
            alert("Không tìm thấy câu hỏi nào cho các chương đã chọn.");
            return;
        }

        document.getElementById('quiz-timer-container').style.display = 'none';
        this.startQuizSession();
    }

    startMockTest() {
        if (!this.database) return;
        this.currentMode = 'mock';
        
        // Gộp tất cả câu hỏi từ database.revision và database.mockTest
        let allPool = [...this.database.revision, ...this.database.mockTest];
        
        // Loại bỏ câu hỏi trùng lặp dựa trên nội dung text
        let uniqueQuestions = [];
        let seenTexts = new Set();
        for (let q of allPool) {
            let cleanText = q.question.toLowerCase().replace(/\s+/g, '');
            if (!seenTexts.has(cleanText)) {
                seenTexts.add(cleanText);
                uniqueQuestions.push(q);
            }
        }

        // Xáo trộn và lấy ngẫu nhiên 40 câu
        uniqueQuestions = uniqueQuestions.sort(() => Math.random() - 0.5);
        this.questions = uniqueQuestions.slice(0, 40);

        if (this.questions.length === 0) {
            alert("Không có dữ liệu đề thi thử."); return;
        }

        document.getElementById('quiz-timer-container').style.display = 'flex';
        this.timeLeft = 60 * 60; // 60 minutes
        this.startTimer();
        this.startQuizSession();
    }

    // --- Quiz Logic ---
    startQuizSession() {
        this.currentQuestionIndex = 0;
        this.userAnswers = {};
        this.renderDots();
        this.renderQuestion();
        this.switchScreen('quiz-screen');
    }

    renderDots() {
        const container = document.getElementById('question-dots');
        container.innerHTML = '';
        this.questions.forEach((_, idx) => {
            const dot = document.createElement('div');
            dot.className = 'dot';
            dot.onclick = () => {
                this.currentQuestionIndex = idx;
                this.renderQuestion();
            };
            container.appendChild(dot);
        });
    }

    updateDots() {
        const dots = document.querySelectorAll('.dot');
        dots.forEach((dot, idx) => {
            dot.className = 'dot';
            const userAns = this.userAnswers[idx];
            if (userAns) {
                dot.classList.add('answered');
                // Trong chế độ ôn tập, đổi màu dot thành xanh/đỏ
                if (this.currentMode === 'revision') {
                    const q = this.questions[idx];
                    if (userAns === q.correctAnswer) {
                        dot.classList.add('correct');
                    } else {
                        dot.classList.add('wrong');
                    }
                }
            }
            if (idx === this.currentQuestionIndex) dot.classList.add('active');
        });
    }

    // Hàm tạo giải thích tự động so sánh
    generateSmartExplanation(q, userAns) {
        if (q.detailed_explanation) {
            return q.detailed_explanation;
        }

        let correctText = "";
        let wrongText = "";
        
        q.options.forEach(opt => {
            if (opt.startsWith(q.correctAnswer + ".")) {
                correctText = opt.substring(2).trim();
            }
            if (userAns && userAns !== q.correctAnswer && opt.startsWith(userAns + ".")) {
                wrongText = opt.substring(2).trim();
            }
        });

        let explanation = `<div style="margin-bottom: 8px;"><strong>Giải thích:</strong> ${q.explanation && q.explanation.length > 5 ? q.explanation : correctText}</div>`;
        
        q.options.forEach(opt => {
            let letter = opt.substring(0, 1);
            let text = opt.substring(2).trim();
            if (letter !== q.correctAnswer) {
                let reason = 'Phương án này không phản ánh đầy đủ bản chất hoặc không phải là đáp án đúng trong ngữ cảnh này.';
                if (userAns && letter === userAns) {
                    reason = 'Phương án bạn chọn không chính xác trong ngữ cảnh này.';
                }
                explanation += `<div style="margin-top: 4px;">- <strong>Loại ${letter}:</strong> ${text}. ${reason}</div>`;
            }
        });

        return explanation;
    }

    renderQuestion() {
        const q = this.questions[this.currentQuestionIndex];
        const container = document.getElementById('question-container');
        
        // Progress
        document.getElementById('quiz-progress-text').innerText = `Câu ${this.currentQuestionIndex + 1}/${this.questions.length}`;
        document.getElementById('quiz-progress-fill').style.width = `${((this.currentQuestionIndex + 1) / this.questions.length) * 100}%`;

        const userAns = this.userAnswers[this.currentQuestionIndex];
        const showResultInline = this.currentMode === 'revision' && userAns; // Chỉ hiện đáp án inline khi ôn tập & đã chọn

        // Generate Options HTML
        let optionsHtml = '';
        q.options.forEach(opt => {
            const optLetter = opt.substring(0, 1);
            let optClass = 'option-item';
            
            if (showResultInline) {
                if (optLetter === q.correctAnswer) {
                    optClass += ' selected-correct'; // Đáp án đúng -> xanh
                } else if (optLetter === userAns && userAns !== q.correctAnswer) {
                    optClass += ' selected-wrong'; // Đáp án sai mà user chọn -> đỏ
                }
            } else {
                if (userAns === optLetter) {
                    optClass += ' selected';
                }
            }

            // Nếu đang ôn tập và đã trả lời, không cho click nữa
            const clickHandler = showResultInline ? '' : `onclick="app.selectOption('${optLetter}')"`;

            optionsHtml += `
                <div class="${optClass}" ${clickHandler}>
                    ${opt}
                </div>
            `;
        });

        const metaText = q.chapter ? `<small style="color: var(--text-secondary); margin-bottom: 0.5rem; display: block;">Chương ${q.chapter} - ${q.topic}</small>` : '';

        let explanationHtml = '';
        if (showResultInline && q.correctAnswer) {
            const smartExpl = this.generateSmartExplanation(q, userAns);
            explanationHtml = `
                <div class="explanation-box fade-in-up mt-4">
                    <h4 style="display: flex; align-items: center; gap: 5px; margin-bottom: 10px;">
                        <i data-feather="book-open" style="width: 16px; height: 16px;"></i> Phân tích đáp án:
                    </h4>
                    <div style="font-size: 0.95rem; line-height: 1.6;">${smartExpl}</div>
                </div>
            `;
        } else if (showResultInline && !q.correctAnswer) {
            explanationHtml = `
                <div class="explanation-box fade-in-up mt-4" style="border-left-color: var(--warning);">
                    <h4><i data-feather="alert-circle" style="width: 14px; height: 14px;"></i> Không có đáp án</h4>
                    <p>Câu hỏi này hiện chưa có đáp án trong hệ thống.</p>
                </div>
            `;
        }

        container.innerHTML = `
            ${metaText}
            <div class="question-text">${q.question}</div>
            <div class="options-list">
                ${optionsHtml}
            </div>
            ${explanationHtml}
        `;

        this.updateDots();
        if (typeof feather !== 'undefined') feather.replace();

        // Btn states
        document.getElementById('prev-btn').style.visibility = this.currentQuestionIndex === 0 ? 'hidden' : 'visible';
        document.getElementById('next-btn').style.visibility = this.currentQuestionIndex === this.questions.length - 1 ? 'hidden' : 'visible';
    }

    selectOption(optLetter) {
        this.userAnswers[this.currentQuestionIndex] = optLetter;
        this.renderQuestion(); // re-render to update selection style & show explanation (if revision)
        
        // Tự động chuyển câu tiếp theo nếu là thi thử (không hiện giải thích)
        if (this.currentMode === 'mock' && this.currentQuestionIndex < this.questions.length - 1) {
            setTimeout(() => this.nextQuestion(), 300);
        }
    }

    nextQuestion() {
        if (this.currentQuestionIndex < this.questions.length - 1) {
            this.currentQuestionIndex++;
            this.renderQuestion();
        }
    }

    prevQuestion() {
        if (this.currentQuestionIndex > 0) {
            this.currentQuestionIndex--;
            this.renderQuestion();
        }
    }

    // --- Timer ---
    startTimer() {
        clearInterval(this.timerInterval);
        this.updateTimerDisplay();
        this.timerInterval = setInterval(() => {
            this.timeLeft--;
            this.updateTimerDisplay();
            
            if (this.timeLeft <= 300) { // 5 minutes left
                document.getElementById('quiz-timer-container').classList.add('danger');
            }

            if (this.timeLeft <= 0) {
                clearInterval(this.timerInterval);
                alert("Hết giờ làm bài! Hệ thống tự động nộp bài.");
                this.submitQuiz();
            }
        }, 1000);
    }

    updateTimerDisplay() {
        const m = Math.floor(this.timeLeft / 60).toString().padStart(2, '0');
        const s = (this.timeLeft % 60).toString().padStart(2, '0');
        document.getElementById('time-left').innerText = `${m}:${s}`;
    }

    // --- Submit & Results ---
    submitQuiz() {
        clearInterval(this.timerInterval);
        
        let correctCount = 0;
        this.questions.forEach((q, idx) => {
            const userAns = this.userAnswers[idx];
            if (userAns && userAns === q.correctAnswer) {
                correctCount++;
            }
        });

        document.getElementById('score-text').innerText = `${correctCount}/${this.questions.length}`;
        
        const scorePercent = correctCount / this.questions.length;
        const msgEl = document.getElementById('score-message');
        if (scorePercent >= 0.8) {
            msgEl.innerText = "Tuyệt vời! Bạn nắm kiến thức rất chắc.";
            msgEl.style.color = "var(--success)";
        } else if (scorePercent >= 0.5) {
            msgEl.innerText = "Khá tốt! Hãy xem lại các câu sai để hoàn thiện nhé.";
            msgEl.style.color = "var(--warning)";
        } else {
            msgEl.innerText = "Cần cố gắng hơn! Hãy tập trung ôn lại các phần bị sai.";
            msgEl.style.color = "var(--danger)";
        }

        this.switchScreen('result-screen');
    }

    reviewAnswers() {
        const container = document.getElementById('review-container');
        container.innerHTML = '';

        this.questions.forEach((q, idx) => {
            const userAns = this.userAnswers[idx];
            // Fix possible missing correctAnswer from extraction
            const isCorrect = userAns && userAns === q.correctAnswer;
            const isUnanswered = !userAns;
            const noAnswerKey = !q.correctAnswer;

            let statusHtml = '';
            let cardClass = '';
            
            if (noAnswerKey) {
                statusHtml = `<span class="review-status" style="color:var(--warning)">Không có đáp án tham chiếu</span>`;
            } else if (isUnanswered) {
                statusHtml = `<span class="review-status status-wrong">Chưa trả lời</span>`;
                cardClass = 'wrong-card';
            } else if (isCorrect) {
                statusHtml = `<span class="review-status status-correct">Đúng</span>`;
                cardClass = 'correct-card';
            } else {
                statusHtml = `<span class="review-status status-wrong">Sai</span>`;
                cardClass = 'wrong-card';
            }

            // Options rendering
            let optionsHtml = '';
            q.options.forEach(opt => {
                const optLetter = opt.substring(0, 1);
                let optClass = 'r-opt';
                
                if (optLetter === q.correctAnswer) {
                    optClass += ' is-correct';
                } else if (optLetter === userAns && !isCorrect) {
                    optClass += ' is-wrong';
                }

                optionsHtml += `<div class="${optClass}">${opt}</div>`;
            });

            // Revision Direction & Explanation
            let revisionText = '';
            if (q.chapter || q.sourceChapter) {
                const chap = q.chapter || q.sourceChapter;
                const top = q.topic || q.sourceTopic;
                revisionText = `Hướng ôn tập: Chương ${chap} - ${top}`;
            }

            let explanationHtml = '';
            if (q.correctAnswer) {
                const smartExpl = this.generateSmartExplanation(q, userAns);
                explanationHtml = `
                    <div class="explanation-box" style="margin-top: 15px;">
                        <h4 style="margin-bottom: 10px;"><i data-feather="book-open" style="width: 14px; height: 14px;"></i> Phân tích đáp án:</h4>
                        <div style="font-size: 0.9rem;">${smartExpl}</div>
                    </div>
                `;
            }

            container.innerHTML += `
                <div class="review-item ${cardClass} fade-in-up" style="animation-delay: ${Math.min(idx * 0.05, 0.5)}s">
                    <div class="review-q-header">
                        <strong>Câu ${idx + 1}</strong>
                        <div>
                            <span class="revision-dir mr-3" style="margin-right: 1rem;">${revisionText}</span>
                            ${statusHtml}
                        </div>
                    </div>
                    <div class="question-text" style="font-size: 1rem; margin-bottom: 1rem;">${q.question}</div>
                    <div class="review-options">
                        ${optionsHtml}
                    </div>
                    ${explanationHtml}
                </div>
            `;
        });

        this.switchScreen('review-screen');
    }

    resetState() {
        clearInterval(this.timerInterval);
        this.questions = [];
        this.userAnswers = {};
        this.currentMode = null;
        document.getElementById('quiz-timer-container').classList.remove('danger');
    }
}

// Khởi tạo app
const app = new QuizApp();
