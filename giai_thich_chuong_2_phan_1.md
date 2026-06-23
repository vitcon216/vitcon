# Giải thích chi tiết - Chương 2: Các mẫu kiến trúc phần mềm (Phần 1 - Câu 68 đến 97)

## Kiến trúc Ống và Lọc (Pipe and Filter)

**Câu 68 (q_68): Kiến trúc ống và lọc là gì?**
Đáp án đúng: B
Giải thích: Định nghĩa chuẩn của kiến trúc Pipe and Filter là chia quy trình thành các bước riêng biệt (bộ lọc) được liên kết bằng các kênh truyền tải (ống).
- Loại A: Định nghĩa quá chung chung và chưa nêu rõ được cơ chế chia nhỏ quy trình.
- Loại C: Đây là đặc điểm của kiến trúc chia sẻ bộ nhớ (Shared memory) hoặc Blackboard, nơi mọi thành phần cùng đọc/ghi vào một kho dữ liệu chung.
- Loại D: Đây không phải là mẫu kiến trúc sinh ra để dành riêng cho giao diện người dùng (UI), mà dùng cho luồng xử lý dữ liệu.

**Câu 69 (q_69): Điều nào sau đây là một đặc điểm của kiến trúc ống và lọc?**
Đáp án đúng: C
Giải thích: Tính mô-đun cao là ưu điểm nổi bật do mỗi bộ lọc (filter) chỉ thực hiện một nhiệm vụ độc lập và có thể thay thế dễ dàng.
- Loại A: Các bộ lọc hoạt động hoàn toàn độc lập, không phụ thuộc chặt chẽ vào nhau (loose coupling).
- Loại B: Kiến trúc này cho phép khả năng tái sử dụng bộ lọc rất cao ở nhiều quy trình khác nhau.
- Loại D: Kiến trúc này có khả năng mở rộng (scalability) tốt thông qua việc bổ sung thêm bộ lọc.

**Câu 70 (q_70): Trong kiến trúc ống và lọc, dữ liệu được xử lý như thế nào?**
Đáp án đúng: C
Giải thích: Dữ liệu đi qua các ống vào từng bộ lọc để xử lý theo một trình tự tuyến tính (tuần tự) đã được định sẵn.
- Loại A: Dữ liệu chảy theo luồng tuyến tính cố định, hoàn toàn không ngẫu nhiên.
- Loại B: Dù một số bộ lọc ở các giai đoạn khác nhau có thể chạy cùng lúc, nhưng dòng dữ liệu cho một chuỗi cụ thể vẫn có tính tuần tự, không thể "song song hoàn toàn" từ đầu đến cuối bỏ qua các bước.
- Loại D: Không phải hệ thống ống và lọc nào cũng xử lý thời gian thực, có rất nhiều hệ thống áp dụng xử lý theo lô (batch processing).

**Câu 71 (q_71): Một trong những thách thức chính của kiến trúc ống và lọc là gì?**
Đáp án đúng: B
Giải thích: Quá trình truyền, chuyển đổi định dạng và sao chép dữ liệu qua nhiều ống và bộ lọc khác nhau sinh ra chi phí hiệu năng (overhead).
- Loại A: Có thể quản lý trạng thái, dù việc này có thể làm mất đi tính stateless lý tưởng.
- Loại C: Việc xử lý lỗi không nhất thiết quá phức tạp nếu thiết kế từng module đủ tốt.
- Loại D: Việc khó quản lý trạng thái chưa phải là thách thức nghiêm trọng nhất bằng việc độ trễ bị tăng cao khi luân chuyển dữ liệu.

