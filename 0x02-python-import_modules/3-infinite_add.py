#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = len(sys.argv)
    if length < 2:
        print("{}".format(length - 1))
    else:
        Total = 0
        for x in range(1, length):
            Total += int(sys.argv[x])
        print("{}".format(Total))
