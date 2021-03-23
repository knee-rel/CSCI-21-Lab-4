# Nirel Marie M. Ibarra
# 192468
# March 22, 2021

# I have not discussed the Python language code in my program
# with anyone other than my instructor or the teaching assistants
# assigned to this course

# I have not used Python language code obatained from another student
# or any other unauthorized source, either modified or unmodified

# If any Python language code or documentation used in my program 
# was obtained from another source, such as a textbook or website,
# that has clearly noted with a proper ciration in the comments
# of my program

i = 0
while True:
    counter = int(input())
    if counter == -1:
        break
    else:
        total = 0
        phrases = ''
        s = []
        i += 1
        j = -1
        while total < counter:
            user_input = input()
            s.append(user_input)
            total += 1
        print('Case:', i)
        while j >= -len(s):
            print(s[j])
            j += -1
        continue


