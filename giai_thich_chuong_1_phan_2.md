# Giải thích chi tiết - Chương 1: Tổng quan Kiến trúc phần mềm (Phần 2 - Câu 36 đến 67)

**Câu 36 (q_36): Thuộc tính chất lượng nào liên quan đến khả năng phần mềm đáp ứng các yêu cầu về tốc độ và thời gian phản hồi?**
Đáp án đúng: A
Giải thích: Hiệu suất (Performance) đánh giá xem hệ thống xử lý các giao dịch nhanh đến mức nào và mất bao lâu để phản hồi một yêu cầu.
- Loại B (Khả năng mở rộng): Đánh giá việc xử lý số lượng truy cập lớn (Scalability), không trực tiếp là tốc độ phản hồi hiện tại.
- Loại C (Độ tin cậy): Đo lường hệ thống không bị lỗi.
- Loại D (Khả năng bảo trì): Đo lường sự dễ dàng khi nâng cấp mã nguồn.

**Câu 37 (q_37): Khả năng phần mềm dễ dàng được người dùng sử dụng được gọi là gì?**
Đáp án đúng: A
Giải thích: Khả năng sử dụng (Usability) là mức độ mà một sản phẩm có thể được người dùng sử dụng để đạt được mục tiêu một cách hiệu quả, hiệu lực và thỏa mãn.
- Loại B (Khả năng bảo mật): Bảo vệ dữ liệu khỏi truy cập trái phép.
- Loại C (Khả năng kiểm thử): Dễ dàng viết test case kiểm tra lỗi logic.
- Loại D (Khả năng tái sử dụng): Tính chất của module/code.

**Câu 38 (q_38): Khả năng phần mềm dễ dàng được kiểm tra các sai sót được gọi là gì?**
Đáp án đúng: C
Giải thích: Khả năng kiểm thử (Testability) cho phép đội ngũ QA dễ dàng viết script, cô lập module để test và tìm lỗi nhanh chóng.
- Loại A, B, D: Là các thuộc tính khác (Sử dụng, Bảo mật, Tái sử dụng).

**Câu 39 (q_39): Thuộc tính chất lượng nào đo lường khả năng phần mềm đáp ứng được các yêu cầu về thời gian đáp ứng, dung lượng bộ nhớ và khả năng xử lý?**
Đáp án đúng: A
Giải thích: Hiệu suất (Performance) không chỉ bao gồm tốc độ thời gian phản hồi (latency) mà còn đo lường thông lượng xử lý (throughput) và mức độ tiêu thụ tài nguyên phần cứng (bộ nhớ, CPU).
- Loại B: Mở rộng là về việc tăng thêm node hoặc tài nguyên khi tải tăng.
- Loại C, D: Tin cậy và bảo trì không liên quan đến thời gian đáp ứng.

**Câu 40 (q_40): Mục tiêu chính của chiến lược thiết kế tập trung vào người dùng là gì?**
Đáp án đúng: C
Giải thích: Thiết kế tập trung vào người dùng (User-Centered Design - UCD) lấy người dùng làm trung tâm, nên mục tiêu số 1 là giải quyết và đáp ứng chính xác nhu cầu của họ.
- Loại A: Đẹp mắt là UX/UI, nếu đẹp mà không đúng nhu cầu thì sản phẩm thất bại.
- Loại B: Tối ưu lợi nhuận là mục tiêu kinh doanh, không phải cốt lõi của UCD.
- Loại D: Công nghệ tiên tiến không có ý nghĩa nếu người dùng không cần.

**Câu 41 (q_41): Nguyên tắc nào KHÔNG thuộc về thiết kế tập trung vào người dùng?**
Đáp án đúng: C
Giải thích: UCD yêu cầu phải lắng nghe người dùng. Tập trung vào ý kiến cá nhân/cảm tính của nhà thiết kế là vi phạm nguyên tắc cốt lõi của UCD.
- Loại A, B, D: Đều là các nguyên tắc cốt lõi của UCD (Thấu cảm, hiểu ngữ cảnh, đánh giá liên tục).

