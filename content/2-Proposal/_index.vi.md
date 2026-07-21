---
title: "Bản đề xuất"
date: 2026-07-01
weight: 2
chapter: false
pre: "<b> 2. </b>"
---

# Real-time Serverless Game Platform
## Giải pháp AWS Serverless hợp nhất cho Game Multiplayer Real-time thời gian thực

### 1. Tóm tắt điều hành
Dự án **DoAnMiniGame** được thiết kế nhằm xây dựng một hệ thống nền tảng Game Multiplayer Real-time (Thời gian thực) tối ưu. Hệ thống hỗ trợ xử lý mượt mà các luồng kết nối đồng thời từ ứng dụng client viết bằng Flutter. Nền tảng tận dụng tối đa sức mạnh của mô hình **AWS Serverless** và quy trình **CI/CD tự động (GitHub Actions + AWS SAM)** giúp loại bỏ hoàn toàn chi phí quản lý hạ tầng máy chủ vật lý, cung cấp khả năng giám sát thời gian thực, tối ưu hóa bảo mật và tiết kiệm chi phí vận hành dựa trên lượng tài nguyên thực tế tiêu thụ.

---

### 2. Tuyên bố vấn đề

#### Vấn đề hiện tại
Các kiến trúc game multiplayer truyền thống yêu cầu duy trì cụm máy chủ chuyên dụng chạy liên tục 24/7, dẫn đến chi phí cố định rất cao ngay cả khi không có người chơi. Bên cạnh đó, việc cấu hình co giãn tự động (Auto-scaling) thủ công thường không đáp ứng kịp thời khi lượng người chơi tăng đột biến, dễ gây nghẽn mạng hoặc sập hệ thống. Việc đồng bộ hóa trạng thái game (Game State) thời gian thực giữa các phòng chơi cũng rất phức tạp và đòi hỏi hạ tầng có độ trễ cực thấp.

#### Giải pháp
Nền tảng sử dụng **Amazon API Gateway (WebSocket API)** để duy trì kết nối hai chiều liên tục, **AWS Lambda** để xử lý logic game độc lập (Event-driven), và **Amazon DynamoDB** làm cơ sở dữ liệu NoSQL lưu trữ session kết nối (`Connections`) và trạng thái phòng chơi (`Games`). Tầng Phân phối & Cổng vào (Edge Layer) được tinh giản hoàn toàn bằng cách sử dụng **AWS Amplify (Web Hosting & CDN)** để phân phối Flutter Web ổn định, kết hợp **AWS WAF** chặn DDoS và **Route 53** phân giải tên miền. Quy trình triển khai được tự động hóa hoàn toàn thông qua **GitHub Actions** phối hợp với **AWS SAM CLI** để đóng gói và deploy hạ tầng dưới dạng mã (IaC).

#### Lợi ích và hoàn vốn đầu tư (ROI)
Giải pháp tạo nền tảng cơ sở vững chắc cho một hệ thống game multiplayer thời gian thực chạy ổn định với độ trễ tối thiểu (chỉ vài mili-giây) và khả năng co giãn tự động. Hệ thống giảm bớt gánh nặng quản trị hạ tầng, đơn giản hóa quy trình cập nhật mã nguồn backend và frontend, đồng thời cải thiện độ tin cậy của dữ liệu phòng chơi. Chi phí hằng tháng ước tính cực kỳ tối ưu vì hầu hết các dịch vụ đều nằm trong hạn mức AWS Free Tier khi chạy thử nghiệm, thời gian hoàn vốn nhanh nhờ tiết kiệm tối đa chi phí tài nguyên máy chủ cố định.

---

### 3. Kiến trúc giải pháp
Nền tảng áp dụng kiến trúc Serverless Game Topology để quản lý các phiên kết nối thời gian thực dài hạn từ client Flutter. Toàn bộ hạ tầng được định nghĩa bằng mã nguồn (IaC) thông qua AWS SAM template để đảm nhận tính đồng nhất.

#### Sơ đồ kiến trúc hệ thống
Để sơ đồ hiển thị trực quan và thu hút trong tài liệu, hình ảnh kiến trúc được tích hợp trực tiếp bên dưới:

<p align="center">
  <img width="2761" height="1090" alt="image" src="https://github.com/user-attachments/assets/38c2f3f1-2850-4306-adbf-fb15941edb05" />

" alt="AWS Serverless Game Architecture" width="100%">
  <br>
  <i>Hình 3.1: Sơ đồ kiến trúc Real-time Serverless Game Platform sử dụng AWS SAM và GitHub Actions</i>
