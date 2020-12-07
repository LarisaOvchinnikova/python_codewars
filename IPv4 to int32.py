https://www.codewars.com/kata/52ea928a1ef5cfec800003ee
def ip_to_int32(ip):
    ip = ip.split('.')
    ip1 = bin(int(ip[0]))[2:].zfill(8)
    ip2 = bin(int(ip[1]))[2:].zfill(8)
    ip3 = bin(int(ip[2]))[2:].zfill(8)
    ip4 = bin(int(ip[3]))[2:].zfill(8)
    s = ip1+ip2+ip3+ip4
    return int(s,2)