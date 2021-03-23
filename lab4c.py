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

words = input()
word = words.split(' ')
phrases = word
indices = input().split(' ')
index = [int(i) for i in indices]
numbers = index
length = len(word)
for n in index:
    if n > length or n <= 0:
        print('NO')
    else:
        print(word[n-1])



        
        