---
title: "Nhật ký thực tập Tuần 3"
date: 2026-05-01
weight: 3
chapter: false
pre: "<b> 1.3. </b>"
---

### Mục tiêu Tuần 3:
* Nắm vững cơ chế tự động co giãn tài nguyên hệ thống máy chủ dựa trên nhu cầu sử dụng thực tế của hạ tầng.
* Tiếp cận tư duy phát triển ứng dụng trên kiến trúc phi máy chủ (Serverless), tối ưu hóa hiệu năng xử lý mã nguồn.
* Thiết lập chu trình kết nối dữ liệu tự động giữa tầng xử lý logic và tầng giao tiếp API đám mây.

### Danh sách công việc thực hiện:

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **[Nghiên cứu Lab 6]:** Phân tích nguyên lý hoạt động của Amazon EC2 Auto Scaling, cơ chế giám sát tải và các cấu hình kích hoạt Launch Templates. | 01/05/2026 | 01/05/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **2** | **[Thực hành Lab 6 - Phần 1]:** Thiết lập cấu hình máy chủ mẫu, khởi tạo nhóm Auto Scaling Group và cấu hình chính sách Manual Scaling. | 02/05/2026 | 02/05/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **3** | **[Thực hành Lab 6 - Phần 2]:** Cấu hình Dynamic Scaling, giả lập tải hệ thống để kiểm thử quy trình tự động tăng/giảm số lượng máy chủ ảo EC2. | 03/05/2026 | 03/05/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **4** | **[Nghiên cứu Lab 8]:** Khám phá kiến trúc phi máy chủ AWS Serverless, cơ chế hướng sự kiện (Event-driven) và nguyên lý hoạt động của AWS Lambda. | 04/05/2026 | 04/05/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **5** | **[Thực hành Lab 8 - Phần 1]:** Viết mã nguồn triển khai hàm xử lý logic trên AWS Lambda, thiết lập môi trường chạy thử nghiệm. | 05/05/2026 | 05/05/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **6** | **[Thực hành Lab 8 - Phần 2]:** Tích hợp AWS Lambda với Amazon API Gateway, công khai Function URL để xử lý các yêu cầu HTTP bên ngoài và dọn dẹp tài nguyên. | 06/05/2026 | 06/05/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |

---

### Chi tiết tiến độ hằng ngày (Cập nhật: 06/05/2026)

**Nội dung đã thực hiện ngày 05/05 (Trọng tâm: Lab 8):**
* Hoàn thành việc khởi tạo và cấu hình hàm Lambda thực thi các tác vụ logic mà không cần quản lý hệ điều hành nền.
* Cấu hình môi trường Runtime, thiết lập dung lượng bộ nhớ phù hợp và tối ưu hóa mã xử lý đầu vào để chuẩn bị cho bước tích hợp mạng tiếp theo.

**Kế hoạch ngày 06/05 (Trọng tâm: Lab 8):**
* Triển khai tạo và kết nối cổng dịch vụ Amazon API Gateway làm điểm tiếp nhận yêu cầu từ người dùng.
* Cấu hình Route định tuyến luồng HTTP trực tiếp đến hàm AWS Lambda thông qua tính năng Function URL, tiến hành kiểm thử gửi nhận dữ liệu thực tế trên trình duyệt, sau đó thực hiện xóa bỏ toàn bộ hạ tầng thử nghiệm để bảo vệ hạn mức tài khoản.

---

### Kết quả đạt được trong Tuần 3:

* **Tự động hóa quy mô hạ tầng tính toán (Lab 6):**
    * Nắm vững tư duy thiết kế hệ thống có khả năng tự phục hồi và co giãn linh hoạt dựa trên các chỉ số hiệu năng cụ thể (CPU, RAM).
    * Thành thạo kỹ năng tạo lập khuôn mẫu máy chủ chuẩn hóa, cấu hình ngưỡng cảnh báo giúp tối ưu hóa chi phí vận hành hạ tầng doanh nghiệp.
* **Lập trình và làm chủ kiến trúc phi máy chủ Serverless (Lab 8):**
    * Thay đổi tư duy quản trị từ quản lý hệ điều hành sang quản lý luồng sự kiện xử lý mã nguồn độc lập.
    * Đạt kỹ năng xây dựng API đám mây tốc độ cao, kết nối nhịp nhàng các dịch vụ tính toán hướng sự kiện để tạo nên một ứng dụng web hoàn chỉnh.
* **Tối ưu hóa tài nguyên & Kỹ năng bổ trợ kỹ thuật:**
    * Nâng cao năng lực phân tích nhật ký hoạt động thông qua các số liệu đo đạc tải hệ thống thực tế.
    * Tiếp tục duy trì thói quen giải phóng tài nguyên sau thực hành, cập nhật tiến độ kỹ thuật đều đặn và quản lý mã nguồn bài Lab chặt chẽ trên GitHub.
