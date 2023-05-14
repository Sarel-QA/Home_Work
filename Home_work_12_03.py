##### 05/03/2023 ######
# 1)
def print_negative(number):
    i = int(input('enter number:'))
    while i <= number:
        print(i)
        i += 1
    else:
        print()
print_negative(0)

#  2)
def count_capital(s):
    counter = 0
    for c in s:
        if c.isupper():
            counter += 1
    return counter
print(count_capital(input('please enter string:')))


