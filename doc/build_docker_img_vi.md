# HƯỚNG DẪN XÂY DỰNG VÀ ĐẨY DOCKER IMAGES LÊN DOCKER HUB

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

## Docker file
Dockerfile là một file dạng text không có phần đuôi mở rộng, chứa các đặc tả về một trường thực thi phần mềm, cấu trúc cho Docker Image. Từ những câu lệnh đó, Docker sẽ xây dựng một Docker image (thường có dung lượng nhỏ từ vài MB đến lớn vài GB).

[Dockerfile](/Dockerfile)

- FROM python:3.11: Dòng lệnh này xác định môi trường cho Docker image là python3.11.

- WORKDIR /app: Đặt đường dẫn hiện tại cho Docker container là /app. Đây là nơi các lệnh tiếp theo sẽ được thực thi và cũng là thư mục nơi các tập tin sẽ được sao chép vào.

- COPY requirement.txt ./: Sao chép nội dung tệp requirement.txt từ đường dẫn chính (Đường dẫn chứa  tệp Docker) đến thư mục /app trong container.

- RUN pip install --upgrade pip: Cập nhật phiên bản mới nhất của pip, trình cài đặt gói python. Điều này đảm bảo sẽ không xảy ra lỗi khi cài đặt các thư viện cần thiết.

- RUN pip install -r requirement.txt: Tải các thư viện python cần thiết được khai báo trong tệp requirement.txt bằng pip. Các thư viện này là cần thiết để chạy ứng dụng.

- COPY . .: Dòng lệnh này sao chép tất cả các tệp từ đường dẫn chính(Đường dẫn chứa tệp Dockerfile) đến thư mục /app trong container. Các tệp này là mã nguồn và các tệp thiết yếu để chạy ứng dụng.

- CMD ["python", "./src/word_recommend_api.py"]: Dòng lệnh xác định các dòng lệnh sẽ được chạy bằng command khi khởi chạy container. Tệp word_recommend_api.py tại đường dẫn /app/src sẽ được bằng trình thông dịch của python.






## Docker build

xây dựng Docker image từ Dockerfile và mã nguồn tại ```PATH``` hay ```URL```. Quá trình xây dựng tham chiếu đến tất cả các tệp tại đường dẫn được cung cấp.


```
docker build -t word_recommend .
```

- ```-t word_recommend```: Chỉ định tên và tag cho Docker image đang được tạo. Trong trường hợp này, Docker image sẽ có tên là word_recommend và sẽ có thẻ mặc định ```latest```. Tùy chọn ```-t``` là viết tắt của ```--tag```.



- ```.```: Đây là đường dẫn đến thư mục muốn tạo Docker image. Trong trường hợp này, "." đề cập đến thư mục hiện tại, nghĩa là Docker sẽ tìm Dockerfile trong đường dẫn hiện tại để sử dụng cho việc xây dựng image.
## Đẩy Docker image lên Docker hub

Nếu image chưa đúng với cấu trúc bên dưới, ta phải đổi tên để tiến hành đẩy lên Docker hub. 
```
docker tag imgname username/imgname:verionname

docker tag word_recommend khanhng29/word_recommend:latest
```

Đăng nhập vào Docker hub:
```
docker login
```

Bằng cách đẩy Docker image lên Docker Hub, ta có thể dễ dàng chia sẻ với người khác và truy cập từ mọi nơi.
```
docker push khanhng29/word_recommend:version1.0
```
Sau khi đẩy Docker image lên Docker hub, có thể sử dụng và chia sẻ với mọi người. Xem cách tải xuống và sử dụng Docker image ở [đây](link_to_docker.md).


