#!/usr/bin/python

import time
import socket
import struct
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('',4444))
mreq = struct.pack("=4sl", socket.inet_aton("224.51.105.104"), socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
count = 0
last_count = 0
cur_count = 0
total_dropped = 0
total_packets = 40000
while True:
  time1 = time.time()
  ret = sock.recv(65502)
  time2 = time.time()
  if ret == "END":
    print "Finished (" + str(total_packets-count) +")"
    sys.exit(0)
  cur_count = int(ret)
  if (cur_count - 1) != last_count:
    total_dropped += (cur_count-last_count+1)
#    print ("Dropped packets %d (%d)" % ((cur_count-last_count+1),total_dropped)),
#    print "%d: %d - %f" % (count,cur_count, 1000*(time2-time1))
  last_count = cur_count
  l = len(ret)
  if l > 5:
    finalout = ret[-5:]
  else:
    finalout = ret
  count += 1
  if count % 1000 == 0:
    sys.stdout.write(".")
    sys.stdout.flush()