</p>

#### Dịch vụ AWS sử dụng
* **AWS Amplify**: Lưu trữ và phân phối giao diện ứng dụng Flutter Web nhanh chóng qua hệ thống CDN toàn cầu.
* **AWS Lambda**: Xử lý logic nghiệp vụ game, xác thực và phát (broadcast) sự kiện (Hệ thống gồm 4 hàm Node.js biệt lập).
* **Amazon API Gateway**: Thiết lập cổng WebSocket API định tuyến chuẩn xác các gói tin dựa trên JSON action.
* **Amazon DynamoDB**: Lưu trữ session kết nối người chơi và trạng thái các phòng game (2 bảng dữ liệu NoSQL tốc độ cao).
* **Amazon Route 53 & AWS WAF**: Phân giải DNS Alias linh hoạt và thiết lập tường lửa biên ngăn chặn bot tấn công spam hoặc vượt giới hạn truy cập (Rate Limit).
* **Amazon Cognito**: Quản lý quy trình đăng ký, đăng nhập và cấp mã token JWT an toàn để xác thực thông tin người chơi.
* **Amazon CloudWatch**: Giám sát nhật ký (logs) toàn bộ hệ thống, giới hạn thời gian lưu trữ giúp tối ưu hóa chi phí phát sinh.

#### Thiết kế thành phần
* **Ứng dụng Client**: Ứng dụng xây dựng trên Flutter tích hợp bộ công cụ AWS Amplify SDK phục vụ luồng xác thực (Auth), thiết lập kết nối hai chiều trực tiếp bằng giao thức mạng mã hóa `wss://` đến cổng API Gateway.
* **Tiếp nhận & Bảo mật biên**: Dịch vụ Route 53 điều phối toàn bộ lưu lượng truy cập qua bộ lọc an toàn AWS WAF, bảo vệ hệ thống trước khi chuyển tiếp gói tin kết nối đến bộ xác thực định danh Cognito Lambda Authorizer.
* **Xử lý dữ liệu**: Các hàm AWS Lambda tiếp nhận tín hiệu sự kiện từ API Gateway, tự động ghi nhận mã kết nối vào bảng lưu trữ DynamoDB, thực thi toàn bộ logic trò chơi và gửi cập nhật trạng thái mới nhất tới phòng chơi.
* **Lưu trữ dữ liệu**: Bảng dữ liệu `Connections` quản lý các phiên kết nối hiện hành (được cấu hình thêm chỉ mục Global Secondary Index dựa trên trường dữ liệu `roomId`); bảng `Games` đảm nhận cấu trúc ma trận trạng thái trận đấu. Cả hai bảng đều được kích hoạt thuộc tính TTL (Time to Live) để tự động xóa sạch dữ liệu lỗi thời hoặc rác hệ thống.

---

### 4. Triển khai kỹ thuật

#### Các giai đoạn triển khai
Dự án được thực hiện toàn diện qua 4 giai đoạn nối tiếp cuốn chiếu:
1.  **Nghiên cứu và vẽ kiến trúc**: Khảo sát sâu về giao thức WebSocket API trên API Gateway, xây dựng cấu trúc sơ đồ thực thể (schema) cho DynamoDB NoSQL và hoàn thiện mô hình thiết kế đồ họa hệ thống trên nền tảng trực tuyến Draw.io.
2.  **Tính toán chi phí và kiểm tra tính khả thi**: Sử dụng công cụ AWS Pricing Calculator chuyên nghiệp từ AWS để dự toán chính xác ngân sách vận hành và cấu hình các mốc cảnh báo chi phí.
3.  **Điều chỉnh kiến trúc tối ưu**: Tinh chỉnh toàn bộ mô hình sang giải pháp Serverless 100%. Chuyển dịch phân phối tầng giao diện web sang **AWS Amplify**, tích hợp luồng tự động hóa CI/CD thông qua **GitHub Actions + AWS SAM** để hoàn thiện việc quản lý hạ tầng bằng mã (IaC).
4.  **Phát triển, kiểm thử, triển khai**: Viết mã nguồn nghiệp vụ Lambda bằng Node.js, lập trình hoàn thiện ứng dụng phía máy khách (Flutter client), tổ chức viết file kịch bản workflow CI/CD và tiến hành đo kiểm hiệu năng chịu tải (load test) kết nối thông qua công cụ dòng lệnh wscat.

