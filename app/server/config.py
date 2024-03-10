from ipaddress import ip_address
from dotenv import load_dotenv
from os import getenv
load_dotenv()


subnet_mask = int(ip_address(getenv('SUBNET_MASK')))
ip = int(ip_address(getenv('IP')))