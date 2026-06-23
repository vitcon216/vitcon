# Giải thích chi tiết - Chương 4: Thiết kế mẫu (Design Patterns)

**Câu 1 (q_194): Trong một ứng dụng quản lý cấu hình, bạn cần đảm bảo chỉ có một đối tượng cấu hình duy nhất. Mẫu thiết kế nào phù hợp?**
Đáp án đúng: C
Giải thích: Mẫu Singleton được sử dụng để đảm bảo rằng một lớp chỉ có duy nhất một thể hiện (instance) và cung cấp một điểm truy cập toàn cục tới thể hiện đó.
- Loại A (Factory Method): Dùng để tạo đối tượng thông qua interface, không giới hạn số lượng đối tượng được tạo ra.
- Loại B (Abstract Factory): Dùng để tạo ra các họ đối tượng liên quan với nhau, không đảm bảo tính duy nhất.
- Loại D (Builder): Dùng để xây dựng một đối tượng phức tạp từng bước, không liên quan đến việc giới hạn số lượng thể hiện.

**Câu 2 (q_195): Bạn cần tạo ra các loại báo cáo khác nhau (PDF, Excel, Word) từ một giao diện chung. Mẫu thiết kế nào phù hợp?**
Đáp án đúng: B
Giải thích: Factory Method cung cấp một interface để tạo đối tượng, nhưng để các lớp con quyết định lớp nào sẽ được khởi tạo (PDF, Excel, Word).
- Loại A (Prototype): Dùng để copy (clone) từ một mẫu có sẵn, không phải để tạo ra các loại báo cáo khác nhau.
- Loại C (Singleton): Đảm bảo duy nhất một đối tượng, không phù hợp để tạo nhiều báo cáo.
- Loại D (Builder): Dùng để xây dựng từng phần của đối tượng phức tạp, trong khi ở đây chỉ cần tạo ra toàn bộ báo cáo từ một loại.

**Câu 3 (q_196): Một ứng dụng cần tạo ra các giao diện người dùng cho các nền tảng khác nhau (Windows, macOS, Linux). Mẫu thiết kế nào phù hợp?**
Đáp án đúng: C
Giải thích: Abstract Factory cung cấp interface để tạo ra các "họ" (families) đối tượng liên quan (như nút bấm, thanh cuộn...) cho từng nền tảng mà không chỉ định lớp cụ thể.
- Loại A (Prototype): Tập trung vào việc nhân bản đối tượng.
- Loại B (Factory Method): Thường chỉ tạo ra một sản phẩm duy nhất, không phù hợp tạo "họ" các sản phẩm giao diện.
- Loại D (Builder): Dùng để lắp ráp đối tượng phức tạp thay vì tạo nhiều loại đối tượng theo nhóm nền tảng.

**Câu 4 (q_197): Bạn cần xây dựng một đối tượng phức tạp (ví dụ: một chiếc xe) với các tùy chọn khác nhau. Mẫu thiết kế nào phù hợp?**
Đáp án đúng: D
Giải thích: Mẫu Builder tách rời quá trình xây dựng một đối tượng phức tạp khỏi biểu diễn của nó, cho phép cùng một quy trình xây dựng có thể tạo ra các biểu diễn khác nhau (ví dụ xe thể thao, xe SUV).
- Loại A (Prototype): Tạo bằng cách sao chép, không hỗ trợ xây dựng từng bước.
- Loại B (Factory Method): Tạo đối tượng trong một bước duy nhất thay vì lắp ráp nhiều thành phần.
- Loại C (Singleton): Chỉ cho phép tạo một đối tượng duy nhất của toàn hệ thống.

**Câu 5 (q_198): Một ứng dụng cần tạo ra các bản sao của một tài liệu mà không cần phải tạo lại từ đầu. Mẫu thiết kế nào phù hợp?**
Đáp án đúng: A
Giải thích: Mẫu Prototype cho phép tạo đối tượng mới bằng cách sao chép (clone) một nguyên mẫu đã tồn tại, giúp tiết kiệm chi phí khởi tạo.
- Loại B (Factory Method): Yêu cầu khởi tạo đối tượng mới từ đầu dựa trên logic.
- Loại C (Singleton): Đảm bảo chỉ có một thể hiện, hoàn toàn ngược lại với việc tạo bản sao.
- Loại D (Builder): Xây dựng từng bước từ đầu, không tận dụng trạng thái của đối tượng cũ.

