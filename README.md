# Notem

Notem là một công cụ dòng lệnh để quản lý và chia sẻ các đoạn mã một cách dễ dảng trong một kho Git. Nó cho phép người dùng liệt kê, xem, tạo, xóa và đẩy các đoạn mã được lưu trữ dưới dạng tệp văn bản.

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

1. Tải xuống tập tin `install.bat` và `notem.py`.
2. Đặt cả hai tập tin vào cùng một thư mục.
3. Nhấp chuột phải vào tệp `install.bat` và chọn "Chạy với quyền quản trị viên".
4. Tập lệnh cài đặt sẽ tự động:

    - Cài đặt Python nếu chưa được cài đặt
    - Cài đặt thư viện `pyperclip` cần thiết
    - Tạo thư mục cài đặt trong Program Files
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
