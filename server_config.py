import string

class MyConfig(object):

    char_whitelist = string.ascii_letters + string.punctuation + string.digits
    char_whitelist = list(map(ord, char_whitelist))
