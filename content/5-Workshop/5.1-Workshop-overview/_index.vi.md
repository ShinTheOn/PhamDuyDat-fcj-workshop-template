---
title : "Tổng quan Workshop"
date : 2026-07-12
weight : 1
chapter : false
pre : " <b> 5.1. </b> "
---

#### 1. Bối cảnh và bài toán

Hệ thống được xây dựng trong workshop này là **backend cho một game nhiều người chơi theo thời gian thực (real-time multiplayer game)**, phục vụ người chơi truy cập qua **Mobile App (Flutter)** hoặc **Web App (trình duyệt)**.

Với game nhiều người chơi, kiến trúc REST API truyền thống (client hỏi – server trả lời) không phù hợp: server cần **chủ động đẩy** cập nhật trạng thái trận đấu đến tất cả người chơi ngay khi có sự kiện xảy ra (ví dụ một người chơi thực hiện nước đi), thay vì để client liên tục polling — vừa tốn tài nguyên vừa gây độ trễ cao, ảnh hưởng trải nghiệm chơi game.

Bên cạnh bài toán real-time, hệ thống còn cần giải quyết:
+ Xác thực người chơi an toàn trước khi cho phép tham gia trận đấu.
+ Hạ tầng có thể tự động mở rộng theo số người chơi đồng thời, không cần dự đoán trước số lượng server.
+ Một quy trình triển khai (CI/CD) để đội ngũ phát triển release tính năng/bản vá nhanh chóng mà không thao tác thủ công trên console.

#### 2. Mục tiêu cụ thể

+ Xây dựng kênh giao tiếp **real-time hai chiều** giữa client và backend bằng **API Gateway WebSocket API**.
+ Xác thực người chơi bằng **Amazon Cognito**, bảo vệ mọi kết nối WebSocket bằng **Lambda Authorizer**.
+ Lưu `connectionId` của từng người chơi và trạng thái trận đấu trong **DynamoDB** với độ trễ đọc/ghi ở mức mili-giây.
+ Tự động **broadcast** cập nhật trạng thái trận đấu tới toàn bộ người chơi đang kết nối thông qua API Gateway Management API (`@connections`).
+ Lưu trữ & phân phối frontend qua **AWS Amplify** (Hosting + CDN), bảo vệ bằng **AWS WAF**, định tuyến domain bằng **Route 53**.
+ Tự động hoá triển khai toàn hệ thống (web + backend) bằng **GitHub Actions + AWS SAM** mỗi khi có Git push.
+ Giám sát vận hành tập trung qua **CloudWatch** (Logs/Alarms).

#### 3. Kiến trúc hệ thống (Architecture Diagram)

![architecture](/images/5-Workshop/5.1-Workshop-overview/architecture.png)

Kiến trúc gồm 4 tầng chính trong AWS Cloud (region **ap-southeast-1**):

| Tầng | Thành phần | Chức năng |
|---|---|---|
| **Edge Layer** (Phân phối & Cổng vào) | Route 53, AWS WAF, AWS Amplify | Phân giải DNS, lọc traffic độc hại, host & phân phối web app qua CDN |
| **Security Layer** | Amazon Cognito, IAM Role | Xác thực người dùng, cấp quyền least-privilege cho các Lambda |
| **Serverless Game Layer** | API Gateway (WebSocket), 3 Lambda (`$connect`, Game Logic, `$disconnect`), DynamoDB, CloudWatch | Quản lý kết nối, xử lý logic game real-time, lưu trạng thái, giám sát |
| **CI/CD Layer** | GitHub Actions, AWS SAM | Tự động build & deploy web lẫn backend từ source code |

**Luồng xử lý chính (16 bước):**

*Truy cập & tải ứng dụng web*
1. Người dùng (Mobile App/Web App) truy cập domain của hệ thống.
2. Route 53 phân giải DNS, chuyển hướng request đến AWS WAF.
3. AWS WAF lọc traffic độc hại rồi chuyển tiếp đến AWS Amplify để lấy file web.
4. AWS Amplify trả ứng dụng web (SPA) về cho trình duyệt/app.

*Xác thực người dùng*
5. Client gọi endpoint `/auth/*` để đăng nhập qua Amazon Cognito và nhận token (JWT).

*Thiết lập kết nối real-time*
6. Client dùng token vừa nhận, kết nối **WSS trực tiếp** đến API Gateway WebSocket (không đi qua Amplify).
7. API Gateway gọi **Lambda Authorizer** để xác thực token với Cognito trước khi chấp nhận kết nối.
8. Nếu hợp lệ, route `$connect` được trigger, gọi Lambda (`$connect`).
9. Lambda (`$connect`) lưu `connectionId` của người chơi vào DynamoDB (bảng Connections).

