from flask import Flask, request
from dotenv import load_dotenv
from os import getenv
from ipaddress import ip_address
from collections import deque

load_dotenv()



app = Flask(__name__)

subnet_mask = int(ip_address(getenv('SUBNET_MASK')))

broadcast = int(ip_address('255.255.255.255'))
unused_ip = subnet_mask & broadcast


def gen_ip():
    global unused_ip
    if unused_ip + 1 + subnet_mask == broadcast:
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
