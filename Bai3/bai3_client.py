import socket 
from base64 import decode

# Thực hiện nhập dữ liệu
print("Nhập vào một chuỗi gồm 3 giá trị dạng [Đối số 1] [Phép toán muốn thực hiện: + - * /] [Đối số 2] phân biệt nhau bởi dấu khoảng trắng:")
strs = input()
print("Biểu thức bạn đã thực hiện nhập là: ", strs)

# Thực hiện xử lý chuỗi trước khi gửi lên Server
strs = str.encode(strs)


serverAddressPort = ("localhost", 8888)
bufferSize = 8192

# Thực hiện sử dụng UDP Socket tại Client
UDPClientSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)

# Thực hiện gửi dữ liệu lên Server
UDPClientSocket.sendto(strs, serverAddressPort)

# Lấy kết quả từ server về
messFromServer = UDPClientSocket.recvfrom(bufferSize)
mess = "Kết quả phép tính là: {}".format(messFromServer[0].decode())
print(mess)
