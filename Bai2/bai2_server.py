import socket
import sys

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Thực hiện kết nối socket với server lắng nghe cổng 8888
server_address = ('localhost', 8888)    
print("Khởi động trên cổng là: ", server_address)
mysock.bind(server_address)

# Thực hiện lắng nghe kết nối
mysock.listen(1)


# Thực hiện biến đổi ký tự số thành chuỗi
def number_to_string(number):
    if number == 1:
        kq = "mot"
    elif number == 2:
        kq = "hai"
    elif number == 3:
        kq = "ba"
    elif number == 4:
        kq = "bon"
    elif number == 5:
        kq = "nam"
    elif number == 6:
        kq = "sau"
    elif number == 7:
        kq = "bay"
    elif number == 8:
        kq = "tam"
    elif number == 9:
        kq = "chin"
    else:
        kq = "Không phải số nguyên"
    return kq;

while True:
    # Đang đợi kết nối
    print('Đang thực hiện đợi kết nối...')
    connection, client_address = mysock.accept()
    try:
        print('Kết nối được thực hiện từ phía Client: ', client_address)
        while True:
            data = connection.recv(50)
            print('Ký tự số nhận được từ phía Client: ' + data.decode())
            if data:
                #  Thực hiện ép kiểu dữ liệu nhập từ string sang int để so sánh và gửi kết quả về Client
                print('Thực hiện chuyển đổi số nhận được từ Client và gửi lại kết quả cho Client')
                data = int(data)
                result = number_to_string(data)
                connection.sendall(result.encode(), )
                break
            else:
                print('Không nhận được dữ liệu từ phía Client', client_address)
                break
    finally:
        print('Kết nối đã đóng lại!')
        connection.close()
        