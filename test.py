to_do_list = []
question = []

def add_task():
    to_do_list.append(input('Введите текст задачи: '))
    print(to_do_list)

def view_tasks():
        print(to_do_list)

def delete_task():
    print(to_do_list)
    to_do_list.pop(int(input('Введите индекс задачи которую хотите удалить')))



def main():
    while True:
        question = int(input('Введите номер действия которое хотите сделать'
                             ' 1 - добавить задачу, 2 - просмотреть список всех задач'
                             ' 3 - удалить задачу, 4 выйти из программы: '))

        if question == 1:
            add_task()
        elif question == 2:
            view_tasks()
        elif question == 3:
            delete_task()
        else:
            break
main()