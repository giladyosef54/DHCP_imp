from flask import Flask, request
from dotenv import load_dotenv
from os import getenv

load_dotenv()


app = Flask(__name__)
subnet_mask = getenv('SUBNET_MASK')


@app.get('/get_ip')
def get_ip():
    pass


def main():
    app.run()


if __name__ == '__main__':
    main()
