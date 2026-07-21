---
title: "Nhật ký thực tập Tuần 6"
date: 2026-05-22
weight: 6
chapter: false
pre: "<b> 1.6. </b>"
---

### Mục tiêu Tuần 6:
* Nghiên cứu giải pháp lưu trữ tệp tin chia sẻ dung lượng lớn, có khả năng gắn kết đồng thời vào nhiều máy chủ.
* Master bộ công cụ quản trị hệ thống tự động nhằm cấu hình và vá lỗi máy chủ hàng loạt từ xa.
* Tối ưu hóa quy trình quản lý tập trung mã cấu hình cấu trúc và tham số bí mật của hệ thống.

### Danh sách công việc thực hiện:

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **[Nghiên cứu Lab 15]:** Tìm hiểu cơ chế hoạt động của hệ thống lưu trữ tệp tin chia sẻ Amazon EFS (Elastic File System), phân biệt với EBS và S3. | 22/05/2026 | 22/05/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **2** | **[Thực hành Lab 15]:** Khởi tạo hệ thống tệp tin Amazon EFS, cấu hình Mount Targets và thực hiện gắn kết chia sẻ ổ đĩa đồng thời vào cụm máy chủ EC2. | 23/05/2026 | 23/05/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **3** | **[Nghiên cứu Lab 16]:** Khám phá bộ công cụ quản lý vận hành AWS Management Tools, nghiên cứu các tính năng cốt lõi của AWS Systems Manager (SSM). | 24/05/2026 | 24/06/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **4** | **[Thực hành Lab 16 - Phần 1]:** Cấu hình IAM Role cho SSM Agent, thực hiện kết nối thiết lập máy chủ Linux an toàn không cần sử dụng khóa SSH truyền thống. | 25/05/2026 | 25/05/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **5** | **[Thực hành Lab 16 - Phần 2]:** Sử dụng SSM Run Command để thực thi các câu lệnh cài đặt phần mềm hàng loạt trên cụm máy chủ và quản lý tham số bí mật bằng SSM Parameter Store. | 26/05/2026 | 26/05/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **6** | **[Thực hành Lab 16 - Phần 3]:** Kiểm thử chu trình tự động cập nhật bản vá hệ điều hành (Patch Manager) thời gian thực và thực hiện giải phóng tài nguyên Lab. | 27/05/2026 | 27/05/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |

---

### Chi tiết tiến độ hằng ngày (Cập nhật: 27/05/2026)

**Nội dung đã thực hiện ngày 26/05 (Trọng tâm: Lab 16):**
* Hoàn thành việc tích hợp và lưu trữ các biến cấu hình môi trường, mật khẩu cơ sở dữ liệu một cách an toàn bên trong kho lưu trữ dữ liệu tập trung SSM Parameter Store.
* Thực hiện gửi lệnh chạy script cài đặt cập nhật ứng dụng hàng loạt đến toàn bộ danh sách máy chủ đích từ xa thông qua tính năng Run Command mà không cần đăng nhập thủ công.

**Kế hoạch ngày 27/05 (Trọng tâm: Lab 16):**
* Cấu hình và thiết lập quy trình quét, cài đặt tự động các bản vá bảo mật hệ điều hành quan trọng cho cụm EC2 instance bằng công cụ Patch Manager.
* Xác thực kết quả log báo cáo trạng thái tuân thủ bảo mật phần cứng thành công, sau đó tiến hành gỡ bỏ các cấu hình lưu trữ, tắt máy chủ thử nghiệm nhằm bảo vệ hạn mức tín dụng tài khoản thực tập.

---

### Kết quả đạt được trong Tuần 6:

* **Ứng dụng công nghệ lưu trữ dữ liệu dùng chung (Lab 15):**
    * Làm chủ giải pháp thiết kế phân vùng ổ đĩa mạng chia sẻ dữ liệu chung cho cụm máy chủ Linux, xử lý triệt để bài toán đồng bộ hóa dữ liệu phân tán.
    * Nắm vững kỹ năng cấu hình tối ưu hóa tốc độ đọc ghi luồng dữ liệu mạng dựa trên các lớp lưu trữ tệp tin chuyên biệt.
* **Tự động hóa quản trị hạ tầng quy mô lớn (Lab 16):**
    * Thay đổi phương thức quản lý máy chủ đơn lẻ truyền thống sang mô hình điều khiển tập trung tự động bằng mã lệnh từ xa.
    * Đạt tư duy bảo mật hạ tầng nâng cao thông qua việc cô lập cổng kết nối SSH, thay thế bằng cơ chế phân quyền kiểm soát truy cập phiên (Session Manager).
* **Chuẩn hóa quy trình kỹ thuật & Quản trị tài nguyên:**
    * Làm chủ kỹ năng quản lý và mã hóa thông tin mật cấu hình hệ sinh thái ứng dụng đám mây một cách khoa học.
    * Nghiêm túc duy trì quy trình thu dọn sạch sẽ hạ tầng tài nguyên thử nghiệm sau bài Lab, đồng bộ đầy đủ các cập nhật ghi chép nhật ký lên GitHub.
