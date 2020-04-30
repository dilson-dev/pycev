# Exercício Python #047 - Contagem de pares

# print()
# for num in range(2, 51, 2):
#     print(num, end='; ')
#     '''if num % 2 == 0:
#         print(num)'''
# print()

[print(num, end=', ' if num != 50 else '.') for num in range(2, 51, 2)]
