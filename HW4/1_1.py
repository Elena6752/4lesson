# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001

# out
# 9.000000

import decimal
num1 = decimal.Decimal(8.98785)
print(num1)
num2 = round(num1, 3)
print(num2)