**Câu 42 (q_42): Lợi ích chính của chiến lược thiết kế dựa trên dữ liệu (DDD) là gì?**
Đáp án đúng: B
Giải thích: DDD (Data-Driven Design) dùng số liệu thực tế (A/B testing, Analytics) để quyết định, tránh các định kiến chủ quan, giúp sản phẩm đi đúng hướng.
- Loại A: Phân tích dữ liệu đôi khi lại gò bó bớt tính "bay bổng" sáng tạo.
- Loại C: Đôi khi phải tốn kém xây dựng hệ thống thu thập dữ liệu (Analytics/Big Data).
- Loại D: Phân tích dữ liệu có thể tốn thời gian hơn là "đoán đại".

**Câu 43 (q_43): Đánh giá khả năng sử dụng (usability testing) nhằm mục đích gì?**
Đáp án đúng: B
Giải thích: Usability testing (thử nghiệm tính khả dụng) cho phép quan sát cách người dùng thực sự dùng sản phẩm, từ đó đo lường độ hài lòng và phát hiện điểm vướng mắc.
- Loại A: Tìm lỗi code là nhiệm vụ của QA/Tester, không phải Usability test.
- Loại C: Đánh giá Marketing là chuyện của bộ phận Sale/Marketing.
- Loại D: Kiểm tra bảo mật là Security Test.

**Câu 44 (q_44): Persona (hình mẫu người dùng) được sử dụng để làm gì trong chiến lược thiết kế tập trung vào người dùng (UCD)?**
Đáp án đúng: B
Giải thích: Persona là một nhân vật giả định mang đầy đủ đặc điểm của nhóm khách hàng mục tiêu, giúp đội ngũ thiết kế đồng cảm và dễ dàng hình dung họ đang thiết kế cho ai.
- Loại A: Đại diện phân khúc thị trường thiên về Marketing.
- Loại C: Không liên quan đến đối thủ cạnh tranh.
- Loại D: Lên kế hoạch kinh doanh là của phòng ban khác.

**Câu 45 (q_45): Thiết kế tương tác (interaction design) tập trung vào điều gì trong chiến lược thiết kế tập trung vào người dùng (UCD)?**
Đáp án đúng: B
Giải thích: Interaction Design (IxD) nghiên cứu cách con người tương tác trực tiếp với giao diện (click, vuốt, cuộn) và cách hệ thống phản hồi lại để mang đến trải nghiệm mượt mà.
- Loại A: Giao diện trực quan là của Visual Design (UI).
- Loại C: Cấu trúc cơ sở dữ liệu là của backend.
- Loại D: Thuật toán là của lập trình viên.

**Câu 46 (q_46): Lợi ích chính của chiến lược thiết kế linh hoạt (Agile design) là gì?**
Đáp án đúng: A
Giải thích: Agile chia nhỏ dự án thành các chu kỳ ngắn, giúp đội ngũ có thể quay xe, thay đổi thiết kế ngay lập tức nếu yêu cầu thị trường biến động, giảm rủi ro đi sai hướng kéo dài.
- Loại B: Không hẳn tiết kiệm chi phí, đôi khi phải làm đi làm lại (Refactor).
- Loại C: Agile không hứa hẹn sản phẩm hoàn hảo ngay lần đầu, mà hoàn thiện dần qua các vòng lặp.
- Loại D: Agile đòi hỏi khách hàng tham gia liên tục (Feedback loop).

**Câu 47 (q_47): Khả năng mở rộng (scalability) của hệ thống là gì?**
Đáp án đúng: B
Giải thích: Scalability là khả năng của hệ thống tăng thêm tài nguyên (scale up/out) để đáp ứng được tải lượng công việc ngày càng cao (nhiều người dùng hơn, nhiều dữ liệu hơn) mà không làm sập hệ thống.
- Loại A: Khả năng hoạt động trên đa nền tảng là Portability.
- Loại C: Khả năng phục hồi là Resilience/Fault tolerance.
- Loại D: Khả năng bảo vệ dữ liệu là Security.

**Câu 48 (q_48): Chiến lược thiết kế linh hoạt (Agile design) là gì?**
Đáp án đúng: B
Giải thích: Là cách làm việc lặp đi lặp lại (iterative), chia nhỏ yêu cầu và phản hồi liên tục, luôn sẵn sàng thích ứng trước các thay đổi.
- Loại A: Lên kế hoạch chi tiết từ đầu là mô hình thác nước (Waterfall).
- Loại C: Áp dụng được cho cả dự án nhỏ.
- Loại D: Cực kỳ cần sự tham gia của khách hàng.

