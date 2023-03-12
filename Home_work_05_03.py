                                                                                    ##### 05/03/2023 ######
# 1)
def last_and_first (name):
    if name[0] == name[3]:
        return True
    else:
        return False

letters = last_and_first('sail')
print(f'the answer for exercise 1 is {letters}')

# bonus#1
# def last_and_first (name): return name[0] == name[3]

# letters_2 = last_and_first('sars')
# print(f'the answer for bonus exercise is {letters_2}')

# bonus#2
# def last_and_first (name): return name[0] == name[3]
#
# b = last_and_first('Sars')
# print(f'the answer for bonus exercise is {b}')

# 2)
def powers_that_be (low, high):
    return low ** high
calculation = powers_that_be(4, 7)
print(f'the answer for exercise 2 is {calculation}')

# 3)
def combine_lists (list1, list2):
    return list1[2:3] and list2[0:1]

list1 = ['a','b',6,5]
list_2 = [True,'z', 1, 0]

print(list1, list_2)