**Câu 6 (q_199): Khi nào nên sử dụng mẫu Factory Method thay vì tạo đối tượng trực tiếp bằng new?**
Đáp án đúng: B
Giải thích: Factory Method cung cấp sự linh hoạt khi hệ thống cần tạo đối tượng dựa trên giao diện hoặc lớp trừu tượng, và để lớp con quyết định lớp cụ thể nào được triển khai, thay vì gọi `new` làm mã bị kết dính.
- Loại A: Việc quản lý đối tượng duy nhất là chức năng của Singleton.
- Loại C: Quản lý danh sách đối tượng có thể dùng Collection hoặc Pool.
- Loại D: Đối tượng cấu trúc phức tạp thì nên dùng Builder.

**Câu 7 (q_200): Tại sao mẫu Builder hữu ích trong việc xây dựng một đối tượng phức tạp?**
Đáp án đúng: A
Giải thích: Builder giúp tách biệt quá trình lắp ráp (construction step-by-step) khỏi các bộ phận tạo nên nó, mang lại sự linh hoạt tối đa khi ráp các cấu hình khác nhau.
- Loại B: Việc tạo đối tượng duy nhất là chức năng của Singleton.
- Loại C: Phụ thuộc một-nhiều là chức năng của Observer.
- Loại D: Quá chung chung, bất kỳ Creational pattern nào cũng đáp ứng yêu cầu người dùng.

**Câu 8 (q_201): Bài toán: Bạn đang xây dựng một hệ thống quản lý cấu hình ứng dụng và quyết định áp dụng mẫu thiết kế Singleton. Câu hỏi: Kết quả chính của việc áp dụng mẫu thiết kế này là gì?**
Đáp án đúng: B
Giải thích: Singleton đảm bảo suốt vòng đời ứng dụng chỉ có duy nhất một đối tượng Configuration được khởi tạo và sử dụng toàn cục, đảm bảo tính nhất quán của dữ liệu.
- Loại A: Đi ngược lại mục đích Singleton (tạo nhiều đối tượng).
- Loại C: Làm phân mảnh cấu hình, trái với bản chất nhất quán.
- Loại D: Việc tạo đối tượng mới mỗi khi cấu hình thay đổi là không đúng với Singleton.

**Câu 9 (q_202): Bài toán: Bạn đang phát triển một ứng dụng hỗ trợ đa nền tảng và sử dụng mẫu thiết kế Abstract Factory để tạo các thành phần giao diện người dùng. Câu hỏi: Kết quả chính của việc sử dụng mẫu thiết kế này là gì?**
Đáp án đúng: B
Giải thích: Abstract Factory đảm bảo rằng ứng dụng luôn tạo ra "cùng một bộ/họ" thành phần (như Windows Button đi với Windows Scrollbar), tránh râu ông nọ cắm cằm bà kia.
- Loại A: Các thành phần giao diện không hề độc lập mà liên kết chặt chẽ theo cùng một họ nền tảng.
- Loại C: Việc tạo theo từng bước cấu hình là đặc tính của Builder.
- Loại D: Trái ngược với lợi ích cốt lõi của Abstract Factory.

**Câu 10 (q_203): Bài toán: Áp dụng Prototype để tạo các đơn vị quân trong một trò chơi chiến thuật (ví dụ: tạo nhiều lính bộ binh giống nhau từ một nguyên mẫu) sẽ mang lại kết quả gì?**
Đáp án đúng: B
Giải thích: Trong game, việc khởi tạo model lính từ đầu tốn rất nhiều tài nguyên bộ nhớ/CPU. Clone từ một prototype giúp quá trình spawn diễn ra cực nhanh và tối ưu.
- Loại A: Các đơn vị clone giữ nguyên thuộc tính ban đầu chứ không ngẫu nhiên.
- Loại C: Việc đẹp hơn, chuyên nghiệp hơn là do thiết kế đồ họa, không phải do mẫu thiết kế.
- Loại D: Thiết lập thuộc tính phức tạp cần quy trình là đặc điểm của Builder.

