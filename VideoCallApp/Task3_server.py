
'''Task Completed by Yatin Kumar Singh'''


import socket as s
import cv2 #For Image Processing
import pickle #The pickle module implements binary protocols for serializing and de-serializing a Python object structure. “Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, and “unpickling” is the inverse operation,
# whereby a byte stream (from a binary file or bytes-like object) is converted back into an object hierarchy. Pickling (and unpickling) is alternatively known as “serialization”, “marshalling,” 1 or “flattening”; however,
# to avoid confusion, the terms used here are “pickling” and “unpickling”.
import struct as st #This module performs conversions between Python values and C structs represented as Python bytes objects. This can be used in handling binary data stored 
#in files or from network connections, among other sources. It uses Format Strings as compact descriptions of the layout of the C structs and the intended conversion to/from Python value"""



s_s = s.socket(s.AF_INET,s.SOCK_STREAM) #Obtaining the socket Kind And which family it belongs to

host_name  = s.gethostname() #obtaining host name using 
host_ip = s.gethostbyname(host_name) #obtaining Host IP address
print('IP Of the Host:',host_ip)

port = 1234 #enter your Port number here
s_address = ('192.168.29.108',port)
print("Socket Created Successfully")
s_s.bind(s_address)
print("Socket Bind Successfully")
s_s.listen(5) #for listening to Client Observations and actions/request

while True:
    client_s,addr = s_s.accept()
    print('GOT CONNECTION FROM:',addr)
    if client_s:
        vid = cv2.VideoCapture(0)#Using Opencv to capture video
        
        while(vid.isOpened()):
            img,frame = vid.read() #Reading Image from Webcam video
            a = pickle.dumps(frame)
            message = st.pack("Q",len(a))+a
            client_s.sendall(message)
            
		
            cv2.imshow('Friend_1',frame)
            key = cv2.waitKey(1) & 0xFF
            if key ==ord('q'):
                client_s.close()