immutable_var = 1, 2, 3, 'meow', True
print(immutable_var)
# immutable_var[1] = 102 Нельзя изменить элемент кортежа, т.к. кортеж неизменяемая коллекция. Можно изменить определенные элементы находящиеся в кортеже такие как списки.

mutable_list = [1, 421, 193], 182, 'krya', True
mutable_list[0][2] = 'meow'
print(mutable_list)
