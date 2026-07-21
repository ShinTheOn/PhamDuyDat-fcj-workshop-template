---
title: "Nhật ký thực tập Tuần 2"
date: 2026-04-24
weight: 2
chapter: false
pre: "<b> 1.2. </b>"
---

### Mục tiêu Tuần 2:
* Làm chủ chính sách kiểm soát truy cập và cấu trúc quản lý phân quyền người dùng trong môi trường doanh nghiệp.
* Nắm vững kiến trúc phân vùng cô lập hạ tầng hệ thống thông qua việc tùy biến sơ đồ mạng Cloud.
* Triển khai giải pháp lưu trữ đối tượng bền vững, cấu hình nâng cao các quy tắc vòng đời cho tệp tin.

### Danh sách công việc thực hiện:

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **[Nghiên cứu Lab 4]:** Tìm hiểu mô hình phân quyền doanh nghiệp, cơ chế xác thực danh tính và các chính sách quản lý AWS IAM. | 24/04/2026 | 24/04/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **2** | **[Thực hành Lab 4]:** Khởi tạo các nhóm người dùng chuyên biệt, thiết lập chính sách Policies chi tiết và ép buộc xác thực MFA. | 25/04/2026 | 25/04/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **3** | **[Nghiên cứu Lab 5]:** Phân tích cơ chế cô lập lưu lượng mạng, nguyên lý định tuyến và thiết kế mô hình mạng độc lập Amazon VPC. | 26/04/2026 | 26/04/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **4** | **[Thực hành Lab 5 - Phần 1]:** Triển khai sơ đồ mạng VPC tùy chỉnh, phân chia các phân vùng Public Subnet, Private Subnet và thiết lập bảng định tuyến Route Table. | 27/04/2026 | 27/04/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **5** | **[Thực hành Lab 5 - Phần 2]:** Cấu hình cổng Internet Gateway, thiết lập trạm NAT Gateway và thắt chặt an toàn phân vùng bằng Network ACLs. | 28/04/2026 | 28/04/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **6** | **[Thực hành Lab 7]:** Khởi tạo các kho lưu trữ dữ liệu Amazon S3, cấu hình mã hóa tài sản hệ thống và thiết lập quy tắc vòng đời Lifecycle. | 29/04/2026 | 29/04/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |

---

### Chi tiết tiến độ hằng ngày (Cập nhật: 29/04/2026)

**Nội dung đã thực hiện ngày 28/04 (Trọng tâm: Lab 5):**
* Hoàn thiện kiến trúc phân tầng lưu lượng bên trong phân vùng mạng cô lập Virtual Private Cloud (VPC).
* Cấu hình thành công các tuyến đường vận hành để định tuyến luồng dữ liệu một cách an toàn và thiết lập chi tiết bộ quy tắc tường lửa trong Network ACLs.

**Kế hoạch ngày 29/04 (Trọng tâm: Lab 7):**
* Thiết lập kho lưu trữ đối tượng bền vững thông qua giao diện quản lý của dịch vụ Amazon Simple Storage Service (S3).
* Cấu hình các chính sách Bucket Policy để chặn hoàn toàn nguy cơ rò rỉ dữ liệu ra ngoài Internet công cộng, thử nghiệm tương tác dữ liệu liên vùng và thiết lập quy trình tự động chuyển đổi định dạng tệp tin lưu trữ sang các lớp có chi phí thấp hơn nhằm tối ưu hóa ngân sách trước khi dọn dẹp môi trường thử nghiệm.

---

### Kết quả đạt được trong Tuần 2:

* **Quản trị định danh & Kiểm soát truy cập doanh nghiệp (Lab 4):**
    * Nắm toàn quyền kiểm soát quy trình cấp phát tài nguyên thông qua khung bảo mật IAM, loại bỏ thói quen sử dụng tài khoản Root để quản trị.
    * Đạt kỹ năng thực tế trong việc phân bổ các chính sách bảo mật chi tiết và quản lý an toàn mã khóa truy cập từ xa cho lập trình viên.
* **Xây dựng hạ tầng mạng độc lập chuẩn Production (Lab 5):**
    * Tích lũy kinh nghiệm thiết kế toàn diện sơ đồ mạng Cloud bao gồm phân tầng hệ thống và định tuyến phân vùng thông suốt.
    * Triển khai thành công bộ quy tắc kiểm soát truy cập tại ranh giới mạng nhằm lọc bỏ và ngăn chặn các yêu cầu kết nối không hợp lệ.
* **Hệ thống hóa giải pháp lưu trữ đối tượng quy mô lớn (Lab 7):**
    * Làm chủ các tính năng quản lý lưu trữ nâng cao như thiết lập tham số bảo mật cấu hình, mã hóa tài sản máy chủ và kiểm soát điểm truy cập.
    * Ứng dụng thành công quy trình tự động hóa chu kỳ tệp tin để dịch chuyển dữ liệu cũ sang các tầng lưu trữ tối ưu theo thời gian.