#### Yêu cầu kỹ thuật môi trường
* **Môi trường Phát triển**: Hệ thống máy trạm cài đặt sẵn AWS CLI v2, AWS SAM CLI, môi trường Node.js phiên bản 18+, bộ công cụ Flutter SDK và thư viện wscat trên local.
* **Hệ thống Backend (IaC)**: Toàn bộ cấu trúc thành phần từ API Gateway, Lambda, cho tới DynamoDB đều được định nghĩa tập trung và quản lý tường minh trong tệp tin `template.yaml` của AWS SAM, áp dụng triệt để các biến môi trường cấu hình linh hoạt nhằm tránh việc hardcode mã nguồn.
* **Ứng dụng Frontend (Flutter)**: Tích hợp tệp liên kết cấu hình `amplifyconfiguration.dart` đồng bộ phần xác thực với Cognito User Pool. Sử dụng thư viện bảo mật `flutter_secure_storage` tại client để lưu giữ chuỗi Token JWT an toàn tuyệt đối.

---

### 5. Lộ trình & Mốc triển khai
* **Trước thực tập (Tháng 0)**: Dành ra 1 tháng nghiên cứu chuyên sâu cơ chế kết nối thời gian thực WebSocket và phác thảo sơ bộ bản vẽ kiến trúc trên phần mềm Draw.io.
* **Thực tập (Tháng 1–3)**:
    * **Tháng 1**: Làm chủ công cụ AWS SAM CLI để tự động hóa định nghĩa tài nguyên mã nguồn IaC. Khởi tạo dịch vụ quản lý người dùng Cognito User Pool và thiết lập mô hình chính sách IAM Role theo nguyên tắc đặc quyền tối thiểu (Least Privilege).
    * **Tháng 2**: Khởi tạo cấu trúc các phân vùng bảng lưu trữ DynamoDB Tables, cấu hình hệ thống Index tăng tốc truy vấn và cơ chế tự hủy TTL. Tập trung phát triển mã nguồn xử lý cho 4 hàm chức năng Lambda Node.js và hoàn thiện cấu trúc định tuyến dữ liệu cho WebSocket API Gateway.
    * **Tháng 3**: Hoàn thiện toàn bộ giao diện và chức năng của ứng dụng Flutter, cấu hình chuẩn tệp mã lệnh workflow của GitHub Actions giúp chạy kiểm thử và deploy song song cả thành phần Frontend (Amplify) lẫn Backend (SAM). Cấu hình bộ cảnh báo CloudWatch Alarms tự động gửi thư điện tử thông báo nếu xuất hiện lỗi phát sinh từ Lambda.

---

### 6. Ước tính ngân sách
Bảng dự toán kinh phí vận hành hàng tháng dưới đây được tính toán chi tiết dựa trên công cụ AWS Pricing Calculator tại trung tâm dữ liệu khu vực khu vực Singapore (`ap-southeast-1`):

| Thành phần dịch vụ AWS | Chi phí hàng tháng (USD) | Ghi chú & Tối ưu hóa chi phí |
| :--- | :--- | :--- |
| **AWS Lambda** | 0.00 USD | Nằm trong giới hạn Free Tier lâu dài (Miễn phí 1 triệu lượt triệu gọi đầu tiên). |
| **Amazon API Gateway (WebSocket)** | 0.00 USD | Tận dụng gói Free Tier cơ bản (Miễn phí hoàn toàn cho 1 triệu tin nhắn trao đổi). |
| **Amazon Cognito** | 0.00 USD | Không phát sinh chi phí đối với lượng người dùng hoạt động hàng tháng (MAUs) quy mô nhỏ. |
| **AWS Amplify** | ~0.35 USD | Tích lũy chi phí dung lượng thấp dựa trên không gian lưu trữ thực tế của ứng dụng Web. |
| **Amazon DynamoDB** | ~0.30 USD | Áp dụng cấu hình chế độ chi trả theo lượng tài nguyên sử dụng thực tế (On-Demand). |
| **Amazon CloudWatch** | ~0.15 USD | Tối ưu hóa ngân sách nhờ giới hạn thời gian lưu giữ nhật ký vết (Retention) xuống còn 14 ngày. |
| **AWS WAF** | ~5.00 USD | Mức phí duy trì cố định áp dụng cho 1 cấu hình quy tắc Web ACL cơ bản ở lớp biên. |
| **TỔNG CỘNG** | **~5.80 USD / tháng** | *Tương đương khoảng ~69.60 USD cho cả năm vận hành hệ thống thử nghiệm.* |

