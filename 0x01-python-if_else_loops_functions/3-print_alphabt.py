#!/usr/bin/python3
for ch in range(97, 123):
    if ch != 100 & ch != 112:
        print("{}".format(chr(ch)), end="")
