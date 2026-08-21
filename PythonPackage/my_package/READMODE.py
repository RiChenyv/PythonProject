def ReadMode(path):
    temp = open(path, "r", encoding="utf-8")
    return temp


if __name__ == '__main__':
    f = ReadMode("/test.txt")
    print(f.readline())
