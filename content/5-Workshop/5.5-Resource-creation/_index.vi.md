---
title : "Xác nhận và Tạo Tài Nguyên"
date: 2026-07-12
weight : 5
chapter : false
pre : " <b> 5.5. </b> "
---

#### Mục tiêu

Trong phần này, bạn sẽ tiếp tục quá trình thiết lập pipeline bằng cách kiểm tra lại toàn bộ cấu hình trước khi AWS tạo các tài nguyên thực tế. Đây là bước quan trọng để đảm bảo pipeline có thể chạy thành công khi bắt đầu deployment.

#### Bước 3: Xác nhận và tạo tài nguyên

Sau khi đã nhập đầy đủ thông tin cho các stage và cấu hình pipeline, hệ thống sẽ hiển thị một bảng tổng hợp để bạn kiểm tra lại trước khi tiến hành tạo tài nguyên.

1. Hệ thống sẽ hiển thị bảng tóm tắt cấu hình (Summary).
2. Hãy đọc kỹ từng mục như stage name, region, profile, template path, stack name và các tài nguyên sẽ được tạo tự động.
3. Nếu mọi thông tin đều phù hợp, nhấn `Enter` để xác nhận tiếp tục.
4. Tại câu hỏi `Should we proceed with the creation? [y/N]`, nhập `y` để đồng ý tạo các tài nguyên trên AWS.
5. Chờ quá trình tạo tài nguyên chạy. Khi hệ thống hoàn tất, bạn sẽ nhận được thông báo `Successfully created!`.


#### Những mục cần kiểm tra trước khi tạo

Trước khi nhấn `y`, hãy chắc chắn rằng các mục sau đã đúng:
- Tên stage `dev` và `prod` đã được đặt đúng.
- Region AWS đã khớp với môi trường triển khai của bạn.
- Profile AWS đã được cấu hình và có quyền tạo stack, bucket, role và các tài nguyên cần thiết.
- Template path và stack name đã trỏ đúng tới project của bạn.
- Các giá trị ARN, role hay bucket nếu được để trống thì SAM sẽ tự tạo, nhưng bạn vẫn nên kiểm tra xem chúng có phù hợp không.

#### Ý nghĩa của việc xác nhận tạo

Khi bạn chọn `y`, AWS SAM sẽ tiến hành:
- Tạo các tài nguyên bootstrap cần thiết cho pipeline.
- Tạo các stack liên quan tới môi trường Dev và Prod.
- Cấu hình các file pipeline và tham chiếu deployment ban đầu.

Nếu quá trình hoàn tất thành công, bạn sẽ thấy thông báo `Successfully created!`, cho thấy hệ thống đã tạo xong cấu hình và tài nguyên cần thiết cho bước tiếp theo.

#### Kết quả mong đợi

Sau khi hoàn tất bước này, bạn sẽ có:
- Một pipeline cấu hình sẵn để tiếp tục chỉnh sửa hoặc liên kết với GitHub.
- Các tài nguyên AWS được khởi tạo tự động cho môi trường triển khai.
- Một nền tảng sẵn sàng để bước tiếp theo là kết nối repository và chạy deployment.

![Ảnh 1](/images/5-Workshop/5.5-Resource-creation/anh1.png)

![Ảnh 2](/images/5-Workshop/5.5-Resource-creation/anh2.png)

