# Giải thích chi tiết - Chương 2: Các mẫu kiến trúc phần mềm (Phần 3 - Câu 128 đến 157)

## Kiến trúc Gọi và Trả lời (Tiếp tục)

**Câu 128 (q_128): Một ứng dụng email (client) kết nối đến một máy chủ email để tải về các email mới nhất. Thành phần nào đóng vai trò client?**
Đáp án đúng: B
Giải thích: Ứng dụng email (như Outlook, Gmail app) cài trên máy người dùng là Client. Nó gửi yêu cầu tải thư đến Máy chủ (Server).
- Loại A: Máy chủ lưu trữ là Server.
- Loại C: Giao thức mạng chỉ là phương thức giao tiếp (như IMAP/POP3).
- Loại D: Người dùng điều khiển Client, không phải là thành phần phần mềm.

## Kiến trúc Hướng Dịch Vụ (Service-Oriented Architecture - SOA)

**Câu 129 (q_129): Lợi ích chính của kiến trúc hướng dịch vụ (SOA) là gì?**
Đáp án đúng: C
Giải thích: SOA giúp xây dựng các chức năng thành các "dịch vụ" độc lập, có thể dùng đi dùng lại ở nhiều dự án khác nhau (tái sử dụng), và dễ dàng liên kết (tích hợp) các nền tảng khác nhau thông qua mạng.
- Loại A: SOA chia nhỏ hệ thống thành nhiều dịch vụ, do đó giảm sự phụ thuộc nguyên khối, tuy nhiên độ phức tạp quản trị mạng lại tăng lên.
- Loại B: Bảo mật mạng thực tế khó hơn, và không giới hạn mở rộng.
- Loại D: SOA luôn có độ trễ do gọi qua mạng, nên không tối ưu hóa mã nguồn chạy trên một máy cục bộ.

**Câu 130 (q_130): Một ứng dụng ngân hàng cần liên tục cập nhật thông tin tỷ giá hối đoái. Phương pháp thiết kế SOA nào là phù hợp nhất?**
Đáp án đúng: B
Giải thích: Xây dựng (hoặc thuê) một "Dịch vụ tỷ giá" độc lập. Ngân hàng và các ứng dụng vệ tinh chỉ cần gọi API của dịch vụ này để lấy dữ liệu.
- Loại A: Tích hợp mã nguồn trực tiếp vào là Monolithic (Nguyên khối), làm ứng dụng phình to.
- Loại C: Gửi email thủ công không phải là giải pháp phần mềm tự động.
- Loại D: Database chung dẫn đến phụ thuộc chặt chẽ (tight coupling), trái với nguyên lý SOA.

**Câu 131 (q_131): Một nhược điểm phổ biến của kiến trúc SOA là gì?**
Đáp án đúng: B
Giải thích: Do các dịch vụ giao tiếp với nhau qua môi trường mạng (HTTP/SOAP), độ trễ (latency) của mạng cộng với quá trình đóng gói/giải nén dữ liệu (serialize) làm tăng thời gian phản hồi so với gọi hàm nội bộ.
- Loại A: SOA không giới hạn ngôn ngữ, các dịch vụ có thể viết bằng Java, C#, Python... tùy ý.
- Loại C: Chi phí bảo trì có thể cao do kiến trúc mạng phức tạp.
- Loại D: SOA rất dễ mở rộng bằng cách thêm server cho từng dịch vụ riêng biệt.

**Câu 132 (q_132): Thành phần nào thường được sử dụng trong SOA để đóng vai trò trung gian, chuyển đổi định dạng dữ liệu và định tuyến thông điệp giữa các dịch vụ?**
Đáp án đúng: C
Giải thích: ESB (Enterprise Service Bus) là trái tim của hệ thống SOA truyền thống. Nó đứng ở giữa, nhận thông điệp, dịch từ chuẩn này sang chuẩn khác và tìm đúng dịch vụ đích để gửi đi.
- Loại A: Router mạng chỉ chuyển tiếp gói tin ở tầng Network (IP), không hiểu logic ứng dụng.
- Loại B: Load balancer cân bằng tải cho cùng một dịch vụ, không dịch định dạng.
- Loại D: Database chỉ lưu trữ.

