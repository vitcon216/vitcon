# Giải thích chi tiết - Chương 2: Các mẫu kiến trúc phần mềm (Phần 2 - Câu 98 đến 127)

## Kiến trúc Phân lớp (Layered Architecture)

**Câu 98 (q_98): Kiến trúc phân lớp (Layered Architecture) là gì?**
Đáp án đúng: B
Giải thích: Kiến trúc phân lớp là việc tổ chức mã nguồn hệ thống thành các tầng/lớp (layers) xếp chồng lên nhau. Mỗi lớp thực hiện một nhóm chức năng chuyên biệt (ví dụ: giao diện, nghiệp vụ, dữ liệu).
- Loại A: Không thể chạy độc lập hoàn toàn vì lớp trên cần gọi lớp dưới.
- Loại C: Thành phần phân tán tự động là đặc tính của Service-Oriented hoặc Microservices.
- Loại D: Không có quy định bắt buộc phải kết nối chung bằng một "bus", việc gọi giữa các lớp thường là gọi hàm hoặc đối tượng.

**Câu 99 (q_99): Lợi ích chính của kiến trúc phân lớp là gì?**
Đáp án đúng: C
Giải thích: Tách biệt mối quan tâm (Separation of Concerns) giúp hệ thống dễ hiểu, dễ kiểm thử, dễ bảo trì và có khả năng thay thế một lớp (ví dụ đổi UI) mà không làm hỏng lớp khác.
- Loại A: Hiệu suất thường bị giảm (overhead) do dữ liệu phải đi xuyên qua nhiều lớp.
- Loại B: Không giải quyết trực tiếp bài toán chịu tải hoặc khôi phục sau sự cố (Fault tolerance).
- Loại D: Kiến trúc phân lớp vẫn có thể bị sập một phần gây ảnh hưởng dây chuyền.

**Câu 100 (q_100): Nhược điểm của kiến trúc phân lớp là gì?**
Đáp án đúng: B
Giải thích: Khi một yêu cầu được gửi từ giao diện xuống database, nó phải đi qua lớp UI -> logic -> data access, gây ra độ trễ (latency/overhead). Đôi khi có hiện tượng "Lỗ hổng kiến trúc" (Architecture sinkhole) khi yêu cầu chỉ đi xuyên qua các lớp mà không có xử lý logic gì.
- Loại A: Kiến trúc này đặc biệt nổi tiếng vì DỄ bảo trì, chứ không phải khó.
- Loại C: Dễ hiểu và rõ ràng.
- Loại D: Tái sử dụng là ưu điểm của nó.

**Câu 101 (q_101): Lớp nào trong kiến trúc phân lớp tương tác trực tiếp với người dùng?**
Đáp án đúng: A
Giải thích: Lớp trình bày (Presentation Layer / UI Layer) chịu trách nhiệm hiển thị thông tin ra màn hình và bắt các sự kiện tương tác của người dùng.
- Loại B: Lớp nghiệp vụ xử lý logic tính toán ngầm.
- Loại C: Lớp truy cập dữ liệu giao tiếp với Database.
- Loại D: Lớp dịch vụ cung cấp API.

**Câu 102 (q_102): Lớp nghiệp vụ (Business Logic Layer) chịu trách nhiệm gì?**
Đáp án đúng: B
Giải thích: Là bộ não của ứng dụng, chứa các quy tắc kinh doanh (business rules), công thức tính toán và xử lý các luồng nghiệp vụ.
- Loại A: Việc lưu trữ là của lớp dữ liệu.
- Loại C: Giao diện là của Presentation Layer.
- Loại D: Gọi API ngoài là của lớp Tích hợp/Dịch vụ.

**Câu 103 (q_103): Lớp truy cập dữ liệu (Data Access Layer) làm gì?**
Đáp án đúng: B
Giải thích: Data Access Layer (DAL) chuyên chịu trách nhiệm đọc/ghi, truy vấn dữ liệu từ cơ sở dữ liệu (Database) hoặc các kho lưu trữ khác.
- Loại A: Không xử lý logic kinh doanh ở đây.
- Loại C: Quản lý giao diện là của lớp trên cùng.
- Loại D: Truyền nhận sự kiện thuộc về Broker hoặc Layer khác.