*Xử lý logic game theo thời gian thực*
10. Khi người chơi thực hiện hành động trong trận, client gửi sự kiện qua WebSocket, API Gateway trigger Lambda (Game Logic).
11. Lambda (Game Logic) đọc/ghi trạng thái trận đấu trong DynamoDB (bảng Games).
12. Lambda (Game Logic) gọi API Gateway Management API để **push `@connections`**, cập nhật trạng thái mới tới tất cả người chơi đang kết nối trong trận.

*Ngắt kết nối*
13. Khi người chơi thoát/mất kết nối, route `$disconnect` được trigger, gọi Lambda (`$disconnect`).
14. Lambda (`$disconnect`) xoá `connectionId` tương ứng khỏi DynamoDB.

*CI/CD*
15. Lập trình viên Git push code lên GitHub repo, trigger GitHub Actions.
16. GitHub Actions build & deploy bằng AWS SAM: **(16a)** deploy phần web lên Amplify, **(16b)** deploy phần backend (API Gateway, Lambda, DynamoDB…).

Xuyên suốt hệ thống, mỗi Lambda chạy dưới một **Execution Role** riêng (IAM Role least privilege), và log từ tầng Serverless được gửi về **CloudWatch** để giám sát.

#### 4. Vì sao chọn các dịch vụ này

| Dịch vụ AWS | Vai trò | Lý do lựa chọn |
|---|---|---|
| Route 53 | DNS cho domain hệ thống | Managed DNS, độ trễ thấp, tích hợp sẵn với Amplify/CloudFront |
| AWS WAF | Lọc traffic độc hại ở edge | Chặn tấn công phổ biến (SQLi, XSS, bot xấu) trước khi vào Amplify, không cần tự vận hành firewall |
| AWS Amplify | Web Hosting & CDN | Có sẵn CI/CD, CDN toàn cầu, HTTPS, custom domain — nhanh hơn tự dựng S3 + CloudFront thủ công |
| Amazon Cognito | Xác thực người dùng | Managed user pool, tự phát hành JWT, tích hợp trực tiếp Lambda Authorizer — không cần tự xây hệ thống auth |
| API Gateway (WebSocket) | Kênh real-time 2 chiều | So với REST, WebSocket cho phép server chủ động push dữ liệu — bắt buộc cho game nhiều người chơi, tránh polling |
| AWS Lambda | Xử lý `$connect`/Game Logic/`$disconnect` | Serverless, tự scale theo số kết nối đồng thời, chỉ trả phí theo lượt gọi — phù hợp traffic không ổn định của game hơn EC2 (phải trả phí cả lúc idle) |
| Amazon DynamoDB | Lưu connectionId & trạng thái trận đấu | Độ trễ đọc/ghi mili-giây, scale ngang tốt, chế độ on-demand phù hợp traffic biến động — phù hợp hơn RDS vốn giới hạn connection pool khi gọi từ nhiều Lambda đồng thời |
| CloudWatch | Logs & Alarms | Tích hợp sẵn với Lambda/API Gateway, dễ đặt alarm khi lỗi/traffic bất thường mà không cần công cụ ngoài |
| AWS SAM | Infrastructure as Code & CI/CD | Framework chuyên cho serverless, cú pháp gọn hơn CloudFormation thuần, tích hợp tốt với GitHub Actions |

{{% notice note %}}
Với mỗi dịch vụ, nên nêu cả phương án đã cân nhắc nhưng không chọn: ví dụ WebSocket API thay vì REST + polling; Lambda thay vì EC2/ECS; DynamoDB thay vì RDS — để làm rõ sự đánh đổi giữa chi phí, độ phức tạp vận hành và yêu cầu độ trễ thấp của game real-time.
{{% /notice %}}

#### 5. Bảo mật và vận hành

+ **IAM:** mỗi Lambda (`$connect`, Game Logic, `$disconnect`) có Execution Role riêng, chỉ được cấp đúng action cần thiết trên DynamoDB & API Gateway Management API — nguyên tắc đặc quyền tối thiểu (least privilege).
+ **Xác thực:** mọi kết nối WebSocket bắt buộc kèm token hợp lệ (lấy ở bước 5), được Lambda Authorizer xác thực với Cognito trước khi API Gateway chấp nhận `$connect` — không tồn tại kết nối ẩn danh.
+ **Bảo vệ tầng edge:** AWS WAF đặt trước Amplify để lọc traffic độc hại trước khi vào ứng dụng.
+ **Giám sát:** log từ tầng Game Serverless được gửi về CloudWatch; nên đặt Alarm khi tỷ lệ lỗi/throttle của Lambda vượt ngưỡng.
+ **Khả năng mở rộng:** Lambda tự scale theo số sự kiện WebSocket đồng thời; DynamoDB on-demand tự scale theo traffic đọc/ghi; API Gateway WebSocket hỗ trợ hàng nghìn kết nối đồng thời; Amplify CDN phân phối web toàn cầu.