**Câu 133 (q_133): Điều gì là một khó khăn lớn khi áp dụng kiến trúc SOA để tích hợp với các ứng dụng cũ (legacy applications)?**
Đáp án đúng: B
Giải thích: Các phần mềm cũ thường viết nguyên khối (monolithic) và không có cổng giao tiếp API (như REST/SOAP). Phải viết các Adapter hoặc "đập đi xây lại" một phần mới có thể bọc chúng thành Dịch vụ.
- Loại A: Có thể dùng Adapter để giao tiếp dù khác ngôn ngữ.
- Loại C: SOA không bắt buộc dùng chung Database.
- Loại D: Legacy app không hỗ trợ thì càng cần SOA bọc lại, nhưng khó khăn chính là do bản thân app cũ không có thiết kế service.

**Câu 134 (q_134): Trong môi trường phát triển phần mềm, kiến trúc SOA mang lại lợi ích gì so với kiến trúc nguyên khối (Monolithic)?**
Đáp án đúng: C
Giải thích: Nhờ chia nhỏ thành các Service có Interface rõ ràng, công ty có thể chia thành nhiều Team. Team A làm Service A, Team B làm Service B hoàn toàn độc lập mà không dẫm chân lên code của nhau.
- Loại A: Tốn nhiều thời gian thiết kế kiến trúc và DevOps hơn.
- Loại B: Phải tốn tài nguyên quản lý mạng và server hơn.
- Loại D: Độ bảo mật có thể phức tạp hơn vì có nhiều điểm vào (endpoints) trên mạng.

**Câu 135 (q_135): Kiến trúc SOA khác với kiến trúc Microservices như thế nào?**
Đáp án đúng: B
Giải thích: SOA thường dùng Enterprise Service Bus (ESB) rất đồ sộ, nặng nề, tập trung quản lý logic tích hợp. Microservices chia nhỏ hơn nữa, dùng các giao thức cực nhẹ (như REST/gRPC), loại bỏ ESB để dịch vụ thực sự độc lập (Smart endpoints, dumb pipes).
- Loại A: Microservices lại càng không chia sẻ Database (Database per service).
- Loại C: Microservices mới là xu hướng hiện tại và tương lai.
- Loại D: Microservices là phiên bản "tiến hóa" chia nhỏ hơn của SOA.

**Câu 136 (q_136): Khi nào thì kiến trúc SOA là lựa chọn tốt nhất?**
Đáp án đúng: B
Giải thích: SOA cực kỳ mạnh mẽ ở cấp độ doanh nghiệp lớn (Enterprise), nơi có hàng tá hệ thống cũ mới đan xen (ERP, CRM, Kế toán). SOA dùng ESB để tích hợp tất cả chúng lại với nhau.
- Loại A: Khởi nghiệp/nhỏ nên dùng Monolithic hoặc Microservices nhẹ.
- Loại C: Ưu tiên thời gian thực cực thấp thì không nên dùng mạng phân tán nhiều trễ.
- Loại D: Không cần mở rộng thì dùng Monolithic cho rẻ.

**Câu 137 (q_137): Một hệ thống thông tin y tế chia sẻ dữ liệu bệnh nhân giữa các bệnh viện. Lớp nào sẽ cung cấp dữ liệu bệnh nhân cho các bệnh viện khác?**
Đáp án đúng: B
Giải thích: Trong kiến trúc phân lớp kết hợp hướng dịch vụ, Lớp Dịch vụ (Service Layer / API Layer) có chức năng mở cửa (expose) các API để các hệ thống/bệnh viện bên ngoài có thể gọi và lấy dữ liệu một cách an toàn.
- Loại A: Lớp trình bày chỉ hiển thị nội bộ cho user ở bệnh viện đó.
- Loại C: Lớp dữ liệu không bao giờ được phép cho bên ngoài truy cập trực tiếp vì rủi ro bảo mật khổng lồ.
- Loại D: Lớp nghiệp vụ chỉ tính toán logic, cần Lớp dịch vụ bọc lại để giao tiếp mạng.

**Câu 138 (q_138): Ứng dụng thương mại điện tử cần giao tiếp với hệ thống thanh toán của bên thứ ba. Tại sao kiến trúc SOA lại phù hợp hơn kiến trúc phân lớp trong trường hợp này?**
Đáp án đúng: C
Giải thích: Thanh toán của bên thứ ba (như VNPay, PayPal) là hệ thống độc lập, khác công ty, khác máy chủ. SOA (gọi API) giúp ứng dụng và hệ thống thanh toán hoạt động tách biệt, không cần biết bên kia code bằng gì hay lưu database ra sao.
- Loại A: Không cần chung một cơ sở dữ liệu.
- Loại B: Gọi qua mạng SOA thường chậm hơn gọi nội bộ trong phân lớp.
- Loại D: Nếu code thanh toán hỏng, app vẫn có thể báo "Lỗi thanh toán" thay vì sập toàn bộ app.

