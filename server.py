import socket as soc
import cv2,pickle,struct

server_soc = soc.socket(soc.AF_INET,soc.SOCK_STREAM)
host_name = soc.gethostname()
host_ip = soc.gethostbyname(host_name)
print("HOST IP: ",host_ip)

port = 9090
soc_address = ('0.0.0.0',port)
print("Created successfully !!")

server_soc.bind(soc_address)
print("Bind Successfully !!")

server_soc.listen(5)
print("LISTENING AT: ",soc_address)

print("SOCKET ACCEPT")

while True:
    client_soc,addr = server_soc.accept()
    print("Got the connection from :" , addr)
    if client_soc:
        vid=cv2.VideoCapture(0)

        while(vid.isOpened()):
            img,frame = vid.read()
            a = pickle.dumps(frame)
            message = struct.pack("Q",len(a))+a
            client_soc.sendall(message)

            cv2.imshow("VIDEO ",frame)
            key=cv2.waitKey(1) & 0xFF
            if key ==ord('q'):
                client_soc.close()

print("COMPLETED !! ")                