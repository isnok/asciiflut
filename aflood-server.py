#!/usr/bin/env python

import click
import curses
from flask import Flask, request, render_template, abort
from flask_restful import Resource, Api, reqparse

from server_config import MyConfig as ServerConfig

app_name = ServerConfig.server_name if hasattr(ServerConfig, 'server_name') else __name__
app = Flask(app_name)
app.config.from_object(ServerConfig)

api = Api(app)

stdscr = None

@app.route('/')
def index_page():
    ctx = {
        'config': ServerConfig
    }
    return render_template('index.html.j2', **ctx)

class DrawResource(Resource):

    def get(self, y, x, char):

        if char not in ServerConfig.char_whitelist:
            return {
                'status': 'illegal char',
                'value': char,
            }, 403

        parser = reqparse.RequestParser()
        parser.add_argument('color', type=int, help='color code', required=False)
        req_args = parser.parse_args()
        color = req_args.get('color')

        try:
            stdscr.addch(y, x, char, curses.color_pair(color))
        except curses.error as ex:
            return {
                'status': 'curses error',
                'value': ex.args,
            }, 500
        finally:
            stdscr.refresh()
        return {
            'status': 'ok',
            'value': req_args,
        }

api.add_resource(DrawResource, '/draw/<int:y>/<int:x>/<int:char>/')

# @app.route('/draw/<int:y>/<int:x>/<int:char>/')
# def draw_char(y, x, char):

    # if char not in ServerConfig.char_whitelist:
        # abort(403)

    # stdscr.addch(y, x, char)
    # stdscr.refresh()
    # return "Yes"


@app.route('/test/')
def do_foo():
    try:
        for i in range(0, 255):
            stdscr.addstr(str(i), curses.color_pair(i))
    except curses.error as ex:
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

    curses.curs_set(False)

    curses.start_color()
    curses.use_default_colors()

    for i in range(0, curses.COLOR_PAIRS):
        curses.init_pair(i + 1, i, -1)
        #curses.init_pair(i, i, -1)

    # stdscr.refresh()


@click.command()
def main():
    app.run()
    curses.endwin()

if __name__ == '__main__':
    main()
