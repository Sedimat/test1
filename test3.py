n =  int(input("кількість елементів списку"))
user_list = []

i = 0

while i < n:
    spisok = "добав елемент #" +str(i + 1)+ ":"
    user_list.append(input(spisok))
    i +=1
user_list.sort()
print(user_list)