#!/usr/bin/python3
""" UTF8 """
import chardet


def validUTF8(data):
    if type(data) is str:
        return chardet.detect(bytearray(data,"utf-8"))['encoding']
        in ("utf-8", "ascii")
    try:
        return chardet.detect(bytearray(data))['encoding'] in ("utf-8", "ascii")
    except:
        return False
if __name__ == "__main__":
    print(validUTF8("wxcdsfvds"))
