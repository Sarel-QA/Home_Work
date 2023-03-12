##### 05/03/2023 ######
# 1)
def last_and_first(name):
    if name[0] == name[-1]:
        return True
    else:
        return False


letters = last_and_first('sail')
print(f'the answer for exercise 1 is {letters}')


# bonus_1
def last_and_first (name): return name[0] == name[-1]

letters_2 = last_and_first('sars')
print(f'the answer for bonus number 1 is {letters_2}')

# bonus_2
def last_and_first(name): return name[0].lower() == name[3].lower()

b = last_and_first('Sars')
print(f'the answer for bonus number 2 is {b}')


# 2)
def powers_that_be(num_1, num_2):
    return num_1 ** num_2


calculation = powers_that_be(4, 7)
print(f'the answer for exercise 2 is {calculation}')


# 3)
def combine_lists(list1, list2):
    return list1[:len(list1)//2] + list2[len(list2)//2:]

print(combine_lists(['a', 'b', 6, 5] , [True, 'z', 1, 8]))
