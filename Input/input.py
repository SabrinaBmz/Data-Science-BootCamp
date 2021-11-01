direct = open('C:/Users/user/PycharmProjects/Data Science Bootcamp/Input/student_names.txt')

students = direct.read()

random = ["Sabrina Bmz", "Alessia Cara", "Marshal Mathers", "Clara Jen"]
for student in random:
    students = students + "\n" + student

direct = open('C:/Users/user/PycharmProjects/Data Science Bootcamp/Input/student_names.txt', 'w')

direct.write(students)
direct.close()

# read the first n lines

direct = open('C:/Users/user/PycharmProjects/Data Science Bootcamp/Input/student_names.txt')
f_lines = 3
for i in range(3):
    line = direct.readline()
    print(line)
direct.close()

# read the last n lines

direct = open('C:/Users/user/PycharmProjects/Data Science Bootcamp/Input/student_names.txt', 'r')
l_lines = -3
lines = direct.readlines()
l_line = lines[l_lines:]
for i in l_line:
    print(i)
direct.close()

# x name test
direct = open('C:/Users/user/PycharmProjects/Data Science Bootcamp/Input/student_names.txt', 'r')
name = "Mason Smith"
lines = direct.readline()
l_line = lines
for i in l_line:
    if l_line == name:
        break

# generate files

files_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'T', 'O', 'P', 'U', 'V', 'W', 'X', 'Y', 'Z']
for i in range(len(files_names)):
    file_name = files_names[i]
    file = file_name + '.txt'
    open(file, 'w').write(files_names[i])