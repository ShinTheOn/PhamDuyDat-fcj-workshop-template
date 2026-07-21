---
title: "Nhật ký thực tập Tuần 8"
date: 2026-06-05
weight: 8
chapter: false
pre: "<b> 1.8. </b>"
---

### Mục tiêu Tuần 8:
* Nghiên cứu giải pháp thu thập, chuyển đổi và phân tích luồng nhật ký hệ thống quy mô lớn theo thời gian thực.
* Tìm hiểu chiến lược và các công cụ dịch chuyển cơ sở dữ liệu từ hạ tầng On-premise lên đám mây an toàn.
* Xây dựng hệ thống truy vấn dữ liệu trực tiếp giúp tối ưu hóa khả năng giám sát và khai thác thông tin hệ thống.

### Danh sách công việc thực hiện:

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **[Nghiên cứu Lab 19]:** Tìm hiểu kiến trúc xử lý luồng dữ liệu Analytics trên AWS, nghiên cứu cơ chế hoạt động của Amazon Kinesis và Amazon Athena. | 05/06/2026 | 05/06/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **2** | **[Thực hành Lab 19 - Phần 1]:** Cấu hình Amazon Kinesis Data Firehose để thu thập và tự động chuyển luồng log hệ thống lưu trữ vào Amazon S3. | 06/06/2026 | 06/06/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **3** | **[Thực hành Lab 19 - Phần 2]:** Khởi tạo AWS Glue Data Catalog để định nghĩa cấu trúc dữ liệu log và sử dụng Amazon Athena viết câu lệnh SQL truy vấn trực tiếp dữ liệu. | 07/06/2026 | 07/06/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **4** | **[Nghiên cứu Lab 20]:** Khám phá các mô hình di chuyển hạ tầng Migration nâng cao, nghiên cứu công cụ dịch chuyển cơ sở dữ liệu AWS Database Migration Service (DMS). | 08/06/2026 | 08/06/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **5** | **[Thực hành Lab 20]:** Cấu hình Replication Instance, thiết lập Source/Target Endpoints và tạo tác vụ dịch chuyển dữ liệu (Migration Task) giả lập. | 09/06/2026 | 09/06/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **6** | **[Thực hành Lab 20 - Kiểm thử]:** Vận hành tác vụ chuyển đổi dữ liệu, kiểm tra tính toàn vẹn của cấu trúc database sau chuyển đổi và thực hiện giải phóng tài nguyên. | 10/06/2026 | 10/06/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |

---

### Chi tiết tiến độ hằng ngày (Cập nhật: 10/06/2026)

**Nội dung đã thực hiện ngày 09/06 (Trọng tâm: Lab 20):**
* Hoàn thành việc thiết lập và cấu hình các điểm kết nối mã hóa cho dịch vụ dịch chuyển cơ sở dữ liệu độc lập AWS DMS.
* Định nghĩa thành công các quy tắc ánh xạ bảng dữ liệu (Table mappings) và khởi tạo tiến trình Replication để chuẩn bị cho chu trình đồng bộ cấu trúc hệ thống.

**Kế hoạch ngày 10/06 (Trọng tâm: Lab 20):**
* Kích hoạt tác vụ Migration Task thực thi quá trình chuyển đổi dữ liệu giả lập từ nguồn máy chủ nội bộ lên dịch vụ cơ sở dữ liệu đám mây.
* Xác thực đối chiếu số lượng bản ghi giữa hai môi trường để đảm bảo không xảy ra lỗi mất mát cấu trúc thông tin, sau đó thực hiện xóa bỏ toàn bộ hạ tầng thử nghiệm nhằm bảo vệ hạn mức credit tài khoản.

---

### Kết quả đạt được trong Tuần 8:

* **Xây dựng chu trình phân tích luồng dữ liệu lớn (Lab 19):**
    * Làm chủ giải pháp thiết lập đường ống thu thập log tự động, xử lý triệt để bài toán lưu trữ và phân tích dữ liệu phi cấu trúc quy mô lớn.
    * Đạt năng lực sử dụng các công cụ truy vấn không máy chủ để bóc tách thông tin hệ thống trực tiếp mà không cần khởi chạy cơ sở dữ liệu truyền thống.
* **Làm chủ quy trình quản trị dịch chuyển hạ tầng (Lab 20):**
    * Thay đổi tư duy chuyển đổi dữ liệu thủ công rủi ro cao sang mô hình dịch chuyển tự động, đảm bảo hệ thống đích hoạt động liên tục.
    * Thành thạo kỹ năng cấu hình thiết lập các tham số kết nối, xử lý ánh xạ dữ liệu đồng bộ mượt mà giữa các nền tảng database khác nhau.
* **Nâng cao tiêu chuẩn kỹ thuật & Quản lý tài nguyên:**
    * Phát triển năng lực kiểm thử và đối soát tính toàn vẹn của hệ thống dữ liệu sau khi thực hiện cấu hình nâng cao.
    * Nghiêm túc duy trì quy trình giải phóng môi trường Lab sau khi hoàn tất đánh giá kỹ thuật, đồng bộ đầy đủ dữ liệu báo cáo lên GitHub.