## Mô hình hóa Dịch vụ & Thiết kế SOA

**Câu 139 (q_139): Khi thiết kế phần mềm quản lý đào tạo, tập hợp đối tượng cốt lõi là:**
Đáp án đúng: C
Giải thích: Trong mô hình đào tạo giáo dục, cốt lõi là Sinh viên, Lớp học và Giảng viên.

**Câu 140 (q_140): Hệ thống quản lý thư viện, tập hợp đối tượng cốt lõi là:**
Đáp án đúng: B
Giải thích: Thư viện xoay quanh thực thể Sách, người mượn (Độc giả) và quá trình mượn (Phiếu mượn).

**Câu 141 (q_141): Hệ thống đặt vé máy bay, tập hợp đối tượng cốt lõi là:**
Đáp án đúng: C
Giải thích: Khách hàng đặt vé để đi trên một Chuyến bay. Ba thực thể chính là: Khách hàng, Chuyến bay, Vé máy bay.

**Câu 142 (q_142): Quản lý bệnh viện, tập hợp đối tượng cốt lõi là:**
Đáp án đúng: A
Giải thích: Bệnh viện xoay quanh việc Bác sĩ khám cho Bệnh nhân, và lưu lại trong Hồ sơ bệnh án.

**Câu 143 (q_143): Ứng dụng thương mại điện tử, tập hợp đối tượng cốt lõi là:**
Đáp án đúng: A
Giải thích: Khách hàng mua Sản phẩm, tạo ra các Đơn hàng.

**Câu 144 (q_144): Quản lý nhân sự, tập hợp đối tượng cốt lõi là:**
Đáp án đúng: A
Giải thích: Nhân sự (Nhân viên) làm việc ở các Phòng ban, và được trả Bảng lương.

**Câu 145 (q_145): Quản lý sự kiện, tập hợp đối tượng cốt lõi là:**
Đáp án đúng: C
Giải thích: Một sự kiện có người tham gia thông qua hành động đăng ký. (Người tham gia, Sự kiện, Đăng ký tham gia).

**Câu 146 (q_146): Kiến trúc hướng dịch vụ (SOA) dựa trên nguyên tắc nào?**
Đáp án đúng: A
Giải thích: Nguyên lý nền tảng của SOA là đóng gói các chức năng kinh doanh (business functions) thành các dịch vụ độc lập, có chuẩn giao tiếp chung để tái sử dụng ở nhiều nơi.
- Loại B: SOA yêu cầu liên kết lỏng (Loose coupling), không phải liên kết chặt (Tight coupling).
- Loại C: Dữ liệu có thể (và thường) phân tán theo từng dịch vụ.
- Loại D: Không liên quan đến thiết kế thủ tục.

**Câu 147 (q_147): Giao thức nào thường được sử dụng để giao tiếp giữa các dịch vụ trong kiến trúc hướng dịch vụ (SOA)?**
Đáp án đúng: C
Giải thích: SOAP (XML) là giao thức chuẩn mực truyền thống của SOA. Hiện nay, REST (JSON) thường được sử dụng thay thế do tính nhẹ và dễ phát triển.
- Loại A (FTP): Truyền file.
- Loại B (SMTP): Gửi email.
- Loại D (TCP/IP): Là tầng mạng cấp thấp, SOA dùng giao thức ứng dụng (HTTP/SOAP).

**Câu 148 (q_148): Thành phần nào trong kiến trúc hướng dịch vụ (SOA) giúp điều phối và quản lý các dịch vụ?**
Đáp án đúng: C
Giải thích: Enterprise Service Bus (ESB) là xương sống của SOA, nhận mọi thông điệp, điều phối (orchestration), định tuyến (routing) đến các dịch vụ thích hợp.
- Loại A, B: Là bên cung cấp và bên gọi dịch vụ.
- Loại D: Service Registry (như một trang danh bạ vàng) chỉ để tra cứu địa chỉ dịch vụ.

