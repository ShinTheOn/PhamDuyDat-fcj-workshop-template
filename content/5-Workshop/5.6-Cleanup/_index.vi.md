---
title : "Dọn dẹp tài nguyên"
date : 2026-07-01
weight : 6
chapter : false
pre : " <b> 5.6. </b> "
---

#### Dọn dẹp tài nguyên

Quy trình xóa bỏ các tài nguyên hạ tầng đã khởi tạo để tránh phát sinh chi phí duy trì sau khi kết thúc bài thực hành:

1. Điều hướng đến **Hosted Zones** ở danh sách menu phía bên trái của bảng điều khiển **Route 53**. Nhấp chọn vào tên của Hosted Zone `s3.us-east-1.amazonaws.com`. Nhấp vào **Delete** và xác nhận việc xóa bằng cách nhập từ khóa `delete`.

![hosted zone](/images/5-Workshop/5.6-Cleanup/delete-zone.png)

2. Di chuyển đến mục **Resolver Rules** trong bảng điều khiển Route 53. Thực hiện gỡ bỏ liên kết (**Disassociate**) quy tắc `myS3Rule` ra khỏi **"VPC Onprem"** và tiến hành xóa bỏ hoàn toàn.

![hosted zone](/images/5-Workshop/5.6-Cleanup/vpc.png)

3. Mở bảng điều khiển của dịch vụ **AWS CloudFormation** và thực hiện xóa hai stack đã triển khai cho bài thực hành này:
   * **`PLOnpremSetup`**
   * **`PLCloudSetup`**

![delete stack](/images/5-Workshop/5.6-Cleanup/delete-stack.png)

4. Xóa các Amazon S3 bucket:
   * Mở bảng điều khiển dịch vụ **Amazon S3**.
   * Chọn đúng S3 bucket đã tạo cho bài lab, nhấp chọn **Empty** và xác nhận để làm trống toàn bộ các đối tượng bên trong.
   * Nhấp chọn **Delete** và nhập lại chính xác tên bucket để hoàn tất việc xóa bỏ tài nguyên.

![delete s3](/images/5-Workshop/5.6-Cleanup/delete-s3.png)
