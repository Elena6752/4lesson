# 2. Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.
# Простые делители числа
# Простые делители числа онлайн

# in
# 54

# out
# [2, 3, 3, 3]

num = int(input("Введите число: "))
i = 2  
lst = []
old = num
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(lst)