**Câu 49 (q_49): Thiết kế dựa trên dữ liệu (DDD) là gì?**
Đáp án đúng: B
Giải thích: Data-Driven Design là việc sử dụng thông tin định lượng (Analytics, Logging, A/B Testing) để hướng dẫn và chứng minh các quyết định thiết kế thay vì cảm tính.
- Loại A: Thiết kế cảm tính là đối lập với DDD.
- Loại C, D: Xu hướng hay ý kiến khách hàng (định tính) chỉ là một phần nhỏ, cốt lõi phải là phân tích bộ dữ liệu thực tế.

**Câu 50 (q_50): Khi nào nên bắt đầu áp dụng chiến lược thiết kế tập trung vào người dùng (UCD)?**
Đáp án đúng: C
Giải thích: UCD phải làm từ khâu khảo sát yêu cầu ban đầu (ví dụ: tạo Persona, User Journey) để định hình toàn bộ sản phẩm.
- Loại A, B: Làm sau khi ra mắt hoặc thử nghiệm sẽ quá muộn, nếu sai thì chi phí đập đi làm lại rất khổng lồ.
- Loại D: Phản hồi tiêu cực mới làm thì sản phẩm đã mất uy tín.

**Câu 51 (q_51): Phương pháp nào thường được sử dụng trong chiến lược thiết kế linh hoạt (Agile design) để chia nhỏ công việc thành các phần nhỏ hơn?**
Đáp án đúng: C
Giải thích: Scrum chia công việc thành các Sprint ngắn, Kanban chia công việc qua các cột quy trình liên tục. Cả hai là đại diện tiêu biểu của Agile.
- Loại A: Waterfall là mô hình truyền thống (tuyến tính).
- Loại B: Mô hình xoắn ốc tập trung quản trị rủi ro cao.
- Loại D: Prototype là mô hình tạo mẫu thử.

**Câu 52 (q_52): Nguyên tắc nào sau đây KHÔNG thuộc về chiến lược thiết kế linh hoạt (Agile design)?**
Đáp án đúng: C
Giải thích: Agile có tôn chỉ "Working software over comprehensive documentation" - ưu tiên phần mềm chạy được hơn là tài liệu phức tạp. Việc bắt buộc hoàn thành tài liệu chi tiết từ đầu là tư duy của Waterfall.
- Loại A, B, D: Đều là các nguyên lý nòng cốt của tuyên ngôn Agile (Agile Manifesto).

**Câu 53 (q_53): Tại sao việc tạo mẫu (prototyping) lại quan trọng trong chiến lược thiết kế tập trung vào người dùng (UCD)?**
Đáp án đúng: B
Giải thích: Prototyping cho phép người dùng tương tác thử với ý tưởng (trên bản nháp/Figma) để xem họ có hiểu và thao tác được không, trước khi tốn tiền code thật.
- Loại A: Giúp tiết kiệm chi phí, nhưng mục tiêu là để kiểm tra khả năng sử dụng (usability).
- Loại C: Gây ấn tượng cho nhà đầu tư không phải mục đích cốt lõi của UCD.
- Loại D: Không cần hoàn thiện, mẫu thử chỉ cần đủ để test.

**Câu 54 (q_54): Loại dữ liệu nào KHÔNG được sử dụng trong chiến lược thiết kế dựa trên dữ liệu (DDD)?**
Đáp án đúng: C
Giải thích: Cảm tính của nhà thiết kế hoàn toàn đối lập với tư duy "Dựa trên dữ liệu" (Data-Driven), vì nó là định kiến chủ quan.
- Loại A, B, D: Đều là dữ liệu quan trọng phục vụ phân tích (hành vi, nhân khẩu học, khảo sát).

