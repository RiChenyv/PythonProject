__all__ = ["readMode"]


def readMode(path):
    temp = open(path, "r", encoding="utf-8")
    return temp


def CountMode(z, b):
    print(z, b)


if __name__ == '__main__':
    f = readMode("/test.txt")
    print(f.readline())
