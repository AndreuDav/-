to_do_list = []
question = []
while question != 4:
    question = int(input('Введите номер действия которое хотите сделать'
      '1 - добавить задачу, 2 - просмотреть список всех задач'
      '3 - удалить задачу, 4 выйти из программы: '))
    if question == 1:
        to_do_list.append(input('Введите текст задачи по числам: '))
        print(to_do_list)
    if question == 2:
        print(to_do_list)
    if question == 3:
        print(to_do_list)
        to_do_list.pop(int(input('Введите индекс задачи которую хотите удалить')))