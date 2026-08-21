def str_reverse(s):
    length = len(s)
    count = length - 1
    str = ''
    while count >= 0:
        str += s[count]
        count -= 1
    return str


# return s[::-1]        字符串切片操作进行翻转


def substr(s, x, y):
    start = x - 1
    end = y - 1
    str = ''
    while start <= end:
        str += s[start]
        start += 1
    return str
    # return s[x-1:y-1]


if __name__ == '__main__':
    final = str_reverse("羽辰日")
    print(final)
    final = substr("日寸日辰羊羽", 3, 5)
    print(final)
