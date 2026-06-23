# Giải thích chi tiết - Chương 1: Tổng quan Kiến trúc phần mềm (Phần 1 - Câu 1 đến 35)

**Câu 1 (q_1): Kiến trúc phần mềm là gì?**
Đáp án đúng: B
Giải thích: Cấu trúc tổng thể của một hệ thống phần mềm, bao gồm các thành phần, mối quan hệ giữa chúng và các nguyên tắc chi phối thiết kế và phát triển.
- Loại A: Quá trình viết mã là khâu lập trình (Implementation), chỉ là một phần nhỏ.
- Loại C: Giao diện và ngôn ngữ lập trình là chi tiết cài đặt cụ thể, kiến trúc phần mềm không bắt buộc phải quy định cứng nhắc các chi tiết này ở mức độ tổng quát.

**Câu 2 (q_2): Chọn khái niệm đúng về kiến trúc phần mềm:**
Đáp án đúng: A
Giải thích: Kiến trúc phần mềm là cấu trúc cơ bản của một hệ thống phần mềm, bao gồm các thành phần, mối quan hệ giữa chúng và các nguyên tắc hướng dẫn thiết kế và phát triển.
- Loại B: Kiến trúc hướng dẫn "thiết kế", không phải hướng dẫn chi tiết "cài đặt và lập trình".
- Loại C: Việc "kiểm thử" nằm ở khâu Testing, không phải cốt lõi của việc định nghĩa kiến trúc.
- Loại D: "Phân tích và bảo trì" là các giai đoạn khác, kiến trúc chủ yếu tập trung vào cấu trúc và thiết kế.

**Câu 3 (q_3): Ai trong số những người sau đây không được biết đến với việc đưa ra các khái niệm chính thức về kiến trúc phần mềm?**
Đáp án đúng: D
Giải thích: Bill Gates là nhà sáng lập Microsoft, một doanh nhân và lập trình viên, nhưng không phải là nhà nghiên cứu học thuật nổi tiếng đưa ra định nghĩa chuẩn mực về Kiến trúc phần mềm.
- Loại A (Grady Booch): Đồng sáng lập UML, nhà thiết kế phần mềm nổi tiếng.
- Loại B (Martin Fowler): Tác giả nổi tiếng về thiết kế phần mềm và Refactoring.
- Loại C (Bass et al): Các tác giả của cuốn sách kinh điển "Software Architecture in Practice".

**Câu 4 (q_4): Mục tiêu chính của kiến trúc phần mềm là gì?**
Đáp án đúng: B
Giải thích: Mục tiêu quan trọng nhất là tạo ra một hệ thống dễ hiểu, dễ quản lý, từ đó giảm thiểu công sức bảo trì và nâng cấp phần mềm sau này.
- Loại A: Tạo ra mã nguồn phức tạp là điều tối kỵ trong kỹ thuật phần mềm.
- Loại C: Tối ưu hiệu suất phần cứng là việc của hệ điều hành hoặc kỹ sư phần cứng, kiến trúc phần mềm tối ưu hiệu suất phần mềm.
- Loại D: Tính thẩm mỹ giao diện thuộc về lĩnh vực UI/UX Design.

**Câu 5 (q_5): Kiến trúc phần mềm ảnh hưởng chủ yếu đến những yếu tố nào của hệ thống?**
Đáp án đúng: A
Giải thích: Kiến trúc định hình các thuộc tính chất lượng (Quality Attributes) cốt lõi như hiệu năng, khả năng bảo trì, khả năng mở rộng, và độ tin cậy.
- Loại B: Màu sắc giao diện hoàn toàn không liên quan đến kiến trúc tổng thể.
- Loại C: Ngôn ngữ lập trình là công cụ triển khai, có thể thay đổi mà cấu trúc (kiến trúc) vẫn giữ nguyên.
- Loại D: Hệ điều hành là môi trường nền tảng, không phải yếu tố cốt lõi do KTPM quyết định.

**Câu 6 (q_6): Các bên liên quan (stakeholders) quan tâm đến kiến trúc phần mềm bao gồm:**
Đáp án đúng: B
Giải thích: Bao gồm tất cả những người chịu ảnh hưởng hoặc tham gia: Người dùng cuối, nhà phát triển, quản lý dự án, kiến trúc sư phần mềm.
- Loại A: Thiếu người dùng và kiến trúc sư.
- Loại C: Quá thiếu sót.
- Loại D: Chỉ gồm nhà thiết kế và kiến trúc sư là không đủ, bỏ qua khách hàng và người phát triển.

