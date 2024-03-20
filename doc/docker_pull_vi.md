# HƯỚNG DẪN TẢI XUỐNG VÀ CHẠY ỨNG DỤNG TỪ DOCKER HUB

## Cài đặt Docker
Chọn đường dẫn phù hợp với hệ điều hành của bạn, làm theo hướng dẫn để tải xuống Docker:
- [Docker Desktop cho Linux](https://docs.docker.com/desktop/install/linux-install/)
- [Docker Desktop cho Mac (macOS)](https://docs.docker.com/desktop/install/mac-install/)
- [Docker Desktop cho Windows](https://docs.docker.com/desktop/install/windows-install/)

Sau khi tải xuống, kiểm tra phiên bản docker hiện tại bằng cách sử dụng, command line (windows): windows + "cmd" + Enter. Sau đó nhập:

```
docker -v

C:\Users\Admin>docker -v
Docker version 24.0.6, build ed223bc
```
Phiên bản hiển thị là phiên bản Docker mà bạn đã cài đặt thành công.

## Tải Docker image từ Docker hub
Để tải xuống Docker image từ Docker Hub, sử dụng lệnh ```docker pull```. Lệnh này sẽ tải image được chỉ định từ Docker Hub. Khi đã tải xuống, sử dụng ```docker run``` để chạy ứng dụng.

```
docker pull khanhng29/word_recommend:version1.0
```
Kiểm tra tất cả Docker image hiện tại:
```
docker images

C:\Users\Admin>docker images
REPOSITORY                 TAG          IMAGE ID       CREATED        SIZE
khanhng29/word_recommend   version1.0   e40c51257e11   12 hours ago   3.76GB
```
Sử dụng câu lệnh dưới để chạy ứng dụng:
```
docker run -dp 5555:5555 khanhng29/word_recommend:version1.0
```
Cổng 5555 đầu tiên xác định cổng chạy ở máy của bạn. Cổng 5555 thứ hai là cổng chạy trong Docker container.

Để sử dụng ứng dụng trên giao diện, tải xuống tệp [index.html](https://github.com/khanhng29/word_recommend/blob/master/index.html).

Kiểm tra địa chỉ IP hiện tại bằng câu lệnh:
```
ipconfig
```
Sửa địa chỉ IP tại ```dòng 31``` trong tệp HTML vừa tải xuống bằng địa chỉ IP của bạn, chạy tệp HTML bằng trình duyệt web để sử dụng.

