# int/float/str/bool
numero = int(input("Digite um numero para ver sua tabuada: "))

# com FOR
print("\ncom FOR:")
for i in range(1, 11):
    # range: 0, 11 -> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    print(numero, "X", i, "=", numero*i)

# com WHILE
print("\n\ncom WHILE:")
i2 = 1
while i2 <= 10:
    print(numero, "X", i2, "=", numero*i2)
    i2 += 1