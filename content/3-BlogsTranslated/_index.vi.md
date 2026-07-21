---
title: "Các bài blogs đã dịch"
date: 2026-07-09
weight: 3
chapter: false
pre: " <b> 3. </b> "
---

### [Blog 1 - Cách Synthesia tối ưu hóa AI sinh video trên Amazon EC2 G7e](3.1-Blog1/)
Bài viết phân tích giải pháp kỹ thuật có tên gọi *Asynchronous Frame Generation Pipeline* do Synthesia và AWS hợp tác phát triển. Bằng cách tách biệt làn xử lý tính toán của GPU và tận dụng CPU để ghi dữ liệu song song qua cơ chế hàng đợi bộ nhớ đệm (Buffer), hệ thống đã đẩy hiệu suất hoạt động của GPU từ 82% lên mức tối đa 99.9%. Giải pháp này giúp tăng tốc độ xử lý video thêm 8.2% và tiết kiệm chi phí vận hành hạ tầng lên tới $900 cho mỗi 1.000 giờ render video mà hoàn toàn không cần can thiệp hay thay đổi cấu trúc của mô hình AI gốc.

### [Blog 2 - Tự động số hóa hồ sơ bệnh nhân bằng AI](3.2-Blog2/)
Blog này giới thiệu một kiến trúc pipeline tự động hóa quy trình chuyển đổi và số hóa các hồ sơ y tế từ dạng file PDF scan truyền thống sang dạng dữ liệu có cấu trúc. Hệ thống tận dụng sức mạnh trí tuệ nhân tạo của Amazon Bedrock Data Automation để trích xuất hơn 50 trường thông tin lâm sàng cốt lõi, sau đó dùng dịch vụ serverless AWS Lambda để ánh xạ tự động dữ liệu sang định dạng chuẩn y tế quốc tế FHIR R4 trước khi lưu trữ đồng bộ vào kho dữ liệu chuyên dụng AWS HealthLake nhằm tối ưu quy trình tra cứu và trao đổi thông tin.

### [Blog 3 - Cách AWS tối ưu hóa AI cho robot tự hành ngoài thực tế](3.3-Blog3/)
Nội dung bài viết phân tích cách công ty nông nghiệp công nghệ cao Aigen phối hợp cùng hệ sinh thái AWS SageMaker AI để triển khai thành công các mô hình máy học xuống các thiết bị phần cứng giới hạn (Edge AI) trên robot diệt cỏ chạy bằng năng lượng mặt trời. Bài viết đi sâu vào 3 giải pháp kiến trúc cốt lõi bao gồm: Tự động hóa gán nhãn dữ liệu hình ảnh bằng mô hình nền tảng (SAM2, Grounding DINO) kết hợp Active Learning; Chưng cất mô hình và ép kiểu nén (Quantization INT8) về định dạng TFLite siêu nhẹ chỉ 2MB; và thiết lập vòng lặp phản hồi khép kín (Closed-loop) để cập nhật mô hình liên tục qua Amazon S3.
