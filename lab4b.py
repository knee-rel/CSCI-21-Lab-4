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

s = []
index_even = 0
index_odd = 1
names = input().split(' ')
names_list= names
while index_even < len(names_list):
    print(names_list[index_even])
    index_even += 2
while index_odd < len(names_list):
    print(names_list[index_odd])
    index_odd += 2
