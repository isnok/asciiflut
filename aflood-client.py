#!/usr/bin/env python

import requests
import click

SERVER_HOST = 'http://127.0.0.1:5000/'
SERVER_DRAW_URL = SERVER_HOST + 'draw/{y}/{x}/{char}/'

def req(SERVER_URL):
    print("Hi! {}".format(SERVER_URL))
    rsp = requests.get(SERVER_URL)
    if rsp.status_code == 200:
        print(rsp.text)
    else:
        print(rsp.status_code)

@click.command()
def main():
    for y in range(2,8):
        for x in range(3,8):
            req(SERVER_DRAW_URL.format(y=y,x=x,char=42+y))


if __name__ == '__main__':
    main()
