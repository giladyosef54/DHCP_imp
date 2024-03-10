from flask import Flask, request
from ipaddress import ip_address
from collections import deque
import config


app = Flask(__name__)

subnet_mask = int(ip_address(config.subnet_mask))
subnet_ip = int(ip_address(config.ip))

subnet_broadcast_ip = (int(ip_address('255.255.255.255')) ^ subnet_mask) + subnet_ip
unused_ip = subnet_ip


def gen_ip():
    global unused_ip
    if unused_ip + 1 >= subnet_broadcast_ip:
        return None
    else:
        unused_ip += 1
        return unused_ip



@app.get('/getIP')
def get_ip():
    ip = gen_ip()
    if ip is None:
        return 'There is no available IPs', 400
    else:
        return str(ip_address(ip)), 200


def main():
    app.run()


if __name__ == '__main__':
    main()
