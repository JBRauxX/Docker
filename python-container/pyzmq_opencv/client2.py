# run this program on each RPi to send a labelled image stream
import socket
import time
from imutils.video import VideoStream
import imagezmq
import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-s", "--server-ip", required=True,
	help="ip address of the server to which the client will connect")
args = vars(ap.parse_args())

# initialize the ImageSender object with the socket address of the
# server
sender = imagezmq.ImageSender(connect_to='tcp://{}:5555').format(args["server_ip"]) #server host:port

# get the host name, initialize the video stream, and allow the
# camera sensor to warmup
rpi_name = socket.gethostname() # send RPi hostname with each image
picam = VideoStream(usePiCamera=True).start()
time.sleep(2.0)  

# send images as stream until Ctrl-C
while True:
    #read the frame from the camera and send it to the server
    frame = vs.read()
    #image = picam.read() #default format imagezmq
    sender.send_image(rpiName, frame)
    #sender.send_image(rpi_name, image) #default format imagezmq