**Câu 72 (q_72): Chức năng chính của "bộ lọc" trong kiến trúc ống và lọc là gì?**
Đáp án đúng: B
Giải thích: Bộ lọc đóng vai trò nhận dữ liệu đầu vào, thực hiện một thao tác xử lý, biến đổi hoặc tính toán cụ thể, và đẩy dữ liệu đầu ra.
- Loại A: Đây là chức năng chính của các "ống" (pipe).
- Loại C: Lưu trữ dữ liệu thường không phải là nhiệm vụ của bộ lọc (chúng thường xử lý xong đẩy đi luôn).
- Loại D: Việc hiển thị kết quả cuối cùng thường thuộc về hệ thống giao diện, bộ lọc chỉ làm nhiệm vụ logic xử lý.

**Câu 73 (q_73): Một trong những nguyên tắc thiết kế của kiến trúc ống và lọc là gì?**
Đáp án đúng: B
Giải thích: Các bộ lọc nên là không trạng thái (stateless), giúp chúng hoạt động độc lập tuyệt đối, dễ bảo trì, thay thế mà không lo ảnh hưởng lịch sử dữ liệu cũ.
- Loại A: Các thành phần không được phụ thuộc lẫn nhau để đảm bảo tính độc lập.
- Loại C: Dữ liệu được xử lý có chủ đích theo luồng, không phải ngẫu nhiên.
- Loại D: Các ống chỉ được dùng làm kênh truyền dữ liệu, tuyệt đối không tham gia xử lý logic.

**Câu 74 (q_74): Tình huống nào sau đây phù hợp nhất để áp dụng kiến trúc Ống và Lọc?**
Đáp án đúng: B
Giải thích: Xử lý nhật ký (log) là ví dụ cực kì hoàn hảo: luồng log đi từ bước phân tích cú pháp -> trích xuất thông tin -> lưu trữ, theo đúng dòng tuyến tính.
- Loại A: Ứng dụng game 3D yêu cầu phản hồi và tương tác liên tục, thích hợp với Game Loop hoặc Event-driven.
- Loại C: Chỉnh sửa ảnh theo thứ tự bất kỳ không có tính tuyến tính, hợp với thiết kế hướng dịch vụ hoặc layer.
- Loại D: Web thương mại điện tử tương tác liên tục cần MVC hoặc kiến trúc hướng dịch vụ/Microservices.

**Câu 75 (q_75): Loại ứng dụng nào sau đây HƯỞNG LỢI NHIỀU NHẤT từ khả năng tái sử dụng của các bộ lọc trong kiến trúc Ống và Lọc?**
Đáp án đúng: B
Giải thích: Khi một bộ lọc (ví dụ: giải mã, mã hóa) có thể được ứng dụng vào nhiều quy trình nghiệp vụ khác nhau của hệ thống, nhà phát triển tiết kiệm được rất nhiều công sức.
- Loại A: Ứng dụng UI tùy biến cao nên dùng Component-based hoặc MVC.
- Loại C: Xử lý song song quá phức tạp nên dùng kiến trúc phân tán chuyên biệt.
- Loại D: Nếu các bước thay đổi quá thường xuyên, việc sắp xếp lại đường ống sẽ thành điểm yếu.

**Câu 76 (q_76): Trong tình huống nào sau đây, tính linh hoạt của kiến trúc Ống và Lọc là quan trọng nhất?**
Đáp án đúng: B
Giải thích: Tính linh hoạt giúp ta chèn thêm, rút bớt, hoặc đổi chỗ các bộ lọc một cách dễ dàng mà không phá vỡ mã nguồn toàn hệ thống.
- Loại A: Nếu ứng dụng cố định thì không cần tận dụng tính linh hoạt.
- Loại C: Kiến trúc này vốn không tối ưu cho "tương tác người dùng phức tạp".
- Loại D: Pipe and Filter không dành cho các hệ thống ưu tiên "độ trễ thấp nhất" vì chi phí truyền qua các ống.