**Câu 7 (q_7): Đâu là hướng dẫn khi kiến trúc một hệ thống:**
Đáp án đúng: A
Giải thích: Nguyên tắc trừu tượng hóa (Abstraction): Kiến trúc cần thể hiện được cấu trúc tổng quan nhưng phải ẩn giấu các chi tiết cài đặt phức tạp bên trong để dễ hình dung.
- Loại B: Nếu không thể hiện cấu trúc thì không còn là kiến trúc.
- Loại C: Không ẩn giấu chi tiết cài đặt sẽ làm bản vẽ/kiến trúc trở nên quá tải và rối rắm.
- Loại D: Phủ định lại cả hai nguyên tắc cơ bản nhất của kiến trúc.

**Câu 8 (q_8): Thành phần phần mềm được định nghĩa là:**
Đáp án đúng: B
Giải thích: Một đơn vị mô-đun của phần mềm, có tính độc lập, có thể thay thế được, và đóng gói một chức năng cụ thể để cung cấp dịch vụ thông qua giao diện.
- Loại A: Dòng mã quá nhỏ bé, không tạo thành một mô-đun.
- Loại C: Tệp tin dữ liệu là tài nguyên, không phải thành phần xử lý logic.
- Loại D: Tài liệu hướng dẫn không phải là mã phần mềm.

**Câu 9 (q_9): Đặc điểm nào sau đây KHÔNG phải là đặc điểm của thành phần phần mềm?**
Đáp án đúng: C
Giải thích: Tính phụ thuộc chặt chẽ (Tight Coupling) là đặc điểm tồi tệ. Thành phần tốt phải có tính phụ thuộc lỏng lẻo (Loose Coupling).
- Loại A (Tính mô-đun): Là đặc điểm cốt lõi.
- Loại B (Tính đóng gói): Giúp che giấu chi tiết bên trong.
- Loại D (Tính tái sử dụng): Giúp sử dụng lại ở nhiều hệ thống.

**Câu 10 (q_10): Vai trò chính của thành phần phần mềm trong kiến trúc phần mềm là gì?**
Đáp án đúng: C
Giải thích: Thành phần đóng vai trò như những viên gạch (khối xây dựng cơ bản) để lắp ráp và cấu thành nên toàn bộ kiến trúc hệ thống.
- Loại A: Quản lý tài nguyên là nhiệm vụ của OS hoặc middleware.
- Loại B: Chỉ là vai trò của thành phần UI, không đại diện cho mọi thành phần phần mềm.
- Loại D: Tối ưu hiệu suất phần cứng không phải chức năng cốt lõi.

**Câu 11 (q_11): Giao diện của thành phần phần mềm được sử dụng để:**
Đáp án đúng: C
Giải thích: Interface (Giao diện) có hai mục đích: che giấu logic nội bộ (đóng gói) và phơi bày các phương thức để các thành phần khác có thể tương tác (gọi hàm).
- Loại A: Chỉ đúng một nửa (thiếu tương tác).
- Loại B: Chỉ đúng một nửa (thiếu tính đóng gói).
- Loại D: Hoàn toàn sai bản chất.

**Câu 12 (q_12): Lợi ích chính của việc sử dụng thành phần phần mềm là:**
Đáp án đúng: D
Giải thích: Nó mang lại tất cả các lợi ích: Chia để trị giúp giảm phức tạp, sử dụng lại mã giúp tăng tốc độ phát triển và tiết kiệm chi phí.
- Loại A, B, C: Đều là các ý đúng nhưng chưa đầy đủ bằng phương án D.

**Câu 13 (q_13): Trong một ứng dụng web, thành phần nào sau đây có thể được coi là một thành phần phần mềm?**
Đáp án đúng: D
Giải thích: Một hệ thống web tiêu chuẩn thường chia làm 3 lớp thành phần (3-tier): UI (Giao diện), Business logic (Nghiệp vụ), và Data access (Truy cập dữ liệu).
- Loại A, B, C: Bị thiếu một hoặc nhiều thành phần cốt lõi của ứng dụng Web.

**Câu 14 (q_14): Tính "đóng gói" của thành phần phần mềm có nghĩa là:**
Đáp án đúng: B
Giải thích: Đóng gói (Encapsulation) là việc che giấu sự phức tạp và dữ liệu bên trong thành phần, chỉ giao tiếp với bên ngoài thông qua một giao diện chung (API) được định nghĩa sẵn.
- Loại A: Đây là định nghĩa của tính di động (Portability) và tái sử dụng (Reusability).
- Loại C: Đây là định nghĩa của tái sử dụng.
- Loại D: Đây là định nghĩa của tính thay thế (Replaceability).

