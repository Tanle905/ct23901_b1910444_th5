import socket
import sys

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Thực hiện kết nối socket với server lắng nghe cổng 8888
server_address = ('localhost', 8888)
mysock.connect(server_address)

try:
    # Thực hiện nhập 1 ký tự và gửi dữ liệu qua server
    print("Nhập vào một ký tự số từ 0 đến 9")
    number = input()
    print("Ký tự số vừa nhập là: ", number)
    mysock.sendall(number.encode())

    # Nhận kết quả trả về từ Server và thể hiện lên màn hình
    n_received = 0
    n_expected = len(number)
    arr_n = []

    while n_received < n_expected:
        data = mysock.recv(100)
        n_received += len(data)
        arr_n.append(data)
        print('Kết quả là: ', b''.join(arr_n).decode())
finally:
    print('Nhận phản hồi từ Server thành công, kết thúc Socket!')
    mysock.close();


    