**Câu 11 (q_204): Trong một ứng dụng cần tích hợp một thư viện bên ngoài có giao diện khác với giao diện của ứng dụng, mẫu thiết kế nào phù hợp?**
Đáp án đúng: C
Giải thích: Adapter (Bộ chuyển đổi) đóng vai trò trung gian, chuyển đổi giao diện của một lớp/thư viện thành giao diện mà client đang mong đợi.
- Loại A (Bridge): Tách biệt Abstraction và Implementation để cả hai độc lập phát triển.
- Loại B (Composite): Tổ chức các đối tượng theo cấu trúc cây (part-whole).
- Loại D (Decorator): Thêm tính năng mở rộng cho đối tượng một cách linh hoạt lúc runtime.

**Câu 12 (q_205): Một ứng dụng cần chạy trên nhiều nền tảng khác nhau (Windows, macOS, Linux) mà không cần thay đổi nhiều code, mẫu thiết kế nào phù hợp?**
Đáp án đúng: A
Giải thích: Bridge tách phần trừu tượng (Logic nền tảng) ra khỏi phần thực thi (Mã thực hiện trên từng OS), giúp có thể thêm nền tảng mới độc lập mà không phải sửa logic cốt lõi.
- Loại B (Composite): Liên quan đến cấu trúc cây nhóm đối tượng.
- Loại C (Adapter): Chuyển đổi giao diện không khớp, không phải để độc lập nền tảng.
- Loại D (Decorator): Thêm trách nhiệm động cho đối tượng.

**Câu 13 (q_206): Một ứng dụng cần trì hoãn việc tải một hình ảnh lớn cho đến khi người dùng thực sự muốn xem nó, mẫu thiết kế nào phù hợp?**
Đáp án đúng: C
Giải thích: Proxy tạo ra một đối tượng đại diện để kiểm soát quyền truy cập hoặc áp dụng Lazy Initialization (trì hoãn khởi tạo đối tượng nặng cho tới khi cần).
- Loại A (Facade): Cung cấp một giao diện đơn giản cho một hệ thống phức tạp.
- Loại B (Flyweight): Chia sẻ trạng thái chung để tiết kiệm bộ nhớ khi có hàng triệu đối tượng.
- Loại D (Adapter): Chuyển đổi giao diện.

**Câu 14 (q_207): Tại sao mẫu Adapter hữu ích khi tích hợp thư viện bên ngoài?**
Đáp án đúng: B
Giải thích: Thư viện ngoài thường có chuẩn giao diện riêng (ví dụ XML), trong khi app dùng chuẩn khác (ví dụ JSON). Adapter biến đổi lời gọi để chúng tương thích.
- Loại A: Không tạo ra đối tượng có "cùng" giao diện, mà chuyển đổi từ giao diện này sang giao diện khác.
- Loại C: Việc tạo đối tượng duy nhất là Singleton.
- Loại D: Quản lý theo cấu trúc phân cấp là Composite.

**Câu 15 (q_208): Một lớp cần che giấu sự phức tạp của nhiều lớp bên trong và cung cấp một giao diện dễ sử dụng hơn cho người dùng, mẫu thiết kế nào phù hợp?**
Đáp án đúng: A
Giải thích: Facade đóng vai trò như "mặt tiền", cung cấp một phương thức gọi duy nhất, dễ dàng thay vì bắt client phải tương tác với hàng chục lớp con phức tạp.
- Loại B (Flyweight): Nhằm mục đích tiết kiệm RAM, không phải đơn giản hóa giao diện.
- Loại C (Proxy): Kiểm soát truy cập hoặc lazy load, không phải che giấu hệ thống lớn.
- Loại D (Adapter): Chuyển đổi interface để tương thích, không mang tính "gom chung" che giấu nhiều lớp.

**Câu 16 (q_209): Bài toán: Bạn có một hệ thống xử lý dữ liệu từ một nguồn bên ngoài với định dạng khác biệt. Bạn áp dụng mẫu thiết kế Adapter. Câu hỏi: Kết quả chính của việc áp dụng mẫu thiết kế này là gì?**
Đáp án đúng: B
Giải thích: Hệ thống cốt lõi vẫn giữ nguyên logic và chuẩn dữ liệu của mình. Mọi việc chuyển đổi từ dữ liệu nguồn bên ngoài sẽ do Adapter hứng chịu và biến đổi.
- Loại A: Không cần tạo giao diện mới hoàn toàn cho hệ thống.
- Loại C: Đang nói về nguồn bên ngoài (External), không phải nguồn bên trong.
- Loại D: Yêu cầu thay đổi cấu trúc hiện tại là sai, Adapter giúp tránh việc phải thay đổi mã cũ.

