def main():
    while True:
        print("""
               1. show tasks
               2. add task
               3. delete task
               4.edit task
               5. exit """)
        choice = input("please enter your choice:")
        if choice == '1':
            show_tasks()
        elif choice == '2':
            title = input("title:")
            add_tasks(title)
        elif choice == '3':
            show_tasks()
            try:
                index = int(input("please enter the number of the task which you want to delete:"))
                delete_tasks(index)
            except ValueError:
                print("invalid number")
        elif choice == '4':
            show_tasks()
            try:
                index = int(input("please enter the number of the task which you want to edit:"))
                new_title = input('please enter edited title:')
                edit_tasks(index, new_title)
            except ValueError:
                print("invalid number")

        elif choice == '5':
            print("finish")
            break
        else:
            print("invalid choice")


if __name__ == "__main__":
    main()

