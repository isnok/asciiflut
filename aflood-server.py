#!/usr/bin/env python

import click
import curses
from flask import Flask, request, render_template, abort

from server_config import MyConfig as ServerConfig

app_name = ServerConfig.server_name if hasattr(ServerConfig, 'server_name') else __name__
app = Flask(app_name)
app.config.from_object(ServerConfig)

stdscr = None

@app.route('/')
def index_page():
    ctx = {
        'config': ServerConfig
    }
    return render_template('index.html.j2', **ctx)


@app.route('/draw/<int:y>/<int:x>/<int:char>/')
def draw_char(y, x, char):

    if char not in ServerConfig.char_whitelist:
        abort(403)

    stdscr.addch(y, x, char)
    stdscr.refresh()
    return "Yes"


@app.route('/test/')
def do_foo():
    try:
        for i in range(0, 255):
            stdscr.addstr(str(i), curses.color_pair(i))
    except curses.ERR:
        # End of screen reached
        pass
    stdscr.refresh()
    return "Done"


@app.before_first_request
def disable_console_logging():

    import logging
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)


@app.before_first_request
def init_screen():

    global stdscr
    if stdscr is None:
        stdscr = curses.initscr()

    curses.start_color()
    curses.use_default_colors()
    # stdscr.refresh()


@click.command()
def main():
    app.run()
    curses.endwin()

if __name__ == '__main__':
    main()
