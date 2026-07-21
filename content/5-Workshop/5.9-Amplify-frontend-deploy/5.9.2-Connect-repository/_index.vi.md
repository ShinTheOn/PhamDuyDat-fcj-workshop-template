---
title : "Bước 2: Liên kết Repository và Nhánh"
date: 2026-07-12
weight : 2
chapter : false
pre : " <b> 5.9.2. </b> "
---

#### Mục tiêu

Trong bước này, bạn sẽ chọn repository và nhánh phù hợp để Amplify có thể tự động theo dõi và deploy frontend.

#### Hướng dẫn

![alt text](image.png)

1. `Select repository`: chọn đúng kho chứa mã nguồn frontend của bạn, ví dụ `DTDuc04/DoAnMiniGame`.
2. `Select branch`: chọn nhánh Git dùng để trigger deploy tự động, ví dụ `V1`.
3. Nếu ứng dụng của bạn là monorepo, hãy tích chọn `My app is a monorepo` và nhập thư mục frontend trong ô `Monorepo root directory`, ví dụ `frontend`.
4. Nếu repository là dự án độc lập, bạn có thể bỏ qua cấu hình monorepo.

#### Lưu ý

Việc chọn đúng repository và nhánh là rất quan trọng vì Amplify sẽ dùng chúng làm nguồn dữ liệu cho mỗi lần build mới.
