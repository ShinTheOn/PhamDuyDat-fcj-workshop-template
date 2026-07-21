---
title: "Nhật ký thực tập Tuần 1"
date: 2026-04-17
weight: 1
chapter: false
pre: "<b> 1.1. </b>"
---

### Mục tiêu Tuần 1:
* Kết nối, làm quen đội ngũ cán bộ hướng dẫn và các thành viên trong cộng đồng First Cloud Journey (FCJ).
* Tiếp nhận và quán triệt đầy đủ các nội quy, quy định, văn hóa doanh nghiệp cùng tiêu chuẩn báo cáo.
* Triển khai nghiên cứu sâu và làm chủ hạ tầng với 3 bài Lab lớn: AWS Account, AWS CLI, và Amazon EC2 & EBS.

### Danh sách công việc thực hiện:

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| **1** | - Làm quen các thành viên và cán bộ hướng dẫn.<br>- Tiếp nhận bàn giao vị trí, nghiên cứu nội quy thực tập. | 17/04/2026 | 17/04/2026 | [AWS Study Group](https://hcm-rules.awsfcaj.com/) |
| **2** | **[Nghiên cứu Lab 1 & Lab 2]:** Tìm hiểu lý thuyết Cloud, quy trình đăng ký tài khoản và cách thiết lập môi trường CLI. | 18/04/2026 | 18/04/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **3** | **[Thực hành Lab 1 & Lab 2]:** Kích hoạt bảo mật đa lớp MFA, khởi tạo Access Key và kiểm tra cấu hình kết nối AWS CLI. | 19/04/2026 | 19/04/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **4** | **[Nghiên cứu Lab 3]:** Tìm hiểu kiến trúc máy chủ Amazon EC2, phân loại các dòng Instance, ổ đĩa EBS và phương thức SSH. | 20/04/2026 | 20/04/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **5** | **[Thực hành Lab 3 - Phần 1]:** Khởi tạo máy chủ EC2 instance từ Console, thiết lập cặp khóa bảo mật và cấu hình Security Group. | 21/04/2026 | 21/04/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **6** | **[Thực hành Lab 3 - Phần 2]:** Remote SSH vào máy chủ Linux, tạo phân vùng ổ đĩa mạng EBS Volume và dọn dẹp tài nguyên. | 22/04/2026 | 22/04/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |

---

### Chi tiết tiến độ hằng ngày (Cập nhật: 22/04/2026)

**Nội dung đã thực hiện ngày 21/04 (Trọng tâm: Lab 3):**
* Hoàn thành việc thiết lập và cấu hình hoàn chỉnh cho một máy chủ Linux EC2 instance thông qua giao diện Management Console.
* Xây dựng nhóm quy tắc tường lửa Security Group (mở cổng 22 cho cấu hình SSH và cổng 80 cho dịch vụ HTTP) và tạo bộ khóa Key Pair để xác thực danh tính.

**Kế hoạch ngày 22/04 (Trọng tâm: Lab 3):**
* Tiến hành kết nối từ xa trực tiếp vào hệ điều hành máy chủ EC2 bằng Terminal thông qua tệp khóa cá nhân cá nhân hóa.
* Khởi tạo một ổ đĩa Elastic Block Store (EBS Volume) độc lập trên hệ thống, thực hiện các câu lệnh định dạng phân vùng hệ thống tệp và gắn kết (Mount) mở rộng bộ nhớ. Sau khi hoàn thành, tiến hành giải phóng hoàn toàn các tài nguyên để tránh phát sinh chi phí.

---

### Kết quả đạt được trong Tuần 1:

* **Năng lực quản trị tài khoản & Môi trường CLI đám mây (Lab 1 & Lab 2):**
    * Làm chủ quy trình xây dựng tài khoản Root an toàn và thiết lập các lớp bảo mật bảo vệ danh tính thiết bị (MFA).
    * Thành thạo kỹ năng tương tác hệ thống bằng dòng lệnh không qua giao diện web, thiết lập chuẩn cấu hình lưu trữ Access Key và kiểm tra trạng thái các khu vực hệ thống.
* **Kỹ năng quản lý tài nguyên tính toán & Lưu trữ nâng cao (Lab 3):**
    * Hiểu rõ cơ chế phân bổ tài nguyên máy chủ ảo đám mây, biết cách đánh giá và lựa chọn gói dịch vụ tối ưu hiệu năng và kinh phí.
    * Đạt được kỹ năng quản trị lưu trữ tệp tin nâng cao, thực hiện cấu trúc phân vùng ổ cứng, mở rộng dung lượng ổ đĩa đám mây (EBS) cho hệ thống máy chủ Linux.
* **Kiến thức an toàn thông tin & Kỹ năng bổ trợ:**
    * Kiểm soát chặt chẽ lưu lượng kết nối mạng ra vào thông qua cấu hình quy chuẩn Security Group.
    * Thành thạo nguyên lý mã hóa bất đối xứng phục vụ giám sát hạ tầng từ xa bằng mã khóa bảo mật.
    * Thích nghi tốt với môi trường thực tập tại FCJ, làm quen và thực hiện nghiêm túc quy trình viết báo cáo, cập nhật tiến độ kỹ thuật hàng ngày lên GitHub.
