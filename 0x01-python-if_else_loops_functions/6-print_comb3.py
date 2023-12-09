#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i+1, 10):
        if(i < j):
            print("{:01d}{:01d}".format(i,j), end=", ")
            if(i==8) and (j==9):
                print("{:01d}{:01d}\n".format(i,j), end="")
