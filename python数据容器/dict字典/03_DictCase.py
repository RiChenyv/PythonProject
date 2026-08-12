employee_dict = {
    "SCX": {
        "部门": '科技部',
        "工资": 2000,
        "级别": 1
    },
    "RICHENYV": {
        "部门": '市场部',
        "工资": 5000,
        "级别": 32
    },
    "CUNRIUANG": {
        "部门": '战略投资部',
        "工资": 16000,
        "级别": 41
    },
    "Taffy": {
        "部门": '传播部',
        "工资": 30,
        "级别": 1
    }
}
for key in employee_dict:
    if employee_dict[key]["级别"] == 1:
        employee_dict[key]["工资"] += 10000
print(employee_dict)