**Câu 77 (q_77): Ứng dụng nào sau đây có thể tận dụng lợi thế của kiến trúc Ống và Lọc để xử lý khối lượng dữ liệu lớn?**
Đáp án đúng: B
Giải thích: Dữ liệu IoT đẩy liên tục thành dòng stream; áp dụng Pipe and Filter giúp dữ liệu được xử lý cuốn chiếu (tổng hợp, cảnh báo...) vô cùng hiệu quả với dữ liệu lớn.
- Loại A: Áp dụng ngẫu nhiên hiệu ứng phá vỡ tính dòng chảy của ống và lọc.
- Loại C: Trò chơi trực tuyến cần độ trễ thấp và đồng bộ liên tục (Client-Server / Peer-to-peer).
- Loại D: Soạn thảo văn bản cần kiến trúc hướng đối tượng, MVC hoặc Event-driven cho UI.

**Câu 78 (q_78): Trong tình huống nào sau đây, chi phí hiệu suất của việc truyền dữ liệu giữa các bộ lọc (một thách thức của kiến trúc Ống và Lọc) có thể là một vấn đề lớn?**
Đáp án đúng: B
Giải thích: Do mỗi lần truyền qua ống, dữ liệu có thể bị serialize/deserialize sinh ra độ trễ. Ứng dụng cần phản hồi thời gian thực cực thấp sẽ không chịu nổi khoản trễ này.
- Loại A: Hệ thống xử lý lô (batch) thường chạy nền, không khắt khe về từng mili-giây độ trễ.
- Loại C: Nếu phép biến đổi quá đơn giản thì bù trừ được vào tốc độ, ít phát sinh nghẽn.
- Loại D: Nếu cùng máy chủ thì độ trễ truyền ống sẽ ít hơn (truyền qua In-memory), không còn là vấn đề lớn.

**Câu 79 (q_79): Khi nào thì việc quản lý tài nguyên (CPU, bộ nhớ) trở thành một cân nhắc quan trọng khi sử dụng kiến trúc Ống và Lọc?**
Đáp án đúng: B
Giải thích: Trong chuỗi xử lý, nếu có 1 bộ lọc cực kỳ ngốn tài nguyên (nút thắt cổ chai) trong khi các bộ lọc khác nhẹ, ta phải quản lý tài nguyên khéo léo (chạy song song bộ lọc nặng, phân bổ CPU tốt) để không nghẽn cả đường ống.
- Loại A: Ứng dụng nhỏ thì không cần bận tâm nhiều về tối ưu tài nguyên cấp thiết.
- Loại C: Nếu mọi bộ lọc hao tổn giống nhau, luồng dữ liệu sẽ chảy rất đều.
- Loại D: Không yêu cầu mở rộng thì không cần quản lý và quy hoạch tài nguyên quá khắt khe.

**Câu 80 (q_80): Ứng dụng nào sau đây thường sử dụng kiến trúc ống và lọc?**
Đáp án đúng: B
Giải thích: Trình biên dịch (Compiler) là ứng dụng kinh điển của Pipe & Filter: Mã nguồn -> Phân tích từ vựng -> Phân tích cú pháp -> Phân tích ngữ nghĩa -> Sinh mã.
- Loại A: Hệ điều hành phức tạp, ưu tiên Layered (Phân lớp) hoặc Microkernel (Vi nhân).
- Loại C: Phần mềm văn phòng dùng MVC.
- Loại D: Trò chơi điện tử dùng ECS (Entity Component System) hoặc Game Loop.

**Câu 81 (q_81): Trong một hệ thống xử lý dữ liệu lớn, kiến trúc Ống và Lọc được sử dụng để thực hiện các bước: trích xuất, chuyển đổi và tải dữ liệu. Kết quả nổi bật của việc áp dụng kiến trúc này là gì?**
Đáp án đúng: A
Giải thích: Các luồng ETL (Extract, Transform, Load) chia rõ ràng thành các bộ lọc giúp hệ thống không bị rườm rà, rất dễ bảo trì hoặc sửa lỗi từng khâu độc lập.
- Loại B: Giảm phụ thuộc đúng, nhưng mục đích cuối cùng của giảm phụ thuộc chính là giảm độ phức tạp chung.
- Loại C: Đúng nhưng chưa đủ, thiếu ý quan trọng là nâng cao khả năng bảo trì.
- Loại D: Nó thường tăng hiệu suất xử lý chứ không giảm.

