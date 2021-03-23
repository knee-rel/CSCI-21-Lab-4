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

while True:
    n = input()
    if n == '0':
        break
    else:
        numbers = n.split(' ')
        num = [int(i) for i in numbers]
        length = len(num)
        first = 0
        last = length - 1
        status = 1
        while(first < last):
            if(num[first] == num[last]):
                first+=1
                last-=1
                continue
            else:
                status = 0
                break
        if(status):
            print('Yes')
        else:
            print('No')