**Câu 55 (q_55): Công cụ nào thường được sử dụng để phân tích dữ liệu trong chiến lược thiết kế dựa trên dữ liệu (DDD)?**
Đáp án đúng: B
Giải thích: Google Analytics, Mixpanel, Amplitude là các công cụ thống kê trực tiếp hành vi click, bounce rate, funnel của người dùng trên app/web.
- Loại A: Phần mềm vẽ đồ họa.
- Loại C: Quản lý công việc team.
- Loại D: Sai.

**Câu 56 (q_56): Bước đầu tiên trong quy trình chiến lược thiết kế dựa trên dữ liệu (DDD) là gì?**
Đáp án đúng: B
Giải thích: Muốn "dựa trên dữ liệu" thì việc đầu tiên phải có hệ thống thu thập dữ liệu (tracking) và phân tích nó để tìm ra vấn đề trước.
- Loại A, C, D: Đều là các bước sau (tạo bản vẽ, làm prototype, test) khi đã có insight từ dữ liệu.

**Câu 57 (q_57): Chỉ số (metric) nào KHÔNG được sử dụng để đánh giá hiệu quả thiết kế trong chiến lược thiết kế dựa trên dữ liệu (DDD)?**
Đáp án đúng: C
Giải thích: DDD quan tâm đến hiệu năng kinh doanh và trải nghiệm người dùng thực tế. Việc nhà thiết kế hài lòng hay không không phải là thước đo thành công.
- Loại A (Conversion rate): Rất quan trọng để đo doanh thu.
- Loại B (Bounce rate): Rất quan trọng để đo độ hấp dẫn của trang.
- Loại D (Task time): Đo tính khả dụng.

**Câu 58 (q_58): Phương pháp nào giúp thu thập dữ liệu định tính trong chiến lược thiết kế dựa trên dữ liệu (DDD)?**
Đáp án đúng: B
Giải thích: Dữ liệu định tính (Qualitative) trả lời câu hỏi "Tại sao?". Phỏng vấn sâu giúp hiểu được cảm xúc, rào cản và suy nghĩ thầm kín của người dùng.
- Loại A: Server logs là định lượng (Quantitative).
- Loại C: A/B Testing là định lượng (số liệu chuyển đổi).
- Loại D: Khảo sát câu đóng chỉ cung cấp số liệu phân bổ (định lượng).

**Câu 59 (q_59): Tại sao việc trực quan hóa dữ liệu lại quan trọng trong chiến lược thiết kế dựa trên dữ liệu (DDD)?**
Đáp án đúng: B
Giải thích: Hàng ngàn con số thô (raw data) rất khó phân tích. Trực quan hóa (chart, dashboard, heatmap) giúp phát hiện quy luật, điểm rơi rớt để ra quyết định ngay lập tức.
- Loại A: Đẹp không phải mục tiêu chính, mục tiêu là dễ đọc.
- Loại C: Quá trình trực quan hóa cũng mất thời gian.
- Loại D: Trình bày là bước sau, cốt lõi vẫn là hiểu để làm sản phẩm.

**Câu 60 (q_60): Thử nghiệm A/B được sử dụng để làm gì trong chiến lược thiết kế dựa trên dữ liệu (DDD)?**
Đáp án đúng: A
Giải thích: A/B testing tung ra 2 bản thiết kế (ví dụ nút mua hàng màu xanh vs đỏ) cho cùng tệp người dùng ngẫu nhiên để xem bản nào sinh ra tỷ lệ chuyển đổi cao hơn, sau đó chốt bản đó.
- Loại B, C: Là các loại phân tích dữ liệu tổng hợp.
- Loại D: Giả thuyết sinh ra trước khi chạy A/B test.

**Câu 61 (q_61): Thách thức lớn nhất khi áp dụng chiến lược thiết kế dựa trên dữ liệu (DDD) là gì?**
Đáp án đúng: C
Giải thích: Thu thập dữ liệu đã dễ nhờ các công cụ (Google Analytics), nhưng việc "đọc hiểu" con số đó và ra quyết định thay đổi UI/UX sao cho trúng đích mới là phần khó và cần chuyên môn cao nhất.
- Loại A: Công cụ rất nhiều và miễn phí.
- Loại B: Thu thập rất dễ bằng code tracking.
- Loại D: Chi phí không nhất thiết quá cao.

