def check_age(age):
    if age >= 18:
        return "SUCCESS"
    else:
        return None


age = int(input())
if not check_age(age):
    print("未成年")
if check_age(age):
    print("成年了")
