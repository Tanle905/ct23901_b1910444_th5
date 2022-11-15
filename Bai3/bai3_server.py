from base64 import decode
import socket

localIP = "localhost"
localPort = 8888
bufferSize = 8192

def calculate(str, num1, num2):
    if str == "+":
        kq = num1 + num2
    elif str == "-":
        kq = num1 - num2
    elif str == "*":
        kq = num1 * num2
    elif str == "/":
        kq = num1 / num2
    else:
        kq = "Phép toán không hợp lệ"
    return kq;

# Thực hiện sử dụng UDP Socket tại Server
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket.bind((localIP, localPort))

print("UDP Server đã được bật")

while True:
    # Thực hiện lấy dữ liệu từ phía Client
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    strs = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientStrings = "Chuỗi được gửi từ phía Client: {}".format(strs.decode())
    print(clientStrings)

    # Thực hiện xử lý dữ liệu
    arr = strs.decode().split()
    operant1 = int(arr[0])
    op = arr[1]
    operant2 = int(arr[2])

    result = str(calculate(op, operant1, operant2))
    print("Kết quả phép toán: " + result)
    sendresult = str.encode(result)

    # Thực hiện gửi dữ liệu cho Client
    UDPServerSocket.sendto(sendresult, address)
   
    