**Câu 62 (q_62): Trong chiến lược thiết kế linh hoạt (Agile design), việc kiểm tra và đánh giá sản phẩm diễn ra khi nào?**
Đáp án đúng: C
Giải thích: Agile nhấn mạnh việc kiểm thử liên tục (Continuous Testing/Integration) ở từng vòng lặp (sprint) để phát hiện và sửa lỗi ngay từ trong trứng nước.
- Loại A: Chỉ đánh giá ở cuối là tư duy Waterfall.
- Loại B: Không chỉ diễn ra ở cuối sprint, quá trình QA diễn ra liên tục.

**Câu 63 (q_63): Phương pháp nào giúp đảm bảo tính minh bạch và giao tiếp hiệu quả trong chiến lược thiết kế linh hoạt (Agile design)?**
Đáp án đúng: B
Giải thích: Họp đứng 15 phút (Daily Stand-up) giúp mọi người biết hôm nay ai làm gì, có vướng mắc (blocker) gì không. Đánh giá (Sprint review) giúp minh bạch hóa kết quả với khách hàng.
- Loại A: Tài liệu phức tạp cản trở tốc độ và minh bạch của Agile.
- Loại C: Agile khuyến khích giao tiếp liên tục.
- Loại D: Hạn chế email, ưu tiên giao tiếp trực tiếp mặt đối mặt (Face-to-face).

**Câu 64 (q_64): Một công ty khởi nghiệp muốn phát triển một ứng dụng di động mới với nguồn lực hạn chế và yêu cầu thay đổi liên tục. Chiến lược thiết kế nào sau đây sẽ phù hợp nhất?**
Đáp án đúng: C
Giải thích: Agile cực kỳ phù hợp cho môi trường biến động, giúp start-up xoay trục (pivot) liên tục tùy theo phản ứng của thị trường mà không đốt sạch nguồn lực vào một mảng không ai cần.
- Loại A: Waterfall sụp đổ ngay nếu yêu cầu đổi giữa chừng.
- Loại B: Xoắn ốc tốn kém quản trị rủi ro.
- Loại D: Prototype chỉ là khâu tạo mẫu, không quản lý được cả dự án dài hơi.

**Câu 65 (q_65): Một nhóm phát triển phần mềm muốn tăng cường sự hợp tác và giao tiếp giữa các thành viên. Chiến lược thiết kế linh hoạt Agile nào sau đây sẽ hữu ích nhất?**
Đáp án đúng: B
Giải thích: Như đã giải thích ở Câu 63, Daily Stand-up bắt buộc các thành viên phải giao tiếp hàng ngày, tăng cường tính gắn kết và hỗ trợ lẫn nhau ngay lập tức.
- Loại A, C, D: Đều là các tư duy cứng nhắc của phương pháp luận kiểu cũ.

**Câu 66 (q_66): Một nhóm phát triển phần mềm muốn tăng cường khả năng thích ứng với các thay đổi công nghệ. Phương pháp Agile nào sau đây sẽ hữu ích nhất?**
Đáp án đúng: B
Giải thích: Agile đón nhận sự thay đổi (Welcome changing requirements). Nếu có công nghệ mới ưu việt, team có thể thử nghiệm (spike) ngay trong sprint tiếp theo để thích ứng.
- Loại A, C: Tư duy bảo thủ, rụt rè không đại diện cho tinh thần Agile linh hoạt.
- Loại D: Khách hàng thường không biết sâu về công nghệ, dev phải tự chủ động cập nhật kiến trúc.

**Câu 67 (q_67): Một công ty phần mềm muốn cải thiện hiệu suất của ứng dụng. Dữ liệu nào sau đây sẽ hữu ích nhất để phân tích?**
Đáp án đúng: A
Giải thích: Hiệu suất (Performance) đo trực tiếp bằng các chỉ số trễ: Thời gian tải trang (Page Load Time), Thời gian tương tác phản hồi (Time to Interactive / API response time).
- Loại B: Chỉ đo thời gian tải tính năng yêu thích là không đủ bao quát.
- Loại C: Đo đối thủ để so sánh, nhưng muốn cải thiện app mình thì phải đo thông số chi tiết của app mình trước.
- Loại D: Thời gian thiết kế là thời gian của dev, không phải thời gian xử lý của app.
