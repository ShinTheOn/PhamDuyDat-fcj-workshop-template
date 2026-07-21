---
title: "Nhật ký thực tập Tuần 5"
date: 2026-05-15
weight: 5
chapter: false
pre: "<b> 1.5. </b>"
---

### Mục tiêu Tuần 5:
* Nghiên cứu hệ thống tiêu chuẩn bảo mật đám mây và cơ chế quản trị tài nguyên doanh nghiệp nghiêm ngặt.
* Xây dựng giải pháp giám sát, thu thập chỉ số hiệu năng và vết hoạt động toàn diện của hạ tầng.
* Thiết lập hệ thống cảnh báo tự động nhằm phát hiện sớm các sự cố vận hành và rủi ro chi phí.

### Danh sách công việc thực hiện:

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **[Nghiên cứu Lab 13]:** Khám phá các công cụ quản trị Security & Governance, tìm hiểu dịch vụ AWS CloudTrail để ghi nhật ký hoạt động hệ thống. | 15/05/2026 | 15/05/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **2** | **[Thực hành Lab 13]:** Cấu hình AWS CloudTrail thu thập log, thiết lập AWS Config để kiểm tra tính tuân thủ quy định cấu hình tài nguyên tài khoản. | 16/05/2026 | 16/05/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **3** | **[Nghiên cứu Lab 14]:** Phân tích cơ chế giám sát hạ tầng đám mây nâng cao, nghiên cứu dịch vụ Amazon CloudWatch (Metrics, Logs, Alarms). | 17/05/2026 | 17/05/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **4** | **[Thực hành Lab 14 - Phần 1]:** Cấu hình CloudWatch Logs Agent thu thập nhật ký từ máy chủ EC2, xây dựng giao diện Dashboard theo dõi trực quan. | 18/05/2026 | 18/05/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **5** | **[Thực hành Lab 14 - Phần 2]:** Tạo các bộ lọc mã lỗi nhật ký CloudWatch Metric Filters và cấu hình các ngưỡng cảnh báo tự động CloudWatch Alarms. | 19/05/2026 | 19/05/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **6** | **[Thực hành Lab 14 - Phần 3]:** Giả lập lỗi hệ thống để kiểm thử quy trình kích hoạt cảnh báo qua SNS email và tiến hành dọn dẹp các tài nguyên thử nghiệm. | 20/05/2026 | 20/05/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |

---

### Chi tiết tiến độ hằng ngày (Cập nhật: 20/05/2026)

**Nội dung đã thực hiện ngày 19/05 (Trọng tâm: Lab 14):**
* Hoàn thành việc thiết lập bộ lọc số liệu từ luồng nhật ký hệ thống tập trung của máy chủ nhằm bóc tách các mã lỗi ứng dụng.
* Định nghĩa thành công các ngưỡng giới hạn an toàn cho tài nguyên (như quá tải CPU, cạn kiệt bộ nhớ) trên công cụ CloudWatch Alarms.

**Kế hoạch ngày 20/05 (Trọng tâm: Lab 14):**
* Triển khai liên kết các kịch bản cảnh báo CloudWatch với dịch vụ thông báo tin nhắn Amazon SNS để tự động gửi thông tin sự cố về email quản trị viên.
* Bật công cụ kiểm thử giả lập tải nặng và tạo lỗi log nhân tạo để xác thực chu trình gửi cảnh báo thời gian thực, sau đó thực hiện xóa bỏ hạ tầng cấu hình để tối ưu hóa hạn mức tài khoản credit.

---

### Kết quả đạt được trong Tuần 5:

* **Nâng cao năng lực quản trị và kiểm toán an toàn (Lab 13):**
    * Thành thạo cơ chế theo dõi hành vi hệ thống, lưu vết toàn bộ các hoạt động thay đổi kiến trúc đám mây phục vụ công tác điều tra sự cố.
    * Đạt tư duy quản trị chuẩn hóa thông qua việc tự động đánh giá các tài nguyên không tuân thủ chính sách an toàn thông tin doanh nghiệp.
* **Làm chủ giải pháp giám sát toàn diện hệ thống (Lab 14):**
    * Chuyển đổi mô hình vận hành bị động sang chủ động kiểm soát sức khỏe hạ tầng, cấu hình thu thập log tập trung cho máy chủ ảo đám mây.
    * Có khả năng xây dựng các bảng điều khiển trực quan (Dashboard) theo dõi các chỉ số tải kỹ thuật và thiết lập cơ chế phản ứng nhanh trước các dấu hiệu bất thường.
* **Kỹ năng tối ưu hóa vận hành kỹ thuật:**
    * Phát triển tư duy xử lý sự cố (Troubleshooting) dựa trên số liệu thực tế được bóc tách từ nhật ký giám sát.
    * Nghiêm túc duy trì quy trình giải phóng môi trường Lab để bảo vệ tài khoản, thực hiện cập nhật tiến độ kỹ thuật đầy đủ lên kho lưu trữ GitHub.
