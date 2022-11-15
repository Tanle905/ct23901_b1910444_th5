from socket import *

mysocket = socket(AF_INET, SOCK_STREAM);
mysocket.connect(('www.cit.ctu.edu.vn', 80));
mysocket.send(b'GET/HTTP/1.0\n\n');

data = mysocket.recv(10000);
print(data.decode());

mysocket.close ();