**Câu 82 (q_82): Trong một hệ thống xử lý luồng dữ liệu thời gian thực (ví dụ: Apache Flink, Apache Storm), kiến trúc Ống và Lọc được áp dụng để thực hiện các phép biến đổi dữ liệu liên tục. Kết quả chính là gì?**
Đáp án đúng: C
Giải thích: Thiết kế theo dạng pipeline (luồng liên tục) cho phép thông lượng dữ liệu (throughput) đi qua rất cao và độ trễ được kiểm soát ổn định.
- Loại A: Apache Flink/Storm là xử lý stream (thời gian thực), không phải xử lý lô (batch).
- Loại B: Các công cụ này giải quyết tốt vấn đề này thông qua kỹ thuật windowing chứ không tạo ra "khó khăn".
- Loại D: Dù tăng khả năng mở rộng, khả năng giữ thông lượng cao mới là kết quả cốt lõi của xử lý biến đổi dòng chảy.

**Câu 83 (q_83): Trong một hệ thống tích hợp dữ liệu (ví dụ: Apache NiFi), kiến trúc Ống và Lọc được sử dụng để tự động hóa luồng dữ liệu giữa các hệ thống. Kết quả chính là gì?**
Đáp án đúng: B
Giải thích: Người dùng có thể kéo thả để xây dựng các luồng đường ống, định tuyến và chuyển đổi dữ liệu đi khắp hệ thống linh hoạt nhất có thể.
- Loại A: Việc kết nối là dễ dàng chứ không phải "khó khăn".
- Loại C: Khả năng đổi định dạng chỉ là một mảnh ghép nhỏ của việc quản lý luồng dữ liệu tổng thể.
- Loại D: Việc giảm phụ thuộc vào nhà cung cấp (vendor lock-in) không liên quan trực tiếp đến thiết kế Pipe and Filter.

**Câu 84 (q_84): Trong một hệ thống xử lý dữ liệu giáo dục, bộ lọc nào sau đây KHÔNG cần khả năng xử lý dữ liệu học sinh?**
Đáp án đúng: D
Giải thích: "Tài chính" (thu học phí, học bổng) là một luồng (domain) nghiệp vụ hoàn toàn khác và tách biệt, không thuộc về luồng "giáo dục/học thuật" của học sinh.
- Loại A, B, C: Lưu trữ thông tin, phân tích kết quả, và tạo báo cáo đều là các bước xử lý liên tục trực tiếp lên dữ liệu giáo dục học thuật của sinh viên.

**Câu 85 (q_85): Trong một hệ thống xử lý dữ liệu lớn, bộ lọc nào sau đây nên được thiết kế để chạy song song?**
Đáp án đúng: C
Giải thích: Bộ lọc tính toán thống kê tốn tài nguyên và dễ chia nhỏ (chia để trị - MapReduce) nên cần chạy song song trên nhiều luồng/máy chủ để giải quyết nút thắt cổ chai.
- Loại A, B: Đọc ghi tệp tin thường bị giới hạn bởi ổ cứng vật lý (I/O) nên chạy song song quá mức dễ gây nghẽn.
- Loại D: Kiểm tra hợp lệ thường rất nhẹ và nhanh, chạy song song cũng không cải thiện hiệu năng nhiều.

**Câu 86 (q_86): Khi nào thì việc cô lập lỗi của kiến trúc Ống và Lọc trở nên đặc biệt quan trọng?**
Đáp án đúng: B
Giải thích: Ở hệ thống tài chính, nếu để lỗi sai số học lọt qua bước tiếp theo sẽ gây thiệt hại tiền bạc. Việc một bộ lọc lỗi tự sập và cách ly không lây lan sang các bộ lọc khác là tính năng cứu mạng.
- Loại A: Ứng dụng nhỏ thì lỗi dễ phát hiện và chi phí rủi ro thấp.
- Loại C: Ứng dụng web chú trọng UX hơn, thường lỗi backend sẽ trả về mã lỗi 500 chứ không quan trọng việc cô lập luồng ống bằng hệ thống tài chính.
- Loại D: Thường thì cô lập lỗi, giám sát chặt chẽ làm giảm hiệu suất một chút chứ không giúp nó nhanh lên.