**Câu 15 (q_15): Kết nối (connector) trong kiến trúc phần mềm có nhiệm vụ chính là:**
Đáp án đúng: B
Giải thích: Connector (Đường ống, Middleware, Giao thức...) làm nhiệm vụ nối các thành phần lại với nhau và thực thi việc truyền nhận dữ liệu, tương tác giữa chúng.
- Loại A: Lưu trữ dữ liệu là của cơ sở dữ liệu (Component).
- Loại C: Quản lý giao diện là nhiệm vụ của UI Component.
- Loại D: Connector thường làm tăng chi phí truyền dẫn, không tối ưu hóa phần cứng.

**Câu 16 (q_16): Kết nối giúp kiến trúc sư phần mềm làm gì?**
Đáp án đúng: B
Giải thích: Nó giúp xác định rõ ràng cơ chế giao tiếp, giao thức, và cách luân chuyển dữ liệu giữa các khối thành phần với nhau.
- Loại A: Cấu trúc tổng thể được xác định bởi cả Component và Connector.
- Loại C: Vòng đời phần mềm thuộc về quy trình quản lý dự án (SDLC).
- Loại D: Tối ưu mã nguồn thuộc về lập trình viên (Dev).

**Câu 17 (q_17): Trong một ứng dụng web, kết nối nào cho phép trình duyệt web giao tiếp với máy chủ web?**
Đáp án đúng: B
Giải thích: HTTP (HyperText Transfer Protocol) là giao thức truyền tải siêu văn bản, tiêu chuẩn số 1 để kết nối giữa Browser (Client) và Server.
- Loại A: SQL dùng để giao tiếp với hệ quản trị cơ sở dữ liệu.
- Loại C: XML là định dạng dữ liệu, không phải kết nối.
- Loại D: JSON là định dạng dữ liệu.

**Câu 18 (q_18): Hình thức kết nối "Truy nhập dữ liệu chung" cho phép các thành phần tương tác bằng cách nào?**
Đáp án đúng: B
Giải thích: Shared Data/Memory cho phép các thành phần giao tiếp bằng cách cùng đọc và ghi thông tin vào một vùng nhớ, kho lưu trữ (vd: Database chung, Blackboard).
- Loại A: Gửi thông điệp/Gọi phương thức là kết nối gọi thủ tục hoặc message passing.
- Loại C: Gọi từ xa (RPC) là kết nối mạng.
- Loại D: Socket là kết nối luồng.

**Câu 19 (q_19): Trong các hệ phần mềm phức tạp trên mạng, kết nối thường diễn ra giữa bao nhiêu thành phần?**
Đáp án đúng: B
Giải thích: Thường thiết kế theo mô hình Client-Server hoặc Microservices, nơi một thành phần (Client) kết nối đến nhiều thành phần dịch vụ cung cấp chức năng khác nhau.
- Loại A: Hai thành phần quá đơn giản, không phản ánh hệ thống phức tạp trên mạng.
- Loại C: Các thành phần cùng cấp (Peer-to-peer) ít phổ biến hơn client-server trong mô hình doanh nghiệp phức tạp thông thường.
- Loại D: Mô hình cây bị giới hạn về luồng giao tiếp chéo.

**Câu 20 (q_20): Loại kết nối nào được sử dụng để truyền một lượng lớn dữ liệu giữa các tiến trình độc lập?**
Đáp án đúng: C
Giải thích: Kết nối luồng (Stream connector như TCP socket, pipe) được dùng để bơm liên tục một lượng lớn dữ liệu (streaming) giữa các tiến trình mà không làm gián đoạn.
- Loại A: Gọi thủ tục (RPC) thường dùng cho lệnh ngắn, dữ liệu nhỏ.
- Loại B: Kết nối sự kiện chỉ gửi thông điệp ngắn gọn (Event/Message).
- Loại D: Trung gian (Broker) có thể bị nghẽn nếu truyền dữ liệu luồng khổng lồ liên tục.