---

### 7. Đánh giá rủi ro

#### Ma trận đánh giá rủi ro
* **Zombie Connection (Hiện tượng treo kết nối ngầm)**: Xảy ra khi người dùng ẩn ứng dụng game xuống chế độ chạy nền (background) nhưng phiên kết nối WebSocket không được giải phóng hoàn toàn, khiến hệ thống tiếp tục tính phí duy trì liên tục gây lãng phí tài nguyên mạng. *(Mức độ ảnh hưởng: Trung bình | Xác suất xảy ra: Cao)*
* **Cold Start Delay (Độ trễ do khởi động nguội)**: Đối với các hàm Lambda không được gọi liên tục trong thời gian dài, môi trường thực thi sẽ tự động bị thu hồi, dẫn tới việc người dùng đầu tiên truy cập lại sẽ gặp hiện tượng trễ từ 1-3 giây để hệ thống tái khởi động môi trường. *(Mức độ ảnh hưởng: Thấp | Xác suất xảy ra: Trung bình)*
* **Rò rỉ thông tin cấu hình (Credential Leak)**: Sơ suất kỹ thuật dẫn tới việc commit nhầm các tệp tin chứa mã khóa truy cập bảo mật nguy hiểm (như AWS Access Key/Secret Key) công khai lên các kho lưu trữ chung trên GitHub. *(Mức độ ảnh hưởng: Rất cao | Xác suất xảy ra: Thấp)*

#### Chiến lược giảm thiểu & Kế hoạch dự phòng
* **Xử lý treo kết nối**: Phía ứng dụng máy khách (Flutter Client) chủ động bắt sự kiện ứng dụng thay đổi trạng thái và thực hiện ngắt kết nối WebSocket ngay khi phát hiện người dùng chuyển ứng dụng sang chạy ngầm. Ở phần Backend, viết mã lệnh cho hàm Lambda tích hợp cơ chế kiểm tra nhịp tim định kỳ (Heartbeat Ping/Pong) đồng thời kết hợp linh hoạt với thuộc tính cấu hình tự hủy dữ liệu TTL trên cơ sở dữ liệu DynamoDB để dọn dẹp triệt để mọi kết nối ảo.
* **Giảm thiểu hiện tượng Cold Start**: Tổ chức khởi tạo toàn bộ các kết nối SDK mở rộng (ví dụ như kết nối đến DynamoDB) nằm hoàn toàn ở bên ngoài hàm xử lý sự kiện chính (`exports.handler`) nhằm tái sử dụng tối đa môi trường thực thi của các request trước đó. Thu nhỏ dung lượng gói deploy mã nguồn backend bằng câu lệnh tối ưu hóa `npm ci --production`.
* **Bảo mật mã nguồn tuyệt đối**: Khai báo đầy đủ các tệp định nghĩa môi trường `.env` hoặc các thư mục cấu hình nhạy cảm vào danh sách tệp tin bỏ qua của `.gitignore` trước khi đẩy bất kỳ mã nguồn nào lên GitHub. Đồng thời, thiết lập hệ thống cảnh báo ngân sách AWS Billing Alert để nhận thông báo khẩn cấp bằng Email ngay khi tổng chi phí vượt quá ngưỡng thiết lập kiểm soát ban đầu.

---

### 8. Kết quả kỳ vọng
* **Cải tiến kỹ thuật vượt trội**: Xây dựng thành công hệ thống trò chơi multiplayer thời gian thực chạy ổn định trên nền tảng kiến trúc Serverless tiên tiến dựa theo mô hình Event-driven, đạt toàn bộ các chứng chỉ về tiêu chuẩn vận hành an toàn bảo mật. Ứng dụng đảm bảo độ trễ thấp tối thiểu, triệt tiêu hoàn toàn điểm nghẽn hệ thống (Bottleneck) và có khả năng tự co giãn (Auto-scaling) linh hoạt theo số lượng người truy cập thực tế.
* **Giá trị lâu dài đóng góp cho dự án**: Toàn bộ kho mã nguồn định nghĩa kiến trúc cơ sở hạ tầng (AWS SAM Template) cùng hệ thống kịch bản workflow tự động hóa CI/CD của GitHub Actions được chuẩn hóa, đóng gói bài bản và lưu trữ khoa học. Đây sẽ là nền tảng vững chắc giúp đội ngũ kỹ thuật dễ dàng phát triển, kế thừa và mở rộng quy mô các dự án game multiplayer lớn hơn trong tương lai.
