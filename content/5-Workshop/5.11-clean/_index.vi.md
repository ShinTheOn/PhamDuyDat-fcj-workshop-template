---
title : "Dọn dẹp tài nguyên sau workshop"
date: 2026-07-12
weight : 11
chapter : false
pre : " <b> 5.11. </b> "
---

#### Mục tiêu

Trong phần này, bạn sẽ thực hiện quá trình dọn dẹp các tài nguyên AWS đã tạo trong suốt workshop để tránh phát sinh chi phí không cần thiết và giữ môi trường làm việc gọn gàng.

#### Lý do cần dọn dẹp

Sau khi hoàn thành workshop, các dịch vụ như AWS CodePipeline, AWS CloudFormation, AWS Amplify, AWS WAF, CodeConnections và các bucket/S3 liên quan có thể vẫn tiếp tục vận hành và phát sinh chi phí. Vì vậy, nên xóa các tài nguyên không còn dùng đến theo đúng trình tự để tránh lỗi phụ thuộc giữa các dịch vụ.

#### Nguyên tắc dọn dẹp

Nên thực hiện theo thứ tự ngược lại với quy trình tạo tài nguyên:

1. Xóa ứng dụng frontend trên Amplify.
2. Gỡ kết nối WAF và xóa Web ACL nếu không còn cần thiết.
3. Xóa pipeline và các stack CloudFormation liên quan.
4. Xóa các bucket, role, policy và kết nối CodeConnections còn dư thừa.

#### Bước 1: Xóa ứng dụng frontend trên AWS Amplify

1. Truy cập AWS Amplify Console.
2. Chọn ứng dụng frontend mà bạn đã deploy trong workshop.
3. Vào mục `App settings` hoặc `Actions` và chọn `Delete app`.
4. Xác nhận thao tác để xóa toàn bộ ứng dụng khỏi môi trường Amplify.

#### Bước 2: Gỡ WAF và xóa cấu hình bảo mật


1. Vào AWS WAF console hoặc AWS Amplify Firewall section.
2. Xóa các Web ACL, rule groups hoặc firewall association đang liên kết với ứng dụng.
3. Nếu bạn đã tạo cấu hình WAF riêng cho workshop, hãy xóa cấu hình đó sau khi đã gỡ khỏi ứng dụng.

#### Bước 3: Xóa pipeline và các stack CloudFormation


1. Mở AWS CodePipeline và xóa pipeline bạn đã tạo cho workshop.
2. Vào AWS CloudFormation Console, chọn các stack liên quan như stack Dev, stack Prod hoặc stack bootstrap được tạo khi chạy SAM pipeline.
3. Nhấn `Delete` để xóa từng stack.
4. Nếu có bucket S3 được tạo cùng stack, hãy kiểm tra và xóa nội dung trong bucket trước khi xóa stack nếu hệ thống yêu cầu.

#### Bước 4: Xóa kết nối CodeConnections và tài nguyên phụ trợ


1. Vào `Developer Tools` → `Settings` → `Connections`, chọn kết nối GitHub đã tạo và xóa kết nối đó.
2. Vào IAM Console, kiểm tra các role và policy liên quan tới pipeline hoặc deployment, sau đó xóa các tài nguyên không còn cần thiết.
3. Nếu có CloudWatch log group, S3 bucket hoặc resource phụ trợ khác được tạo riêng cho workshop, hãy xóa hoặc dọn sạch trước khi kết thúc.

#### Lưu ý quan trọng

- Trước khi xóa, hãy chắc chắn rằng bạn không còn cần dữ liệu hoặc log nào phục vụ cho báo cáo hoặc đánh giá.
- Một số tài nguyên có thể bị giữ lại trong vài phút sau khi xóa vì AWS cần thời gian xử lý.
- Nếu bạn muốn giữ lại dữ liệu nhưng chỉ muốn ngừng chi phí, bạn có thể tạm ngừng hoặc giữ lại các tài nguyên quan trọng thay vì xóa hoàn toàn.

#### Kết quả mong đợi

Sau khi hoàn tất các bước trên, môi trường workshop sẽ được dọn sạch, giảm chi phí vận hành và không còn các tài nguyên AWS dư thừa sau khi kết thúc thực hành.

