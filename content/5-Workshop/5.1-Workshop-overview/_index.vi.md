---
title : "Tổng quan Workshop"
date: 2026-07-12
weight : 1
chapter : false
pre : " <b> 5.1. </b> "
---

#### Mục tiêu của workshop

Trong workshop này, bạn sẽ xây dựng và triển khai ứng dụng GameHub serverless trên AWS bằng cách:
- Khởi tạo pipeline CI/CD cho backend bằng AWS SAM.
- Cấu hình hai môi trường Dev và Prod cho quá trình deploy.
- Kết nối repository GitHub vào AWS CodePipeline thông qua AWS CodeConnections.
- Triển khai backend bằng CloudFormation và frontend bằng AWS Amplify.
- Bảo vệ ứng dụng frontend bằng AWS WAF và theo dõi hoạt động bằng Amazon CloudWatch.

#### Nội dung chính

1. Khởi tạo pipeline bằng lệnh `sam pipeline init --bootstrap`.
2. Thiết lập các stage Dev và Prod, cấu hình repository, template path, stack name và nhánh deploy.
3. Kết nối GitHub với CodePipeline để tự động trigger deployment khi có thay đổi code.
4. Triển khai frontend Flutter web trên AWS Amplify và cấu hình biến môi trường cho build.
5. Tăng cường bảo mật cho ứng dụng bằng AWS WAF và giám sát hệ thống bằng CloudWatch.

#### Kiến trúc và công nghệ

GameHub là một ứng dụng serverless xây dựng trên các dịch vụ của Amazon:
- AWS Lambda xử lý logic nghiệp vụ.
- Amazon API Gateway cung cấp API HTTP/WebSocket.
- Amazon Cognito quản lý xác thực người dùng.
- AWS Amplify hosting frontend tĩnh và web.
- AWS CodePipeline và AWS SAM hỗ trợ CI/CD.
- AWS WAF bảo vệ ứng dụng khỏi các tấn công web phổ biến.

#### Lưu ý

- Tên `GameHub` là ví dụ; hãy thay bằng tên dự án của bạn.
- Nếu backend và frontend cùng nằm trong một repository, hãy phân tách rõ thư mục.
- Kiểm tra profile AWS và region trước khi chạy các lệnh SAM.

Note (hình ảnh): Chèn ảnh mô hình kiến trúc hệ thống tại vị trí này để trực quan. Thư mục placeholder: `images/5-Workshop/5.1-Workshop-overview/gamehub-architecture.svg`.

