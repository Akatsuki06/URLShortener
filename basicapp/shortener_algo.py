#this contains the algorithm to shorten the url
from math import floor
import string

class algo():
    """the algo converts decimal to other base and vice versa"""

    CHAR_LIST = string.ascii_lowercase+string.ascii_uppercase+string.digits+'_' #base 63
    CHAR_DICT = dict((c, i) for i, c in enumerate(CHAR_LIST))# a character to index dictionary

    def __init__(self):
        super(algo, self).__init__()

    def decode(self,string):
        char_dict=self.CHAR_DICT
        length = len(char_dict)
        ret = 0
        for i, c in enumerate(string[::-1]):
            ret += (length ** i) * char_dict[c]
        return ret

    def encode(self,num):
        char_list=self.CHAR_LIST
        if num == 0:return char_list[0]
        length = len(char_list)
        ret = ''
        while num != 0:
            ret = char_list[num % length] + ret
            num = int(num/length)
        return ret