**Câu 104 (q_104): Lớp nào thường chứa các xử lý liên quan đến bảo mật và xác thực người dùng?**
Đáp án đúng: A
Giải thích: Xác thực (Authentication) và kiểm tra quyền thường được chặn ngay tại cửa vào (Presentation Layer hoặc đôi khi là Security/Service layer nằm phía trước) để từ chối các request không hợp lệ trước khi chúng đi sâu vào hệ thống.
- Loại B, C, D: Đều có thể chứa một phần ủy quyền, nhưng tiếp nhận xác thực từ người dùng là ở Presentation/Controller.

**Câu 105 (q_105): Một ứng dụng web cơ bản thường sử dụng kiến trúc phân lớp gồm bao nhiêu lớp?**
Đáp án đúng: C
Giải thích: Mô hình 3 lớp (3-Tier) là mô hình kinh điển nhất cho Web: Lớp Giao diện (Presentation), Lớp Nghiệp vụ (Business/Application), và Lớp Dữ liệu (Data).
- Loại A: 1 lớp là Monolithic nguyên khối hỗn độn.
- Loại B: 2 lớp thường là Client-Server thuần túy.
- Loại D: 4 lớp thường cho các ứng dụng Enterprise phức tạp hơn.

**Câu 106 (q_106): Thay đổi một lớp có ảnh hưởng đến các lớp khác không?**
Đáp án đúng: C
Giải thích: Việc phân lớp giúp giảm thiểu tối đa tác động. Tuy nhiên nếu đổi giao diện/hàm (API) mà lớp trên gọi xuống lớp dưới, thì lớp liên quan trực tiếp sẽ phải cập nhật theo.
- Loại A: Mọi thay đổi đều ảnh hưởng là sai, nếu chỉ đổi logic bên trong hàm thì không ảnh hưởng lớp khác.
- Loại B: Hoàn toàn không ảnh hưởng là lý thuyết không tưởng nếu đổi Interface.
- Loại D: Luôn ảnh hưởng đến giao diện là sai.

**Câu 107 (q_107): Trong một số trường hợp, kiến trúc phân lớp có thể có thêm một lớp nào nằm ngang và tương tác với tất cả các lớp khác?**
Đáp án đúng: B
Giải thích: Lớp này gọi là Cross-cutting concerns (Mối quan tâm cắt ngang), chứa các chức năng chung dùng cho mọi lớp như: Logging, Security (bảo mật), Exception handling.
- Loại A: Dịch vụ thường có thể nằm ngang, nhưng "Dịch vụ" ở đây mang tính cung cấp tiện ích chung.
- Loại C: Nghiệp vụ nằm ngang là sai cấu trúc.
- Loại D: Lưu trữ luôn nằm ở tầng đáy.

**Câu 108 (q_108): Khi nào thì một lớp có thể bỏ qua lớp ngay bên dưới nó và tương tác trực tiếp với lớp dưới cùng?**
Đáp án đúng: B
Giải thích: Kiến trúc phân lớp thường là "đóng" (Strict Layered). Nhưng đôi khi cho phép "linh hoạt" (Relaxed / Open Layered Architecture) để lớp UI gọi thẳng xuống Database đối với những query đọc dữ liệu quá đơn giản, giúp tránh sinkhole anti-pattern.
- Loại A, C, D: Đều không liên quan đến cơ chế cho phép nhảy lớp của kiến trúc.

