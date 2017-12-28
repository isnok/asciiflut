#!/usr/bin/env python

import requests
import click

SERVER_HOST = 'http://127.0.0.1:5000/'
SERVER_DRAW_URL = SERVER_HOST + 'draw/{y}/{x}/{char}/'

def req(url):
    print("Hi! {}".format(url))
    rsp = requests.get(url)
    if rsp.status_code == 200:
        print(rsp.text)
    else:
        print(rsp.status_code)

@click.group()
def main():
    pass

@main.command()
@click.argument('y', type=int)
@click.argument('x', type=int)
@click.argument('char', type=int)
def draw(y, x, char):
    req(SERVER_DRAW_URL.format(y=y,x=x,char=char))

@main.command()
def devblock():
    for y in range(2,8):
        for x in range(3,8):
            req(SERVER_DRAW_URL.format(y=y,x=x,char=42+y))


if __name__ == '__main__':
    main()
