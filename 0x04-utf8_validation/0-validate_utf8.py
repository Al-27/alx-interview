#!/usr/bin/python3
""" UTF8 """
import chardet


def validUTF8(data):
    return chardet.detect(bytearray(data,"utf-8"))['encoding'] in ("utf-8", "ascii")

if __name__ == "__main__":
    print(validUTF8("wxcdsfvds"))
