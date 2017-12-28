#!/usr/bin/env python

import urllib
import requests
import click
from random import randint, choice
import string

SERVER_HOST = 'http://127.0.0.1:5000/'
SERVER_DRAW_URL = SERVER_HOST + 'draw/{y}/{x}/{char}/'

def req(url):
    print("Hi! {}".format(url))
    rsp = requests.get(url)
    print("{} - {}".format(rsp.status_code, rsp.text))

def draw_api(y, x, char, color=None):
    url = SERVER_DRAW_URL.format(y=y,x=x,char=char)
    if color is not None:
        req_args = {'color': color}
        url += '?' + urllib.parse.urlencode(req_args)
    req(url)


@click.group()
def main():
    pass


@main.command()
@click.option('-c', '--color', type=int, default=None)
@click.argument('y', type=int)
@click.argument('x', type=int)
@click.argument('what', type=str)
def draw(y, x, what, color):
    for c in what:
        draw_api(y, x, ord(c), color=color)
        x += 1

@main.command()
@click.argument('y', type=int)
@click.argument('x', type=int)
@click.argument('char', type=int)
def draw_char(y, x, char):
    draw_api(y, x, char)


TEXT_CHARS = string.ascii_letters + string.punctuation + string.digits
def gen_text():
    word = [choice(TEXT_CHARS) for i in range(randint(1,256))]
    return ''.join(word)


@main.command()
@click.option('-c', '--colorful', is_flag=True)
@click.argument('what', type=str, required=False)
def draw_random(what, colorful):
    if what is None:
        what = gen_text()

    y = randint(0, 55)
    x = max(0, randint(-10, max(80, 300-len(what))))
    color = randint(0,255)

    for c in what:
        draw_api(y, x, ord(c), color=color)
        x += 1
        if colorful:
            color = randint(0,255)

@main.command()
@click.argument('y1', type=int)
@click.argument('y2', type=int)
@click.argument('x1', type=int)
@click.argument('x2', type=int)
@click.argument('char', type=int)
def draw_rect(y1, y2, x1, x2, char):
    for y in range(y1,y2+1):
        for x in range(x1,x2+1):
            draw_api(y, x, char)


if __name__ == '__main__':
    main()
