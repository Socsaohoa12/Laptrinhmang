import socket

def get_stock_price(stock_code):
    host = '127.0.0.1'  # Địa chỉ IP của server
    port = 65432        # Cổng của server

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.sendall(stock_code.encode())  # Gửi mã chứng khoán
        response = client_socket.recv(1024).decode()  # Nhận phản hồi từ server
        return response

if __name__ == "__main__":
    stock_code = input("Nhập mã chứng khoán: ").strip()  # Nhận mã chứng khoán từ người dùng
    price = get_stock_price(stock_code)  # Lấy giá cổ phiếu
    print(f"Giá cổ phiếu của {stock_code} là: {price}")