**Câu 109 (q_109): Khi nâng cấp cơ sở dữ liệu từ MySQL sang PostgreSQL, lớp nào của kiến trúc phân lớp cần thay đổi?**
Đáp án đúng: C
Giải thích: Nhờ tính tách biệt, chỉ có Lớp truy cập dữ liệu (Data Access Layer) chứa các câu lệnh SQL cụ thể mới cần sửa. Các lớp nghiệp vụ và UI không hề hay biết CSDL bên dưới là gì.
- Loại A, B: Không cần thay đổi vì không dính dáng đến câu lệnh DB.
- Loại D: Không cần đổi toàn bộ.

**Câu 110 (q_110): Khi thêm tính năng thanh toán mới vào ứng dụng thương mại điện tử, lớp nào cần thay đổi?**
Đáp án đúng: A
Giải thích: Đây là một tính năng hoàn chỉnh từ trên xuống dưới (Full-stack feature). UI cần thêm nút/màn hình thanh toán, Nghiệp vụ cần thêm logic tính tiền, Dữ liệu cần bảng lưu hóa đơn. Phải thay đổi cả 3 lớp.
- Loại B, C, D: Đều thiếu, vì tính năng mới tác động toàn diện.

**Câu 111 (q_111): Khi muốn tách giao diện ứng dụng thành ứng dụng web và ứng dụng di động, lớp nào bị ảnh hưởng nhiều nhất?**
Đáp án đúng: A
Giải thích: Lớp trình bày (Presentation Layer) sẽ phải phân tách ra hoặc làm mới hoàn toàn (thành Frontend Web và Mobile App). Các lớp bên dưới (API, Logic, DB) hoàn toàn có thể giữ nguyên để dùng chung.
- Loại B, C: Không bị ảnh hưởng nhiều.
- Loại D: Không ảnh hưởng tất cả.

**Câu 112 (q_112): Khi ứng dụng gặp vấn đề về hiệu suất, việc tối ưu hóa cần tập trung vào lớp nào?**
Đáp án đúng: A
Giải thích: Nghẽn cổ chai (bottleneck) có thể xảy ra ở bất kỳ đâu: UI render chậm, logic tính toán lặp vô hạn, hoặc DB truy vấn không có index. Cần profile và tối ưu ở lớp gặp vấn đề.
- Loại B, C, D: Chỉ định một lớp cụ thể là vội vàng và chưa chắc đã đúng nguyên nhân.

**Câu 113 (q_113): Điều gì là một khó khăn phổ biến khi thực hiện kiểm thử tự động trong kiến trúc phân lớp?**
Đáp án đúng: B
Giải thích: Khi test lớp Nghiệp vụ, nó thường gọi xuống Lớp Dữ liệu. Để test độc lập (Unit Test) mà không cần database thật, ta phải tạo các Mock/Stub để làm giả Lớp Dữ liệu.
- Loại A: Các lớp có thể chạy độc lập trong môi trường mock.
- Loại C: Logic phân tán rải rác là vấn đề của Microservices, không phải của Layered.
- Loại D: Thay đổi code không phải vấn đề cốt lõi của kiểm thử.

**Câu 114 (q_114): Kiến trúc phân lớp so với kiến trúc Microservices có đặc điểm gì nổi bật?**
Đáp án đúng: B
Giải thích: Kiến trúc phân lớp thường là Monolithic (Nguyên khối). Việc mở rộng một chức năng nhỏ bắt buộc phải nhân bản toàn bộ cả khối ứng dụng, kém linh hoạt hơn nhiều so với việc chỉ scale một microservice độc lập.
- Loại A: Quản lý dễ hơn nhưng khó phát triển và deploy độc lập.
- Loại C: Bảo mật là một khái niệm rộng, không quyết định bởi mô hình này.
- Loại D: Không thể luôn đảm bảo hiệu năng tốt hơn.

**Câu 115 (q_115): Kiến trúc phân lớp so với kiến trúc hướng sự kiện (Event-Driven) có đặc điểm gì nổi bật?**
Đáp án đúng: B
Giải thích: Event-driven phản hồi cực nhanh nhờ bất đồng bộ. Layered Architecture gọi hàm tuần tự đồng bộ từ trên xuống dưới nên độ trễ thường cao hơn.
- Loại A: Không mở rộng dễ dàng hơn.
- Loại C: Layered thường dễ debug hơn Event-driven.
- Loại D: Bảo mật không liên quan trực tiếp.

