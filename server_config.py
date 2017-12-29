import string

class MyConfig(object):

    realm = 'asciiflut.dev'

    whitelist = string.ascii_letters + string.punctuation + string.digits
    char_whitelist = list(map(ord, whitelist))

    DEBUG = True
    SERVER_NAME = '127.0.0.1:5000'