**Câu 17 (q_210): Bài toán: Bạn đang xây dựng một ứng dụng có thể chạy trên nhiều hệ điều hành khác nhau và sử dụng mẫu thiết kế Bridge. Câu hỏi: Kết quả quan trọng của việc áp dụng mẫu thiết kế này là gì?**
Đáp án đúng: B
Giải thích: Nhờ tách Abstraction và Implementation, phần logic ứng dụng có thể mở rộng thoải mái mà không bị dính chặt (coupled) vào mã render của từng hệ điều hành.
- Loại A: Giao diện giống hệt nhau là do công cụ UI, không phải lợi ích cốt lõi của Bridge.
- Loại C: Nếu thay đổi liên quan mật thiết thì mã nguồn đã bị kết dính chặt (tight coupling), trái với Bridge.
- Loại D: Bridge thiên về tính bảo trì và linh hoạt kiến trúc, không sinh ra tối ưu hóa hiệu suất nền tảng.

**Câu 18 (q_211): Bài toán: Bạn muốn thêm các tính năng bổ sung (ví dụ: mã hóa, nén) vào một đối tượng luồng dữ liệu mà không muốn tạo ra các lớp con mới. Bạn áp dụng mẫu thiết kế Decorator. Câu hỏi: Kết quả quan trọng của việc sử dụng Decorator trong trường hợp này là gì?**
Đáp án đúng: B
Giải thích: Decorator bọc (wrap) đối tượng ban đầu, cho phép bật/tắt (thêm/loại bỏ) các tính năng (như mã hóa, nén) lúc chạy (runtime) thay vì biên dịch bằng Subclass.
- Loại A: Decorator cho phép gỡ bỏ linh hoạt (loại bỏ lớp bọc), không bị giới hạn.
- Loại C: Thêm lớp Decorator thường làm giảm đôi chút hiệu suất do gọi hàm bọc nhiều lớp.
- Loại D: Decorator giữ nguyên giao diện chứ không làm đơn giản hơn (việc làm đơn giản hơn là của Facade).

**Câu 19 (q_212): Trong một ứng dụng GUI, bạn cần xử lý các sự kiện khác nhau (nhấp chuột, gõ phím) bằng các đối tượng xử lý khác nhau. Mẫu thiết kế nào phù hợp?**
Đáp án đúng: C
Giải thích: Mẫu Chain of Responsibility truyền yêu cầu dọc theo chuỗi các đối tượng (ví dụ: Button -> Panel -> Window) cho đến khi có đối tượng bắt lấy và xử lý sự kiện (event bubbling).
- Loại A (Command): Đóng gói một yêu cầu thành đối tượng, dùng cho undo/redo, không ưu tiên luân chuyển tìm người xử lý.
- Loại B (Interpreter): Thiết kế ngôn ngữ hoặc bộ thông dịch.
- Loại D (Iterator): Duyệt tuần tự qua một tập hợp.

**Câu 20 (q_213): Bạn cần xây dựng một bộ thông dịch cho một ngôn ngữ truy vấn cơ sở dữ liệu đơn giản. Mẫu thiết kế nào phù hợp?**
Đáp án đúng: B
Giải thích: Interpreter thiết kế đại diện (ngữ pháp) và các luật diễn dịch cho một ngôn ngữ chuyên biệt (DSL - Domain Specific Language).
- Loại A (Command): Đóng gói lời gọi hàm, không dịch ngôn ngữ.
- Loại C (Chain of Responsibility): Luân chuyển xử lý sự kiện.
- Loại D (Iterator): Duyệt qua cây/cấu trúc dữ liệu.

**Câu 21 (q_214): Một đối tượng cần thay đổi hành vi của nó dựa trên trạng thái bên trong của nó. Mẫu thiết kế nào phù hợp?**
Đáp án đúng: D
Giải thích: Mẫu State cho phép đối tượng thay đổi hành vi khi trạng thái nội tại thay đổi (chuyển đổi qua lại giữa các State object bên trong mà không dùng if/else rối rắm).
- Loại A (Mediator): Điều phối giao tiếp giữa nhiều đối tượng để giảm phụ thuộc chéo.
- Loại B (Memento): Lưu trữ để hoàn tác trạng thái, không trực tiếp đổi hành vi dựa trên nó.
- Loại C (Observer): Thông báo sự kiện cho nhiều đối tượng quan sát viên.

