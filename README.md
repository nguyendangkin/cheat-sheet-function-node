# Notem

Notem là một công cụ dòng lệnh tiên tiến được thiết kế để tối ưu hóa quy trình phát triển phần mềm bằng cách cung cấp truy cập nhanh chóng và hiệu quả đến một kho lưu trữ các đoạn mã mẫu. Được tích hợp chặt chẽ với Git, Notem cho phép lập trình viên truy xuất, quản lý và chia sẻ các đoạn mã trực tiếp từ terminal, loại bỏ nhu cầu chuyển đổi giữa trình duyệt web hoặc các tệp cục bộ để tìm kiếm code mẫu.

Chức năng chính của Notem bao gồm:

1. Truy xuất nhanh: Cho phép người dùng xem và sao chép các đoạn mã mẫu ngay lập tức, tiết kiệm thời gian tìm kiếm trên internet hoặc trong các tệp cục bộ.

2. Quản lý kho mã: Hỗ trợ liệt kê, thêm mới, và xóa các đoạn mã, giúp duy trì một kho lưu trữ có tổ chức và cập nhật.

3. Đồng bộ hóa Git: Tự động đồng bộ hóa kho mã với kho lưu trữ Git từ xa, đảm bảo tất cả các thành viên trong nhóm luôn có quyền truy cập vào phiên bản mới nhất của các đoạn mã.

4. Tương tác qua Terminal: Cung cấp giao diện dòng lệnh đơn giản nhưng mạnh mẽ, cho phép lập trình viên làm việc hiệu quả mà không cần rời khỏi môi trường phát triển của họ.

5. Tích hợp Clipboard: Cho phép sao chép nhanh chóng các đoạn mã vào clipboard, tạo điều kiện thuận lợi cho việc sử dụng lại mã trong các dự án.

Bằng cách cung cấp một cách tiếp cận có hệ thống để quản lý và truy cập các đoạn mã mẫu, Notem giúp tăng năng suất, cải thiện tính nhất quán của mã, và thúc đẩy việc chia sẻ kiến thức trong các nhóm phát triển phần mềm.

## Tính năng

-   Liệt kê tất cả các tệp .txt trong thư mục hiện tại
-   Xem và sao chép nội dung của một tệp cụ thể
-   Tạo tệp mới với mã từ clipboard
-   Xóa tệp và cập nhật kho lưu trữ
-   Đẩy các tệp đang chờ xử lý lên kho lưu trữ
-   Tự động kéo Git để giữ các tệp cục bộ được cập nhật

## Cài đặt

### Yêu cầu hệ thống

-   Hệ điều hành Windows
-   Quyền quản trị viên

### Quy trình cài đặt

0. Yêu cầu máy đã có python (nếu không, bạn vui lòng lên trang chủ python để tải và cài đặt).
1. Clone repo bằng git.
2. Tiến vào folder repo.
3. Nhấp chuột phải vào tệp `install.bat` và chọn "Chạy với quyền quản trị viên".
4. Tập lệnh cài đặt sẽ tự động:

    - Cài đặt thư viện `pyperclip` cần thiết
    - Tạo thư mục cài đặt trong user
    - Sao chép tất cả các tệp cần thiết vào thư mục cài đặt
    - Thêm thư mục cài đặt vào PATH hệ thống

5. Sau khi cài đặt hoàn tất, khởi động lại cửa sổ dòng lệnh để sử dụng các lệnh `notem`.

## Cách sử dụng

Notem cung cấp các lệnh sau:

1. Liệt kê tất cả các tệp .txt:

    ```
    notem ls
    ```

2. Xem nội dung của một tệp cụ thể (và sao chép vào clipboard):

    ```
    notem <số thứ tự>
    ```

    Thay `<số thứ tự>` bằng số của tệp như được hiển thị trong danh sách

3. Tạo tệp mới với mã từ clipboard:

    ```
    notem up <tên_tệp>
    ```

    Thay `<tên_tệp>` bằng tên bạn muốn đặt cho tệp mới. Lệnh này sẽ tạo ra file ở local, muốn đẩy toàn bộ chúng lên repo thì cần đến 'ups' sau khi dùng 'up'.

4. Xóa một tệp:

    ```
    notem rm <số thứ tự>
    ```

    Thay `<số thứ tự>` bằng số của tệp bạn muốn xóa

5. Đẩy tất cả các tệp đang chờ xử lý từ lệnh 'up' lên kho lưu trữ:
    ```
    notem ups
    ```

## Lưu ý

-   Đảm bảo bạn đang ở trong thư mục của kho Git khi sử dụng các lệnh Notem.
-   Notem sẽ tự động kéo các thay đổi từ kho lưu trữ từ xa khi bạn chạy lệnh `ls` để đảm bảo bạn luôn làm việc với phiên bản mới nhất.
-   Khi tạo hoặc xóa tệp, Notem sẽ tự động thêm, commit và đẩy các thay đổi lên kho lưu trữ từ xa.

## Đóng góp

Nếu bạn gặp bất kỳ vấn đề nào hoặc có đề xuất cải tiến, vui lòng tạo một issue hoặc pull request trên kho lưu trữ GitHub của dự án.

## Giấy phép

[Thêm thông tin về giấy phép của dự án ở đây]
