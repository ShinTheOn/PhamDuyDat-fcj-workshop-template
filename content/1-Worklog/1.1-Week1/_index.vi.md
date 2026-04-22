---
title: "Nhật ký thực tập Tuần 1"
date: 2026-04-17
weight: 1
chapter: false
pre: "<b> 1.1. </b>"
---

{{% notice info %}}
**Ghi chú:** Báo cáo này ghi lại tiến độ hoàn thành Module 1 và 5 nhiệm vụ AWS cốt lõi để xây dựng nền tảng Cloud.
{{% /notice %}}

### Mục tiêu Tuần 1:
* Kết nối và làm quen với các thành viên trong cộng đồng First Cloud Journey (FCJ).
* Nắm vững các quy định, nội quy và tiêu chuẩn báo cáo của đơn vị thực tập.
* Thành thạo 5 dịch vụ AWS cơ bản thông qua các bài thực hành "Cloud Journey".

### Danh sách công việc thực hiện:

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| **1** | - Làm quen thành viên FCJ.<br>- Đọc và nắm rõ nội quy thực tập. | 17/04/2026 | 17/04/2026 | FCJ Handbook |
| **2** | **Nhiệm vụ 1:** Khởi tạo máy chủ với **Amazon EC2**. | 18/04/2026 | 18/04/2026 | [AWS Study Group](https://000001.awsstudygroup.com/) |
| **3** | **Nhiệm vụ 2:** Sử dụng mô hình nền tảng trong **Amazon Bedrock**. | 19/04/2026 | 19/04/2026 | [AWS Study Group](https://000001.awsstudygroup.com/) |
| **4** | **Nhiệm vụ 3:** Thiết lập ngân sách chi phí với **AWS Budgets**. | 20/04/2026 | 20/04/2026 | [AWS Study Group](https://000001.awsstudygroup.com/) |
| **5** | **Nhiệm vụ 4:** Tạo ứng dụng web bằng **AWS Lambda**. | 21/04/2026 | 21/04/2026 | [AWS Study Group](https://000001.awsstudygroup.com/) |
| **6** | **Nhiệm vụ 5:** Khởi tạo cơ sở dữ liệu **Amazon Aurora/RDS**. | 22/04/2026 | 22/04/2026 | [AWS Study Group](https://000001.awsstudygroup.com/) |

---

### Chi tiết tiến độ hằng ngày (Cập nhật: 22/04/2026)

**Nội dung đã thực hiện ngày 21/04:**
* **Hoàn thành Nhiệm vụ 4:** Triển khai thành công ứng dụng web không máy chủ (Serverless) bằng **AWS Lambda**.
* Sử dụng Lambda HTTP blueprint để xử lý các yêu cầu web và kiểm tra thành công qua Function URL.
* Thực hiện dọn dẹp tài nguyên (Xóa hàm) để đảm bảo không phát sinh chi phí ngoài ý muốn.

**Kế hoạch ngày 22/04:**
* **Thực hiện Nhiệm vụ 5:** Khởi tạo cụm cơ sở dữ liệu **Amazon RDS/Aurora**.
* Thực hành cấu hình Security Group cho Database và tìm hiểu quy trình quản lý snapshot cũng như xóa dữ liệu an toàn.

---

### Kết quả đạt được trong Tuần 1:

* **Làm chủ các dịch vụ AWS cơ bản:**
    * **Compute:** Có kỹ năng khởi tạo, cấu hình và kết nối SSH vào máy chủ EC2.
    * **GenAI:** Trải nghiệm thực tế về Prompt Engineering và xử lý cấp quyền mô hình (Model Access) trên Bedrock.
    * **Serverless:** Hiểu kiến trúc hướng sự kiện và triển khai ứng dụng web mà không cần quản lý hệ điều hành.
    * **Database:** Biết cách thiết lập và quản lý hệ quản trị cơ sở dữ liệu quan hệ trên đám mây.
* **Thành thạo quản lý chi phí:**
    * Cấu hình thành công **AWS Budgets** với ngưỡng cảnh báo 80%, giúp phòng tránh các "Credit Killers".
    * Hình thành thói quen "Dọn dẹp" (Terminate/Delete) tài nguyên ngay sau khi thực hành để bảo vệ hạn mức Credit.
* **Kỹ năng kỹ thuật & Bảo mật:**
    * Quản lý thành thạo Key Pair và cấu hình Security Group (các luật SSH/HTTP).
    * Biết cách điều hướng và sử dụng tối ưu bảng điều khiển AWS Management Console.
* **Kỹ năng làm việc & Giao tiếp:**
    * Hòa nhập nhanh với đội ngũ FCJ và làm quen với quy trình báo cáo tiến độ hằng ngày (Daily Report).
    * Xây dựng được hệ thống báo cáo khoa học trên GitHub và các kênh liên lạc nhóm.

---
**Ghi chú:** Toàn bộ bằng chứng và ảnh chụp màn hình các bài Lab đã được tổng hợp đầy đủ cho báo cáo cuối Module 1.