**Câu 21 (q_21): Ví dụ nào sau đây KHÔNG thuộc về "Kết nối luồng"?**
Đáp án đúng: C
Giải thích: Lời gọi phương thức trong OOP là gọi hàm (Procedure Call) đồng bộ và tức thì, không phải là cơ chế mở luồng truyền dữ liệu liên tục như Stream.
- Loại A: Socket TCP/UDP tạo luồng mạng.
- Loại B: FTP dùng TCP stream để truyền file.
- Loại D: Dù SOAP dùng HTTP nhưng nó vẫn có thể truyền payload lớn qua luồng mạng, tuy nhiên C sai rõ ràng nhất vì nó hoàn toàn chạy in-memory call. *(Ghi chú: SOAP thường được coi là RPC hơn là luồng, nhưng trong đáp án C chắc chắn sai nhất)*

**Câu 22 (q_22): "Kết nối trung gian" thường được sử dụng trong trường hợp nào?**
Đáp án đúng: B
Giải thích: Trung gian (Message Broker, Event Bus) giúp giải quyết sự phụ thuộc: Thành phần gửi không cần biết thành phần nhận là ai, sống hay chết (Loose coupling).
- Loại A: Nếu biết rõ nhau, họ có thể gọi trực tiếp (Direct Call).
- Loại C: Dữ liệu nhỏ hay lớn không quyết định việc dùng trung gian bằng sự "không biết nhau" (Decoupling).
- Loại D: Client-server thường biết địa chỉ của nhau (IP/Port).

**Câu 23 (q_23): Loại kết nối nào được sử dụng để chỉ ra các tuyến tương tác và điều phối truyền thông giữa các thành phần?**
Đáp án đúng: B
Giải thích: "Tuyến" (Routing/Topology) điều phối luồng thông tin đi qua hệ thống như thế nào (Ví dụ: Enterprise Service Bus định tuyến dữ liệu).
- Loại A, C, D: Là các loại kết nối hướng sự kiện hoặc thích nghi không chuyên tập trung vào "định tuyến".

**Câu 24 (q_24): Kiến trúc phần mềm đóng vai trò gì trong phát triển phần mềm?**
Đáp án đúng: B
Giải thích: Cung cấp tầm nhìn chiến lược, định hướng công nghệ và khung sườn cấu trúc làm nền móng cho tất cả các hoạt động phát triển sau này.
- Loại A: Chỉ thiết kế giao diện là quá hẹp.
- Loại C: Tối ưu phần cứng là phần phụ.
- Loại D: Chỉ quản lý CSDL là khâu Data Modeling.

**Câu 25 (q_25): Kiến trúc phần mềm ảnh hưởng đến thuộc tính chất lượng nào của phần mềm?**
Đáp án đúng: C
Giải thích: Kiến trúc tốt ảnh hưởng đến toàn bộ các thuộc tính hệ thống (NFR - Non-functional requirements): Hiệu suất, mở rộng, tin cậy, bảo trì, bảo mật.
- Loại A, B, D: Đều nêu thiếu một trong các thuộc tính cốt lõi.

**Câu 26 (q_26): Lợi ích chính của việc có một kiến trúc phần mềm tốt là gì?**
Đáp án đúng: B
Giải thích: Bằng cách định hình mọi thứ ngay từ đầu, rủi ro đập đi xây lại ở giai đoạn sau (chi phí cực kỳ tốn kém) sẽ được giảm thiểu tối đa.
- Loại A: Tăng chi phí phát triển là sai (nó giúp giảm chi phí dài hạn).
- Loại C: Tăng sự phức tạp là thiết kế tồi.
- Loại D: Thiết kế tốt làm tăng tốc độ phát triển.

**Câu 27 (q_27): Kiến trúc phần mềm giúp gì trong giao tiếp và hợp tác giữa các bên liên quan?**
Đáp án đúng: B
Giải thích: Nó tạo ra các biểu đồ, tài liệu tổng quan để sếp, lập trình viên, khách hàng đều có thể nhìn vào và hiểu hệ thống hoạt động ra sao.
- Loại A: Hợp đồng giá cả chỉ là yếu tố thương mại, không phải mục đích giao tiếp kỹ thuật.
- Loại C: Phải làm tăng sự tương tác và thống nhất, không phải giảm.
- Loại D: Hoàn toàn sai.

**Câu 28 (q_28): Tại sao kiến trúc phần mềm lại quan trọng trong việc bảo trì phần mềm?**
Đáp án đúng: B
Giải thích: Nhờ tính mô-đun hóa và tách biệt trách nhiệm, khi có lỗi hay cần nâng cấp, lập trình viên biết chính xác phải sửa ở đâu mà không làm sập phần khác.
- Loại A: Độ phức tạp mã nguồn (logic) nằm ở lập trình, kiến trúc không giải quyết trực tiếp logic hàm.
- Loại C: Mọi phần mềm đều phải bảo trì.
- Loại D: Sai hoàn toàn.

