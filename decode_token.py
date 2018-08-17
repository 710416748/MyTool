#!/usr/bin/python
# -*- coding: utf-8 -*-
import base64
import sys
import token
token_base64 = bytes(0)
token_decode = bytes(0)
head = b''

def decode_token():
    if len(token_base64) :
        token_decode = base64.b64decode(token_base64)
        '''
        print(token_decode)
        head = token_decode[1]
        print(head)
        print(hex(int(head)))
        '''
        print("token len is :" + str(len(token_decode)))
        token.Token(token_decode)


if __name__ == '__main__':
    '''
    head = bytes(b'\x55')
    print(head)
    print(head.hex())
    print(len(head))
    '''

    if len(sys.argv) > 1 :
        token_base64 = bytes((sys.argv[1]), encoding="utf-8")
        print(token_base64)

    decode_token()