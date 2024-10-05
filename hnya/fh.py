a, b = int(input()), int(input())
max_num = 0
max_sum_divisors = 0

for i in range(a, b + 1):
    current_sum_divisors = 0
    
    for j in range(1, i + 1):
        if i % j == 0:
            current_sum_divisors += j
            
    if current_sum_divisors > max_sum_divisors:
        max_sum_divisors = current_sum_divisors
        max_num = i 

print(max_num, max_sum_divisors)
