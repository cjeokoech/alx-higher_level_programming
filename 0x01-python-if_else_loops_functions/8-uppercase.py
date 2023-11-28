#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        print(chr(ord(ch) + 32), end='')
        print()
