import socket
import requests
from bs4 import BeautifulSoup

def get_stock_price(stock_code):
    url = "https://iboard.ssi.com.vn/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Tìm kiếm thông tin giá cổ phiếu (cần điều chỉnh class phù hợp)
        stock_info = soup.find('div', {'class': 'stock-info'})  # Thay đổi class cho phù hợp
        if stock_info:
            price = stock_info.find('span', {'class': 'current-price'})  # Thay đổi class cho phù hợp
            if price:
                return price.text.strip()
            else:
                return "Không tìm thấy giá cổ phiếu."
        else:
            return "Không tìm thấy thông tin cho mã chứng khoán này."
    else:
        return "Không thể kết nối đến trang web."

def start_server():
    host = '127.0.0.1'
    port = 65432
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"SERVER đang lắng nghe tại {host}:{port}")
        conn, addr = server_socket.accept()
        with conn:
            print(f"Kết nối từ {addr}")
            data = conn.recv(1024).decode()  # Nhận mã chứng khoán từ client
            if data:
                stock_price = get_stock_price(data.upper())
                conn.sendall(stock_price.encode())

if __name__ == "__main__":
    start_server()
