---
title: "Nhật ký thực tập Tuần 7"
date: 2026-05-29
weight: 7
chapter: false
pre: "<b> 1.7. </b>"
---

### Mục tiêu Tuần 7:
* Nghiên cứu chiến lược quản lý tài chính đám mây, phân tích hiệu suất nhằm cắt giảm tài nguyên lãng phí.
* Triển khai mô hình bảo vệ an toàn dữ liệu doanh nghiệp thông qua kế hoạch sao lưu tự động đa tầng.
* Thiết lập và thử nghiệm quy trình phục hồi hệ thống nhanh chóng sau các kịch bản giả lập sự cố.

### Danh sách công việc thực hiện:

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **[Nghiên cứu Lab 17]:** Khám phá các nguyên tắc tối ưu hóa chi phí Cost Optimization, nghiên cứu cách sử dụng AWS Trusted Advisor và AWS Compute Optimizer. | 29/05/2026 | 29/05/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **2** | **[Thực hành Lab 17]:** Đo đạc hiệu năng thực tế các cụm máy chủ, rà soát hệ thống để phát hiện và thu hồi các ổ đĩa EBS độc lập không sử dụng nhằm tối ưu ngân sách. | 30/05/2026 | 30/05/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **3** | **[Nghiên cứu Lab 18]:** Phân tích các giải pháp sao lưu và phục hồi Backup & Recovery, tìm hiểu cơ chế hoạt động, định nghĩa RPO và RTO trên AWS Backup. | 31/05/2026 | 31/05/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **4** | **[Thực hành Lab 18 - Phần 1]:** Khởi tạo Backup Vault, thiết lập kế hoạch sao lưu (Backup Plan) tự động cho toàn bộ hệ thống máy chủ EC2 và ổ đĩa EBS. | 01/06/2026 | 01/06/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **5** | **[Thực hành Lab 18 - Phần 2]:** Cấu hình cơ chế vòng đời chuyển đổi bản sao dự phòng cũ sang các lớp lưu trữ lạnh (Cold Storage) để tối ưu chi phí lưu trữ. | 02/06/2026 | 02/06/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **6** | **[Thực hành Lab 18 - Phần 3]:** Giả lập kịch bản mất mát dữ liệu hệ thống, thực hiện quy trình khôi phục (Restore) từ bản snapshot và giải phóng tài nguyên Lab. | 03/06/2026 | 03/06/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |

---

### Chi tiết tiến độ hằng ngày (Cập nhật: 03/06/2026)

**Nội dung đã thực hiện ngày 02/06 (Trọng tâm: Lab 18):**
* Hoàn thành việc thiết lập chính sách vòng đời (Lifecycle policy) cho các bản sao lưu dữ liệu hạ tầng tập trung.
* Cấu hình thành công quy trình tự động chuyển dịch các bản snapshot cũ sang kho lưu trữ dài hạn có chi phí thấp sau chu kỳ lưu giữ quy định.

**Kế hoạch ngày 03/06 (Trọng tâm: Lab 18):**
* Thực hiện xóa bỏ thử nghiệm một máy chủ ảo đang chạy để giả lập tình huống thảm họa phần cứng.
* Khởi chạy quy trình khôi phục khẩn cấp từ bản sao lưu gần nhất trong Backup Vault, xác thực tính toàn vẹn của dữ liệu sau phục hồi, sau đó tiến hành gỡ bỏ toàn bộ cấu hình để bảo vệ hạn mức tín dụng tài khoản.

---

### Kết quả đạt được trong Tuần 7:

* **Tối ưu hóa quản trị tài chính đám mây (Lab 17):**
    * Nắm vững tư duy đánh giá hiệu suất hệ thống, biết cách bóc tách chỉ số để thu hẹp quy mô (Right-sizing) tài nguyên phù hợp với nhu cầu thực tế.
    * Thành thạo kỹ năng sử dụng công cụ phân tích tự động để loại bỏ triệt để tình trạng lãng phí tài nguyên ngầm trên Cloud.
* **Xây dựng giải pháp an toàn dữ liệu toàn diện (Lab 18):**
    * Làm chủ quy trình cấu hình hệ thống sao lưu tập trung, đảm bảo tính sẵn sàng cao và khả năng phục hồi dữ liệu cho doanh nghiệp.
    * Đạt được năng lực thiết lập các chỉ số an toàn thông tin (RPO/RTO) chuẩn hóa, đáp ứng yêu cầu vận hành liên tục của hệ thống CNTT.
* **Chuẩn hóa kỹ năng kỹ thuật & Vận hành:**
    * Phát triển kỹ năng xử lý ứng phó sự cố (Disaster Recovery) một cách bài bản thông qua kịch bản khôi phục thực tế.
    * Nghiêm túc duy trì quy trình giải phóng môi trường Lab sau thực hành, hoàn thiện nhật ký kỹ thuật đồng bộ lên hệ thống GitHub.
