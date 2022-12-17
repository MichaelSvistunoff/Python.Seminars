# Задача 4 [task-2]
# Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?  
# Пример:  
# 6 -> 1 4 1  
# 24 -> 4 16 4  
# 60 -> 10 40 10

summ = int(input('Enter the summary of origami: '))

one_child_boy = summ // 6
one_child_girl = one_child_boy * 4

print(f'Katya made {one_child_girl} origamis, Petya and Seryioja - {one_child_boy} and {one_child_boy}')