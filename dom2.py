str = input("Ведіть текст на латиниці: ")

abc = str.lower()

print("В вашому тексті голосних букв A, E, I, O, U, Y: ", abc.count("a") + abc.count("e") + abc.count("i") + abc.count("o") + abc.count("u") + abc.count("y"))

