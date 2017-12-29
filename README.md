# asciiflut
pixelflut clone for text terminals


## How it works

`aflood-server.py` starts a flask web server, as configured in `server_config.py`.
This will bring up the REST-Api that allows clients to draw on the text terminal in which the server is run.
Only one function (`draw`) is provided to do this.
It requires `y` and `x` (the position) as well as `char` as integer arguments, and has an optional `color` argument.

See the provided `aflood-client.py` script for details on how to use the api.
It will also provide an easy way of participating in asciifloods.

Enjoy, Have Fun & Happy Hacking!
