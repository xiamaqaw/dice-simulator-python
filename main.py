from random import randint

print("Привет , это симулятор игры в кости! наслаждайся")

what = input("Готов сыграть?: ")
if what == "Да":
	a = randint(2,12)
	b = randint(2,12)
	if a > b:
		print("Вы выйграли!")
		print(f"Вашему противнику упало {b}, а вам {a} )")
	elif b > a:
		print("Вы проиграли!")
		print(f"Вашему противнику упало {b}, а вам {a}")
	else:
		pass
elif what == "Нет":
	print("Ахахахахах Сыкло")
else:
	print("Удали скрипт")