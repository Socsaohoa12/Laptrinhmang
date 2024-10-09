import socket

def main():
    # Tạo socket cho máy khách
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Kết nối đến máy chủ với địa chỉ IP và cổng
    client_socket.connect(('127.0.0.1', 65432))

    # Nhập hai số từ người dùng
    num1 = input("Nhập số thứ nhất: ")
    num2 = input("Nhập số thứ hai: ")

    # Gửi hai số lên máy chủ
    client_socket.send(f"{num1} {num2}".encode())

    # Nhận kết quả từ máy chủ
    result = client_socket.recv(1024).decode()

    # Hiển thị kết quả
    print(f"Tổng của {num1} và {num2} là: {result}")

    # Đóng kết nối
    client_socket.close()

if __name__ == '__main__':
    main()
