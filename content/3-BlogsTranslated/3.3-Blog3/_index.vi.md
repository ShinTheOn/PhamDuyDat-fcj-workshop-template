---
title : "Cách AWS tối ưu hóa AI cho robot tự hành ngoài thực tế"
date : 2026-07-08
weight : 3
chapter : false
pre : " <b> 3.3. </b> "
---

### [Góc chia sẻ] - Cách AWS tối ưu hóa AI cho robot tự hành ngoài thực tế

Chào mọi người, mình vừa đọc được một case study rất hay từ AWS và muốn tóm tắt lại vài ý chính để chia sẻ với mọi người.

Bài blog phân tích cách Aigen – một công ty làm robot nông nghiệp tự động (chạy bằng năng lượng mặt trời để diệt cỏ dại) – đã giải quyết bài toán đưa AI xuống chạy ở môi trường thực tế.

Vấn đề của Aigen chắc cũng là vấn đề chung của nhiều hệ thống Edge AI:
- **Kết nối kém:** Robot chạy ngoài đồng, Internet chập chờn, khó gửi data liên tục về server.
- **Dữ liệu khổng lồ:** Hàng ngàn bức ảnh cần xử lý mỗi ngày, nếu thuê người gán nhãn (label) thủ công thì chi phí cực đắt và quá chậm.
- **Phần cứng giới hạn:** Không thể bê nguyên một mô hình AI khổng lồ nhét vào bộ xử lý nhỏ gọn trên robot.

Vài đây là cách họ giải quyết triệt để vấn đề này với hệ sinh thái AWS SageMaker:

#### 1. Dùng GenAI để "Tự động hóa" gán nhãn (Auto-labeling)
Thay vì dùng sức người 100%, họ kết hợp các mô hình nền tảng về thị giác (như SAM2, Grounding DINO) để tự động vẽ bounding box và phân vùng ảnh.

Cái hay là họ áp dụng **Active Learning** – hệ thống tự động lọc ra những tấm ảnh khó xử lý nhất (ví dụ góc sáng lạ, cây bị che khuất) để con người kiểm tra lại.

Kết quả: Thời gian xử lý giảm từ gần 15 phút xuống còn vỏn vẹn 41 giây/ảnh. Chi phí dán nhãn giảm tới 22.5 lần.

#### 2. "Chưng cất" AI (Model Distillation & Quantization)
Để giải bài toán phần cứng yếu trên thiết bị Edge, họ chia quy trình huấn luyện AI thành 4 cấp độ từ lớn đến nhỏ:
- **Foundation Models (Lớp 1):** Chạy trên cloud, siêu lớn, tổng quát.
- **Expert & Student Models (Lớp 2, 3):** Bắt đầu "chưng cất" nhỏ lại cho từng tác vụ cụ thể (nhận diện lá, thân cây...).
- **Edge Models (Lớp 4):** Mô hình cuối cùng được ép kiểu (Quantization) về chuẩn INT8 và chuyển sang định dạng TFLite.

Đến bước này, khối lượng model chỉ còn khoảng **2MB**, tiêu thụ vỏn vẹn **1.5W** điện nhưng vẫn chạy mượt mà theo thời gian thực trên bo mạch của robot.

<img width="865" height="487" alt="image" src="https://github.com/user-attachments/assets/5f52e3d7-5745-4f8e-bef9-fa450ba7df1a" />


*Ảnh 1: Mô hình đi qua 4 cấp độ: từ Foundation (siêu lớn, chạy trên Cloud) -> Expert -> Student -> Edge (chỉ còn 2MB, tiêu thụ 1.5W chạy trên bo mạch robot).*

#### 3. Vòng lặp cập nhật liên tục
Robot thu thập data &rarr; Đẩy lên AWS S3 khi có mạng &rarr; Tự động gán nhãn &rarr; Train lại mô hình trên cụm GPU mạnh của cloud &rarr; Đẩy bản cập nhật siêu nhẹ (Edge model) ngược lại xuống robot để thích nghi với điều kiện môi trường mới.

<img width="863" height="486" alt="image" src="https://github.com/user-attachments/assets/ce3b016d-81ea-4925-9c63-a28927b2bfcb" />


*Ảnh 2: Vòng lặp khép kín (Closed-loop) của AWS SageMaker. Dữ liệu thô từ robot tải lên S3 -> được tự động gán nhãn -> Train lại mô hình trên Cloud -> đẩy bản cập nhật siêu nhẹ về lại cánh đồng để robot thích nghi ngay với môi trường mới.*

#### Tóm lại:
Đưa AI ra khỏi phòng lab để chạy mượt trên thực tế đòi hỏi sự kết hợp rất khéo léo giữa năng lực tính toán cực mạnh của Cloud và kỹ thuật nén mô hình tối đa ở thiết bị Edge.

> Bài gốc trên blog AWS: https://aws.amazon.com/blogs/architecture/how-aigen-transformed-agricultural-robotics-for-sustainable-farming-with-amazon-sagemaker-ai/
