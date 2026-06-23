# Giải thích chi tiết - Chương 3: Thiết kế kiến trúc phần mềm

## Phần 1: Các khái niệm, nguyên lý cơ bản của thiết kế kiến trúc

**Câu 158 (q_158): Thiết kế kiến trúc phần mềm là quá trình nào?**
Đáp án đúng: B
Giải thích: Thiết kế kiến trúc là quá trình xác định cấu trúc cơ bản ở mức tổng thể, bao gồm việc định nghĩa các thành phần chính và cách chúng tương tác với nhau.
- Loại A: Viết mã nguồn (Coding) là giai đoạn thực thi (Implementation), diễn ra sau thiết kế.
- Loại C: Thiết kế giao diện (UI/UX) chỉ là một phần rất nhỏ ở bề nổi.
- Loại D: Quản lý CSDL là công việc của Database Administrator (DBA).

**Câu 159 (q_159): Yếu tố nào sau đây là quan trọng nhất trong giai đoạn thiết kế kiến trúc phần mềm?**
Đáp án đúng: B
Giải thích: Việc chọn đúng các mẫu thiết kế (Design patterns / Architectural patterns) như MVC, Microservices, Layered... sẽ định hình toàn bộ khung sườn và chất lượng hệ thống sau này.
- Loại A: Ngôn ngữ lập trình có thể linh hoạt chọn sau khi đã có kiến trúc phân tán.
- Loại C: Giao diện chi tiết (UI) không quyết định kiến trúc lõi bên dưới.
- Loại D: Viết tài liệu cài đặt là công đoạn sau cùng.

**Câu 160 (q_160): Mục tiêu chính của thiết kế kiến trúc phần mềm là gì?**
Đáp án đúng: B
Giải thích: Mục đích tối thượng của kiến trúc là tạo ra một bản thiết kế đảm bảo phần mềm chạy đúng nghiệp vụ (yêu cầu chức năng) và chạy tốt, nhanh, bảo mật (yêu cầu phi chức năng).
- Loại A: Chỉ tối ưu hiệu suất là chưa đủ, còn cần bảo trì, mở rộng, bảo mật...
- Loại C: Tài liệu chỉ là sản phẩm phụ, bản thân thiết kế hệ thống mới là mục tiêu chính.
- Loại D: Kiểm tra lỗi là nhiệm vụ của pha Testing.

**Câu 161 (q_161): Thiết kế kiến trúc phần mềm bao gồm việc xác định:**
Đáp án đúng: A
Giải thích: Kiến trúc là về Component (Thành phần) và Connector (Mối quan hệ/Luồng giao tiếp).
- Loại B: Thuật toán chi tiết thuộc về khâu thiết kế chi tiết (Detailed Design) và lập trình.
- Loại C: Dòng mã cụ thể không bao giờ nằm trong bản vẽ kiến trúc tổng thể.
- Loại D: Tài liệu hướng dẫn sử dụng không phải là thành phần cấu trúc mã.

**Câu 162 (q_162): Bước đầu tiên và quan trọng nhất trong tiến trình thiết kế kiến trúc phần mềm là gì?**
Đáp án đúng: C
Giải thích: Nếu không hiểu rõ "Vấn đề cần giải quyết là gì" (Phân tích yêu cầu), mọi thiết kế kỹ thuật phía sau đều trở nên vô nghĩa (Garbage in, Garbage out).
- Loại A, B, D: Đều là các bước thực hiện sau khi đã hiểu rõ bài toán.

**Câu 163 (q_163): Mục đích của việc xác định các phần tử thiết kế và quan hệ của chúng là gì?**
Đáp án đúng: B
Giải thích: Để tạo ra bản thiết kế (blueprint) chỉ ra rõ hệ thống có bao nhiêu khối (phần tử) và khối nào gọi khối nào (sự phụ thuộc) để dev có thể code.
- Loại A: Chức năng được kiểm chứng ở khâu test.
- Loại C: Đây là mục đích của bước "Đánh giá kiến trúc" (Architecture Evaluation).
- Loại D: Đây là kết quả của bước "Biến đổi thiết kế".

