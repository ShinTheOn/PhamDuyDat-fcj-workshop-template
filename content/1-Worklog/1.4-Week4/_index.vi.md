---
title: "Nhật ký thực tập Tuần 4"
date: 2026-05-08
weight: 4
chapter: false
pre: "<b> 1.4. </b>"
---

### Mục tiêu Tuần 4:
* Tiếp cận và làm chủ công nghệ đóng gói ứng dụng (Containerization) bằng Docker trên nền tảng đám mây.
* Hiểu cơ chế quản lý, lưu trữ và điều phối các cụm ứng dụng Container quy mô lớn.
* Nghiên cứu bộ công cụ phát triển ứng dụng nâng cao nhằm xây dựng chu trình tích hợp và triển khai tự động (CI/CD).

### Danh sách công việc thực hiện:

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **[Nghiên cứu Lab 10]:** Tìm hiểu kiến trúc đóng gói Containers trên AWS, phân biệt Docker Image và Container, nghiên cứu dịch vụ Amazon ECR và ECS. | 08/05/2026 | 08/05/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **2** | **[Thực hành Lab 10 - Phần 1]:** Khởi tạo Dockerfile, đóng gói ứng dụng web thành Docker Image và đẩy (Push) lên kho lưu trữ Amazon ECR. | 09/05/2026 | 09/05/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **3** | **[Thực hành Lab 10 - Phần 2]:** Cấu hình Task Definitions và khởi tạo cluster điều phối cụm Container chạy tự động trên Amazon ECS (Fargate). | 10/05/2026 | 10/05/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **4** | **[Nghiên cứu Lab 11]:** Khám phá bộ công cụ lập trình viên AWS Developer Tools, nguyên lý vận hành của hệ thống CI/CD tự động hóa. | 11/05/2026 | 11/05/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **5** | **[Thực hành Lab 11 - Phần 1]:** Thiết lập kho lưu trữ mã nguồn AWS CodeCommit và cấu hình tệp buildspec cho dịch vụ đóng gói tự động AWS CodeBuild. | 12/05/2026 | 12/05/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **6** | **[Thực hành Lab 11 - Phần 2]:** Xây dựng và liên kết chu trình tự động hóa với AWS CodePipeline, kiểm thử tự động deploy khi thay đổi code và giải phóng tài nguyên. | 13/05/2026 | 13/05/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |

---

### Chi tiết tiến độ hằng ngày (Cập nhật: 13/05/2026)

**Nội dung đã thực hiện ngày 12/05 (Trọng tâm: Lab 11):**
* Hoàn thành việc thiết lập hệ thống lưu trữ mã nguồn nội bộ và cấu hình môi trường tự động biên dịch mã nguồn với tệp cấu hình buildspec.
* Tối ưu hóa các câu lệnh kiểm tra lỗi mã nguồn đầu vào nhằm chuẩn bị tốt cho quá trình tự động hóa đóng gói sản phẩm.

**Kế hoạch ngày 13/05 (Trọng tâm: Lab 11):**
* Triển khai xây dựng chu trình tự động hóa hoàn chỉnh (Pipeline) kết nối liền mạch từ bước nhận code, build tự động cho đến deploy trực tiếp.
* Thực hiện thay đổi một đoạn mã nguồn nhỏ, kiểm thử tính năng tự động cập nhật hệ thống của Pipeline qua giao diện web, sau đó thực hiện dọn dẹp hạ tầng để tối ưu hạn mức tài khoản.

---

### Kết quả đạt được trong Tuần 4:

* **Làm chủ công nghệ đóng gói và điều phối ứng dụng (Lab 10):**
    * Thành thạo kỹ năng viết mã đóng gói ứng dụng, tối ưu kích thước gói sản phẩm đám mây và quản lý kho lưu trữ hình ảnh Docker.
    * Đạt được tư duy vận hành hệ thống Container hiện đại, cấu hình phân bổ tài nguyên tính toán tự động mà không cần can thiệp máy chủ vật lý.
* **Xây dựng chu trình tự động hóa phát triển CI/CD (Lab 11):**
    * Thay đổi quy trình làm việc thủ công sang tư duy tự động hóa hoàn toàn các bước kiểm thử và phát hành sản phẩm phần mềm.
    * Gắn kết thành công các mắt xích dịch vụ nhà phát triển đám mây, giúp tăng tốc độ triển khai dự án doanh nghiệp và giảm thiểu sai sót do con người.
* **Tối ưu hóa quy trình làm việc kỹ thuật:**
    * Nâng cao năng lực sửa lỗi (Debug) các tệp tin cấu hình hệ thống tự động hóa.
    * Tiếp tục duy trì thói quen kiểm tra và giải phóng tài nguyên sau khi hoàn tất Lab để bảo vệ Credit tài khoản, quản lý mã nguồn đồng bộ lên GitHub.