**Câu 87 (q_87): Ứng dụng nào sau đây có thể gặp khó khăn trong việc áp dụng kiến trúc Ống và Lọc do yêu cầu quản lý trạng thái phức tạp?**
Đáp án đúng: C
Giải thích: Ứng dụng web cần duy trì thông tin người dùng (session/state) liên tục qua các trang. Tuy nhiên, Pipe and Filter đòi hỏi các bộ lọc không có trạng thái (stateless), nếu bắt ép áp dụng sẽ rất khó khăn và gượng gạo.
- Loại A: Trình biên dịch là hình mẫu lý tưởng nhất của Pipe and Filter.
- Loại B: Ứng dụng luồng dữ liệu cực kỳ phù hợp với Pipe and Filter.
- Loại D: Hệ thống ETL là một ví dụ hoàn hảo không kém vì nó chỉ xử lý dữ liệu chảy một chiều.

## Kiến trúc Hướng Sự Kiện (Event-Driven Architecture)

**Câu 88 (q_88): Kiến trúc hướng sự kiện (EDA) là gì?**
Đáp án đúng: B
Giải thích: EDA là kiến trúc phân tán mà ở đó các thành phần không gọi hàm nhau trực tiếp mà tương tác gián tiếp bằng cách phát ra và lắng nghe các "Sự kiện" (Events).
- Loại A: "Các sự kiện giao tiếp với nhau" là sai, vì sự kiện chỉ là gói dữ liệu, các "thành phần" (components) mới là thứ giao tiếp với nhau.
- Loại C: Không bắt buộc giao tiếp qua CSDL chung, thường dùng Message Broker.
- Loại D: Giao tiếp qua RPC là đặc trưng của kiến trúc hướng dịch vụ (SOA) hoặc Microservices gọi trực tiếp đồng bộ.

**Câu 89 (q_89): Lợi ích chính của việc sử dụng kiến trúc hướng sự kiện (EDA) là gì?**
Đáp án đúng: A
Giải thích: Bằng cách tách biệt người gửi (Publisher) và người nhận (Subscriber), các thành phần hoàn toàn độc lập (loose coupling), rất dễ mở rộng và không bị lỗi dây chuyền (fault tolerance).
- Loại B: Bảo mật không phải là một lợi ích tự nhiên sinh ra từ EDA.
- Loại C: EDA thường làm hệ thống khó kiểm thử hơn do tính chất bất đồng bộ.
- Loại D: Khả năng tái sử dụng mã thuộc về Component-based hoặc SOA nhiều hơn.

**Câu 90 (q_90): Nhược điểm chính của việc sử dụng kiến trúc hướng sự kiện (EDA) là gì?**
Đáp án đúng: A
Giải thích: Do tính chất bất đồng bộ và rải rác, việc dò tìm luồng dữ liệu (tracing), gỡ lỗi (debugging) và kiểm thử (testing) là cực kỳ khó khăn.
- Loại B: EDA nổi tiếng vì khả năng mở rộng tuyệt vời, không phải hạn chế.
- Loại C: Chi phí và tốc độ phát triển không cố định, phụ thuộc quy mô.
- Loại D: Tính tương tác cực kì tốt (giữa các hệ thống dị đồng).

**Câu 91 (q_91): Mô hình giao tiếp nào được sử dụng phổ biến trong kiến trúc hướng sự kiện (EDA)?**
Đáp án đúng: B
Giải thích: Mô hình Xuất bản - Đăng ký (Publish-Subscribe hay Pub/Sub) là mô hình cốt lõi của EDA, cho phép một sự kiện phát ra có thể được nhiều người tiêu thụ (Subscribers) bắt lấy.
- Loại A: Request-Response là đồng bộ (REST, RPC).
- Loại C: Client-Server quá chung chung và thường là đồng bộ.
- Loại D: Ngang hàng (P2P) dùng cho kiến trúc phi tập trung.

