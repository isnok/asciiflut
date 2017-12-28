import string

class MyConfig(object):

    server_name = 'asciiflut-dev'
    whitelist = string.ascii_letters + string.punctuation + string.digits
    char_whitelist = list(map(ord, whitelist))