**Câu 116 (q_116): Kiến trúc phân lớp khác với mẫu MVC (Model-View-Controller) như thế nào?**
Đáp án đúng: C
Giải thích: Layered Architecture phân chia toàn bộ ứng dụng vật lý/logic (UI, BLL, DAL). MVC thường chỉ là một mẫu thiết kế dùng riêng ở trong tầng Presentation (Lớp trình bày) để điều hướng UI.
- Loại A, B: Sai vì đánh đồng hai khái niệm khác mức độ.
- Loại D: Không hề mâu thuẫn, MVC thường nằm gọn trong một lớp của Layered.

**Câu 117 (q_117): Khi nào nên chọn kiến trúc phân lớp thay vì kiến trúc Microservices?**
Đáp án đúng: A
Giải thích: Phụ thuộc quy mô. Ứng dụng nhỏ/trung bình, team nhỏ thì dùng Layered cho nhanh và dễ quản lý. Ứng dụng khổng lồ, chia nhiều team thì dùng Microservices.
- Loại B: Sai, Layered dùng cho nhỏ/vừa tốt hơn.
- Loại C, D: Đây là quyết định chiến lược (Trade-off), không có cái nào luôn tốt hơn.

**Câu 118 (q_118): Hệ thống quản lý thư viện (Quản lý sách, Độc giả, Mượn trả...): Lớp nào xử lý logic xác định tiền phạt quá hạn?**
Đáp án đúng: B
Giải thích: "Tính tiền phạt" là một quy tắc kinh doanh (Business rule). Do đó, nó phải nằm ở Lớp nghiệp vụ (Business Logic Layer).
- Loại A: Lớp trình bày chỉ hiển thị số tiền phạt.
- Loại C: Lớp dữ liệu chỉ lưu con số.
- Loại D: Lớp dịch vụ thường dùng gọi API ngoài.

**Câu 119 (q_119): Ứng dụng TMĐT (Giỏ hàng, Thanh toán, Lịch sử...): Các lớp tiêu chuẩn là gì?**
Đáp án đúng: A
Giải thích: Các lớp tiêu chuẩn bao gồm: Trình bày (Web/App UI), Nghiệp vụ (Logic tính tiền, giảm giá), Dữ liệu (Lưu Database), và Dịch vụ (Gọi API cổng thanh toán VNPay, Momo...).
- Loại B: Tên gọi hơi lộn xộn nhưng tương tự A, tuy nhiên A chuẩn về thuật ngữ hơn.
- Loại C, D: Đưa các đối tượng (Người dùng, Bạn bè) làm tên lớp kiến trúc là sai hoàn toàn (đó là class/model trong OOP).

**Câu 120 (q_120): Mạng xã hội, để gửi một thông báo tương tác bài viết, lớp nào chịu trách nhiệm quản lý?**
Đáp án đúng: C
Giải thích: Lớp nghiệp vụ sẽ nhận diện logic (có người vừa bình luận), sau đó đưa ra quyết định "phải thông báo", và gọi Lớp dịch vụ (Notification Service/Push Server) để bắn thông báo đi.
- Loại A: Lớp trình bày là Frontend, không được phép xử lý luồng sự kiện thông báo ngầm cho người khác.
- Loại B: DB Trigger không được khuyến khích chứa business logic (trừ phi dùng kiến trúc đặc thù).
- Loại D: Lớp "người dùng" không phải tên một tầng kiến trúc.

