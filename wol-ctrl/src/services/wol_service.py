import socket
import binascii

def wol(dev):

    try:
        b_mac = bytes.fromhex(dev.mac.replace(':', ''))
        magic = b"\xff" * 6 + b_mac * 16
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.sendto(magic, ("<broadcast>", 7))
    except Exception as e:
        return "Failure, message not sent: "+ str(e)
    return magic.hex()
