my_str = "生新来迎中亡死次一在会我"
new_str = ""
count = len(my_str)
while count > 0:
    new_str = new_str + my_str[count - 1]
    count -= 1
indexDead = new_str.index("死")
indexBrith = new_str.index("新")
death = new_str[indexDead:indexDead + 2]
print(death)
birth = new_str[indexBrith:indexBrith + 2]
print(birth)
