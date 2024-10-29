to_do_list = []
question = []
while True:
    main = int(input('Введите номер действия которое хотите сделать'
      '1 - добавить задачу, 2 - просмотреть список всех задач'
      '3 - удалить задачу, 4 выйти из программы: '))
    if main == 1:
        add_task = to_do_list.append(input('Введите текст задачи по числам: '))
        print(to_do_list)
    elif main == 2:
        view_tasks = print(to_do_list)
    elif main == 3:
        print(to_do_list)
        delete_task = to_do_list.pop(int(input('Введите индекс задачи которую хотите удалить')))
    elif main == 4:
        print('Программа завершена')
        break
    else:
        print('Ошибка, введите корректное значение!')