**Câu 121 (q_121): LMS, theo dõi tiến độ học viên: Các lớp phối hợp như thế nào?**
Đáp án đúng: C
Giải thích: Trình tự chuẩn mực của Layered Architecture: Yêu cầu từ UI (Trình bày) -> Truyền xuống Logic (Nghiệp vụ) -> Lấy dữ liệu thô (Dữ liệu) -> Logic tính toán phần trăm hoàn thành -> Trả về UI hiển thị.
- Loại A: UI gọi thẳng DB là bỏ qua bảo mật và logic (trừ khi dùng Relaxed layers nhưng ít gặp với tính toán phức tạp).
- Loại B: DB không nên tự chứa logic tính toán phức tạp.
- Loại D: Dịch vụ không chịu trách nhiệm tính toán nội bộ của hệ thống lõi.

## Kiến trúc Gọi và Trả lời (Call and Return / Client-Server)

**Câu 122 (q_122): Kiến trúc gọi và trả lời là gì?**
Đáp án đúng: B
Giải thích: Đây là bản chất của mô hình Client-Server. Một bên (Client) chủ động tạo lời gọi (Request) và bên kia (Server) thực thi xử lý rồi trả về kết quả (Response).
- Loại A: Bình đẳng là đặc trưng của Peer-to-Peer (P2P).
- Loại C: Giao tiếp qua Bus là Event-driven hoặc SOA.
- Loại D: Giao tiếp qua hàng đợi là Message-based.

**Câu 123 (q_123): Thành phần nào trong kiến trúc client-server yêu cầu dịch vụ?**
Đáp án đúng: B
Giải thích: Khách hàng (Client) luôn là người khởi xướng (Initiator) lời gọi yêu cầu dịch vụ. Server luôn ở trạng thái lắng nghe chờ phục vụ.
- Loại A: Server là người cung cấp dịch vụ.
- Loại C, D: Bus và Queue là môi trường/kênh trung gian.

**Câu 124 (q_124): Lợi ích chính của kiến trúc client-server là gì?**
Đáp án đúng: C
Giải thích: Dữ liệu và logic được quản lý tập trung tại Server, giúp dễ dàng sao lưu, bảo mật và duy trì tính nhất quán. Các client chỉ là nơi hiển thị.
- Loại A: Tăng phức tạp là nhược điểm chứ không phải lợi ích.
- Loại B: Nó thực tế giúp tăng khả năng mở rộng (Scale server).
- Loại D: Dữ liệu tập trung nhưng "tối ưu nhất" là quá cường điệu.

**Câu 125 (q_125): Loại server nào xử lý logic nghiệp vụ cho ứng dụng?**
Đáp án đúng: B
Giải thích: Application Server (Máy chủ ứng dụng) chứa mã nguồn backend thực thi các luật nghiệp vụ (Business logic).
- Loại A: Web Server (như Nginx, Apache) chuyên điều phối HTTP request và file tĩnh.
- Loại C: Database Server (SQL) chuyên lưu trữ dữ liệu.
- Loại D: Mail Server chuyên gửi/nhận email.

**Câu 126 (q_126): Ứng dụng di động lấy dữ liệu từ API RESTful. Thành phần nào gửi yêu cầu và hiển thị?**
Đáp án đúng: B
Giải thích: App điện thoại đóng vai trò là Client (Máy khách). Nó khởi tạo request HTTP RESTful đến Server và dùng JSON trả về để vẽ giao diện hiển thị cho user.
- Loại A: Server cung cấp API.
- Loại C, D: DB và Load balancer nằm ở phía backend.

**Câu 127 (q_127): Ứng dụng thời tiết kết nối dịch vụ trực tuyến. Tương tác nào mô tả đúng nhất?**
Đáp án đúng: C
Giải thích: Mô hình Request - Response cơ bản. Ứng dụng (Client) xin dữ liệu thời tiết (Call/Request), dịch vụ (Server) tính toán và gửi về (Return/Response).
- Loại A: App không thể lưu sẵn tất cả dữ liệu thời tiết thực tế được vì nó luôn biến động.
- Loại B: Server không chủ động đẩy liên tục cho các app trừ khi dùng WebSocket, nhưng Request-Response (Call-return) là giao thức gửi-đáp truyền thống.
- Loại D: Hai bên không bao giờ share chung Database vật lý.
