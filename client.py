import time
import socket
data = ""
count = 0
done = False
#for i in range(1,65502):
while not done:
  if len(data) < 1000:
    data = data +"0"
#  if i < 9000:
#    continue
#  time.sleep(1)
  count += 1

  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
  sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
  sock.sendto(str(count), ("224.51.105.104", 4444))
  print "Sent: %d" % count
  if count == 40000:
      done=True

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
sock.sendto("END", ("224.51.105.104", 4444))

