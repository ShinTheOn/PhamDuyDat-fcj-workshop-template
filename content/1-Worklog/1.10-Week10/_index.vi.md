---
title: "Nhật ký thực tập Tuần 10"
date: 2026-06-19
weight: 10
chapter: false
pre: "<b> 1.10. </b>"
---

### Mục tiêu Tuần 10:
* Tiếp tục hoàn thành các bài Lab chuyên sâu về tối ưu hóa hiệu năng và quản lý cấu trúc hạ tầng đám mây.
* Tích cực phối hợp cùng các thành viên trong nhóm để triển khai, cấu hình và đồng bộ các phân hệ của bài tập nhóm.
* Đóng gói mã nguồn và chuẩn bị tài liệu kỹ thuật phục vụ cho việc nghiệm thu đồ án phân công.

### Danh sách công việc thực hiện:

| Ngày | Nhiệm vụ | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **[Nghiên cứu Lab 23 & Họp nhóm]:** Tìm hiểu giải pháp quản lý hạ tầng bằng mã (Infrastructure as Code - IaC). Họp nhóm phân chia nhiệm vụ thiết kế kiến trúc tổng thể cho bài tập lớn. | 19/06/2026 | 19/06/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **2** | **[Thực hành Lab 23 & Làm bài nhóm]:** Khởi tạo template AWS CloudFormation, thực hiện deploy tự động hạ tầng VPC. Phối hợp với nhóm để tích hợp module mạng dùng chung. | 20/06/2026 | 20/06/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **3** | **[Nghiên cứu Lab 24]:** Tìm hiểu các phương pháp tối ưu hóa bộ nhớ đệm đám mây (Caching), nghiên cứu cơ chế hoạt động của Amazon ElastiCache. | 21/06/2026 | 21/06/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **4** | **[Thực hành Lab 24 & Làm bài nhóm]:** Triển khai cụm Redis/Memcached trên ElastiCache. Hỗ trợ nhóm cấu hình kết nối database an toàn giữa các phân hệ máy chủ ảo. | 22/06/2026 | 22/06/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **5** | **[Làm bài nhóm]:** Ngồi lại với cả nhóm để ráp các phần bài tập lại với nhau, chạy thử toàn bộ hệ thống xem có lỗi kết nối nào không. | 23/06/2026 | 23/06/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |
| **6** | **[Hoàn thiện file nhóm]:** Cùng viết tài liệu hướng dẫn, chụp lại ảnh kết quả chạy thành công và xóa các con server Lab cá nhân để đỡ tốn tiền credit. | 24/06/2026 | 24/06/2026 | [AWS Study Group](https://cloudjourney.awsstudygroup.com/) |

---

### Chi tiết tiến độ hằng ngày (Cập nhật: 24/06/2026)

**Nội dung đã thực hiện ngày 23/06 (Trọng tâm: Tiến độ bài tập nhóm):**
* Đã ngồi kết nối phần app với phần database cùng các thành viên trong nhóm để hệ thống chạy thông suốt.
* Kiểm tra và sửa lại mấy chỗ lỗi chặn cổng ở Security Group giữa các máy chủ của mấy bạn khác trong nhóm để dữ liệu truyền qua lại không bị lỗi.

**Kế hoạch ngày 24/06 (Trọng tâm: Hồ sơ bài tập nhóm):**
* Phối hợp viết nốt phần mô tả kỹ thuật cho bài tập lớn của nhóm, copy code và đẩy mấy file cấu hình chung lên kho Git nhóm.
* Vào lại AWS Console kiểm tra và tắt hết mấy con EC2, dịch vụ làm Lab cá nhân mấy bữa trước đi để bảo vệ tài khoản Free Tier/Credit khỏi bị trừ tiền.

---

### Kết quả đạt được trong Tuần 10:

* **Tiếp thu công nghệ hạ tầng tự động và lưu trữ đệm (Lab 23 & 24):**
    * Làm chủ tư duy triển khai hệ thống bằng mã nguồn, tối ưu hóa tốc độ khởi tạo môi trường doanh nghiệp quy mô lớn qua các tệp template cấu trúc.
    * Nắm vững kỹ năng tối ưu hóa hiệu năng đọc/ghi dữ liệu ứng dụng, giảm thiểu độ trễ truy vấn thông qua việc triển khai các lớp lưu trữ đệm.
* **Nâng cao năng lực làm việc nhóm kỹ thuật:**
    * Thúc đẩy kỹ năng giao tiếp và phối hợp kỹ thuật hiệu quả khi tích hợp hệ thống phân tán phức tạp với các thành viên khác trong đội ngũ.
    * Đạt được tư duy bao quát về kiến trúc hệ thống, biết cách đồng bộ hóa công việc cá nhân khớp với tiến độ chung của toàn đội.
* **Chuẩn hóa quy trình kỹ sư & Quản lý tài nguyên:**
    * Phát triển năng lực đóng gói mã nguồn và xây dựng hồ sơ kỹ thuật đồ án phối hợp chuẩn chỉnh theo tiêu chuẩn vận hành thực tế.
    * Nghiêm túc duy trì quy trình giải phóng môi trường Lab cá nhân để tối ưu ngân sách tài khoản, đồng bộ đầy đủ nhật ký lên GitHub.
