#5.	Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.

s1 = ord(input("Введите первую букву: "))
s2 = ord(input("Введите вторую букву: "))

first = ord("a")
if s1 < s2:
    count = s2 - s1 - 1
elif s2 < s1:
    count = s1 - s2 - 1
else:
    count = 0

print(f"Первая буква находится на {s1 - first + 1}-м месте алфавита")
print(f"Первая буква находится на {s2 - first + 1}-м месте алфавита")
print(f"Между этими буквами находится {count} букв(а)")
