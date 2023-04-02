##### 26/03/2023 ######
# 1)

def letters_to_file(filename, string_to_file, li):
    f = open(filename, 'w')

    words = string_to_file.split()
    for each_word in words:
        for char in li:
            if char in each_word:
                print(each_word)
                f.write(each_word + ' ')
                break
    f.close()



letters_to_file('my_home_work_file.txt', 'hello to all the students', ['d', 'a', 'Z'])