**Câu 92 (q_92): Loại sự kiện nào thường được sử dụng trong kiến trúc hướng sự kiện (EDA)?**
Đáp án đúng: C
Giải thích: Hệ thống EDA phân biệt giữa sự kiện miền (Domain Events - sự việc quan trọng xảy ra trong nghiệp vụ) và sự kiện tích hợp (Integration Events - thông báo để đồng bộ dữ liệu giữa các hệ thống khác nhau).
- Loại A, B: Chỉ nêu được 1 khía cạnh, thiếu khía cạnh còn lại.
- Loại D: Hoàn toàn sai.

**Câu 93 (q_93): Bộ định tuyến sự kiện có vai trò gì trong kiến trúc hướng sự kiện (EDA)?**
Đáp án đúng: C
Giải thích: Router (hoặc Broker) đóng vai trò trung chuyển, nhận sự kiện từ người sản xuất và phân phối (định tuyến) đến đúng các hàng đợi của những người tiêu thụ đang quan tâm (Subscribers).
- Loại A: Producer tạo ra sự kiện, không phải Router.
- Loại B: Consumer tiêu thụ sự kiện.
- Loại D: Lưu trữ sự kiện lâu dài là chức năng của Event Store.

**Câu 94 (q_94): Người tiêu dùng sự kiện có vai trò gì trong kiến trúc hướng sự kiện (EDA)?**
Đáp án đúng: B
Giải thích: Consumer (Người tiêu thụ/người đăng ký) sẽ lắng nghe hàng đợi sự kiện, khi có sự kiện đến, nó sẽ nhận dữ liệu và kích hoạt hành động nghiệp vụ nội bộ của nó.
- Loại A: Producer (Người sản xuất) tạo ra sự kiện.
- Loại C: Broker (Bộ định tuyến) định tuyến sự kiện.
- Loại D: Event Store (Kho sự kiện) lưu trữ sự kiện.

**Câu 95 (q_95): Hai mô hình phổ biến của kiến trúc hướng sự kiện là gì?**
Đáp án đúng: C
Giải thích: Broker Topology (Phân tán, không có trung tâm điều phối, các thành phần tự phát/nhận qua Broker) và Mediator Topology (Có một bộ điều phối trung tâm kiểm soát thứ tự các bước).
- Loại A: Là hai mô hình tổng quát khác (Client-server và Microservices).
- Loại B: Monolithic là nguyên khối.
- Loại D: Layered (phân lớp) không liên quan.

**Câu 96 (q_96): Trong Broker topology, các event được phân phối đến event processor thông qua thành phần nào?**
Đáp án đúng: D
Giải thích: Event Channel (Kênh sự kiện) là đường truyền (topic, queue) bên trong Message Broker dùng để phân phối sự kiện từ Initiator đến Processor.
- Loại A: Mediator thuộc mô hình Mediator Topology, không phải Broker.
- Loại B: Event Queue chỉ là nơi chứa, khái niệm rộng hơn là Event Channel.
- Loại C: Message Broker là cả một hệ thống lớn chứa các Event Channels bên trong.

**Câu 97 (q_97): Thành phần nào trong Mediator topology đóng vai trò điều phối và quản lý luồng sự kiện?**
Đáp án đúng: C
Giải thích: Event Mediator (Bộ điều phối sự kiện) nhận sự kiện ban đầu, phân tích và chủ động gọi (hoặc gửi thông điệp cho) các thành phần khác theo đúng trình tự nghiệp vụ phức tạp.
- Loại A, B: Tên không chuẩn (Queue Mediator, Channel Mediator).
- Loại D: Event Processor là thành phần thực hiện logic, không phải thành phần điều phối tổng.