**Câu 164 (q_164): Bước nào trong tiến trình thiết kế kiến trúc liên quan đến việc áp dụng các thao tác thiết kế để tạo ra một thiết kế mới tốt hơn?**
Đáp án đúng: D
Giải thích: "Biến đổi thiết kế kiến trúc" là quá trình tinh chỉnh (refine) từ bản nháp ban đầu thành bản thiết kế tối ưu hơn bằng cách áp dụng các chiến thuật và mẫu.
- Loại A, B: Là các bước chuẩn bị ban đầu.
- Loại C: Đánh giá chỉ để tìm lỗi, còn áp dụng thao tác sửa nó là "biến đổi".

**Câu 165 (q_165): "Bẫy cài đặt" được đề cập trong thiết kế kiến trúc phần mềm có nghĩa là gì?**
Đáp án đúng: A
Giải thích: "Bẫy cài đặt" (Implementation trap) xảy ra khi kiến trúc sư quá ham mê việc sử dụng công nghệ mới/thuật toán hay mà quên mất việc thiết kế đó có giải quyết đúng bài toán nghiệp vụ của khách hàng hay không.
- Loại B, D: Là lỗi trong pha lập trình và kiểm thử.
- Loại C: "Không hiệu quả" là hệ quả, nhưng định nghĩa của bẫy này nằm ở ý A.

**Câu 166 (q_166): Đánh giá kiến trúc phần mềm tập trung vào việc đánh giá yếu tố nào?**
Đáp án đúng: B
Giải thích: Đánh giá kiến trúc (như phương pháp ATAM) sẽ xem xét bản vẽ, mô tả kiến trúc để xem liệu nó có rủi ro gì không trước khi tiến hành code.
- Loại A, C, D: Là các thao tác đánh giá "Sản phẩm thực tế" sau khi đã code xong, không phải đánh giá "Kiến trúc".

**Câu 167 (q_167): Toán tử thiết kế cơ bản nào được sử dụng trong bước "Biến đổi thiết kế kiến trúc"?**
Đáp án đúng: D
Giải thích: Biến đổi kiến trúc thường dùng 3 phép toán cơ bản: Phân rã (chia lớn thành nhỏ), Nén (gộp nhỏ thành lớn), và Trừu tượng hóa (che giấu chi tiết).
- Loại A, B, C: Bị thiếu một hoặc nhiều toán tử cơ bản.

**Câu 168 (q_168): Một module duy nhất xử lý cả việc nhập kho, xuất kho và thống kê gây khó khăn bảo trì. Nguyên lý nào đã bị vi phạm?**
Đáp án đúng: A
Giải thích: Nguyên lý Đơn nhiệm (Single Responsibility Principle - SRP) quy định mỗi module/lớp chỉ nên có một lý do duy nhất để thay đổi. Gom mọi thứ vào 1 cục (God object) là vi phạm SRP.
- Loại B: Hiểu biết tối thiểu (Law of Demeter) nói về việc không gọi hàm bắc cầu quá sâu.
- Loại C: Phân rã không phải tên nguyên lý chuẩn xác như Đơn nhiệm.
- Loại D: Không lặp lại mã (DRY).

