---
title : "Bước 2: Tùy chọn cấu hình Firewall"
date: 2026-07-12
weight : 2
chapter : false
pre : " <b> 5.10.2. </b> "
---

#### Mục tiêu

Trong bước này, bạn sẽ chọn phương án cấu hình WAF phù hợp và bật các tính năng bảo vệ khuyến nghị.

#### Hướng dẫn

![Ảnh 1](/images/5-Workshop/5.10-Amplify-waf-protection/anh2.png)

Tại trang `Add firewall`, thực hiện các thiết lập sau:

1. `Chọn cấu hình`: chọn `Create new` nếu bạn muốn tạo cấu hình WAF mới, hoặc `Use existing WAF configuration` nếu đã có cấu hình sẵn.
2. `Bảo vệ khuyến nghị`: bật `Enable Amplify-recommended Firewall protection`.
3. Tính năng này sẽ giúp:
   - bảo vệ khỏi các lỗ hổng bảo mật web phổ biến theo OWASP Top 10,
   - ngăn chặn bot và công cụ dò tìm lỗ hổng,
   - chặn các IP độc hại dựa trên dữ liệu tình báo bảo mật của Amazon.
4. Bạn có thể bật thêm cấu hình nâng cao như giới hạn truy cập vào domain mặc định, chặn hoặc cho phép theo IP hoặc quốc gia nếu cần.

#### Lưu ý

Các tùy chọn nâng cao là tùy chọn và có thể được giữ ở mức mặc định nếu bạn chưa cần cấu hình phức tạp.