**Câu 29 (q_29): Kiến trúc phần mềm giúp phát hiện và giải quyết vấn đề thiết kế khi nào?**
Đáp án đúng: C
Giải thích: KTPM được làm ở khâu đầu dự án. Phát hiện lỗi thiết kế ở khâu này rẻ hơn gấp 100 lần so với lúc code đã viết xong.
- Loại A: Sau triển khai mới phát hiện thì hậu quả rất lớn.
- Loại B: Kiểm thử là để phát hiện lỗi logic code, thiết kế phải chốt từ trước đó.
- Loại D: Sai hoàn toàn.

**Câu 30 (q_30): Kiến trúc phần mềm giúp tối ưu hóa việc sử dụng tài nguyên nào?**
Đáp án đúng: C
Giải thích: Kiến trúc tốt quyết định cách hệ thống tiêu thụ RAM, cách CPU xử lý đa luồng, và lưu lượng mạng truyền đi có bị nghẽn không.
- Loại A, B: Nêu thiếu tài nguyên mạng.
- Loại D: "Bất kỳ khác" là không chính xác, nó chỉ ảnh hưởng tài nguyên liên quan đến máy tính.

**Câu 31 (q_31): Kiến trúc phần mềm giúp hệ thống dễ dàng thích ứng với thay đổi nào?**
Đáp án đúng: C
Giải thích: Nếu yêu cầu kinh doanh đổi (chức năng) hoặc đổi server từ Windows sang Linux (môi trường), một kiến trúc linh hoạt (layered, microservices) sẽ giúp chuyển đổi dễ dàng.
- Loại A: Không chỉ chức năng mà cả phi chức năng.
- Loại B: Đối tượng sử dụng thay đổi thường liên quan UX nhiều hơn.
- Loại D: Phủ định sai.

**Câu 32 (q_32): Kiến trúc phần mềm giúp giảm thiểu rủi ro nào trong quá trình phát triển?**
Đáp án đúng: C
Giải thích: Rủi ro trễ tiến độ (thời gian), đội vốn (chi phí) và lỗi hệ thống sập (chất lượng) đều được giải quyết nhờ bản vẽ thiết kế tốt.
- Loại A, B: Thiếu các yếu tố cốt lõi còn lại.
- Loại D: Phủ định sai.

**Câu 33 (q_33): Vai trò của kiến trúc phần mềm trong việc đảm bảo độ tin cậy là gì?**
Đáp án đúng: B
Giải thích: Các kiến trúc nhắm vào độ tin cậy (như failover, load balancing, redundancy) giúp hệ thống cô lập lỗi, tránh sập toàn hệ thống và luôn giữ được độ sẵn sàng (Availability).
- Loại A: Giảm độ phức tạp giúp dễ bảo trì, nhưng độ tin cậy thường yêu cầu thêm cơ chế dự phòng (phức tạp hơn).
- Loại C: Tăng chi phí là nhược điểm.
- Loại D: Hoàn toàn sai.

**Câu 34 (q_34): Kiến trúc phần mềm giúp tối ưu hóa hiệu suất như thế nào?**
Đáp án đúng: B
Giải thích: Kiến trúc tối ưu bằng cách quản lý bộ nhớ đệm (caching), xử lý bất đồng bộ, cân bằng tải, từ đó sử dụng tài nguyên hiệu quả nhất và phản hồi cực nhanh (giảm độ trễ).
- Loại A: Tăng sự phụ thuộc sẽ làm giảm hiệu suất, gây nghẽn cổ chai.
- Loại C: Sự phụ thuộc cao luôn là kẻ thù của hiệu suất.
- Loại D: Sai hoàn toàn.

**Câu 35 (q_35): Thuộc tính chất lượng nào đo lường khả năng phần mềm hoạt động ổn định và không bị lỗi?**
Đáp án đúng: C
Giải thích: Độ tin cậy (Reliability) là xác suất phần mềm chạy mà không có sự cố trong một khoảng thời gian nhất định trong môi trường đã định.
- Loại A: Hiệu suất (Performance) là tốc độ xử lý.
- Loại B: Mở rộng (Scalability) là chịu tải lớn.
- Loại D: Bảo trì (Maintainability) là dễ sửa đổi code.