**Câu 22 (q_215): Bạn cần xử lý một đơn đặt hàng, nơi các bước như "xác nhận đơn hàng", "thanh toán", "giao hàng" có thể được ghi đè bởi các lớp con để xử lý các loại đơn hàng khác nhau. Mẫu thiết kế nào phù hợp?**
Đáp án đúng: B
Giải thích: Template Method định nghĩa cấu trúc (bộ khung các bước) của thuật toán trong một phương thức, và nhường cho các lớp con định nghĩa chi tiết từng bước cụ thể.
- Loại A (Strategy): Đóng gói thuật toán độc lập và thay thế toàn bộ thuật toán.
- Loại C (Visitor): Tách rời thuật toán khỏi cấu trúc đối tượng nó thao tác.
- Loại D (Command): Đóng gói một hành động.

**Câu 23 (q_216): Bạn cần thực hiện chức năng "undo" trong một ứng dụng chỉnh sửa ảnh. Mẫu thiết kế nào phù hợp?**
Đáp án đúng: B
Giải thích: Memento giúp lưu lại (snapshot) trạng thái hiện tại của một đối tượng để sau đó có thể khôi phục lại (undo) mà không phá vỡ tính đóng gói.
- Loại A (Mediator): Trạm trung gian điều phối.
- Loại C (Observer): Cơ chế thông báo sự kiện (Pub-Sub).
- Loại D (State): Chuyển trạng thái để đổi hành vi, không lưu vết để quay lui.

**Câu 24 (q_217): Bài toán: Bạn đang xây dựng một hệ thống xử lý yêu cầu hỗ trợ nhiều loại yêu cầu khác nhau. Bạn áp dụng mẫu thiết kế Chain of Responsibility. Câu hỏi: Kết quả chính của việc áp dụng mẫu thiết kế này là gì?**
Đáp án đúng: B
Giải thích: Các yêu cầu đi qua từng mắt xích trong dây chuyền. Nếu mắt xích đó giải quyết được thì dừng, không thì chuyển tiếp cho mắt xích sau.
- Loại A: Không phải "mỗi loại có bộ riêng ngay từ đầu", mà là ném vào chuỗi để tự phân loại.
- Loại C: Mọi yêu cầu do "chuỗi" xử lý thay vì "một đối tượng xử lý".
- Loại D: Có thể được bắt ở cuối chuỗi, không nhất thiết bị bỏ qua.

**Câu 25 (q_218): Bài toán: Bạn đang xây dựng một hệ thống quản lý trạng thái cho các đối tượng game (ví dụ: nhân vật có trạng thái "đang di chuyển", "đang tấn công"). Bạn áp dụng mẫu thiết kế State. Câu hỏi: Kết quả chính của việc áp dụng mẫu thiết kế này là gì?**
Đáp án đúng: B
Giải thích: Thay vì dùng hàng đống lệnh if/else trong một lớp nhân vật, mỗi trạng thái (Move, Attack) được tách thành một lớp riêng. Hành vi của nhân vật lập tức thay đổi khi tham chiếu State bị đổi.
- Loại A: State không khuyến khích việc giữ cứng (cố định) hành vi.
- Loại C: Tính năng thông báo là của Observer.
- Loại D: Lưu trữ ra ngoài là tính năng của Memento.

**Câu 26 (q_219): Bài toán: Trong một hệ thống giao tiếp giữa nhiều thành phần độc lập, bạn sử dụng mẫu thiết kế Observer. Câu hỏi: Kết quả mong muốn của việc sử dụng Observer là gì?**
Đáp án đúng: B
Giải thích: Khi một Chủ thể (Subject) thay đổi trạng thái, tất cả các Đối tượng quan sát (Observers) đã đăng ký theo dõi nó sẽ tự động nhận được thông báo để cập nhật.
- Loại A: Giao tiếp gián tiếp qua cơ chế đăng ký (Sub), không phải trực tiếp (Tight coupling).
- Loại C: Thay đổi trạng thái thành phần cốt lõi chứ không phải trung gian (Trung gian là Mediator).
- Loại D: Thành phần nhận thông báo tự động bị động (Push) chứ không phải chủ động yêu cầu (Pull) liên tục.
