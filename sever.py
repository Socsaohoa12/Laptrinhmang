import socket

def main():
    # Tạo socket cho máy chủ
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Gán địa chỉ IP và cổng cho máy chủ
    server_socket.bind(('0.0.0.0', 65432))

    # Máy chủ lắng nghe kết nối từ máy khách
    server_socket.listen(1)
    print("Máy chủ đang chờ kết nối...")

    # Chấp nhận kết nối từ máy khách
    client_socket, addr = server_socket.accept()
    print(f"Kết nối từ {addr}")

    while True:
        # Nhận dữ liệu từ máy khách
        data = client_socket.recv(1024).decode()
        if not data:
            break
        
        # Tách hai số từ dữ liệu nhận được
        num1, num2 = map(int, data.split())
        
        # Tính tổng hai số
        result = num1 + num2
        
        # Gửi kết quả về cho máy khách
        client_socket.send(str(result).encode())

    # Đóng kết nối
    client_socket.close()
    server_socket.close()

if __name__ == '__main__':
    main()
