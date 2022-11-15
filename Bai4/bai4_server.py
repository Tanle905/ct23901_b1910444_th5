import os
import socket
import threading

IP = "localhost"
PORT = 8000
ADDR1 = (IP, PORT)
PORT2 = 8001
ADDR2 = (IP, PORT2)
FORMAT = "utf-8"
SIZE = 1024

def get_dir(path):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(ADDR2)

    s.listen(5)
    print("Server: 8001 đang lắng nghe...")
    di, new_address = s.accept()
    print('Kết nối từ ', str(new_address))
    send_data = ""
    files = os.listdir(path)
    if len(files) == 0:
        send_data += "Thư mục máy chủ trống"
    else:
        send_data += "\n".join(f for f in files)
    di.send(str.encode(send_data))
    return

def get_file(path):
    # Sử dụng cổng 8001 để gửi dữ liệu tập tin/thư mục tới Client
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(ADDR2)

    s.listen(5)
    print("Server: 8001 đang lắng nghe...")
    di, new_address = s.accept()     # Establish connection with client.
    print('Kết nối từ ', str(new_address))
    file = open(path, 'rb')
    data = ""
    iter = 1
    data = file.read(SIZE).decode()
    while (data):
        di.send(str.encode(data))
        print('Sent ', iter)
        iter += 1
        data = file.read(SIZE).decode()
        if not data:
            print("Đã gửi tệp, đang thực hiện đóng nối kết...")
            file.close()
            di.close()
            print("Đã đóng nối kết!")
    return

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    conn.send("Xin chào!".encode(FORMAT))

    # Server thực hiện nhận các câu lệnh từ Client
    while True:
        data = conn.recv(SIZE).decode(FORMAT)
        data = data.split(" ")
        cmd = data[0]

        if cmd == "GET":
            if os.path.exists(data[1]):
                send_data = "OK\n"
                conn.send(send_data.encode(FORMAT))
                get_file(data[1])
            else:
                send_data = "ERROR\n"
                conn.send(send_data.encode(FORMAT))

        elif cmd == "DELETE":
            if os.path.exists(data[1]):
                send_data = "OK\n"
                conn.send(send_data.encode(FORMAT))
                os.remove(data[1])
            else:
                send_data = "ERROR\n"
                conn.send(send_data.encode(FORMAT))

        elif cmd == "LIST":
            if os.path.isdir(data[1]):
                send_data = "OK\n"
                conn.send(send_data.encode(FORMAT))
                get_dir(data[1])
            else:
                send_data = "ERROR\n"
                conn.send(send_data.encode(FORMAT))

        elif cmd == "LOGOUT":
            break

    print(f"[DISCONNECTED] {addr} disconnected")
    conn.close()


def main():
    print("Server đang khởi động...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR1)
    server.listen()
    print(f"Server đang lắng nghe từ {IP}:{PORT}.")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


if __name__ == "__main__":
    main()
