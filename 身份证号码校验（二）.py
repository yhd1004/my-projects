# 读取输入
n = int(input())
id_numbers = [input().strip() for _ in range(n)]

# 定义加权因子
weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2, 1]

# 存储错误的身份证号码
invalid_ids = []

# 验证每个身份证号码
for id_number in id_numbers:
    # 计算加权和
    total = 0
    for i in range(17):
        total += int(id_number[i]) * weights[i]
    
    # 获取校验码
    check_code = id_number[17]
    if check_code in ['X', 'x']:
        check_value = 10
    else:
        check_value = int(check_code)
    
    # 计算校验和并验证
    if (total + check_value) % 11 != 1:
        invalid_ids.append(id_number)

# 输出所有错误的身份证号码
for invalid_id in invalid_ids:
    print(invalid_id)