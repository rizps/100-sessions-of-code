# treasure map


# 🚨 Don't change the code below 👇
row1 = ["⬜","⬜","⬜"]
row2 = ["⬜","⬜","⬜"]
row3 = ["⬜","⬜","⬜"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
position = '23'
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
print('------------------------------------')
p0 = int(position[0]) # horizontal - baris - 2
p1 = int(position[1]) # vertical - kolom - 3
# print(map[p0][p1])
map[p1-1][p0-1] = 'X'


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")