**Câu 149 (q_149): Mô hình nào sau đây thường được sử dụng để mô tả các dịch vụ trong kiến trúc hướng dịch vụ (SOA)?**
Đáp án đúng: C
Giải thích: WSDL (Web Services Description Language) là một file XML mô tả chi tiết đầu vào/đầu ra, các hàm (methods) mà một dịch vụ SOAP cung cấp để Client biết cách gọi.
- Loại A, B, D: Là các sơ đồ thiết kế hệ thống chung, không sinh ra code/định nghĩa giao tiếp mạng tự động như WSDL.

**Câu 150 (q_150): Một ứng dụng cần sử dụng các chức năng của một ứng dụng khác mà không cần biết chi tiết về cách thức hoạt động. Khái niệm nào trong SOA giúp đạt được điều này?**
Đáp án đúng: C
Giải thích: Liên kết lỏng lẻo (Loose coupling) cho phép bên gọi (Consumer) chỉ cần biết Interface (WSDL/API) của bên cung cấp mà không cần biết bên kia code bằng ngôn ngữ gì hay dùng Database nào.
- Loại A, B, D: Là đặc tính của Lập trình Hướng đối tượng (OOP).

**Câu 151 (q_151): Một hệ thống cần xử lý một lượng lớn các yêu cầu dịch vụ cùng lúc. Giải pháp nào sau đây giúp hệ thống mở rộng khả năng xử lý?**
Đáp án đúng: B
Giải thích: Áp dụng kiến trúc dịch vụ (Microservices/SOA), nhân bản dịch vụ đó lên nhiều máy chủ (Scale out) và dùng Load Balancing (Cân bằng tải) để chia đều lượng request vào các máy.
- Loại A: Scale up (máy chủ duy nhất mạnh) rất tốn kém và có giới hạn trần vật lý.
- Loại C: Gây nghẽn cổ chai (Bottleneck) ở DB.

**Câu 152 (q_152): Một hệ thống cần tìm kiếm và khám phá các dịch vụ web có sẵn. Thành phần nào trong SOA giúp thực hiện điều này?**
Đáp án đúng: D
Giải thích: Service Registry (như UDDI ngày xưa hoặc Consul/Eureka ngày nay) chứa danh bạ các dịch vụ. Khi một dịch vụ mới bật lên, nó đăng ký địa chỉ IP vào Registry để các dịch vụ khác có thể tìm thấy.
- Loại C: ESB điều phối đường đi thực tế, nhưng Registry là nơi tra cứu thông tin tĩnh.

**Câu 153 (q_153): Một ứng dụng cần sử dụng một dịch vụ web để gửi email. Giao thức nào sau đây thường được sử dụng cho việc này?**
Đáp án đúng: B
Giải thích: SMTP (Simple Mail Transfer Protocol) là chuẩn giao thức toàn cầu để gửi (push) email.

**Câu 154 (q_154): Ưu điểm của kiến trúc hướng dịch vụ (SOA) KHÔNG phải là?**
Đáp án đúng: D
Giải thích: SOA truyền dữ liệu qua mạng, đóng/mở gói XML/JSON nên chắc chắn chậm hơn gọi hàm trực tiếp trong RAM. Do đó "tăng hiệu suất chương trình" là sai, nó chỉ tăng hiệu năng phát triển và bảo trì.
- Loại A, B, C: Là các lợi ích vô giá của SOA.

**Câu 155 (q_155): Khi thiết kế kiến trúc SOA cho phần mềm quản lý bán hàng, tập hợp dịch vụ nào thể hiện chức năng cốt lõi?**
Đáp án đúng: B
Giải thích: Quản lý bán hàng gồm người mua (Khách hàng), hàng hóa (Sản phẩm), lên đơn (Đặt hàng) và thu tiền (Thanh toán).

**Câu 156 (q_156): Khi thiết kế kiến trúc SOA cho phần mềm quản lý dự án, tập hợp dịch vụ nào thể hiện chức năng cốt lõi?**
Đáp án đúng: B
Giải thích: Xoay quanh Dự án, các Công việc trong dự án đó, và các Thành viên thực hiện.

**Câu 157 (q_157): Khi thiết kế SOA cho phần mềm quản lý tài chính cá nhân, tập hợp dịch vụ nào thể hiện chức năng cốt lõi?**
Đáp án đúng: A
Giải thích: Ứng dụng tài chính gồm Người dùng (tài khoản cá nhân), tạo ra các Giao dịch (thu/chi), và xem lại tổng kết thông qua Báo cáo.
