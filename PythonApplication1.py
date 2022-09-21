# с помощью инпут вносим данные
FI=input("Your name and surname: ")
num = input("Enter a age: ")

# переводим строку в число
num = int(num)

# ставим предельно понятные условия для разных категории
if num == 0 and num>=14:#
  print(FI, "is child")
elif num>14 and num<=25:
  print(FI, "is young")
else:
  print(FI, "is adult")