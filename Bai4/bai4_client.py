from fileinput import filename
import socket
import time

IP = "localhost"
PORT = 8000
ADDR1 = (IP, PORT)
PORT2 = 8001
ADDR2 = (IP, PORT2)
FORMAT = "utf-8"
SIZE = 1024


def get_dir():
    receive_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    receive_server.connect(ADDR2)
    data = receive_server.recv(SIZE)
    print(data.decode())
    return

def get_file(cmd):
    receive_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    receive_server.connect(ADDR2)
    filename = cmd.split(' ')[1]
    new_filename = str(time.time()).split('.')[0] + '_' + filename
    file_open = open(new_filename, 'wb')
    while True:
        data = receive_server.recv(SIZE)
        if not data:
            file_open.close()
            break
        file_open.write(data)
        print(data.decode())
    file_open.close()
    return

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR1)
    data = client.recv(SIZE).decode(FORMAT)
    print(data)

    while True:
        cmd_input = input("> ")
        cmd = cmd_input.split(" ")[0]
        # Thực hiện câu lệnh GET
        if cmd == "GET":
            client.send(str(cmd_input).encode(FORMAT))
            while True:
                recev = client.recv(SIZE).decode(FORMAT)
                reply = recev.split("\n", 1)[0]
                print(reply)
                if reply == "OK":
                    get_file(cmd_input)
                    break
                else:
                    break
        
        # Thực hiện câu lệnh DELETE
        elif cmd == "DELETE":
            client.send(str(cmd_input).encode(FORMAT))
            recev = client.recv(SIZE).decode(FORMAT)
            reply = recev.split("\n", 1)[0]
            print(reply)

        # Thực hiện câu lệnh LIST
        elif cmd == "LIST":
            client.send(str(cmd_input).encode(FORMAT))
            recev = client.recv(SIZE).decode(FORMAT)
            reply = recev.split("\n", 1)[0]
            print(reply)
            while True:
                if reply == "OK":
                    get_dir()
                    break
                else:
                    break
        
        # Thực hiện câu lệnh LOGOUT 
        elif cmd == "LOGOUT":
            client.send(cmd.encode(FORMAT))
            break

    print("Đã ngắt kết nối từ Server!")
    client.close()

if __name__ == "__main__":
    main()
