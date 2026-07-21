---
title : "Dọn dẹp tài nguyên"
date : 2026-07-01
weight : 6
chapter : false
pre : " <b> 5.6. </b> "
---

#### Dọn dẹp tài nguyên

Xin chúc mừng bạn đã hoàn thành xong bài thực hành này!
Trong bài thực hành này, bạn đã tìm hiểu và cấu hình thành công các mô hình kiến trúc nâng cao để truy cập dịch vụ Amazon S3 mà không sử dụng Public Internet.

* **Bằng cách tạo Gateway Endpoint:** Bạn đã cho phép thiết lập giao tiếp bảo mật và trực tiếp giữa các tài nguyên EC2 nằm trong mạng nội bộ với Amazon S3 mà không cần đi qua Internet Gateway hay NAT Gateway.
* **Bằng cách tạo Interface Endpoint (AWS PrivateLink):** Bạn đã mở rộng khả năng kết nối an toàn đến S3 cho các tài nguyên đang chạy tại trung tâm dữ liệu cục bộ (On-premises) thông qua kết nối AWS Site-to-Site VPN hoặc AWS Direct Connect mà vẫn đảm bảo lưu lượng dữ liệu đi hoàn toàn trong mạng riêng của AWS.

---

#### Quy trình dọn dẹp chi tiết

Để tránh phát sinh chi phí ngoài ý muốn sau khi hoàn thành bài thực hành, hãy tiến hành dọn dẹp các tài nguyên theo các bước tuần tự dưới đây:

**1. Xóa Route 53 Private Hosted Zone**
* Điều hướng đến mục **Hosted Zones** ở danh sách menu phía bên trái của bảng điều khiển dịch vụ **Amazon Route 53**.
* Nhấp chọn vào tên của Hosted Zone `s3.us-east-1.amazonaws.com` (hoặc khu vực tương ứng bạn đã tạo).
* Nhấp vào nút **Delete** ở góc trên cùng bên phải và xác nhận việc xóa bằng cách nhập từ khóa `delete` vào ô trống.

![hosted zone](/images/5-Workshop/5.6-Cleanup/delete-zone.png)

**2. Gỡ bỏ liên kết và Xóa Route 53 Resolver Rule**
* Di chuyển đến mục **Resolver Rules** trong bảng điều khiển Route 53.
* Chọn Rule có tên **`myS3Rule`**.
* Thực hiện **Disassociate** (Gỡ bỏ liên kết) quy tắc này ra khỏi **"VPC Onprem"**.
* Sau khi gỡ liên kết thành công, chọn Rule đó và nhấn **Delete** để xóa hoàn toàn.

![hosted zone](/images/5-Workshop/5.6-Cleanup/vpc.png)

**3. Xóa các Stack trên AWS CloudFormation**
* Mở giao diện điều khiển của dịch vụ **AWS CloudFormation**.
* Chọn và tiến hành xóa hai stack CloudFormation mà bạn đã triển khai cho bài thực hành này bằng cách nhấn nút **Delete**:
  * **`PLOnpremSetup`**
  * **`PLCloudSetup`**

![delete stack](/images/5-Workshop/5.6-Cleanup/delete-stack.png)

**4. Dọn dẹp và xóa các Amazon S3 Bucket**
* Mở bảng điều khiển dịch vụ **Amazon S3**.
* Tìm và chọn đúng S3 Bucket mà bạn đã khởi tạo phục vụ cho bài lab này.
* Nhấp chọn nút **Empty** (Làm trống) trước để xóa toàn bộ các đối tượng (objects) đang lưu trữ bên trong và xác nhận.
* Sau khi bucket đã trống, nhấp chọn nút **Delete** và nhập lại chính xác tên của bucket để hoàn tất việc xóa bỏ hoàn toàn tài nguyên lưu trữ.

![delete s3](/images/5-Workshop/5.6-Cleanup/delete-s3.png)