**Câu 169 (q_169): Hệ thống có nhiều chức năng không được sử dụng ngay từ đầu, gây khó khăn bảo trì. Nguyên lý nào cần áp dụng?**
Đáp án đúng: D
Giải thích: Nguyên lý cực tiểu hóa thiết kế (KISS - Keep It Simple Stupid, hoặc YAGNI - You Aren't Gonna Need It) khuyên rằng chỉ nên thiết kế những gì hiện tại cần thiết, không thiết kế thừa thãi (Over-engineering).
- Loại A, B, C: Không liên quan trực tiếp đến việc nhồi nhét quá nhiều tính năng tương lai.

**Câu 170 (q_170): Một ứng dụng thiết kế với các module giao diện, xử lý nghiệp vụ và truy xuất dữ liệu tách biệt. Thể hiện nguyên lý nào?**
Đáp án đúng: D
Giải thích: Tách biệt các mối quan tâm (Separation of Concerns - SoC) là nguyên lý chia hệ thống thành các tầng độc lập để không "dẫm chân" lên nhau (Ví dụ điển hình là Layered Architecture).
- Loại A: Đơn nhiệm áp dụng ở cấp độ Class/Function nhiều hơn.
- Loại B, C: Không đại diện rõ nhất cho mô hình 3 lớp như ý D.

**Câu 171 (q_171): Hệ thống được thiết kế với cấu trúc linh hoạt, cho phép thêm module mới dễ dàng. Thể hiện nguyên lý nào?**
Đáp án đúng: B
Giải thích: Tính tiến hóa (Evolutionary Architecture) đảm bảo hệ thống có khả năng lớn lên, thay đổi và mở rộng theo thời gian mà không bị phá vỡ cấu trúc cũ.
- Loại A, C, D: Là các nguyên lý hỗ trợ tính tiến hóa, nhưng bản chất linh hoạt mở rộng đại diện cho sự Tiến hóa.

**Câu 172 (q_172): Ở bước "Hiểu được vấn đề", công việc cụ thể là gì?**
Đáp án đúng: C
Giải thích: Hiểu vấn đề chính là đi thu thập Requirement (Yêu cầu chức năng, phi chức năng) từ khách hàng.
- Loại A: Là khâu Phân tích hướng đối tượng / Thiết kế chi tiết.
- Loại B: Là khâu Thiết kế Dữ liệu.
- Loại D: Là khâu Thiết kế Giao diện (Mockup).

**Câu 173 (q_173): Sau bước "Hiểu được vấn đề", đạt được kết quả gì?**
Đáp án đúng: B
Giải thích: Kết quả của khâu khảo sát yêu cầu là một danh sách các Use case (tính năng) ưu tiên và các kịch bản Quality Attributes (Yêu cầu phi chức năng).
- Loại A, D: Là kết quả của bước Thiết kế kiến trúc.
- Loại C: Là một phần, nhưng B bao quát hơn các khía cạnh cần cho KTPM.

**Câu 174 (q_174): Vai trò nào của thiết kế kiến trúc giúp các thành viên hiểu rõ vai trò trách nhiệm?**
Đáp án đúng: C
Giải thích: Khi có bản vẽ kiến trúc chia hệ thống thành Frontend, Backend, Database. Frontend team biết rõ họ làm gì, Backend biết họ làm gì. Nó cải thiện khả năng hợp tác (Communication).
- Loại A, B, D: Không giải thích trực tiếp ý "thành viên hiểu rõ vai trò".

**Câu 175 (q_175): Thiết kế kiến trúc giúp giảm thiểu rủi ro như thế nào?**
Đáp án đúng: B
Giải thích: Bằng cách phác thảo sơ đồ, ta thấy trước các điểm "nghẽn", các rủi ro phụ thuộc chéo trước khi đặt tay vào viết code, từ đó ngăn chặn thảm họa muộn màng.
- Loại A: Ngôn ngữ chung giúp giao tiếp, không trực tiếp giảm rủi ro thiết kế.
- Loại C, D: Là lợi ích phụ.

## Phần 2: Phương pháp ADD (Attribute-Driven Design) & Các Chiến thuật

**Câu 176 (q_176): Để đảm bảo an toàn, bảo mật dữ liệu khách hàng. Chiến thuật bảo mật nào phù hợp?**
Đáp án đúng: B
Giải thích: Để bảo vệ dữ liệu đứng yên (Data at rest) khỏi hacker, chiến thuật tốt nhất là Mã hóa dữ liệu (Encryption) ngay tại cơ sở dữ liệu.
- Loại A: Chỉ bảo vệ mật khẩu, không bảo vệ các dữ liệu khác.
- Loại C: HTTPS chỉ bảo vệ dữ liệu đường truyền (Data in transit).
- Loại D: Sao lưu (Backup) là chiến thuật Availability, không chống lộ dữ liệu.

**Câu 177 (q_177): Hệ thống TMĐT chịu tải lớn (Black Friday). Chiến thuật hiệu năng phù hợp?**
Đáp án đúng: C
Giải thích: Áp dụng bộ nhớ đệm (Cache - như Redis) giúp giảm số lần truy vấn trực tiếp vào DB, làm giảm độ trễ (latency) và tăng thông lượng (throughput) cực mạnh để chịu tải lớn.
- Loại A: Xác thực đa yếu tố là Security.
- Loại B: Chuyển sang UDP sẽ làm mất gói tin, không dùng cho TMĐT.
- Loại D: Log chi tiết làm giảm hiệu năng (do tốn I/O ghi đĩa).

**Câu 178 (q_178): Khi nào cần áp dụng tính sẵn sàng (Availability)?**
Đáp án đúng: C
Giải thích: Hệ thống điều khiển hàng không có tính mạng con người liên quan, nếu sập vài giây sẽ gây thảm họa. Do đó yêu cầu Availability (99.999%) là bắt buộc sống còn.
- Loại A, B, D: Cần sẵn sàng nhưng không sinh tử/khẩn cấp bằng hệ thống hàng không.

**Câu 179 (q_179): Chức năng của Load Balancer trong tính Sẵn sàng (High Availability)?**
Đáp án đúng: A
Giải thích: Cân bằng tải chia đều truy cập ra nhiều server. Nếu 1 server sập, nó tự chuyển luồng qua server khác đang sống, đảm bảo hệ thống luôn "Sẵn sàng".
- Loại B: Mã hóa là Security.
- Loại C: Tự động khôi phục là tính năng của Orchestrator (như K8s), Load balancer chỉ phân phối tải.
- Loại D: Giảm dung lượng là Compression.

**Câu 180 (q_180): Khái niệm "Tactics" (chiến thuật) trong kiến trúc phần mềm?**
Đáp án đúng: C
Giải thích: Chiến thuật (Tactic) là một quyết định/kỹ thuật thiết kế cụ thể (như Ping/Echo, Heartbeat, Active Queue) nhằm thỏa mãn một "Thuộc tính chất lượng" (Ví dụ: Availability).
- Loại A, B: Quản lý dự án không liên quan đến cấu trúc kỹ thuật.
- Loại D: Lựa chọn ngôn ngữ là Implementation.

**Câu 181 (q_181): Phương pháp ADD (Attribute-Driven Design) là gì?**
Đáp án đúng: B
Giải thích: ADD là phương pháp thiết kế kiến trúc lặp đi lặp lại (Iterative), lấy các thuộc tính chất lượng (Security, Performance, Availability...) làm bánh lái (driver) để lựa chọn chiến thuật và mẫu thiết kế.
- Loại A: Không chỉ là chức năng, mà tập trung chủ yếu vào phi chức năng.
- Loại C: Là phương pháp thiết kế, không phải kiểm thử.
- Loại D: Không tập trung vào giao diện.

**Câu 182 (q_182): Mục tiêu của phương pháp ADD?**
Đáp án đúng: B
Giải thích: ADD giúp tìm ra một thiết kế kiến trúc hoàn chỉnh có thể dung hòa và thỏa mãn cả chức năng (Use cases) lẫn chất lượng (Quality Attributes).
- Loại A: Đánh giá chi phí không phải mục tiêu chính của kỹ thuật ADD.
- Loại C: Không tối ưu quy trình phát triển (đó là việc của Agile).
- Loại D: Không thiết kế CSDL chi tiết.

**Câu 183 (q_183): Ai nên sử dụng phương pháp ADD?**
Đáp án đúng: C
Giải thích: Vì là phương pháp "Thiết kế Kiến trúc", người dùng chính xác nhất phải là Kiến trúc sư phần mềm (Software Architect).
- Loại A, B, D: Dev, QA, PM không trực tiếp thiết kế kiến trúc tổng thể.

**Câu 184 (q_184): ADD không nên được sử dụng trong các dự án phần mềm nào?**
Đáp án đúng: D
Giải thích: ADD khá nặng tính quy trình và phân tích chuyên sâu. Các dự án nhỏ/đơn giản (như web hiển thị tĩnh) áp dụng ADD sẽ tốn thời gian vô ích (Overhead).
- Loại A, B, C: Là các hệ thống phức tạp, cực kỳ cần ADD.

**Câu 185 (q_185): ADD có thể kết hợp với phương pháp thiết kế nào?**
Đáp án đúng: C
Giải thích: ADD linh hoạt, thường kết hợp hoàn hảo với Thiết kế hướng đối tượng (OOD) để tạo cấu trúc Class, hoặc các quy trình lặp (như RUP/Agile) để phát triển.

**Câu 186 (q_186): "Trình điều khiển kiến trúc" (Architectural drivers) là gì?**
Đáp án đúng: C
Giải thích: Nó bao gồm (Use cases quan trọng + Các thuộc tính chất lượng then chốt + Ràng buộc công nghệ). Đây là những yếu tố "lái" / "định hình" hướng đi của kiến trúc sư.
- Loại A, B, D: Sai thuật ngữ chuyên ngành.

**Câu 187 (q_187): Mô hình kiến trúc trong ADD được xây dựng bằng cách kết hợp:**
Đáp án đúng: B
Giải thích: ADD dùng Architectural Drivers để chọn ra các Mẫu kiến trúc (Patterns - ví dụ MVC, Layered) và bổ sung các Chiến thuật (Tactics - ví dụ Cache, Ping/Echo) để hoàn thiện bản vẽ.
- Loại A, C, D: Đều là các công cụ/ngôn ngữ không phải cốt lõi thiết kế tư duy của ADD.

**Câu 188 (q_188): Bước nào sau đây liên quan đến việc xác định yêu cầu chức năng và thuộc tính chất lượng?**
Đáp án đúng: B
Giải thích: Trong quy trình ADD (ADD 3.0), Bước 1: "Review Inputs" (Đánh giá đầu vào) là bước tập hợp, rà soát lại mọi tài liệu yêu cầu (Driver) từ khách hàng.
- Loại A: Bước 2 là chọn driver cho một vòng lặp (iteration).
- Loại C: Bước 4 là chọn concept (mẫu) thiết kế.
- Loại D: Bước 6 là vẽ sơ đồ.

**Câu 189 (q_189): Đầu vào chính của phương pháp ADD là:**
Đáp án đúng: B
Giải thích: ADD (Attribute-Driven Design) có đầu vào trọng tâm là các Kịch bản thuộc tính chất lượng (Quality Attribute Scenarios), giúp định lượng và kiểm chứng dễ dàng (VD: Hệ thống phản hồi < 2s khi có 1000 user).
- Loại A: Yêu cầu chức năng là cần, nhưng không phải nét đặc trưng dẫn dắt của ADD.
- Loại C, D: Sai.

**Câu 190 (q_190): Hệ thống điều khiển giao thông cần xử lý dữ liệu thời gian thực. Bước nào trong ADD giúp chọn chiến thuật?**
Đáp án đúng: B
Giải thích: Bước 4 "Choose design concepts" (Lựa chọn khái niệm thiết kế) là lúc kiến trúc sư quyết định dùng chiến thuật gì (Ví dụ: Tactic "Tăng hiệu năng", Pattern "Event-Driven") để thỏa mãn driver thời gian thực.

**Câu 191 (q_191): Xác định các yêu cầu về khả năng tương tác (interoperability). Bước nào trong ADD?**
Đáp án đúng: C
Giải thích: Interoperability là một yêu cầu chất lượng (Quality Attribute). Việc xác định và ghi nhận nó diễn ra ở Bước 1: Review Inputs.

**Câu 192 (q_192): Áp dụng ADD cho nhà máy sản xuất (cần tính an toàn và thời gian phản ứng). Kết quả là gì?**
Đáp án đúng: C
Giải thích: Do Architectural drivers của dự án này là An toàn (Safety) và Thời gian thực (Performance/Latency), ADD sẽ lái kiến trúc tập trung sinh ra kết quả thỏa mãn các yếu tố này, giúp giảm thiểu rủi ro sinh mạng.
- Loại A, B: Mở rộng / UI đẹp không phải ưu tiên sống còn của nhà máy.
- Loại D: Giá rẻ thường tỷ lệ nghịch với Safety hệ thống công nghiệp.

**Câu 193 (q_193): Áp dụng ADD cho phần mềm CRM tùy chỉnh nhiều ngành. Kết quả là gì?**
Đáp án đúng: B
Giải thích: Driver ở đây là Tính linh hoạt (Modifiability) và Khả năng tùy biến (Customization). ADD sẽ chọn các Pattern như Microkernel hoặc Plugin-based để sinh ra kiến trúc dễ tùy chỉnh nhất.
- Loại A, C, D: Đều lệch trọng tâm của bài toán là "tùy chỉnh cho nhiều ngành".
