import socket as s
import cv2
import pickle #The pickle module implements binary protocols for serializing and de-serializing a Python object structure. “Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, and “unpickling” is the inverse operation,
# whereby a byte stream (from a binary file or bytes-like object) is converted back into an object hierarchy. Pickling (and unpickling) is alternatively known as “serialization”, “marshalling,” 1 or “flattening”; however,
# to avoid confusion, the terms used here are “pickling” and “unpickling”.
import struct as st #This module performs conversions between Python values and C structs represented as Python bytes objects. This can be used in handling binary data stored 
#in files or from network connections, among other sources. It uses Format Strings as compact descriptions of the layout of the C structs and the intended conversion to/from Python value"""

c_s = s.socket(s.AF_INET,s.SOCK_STREAM)# Creating a Socket Connection of Client side

host_ip = '192.168.29.108' #IP address of Host Computer  
port = 1234 #YOu can select any port but make sure that it is free not occupied by any other application

print("Socket Created Successfully and is Ready for transferring Data")


c_s.connect((host_ip,port))
data = b"" # b refers to the bytes and it is empty because when you run it fills with the video/Multiple Images
payload_size = st.calcsize("Q")
print("Socket Accepted")


while True:
    while len(data) < payload_size:
        packet = c_s.recv(2160) #In Networking Data is recieved in packets
        if not packet: break
        data+=packet
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = st.unpack("Q",packed_msg_size)[0] #Unpacking video from Client
    
    while len(data) < msg_size:
        data += c_s.recv(2160)
    frame_data = data[:msg_size]
    data  = data[msg_size:]
    frame = pickle.loads(frame_data) #Serializing the Images of Video
    cv2.imshow("Friend_2",frame)
    key = cv2.waitKey(1) & 0xFF
    if key  == ord('q'): #Meaning if you Pressed 'q' Key Window will exit
        break
c_s.close()#Closing the connection after pressed exit key