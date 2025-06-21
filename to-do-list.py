def main():
    command = ''
    while command != 'exit':
        command = input('show, add, remove, or exit? ')
        if command == 'show':
            show_todo_list()
        elif command == 'add':
            task = input('What task needs to be added? ')
            add_to_todo_list(task)
        elif command == 'remove':
            number = int(input('What item number should be removed? '))
            remove_from_todo_list(number)
    print('Goodbye!')

"""
show, add, remove, or exit? show
Nothing in the list!
show, add, remove, or exit? add
What task needs to be added? Do the Laundry
show, add, remove, or exit? add
What task needs to be added? Go to the Gym
show, add, remove, or exit? show
  * (1) Do the Laundry
  * (2) Go to the Gym
show, add, remove, or exit? exit
Goodbye!
"""

def show_todo_list():
    with open('to-do-list.txt', 'r') as data_file:
        todo_list = data_file.readlines()
        # if the file is empty, say there's no items
        if not todo_list:
            print('Nothing in the list!')
        # else, print each line, starting with "  * (line_num) "
        else:
            line_num = 1
            for line in todo_list:
                print(f'  * ({line_num}) {line}')
                line_num += 1


def add_to_todo_list(item):
    with open('to-do-list.txt', 'a') as data_file:
        data_file.write(item + '\n')

def remove_from_todo_list(num):
    with open('to-do-list.txt', 'r') as file_reader:
        todo_list = file_reader.readlines()

    # check if the number is valid
    if 1 <= num <= len(todo_list):
        del todo_list[num - 1]  # adjust for 0-based index
        # write updated list back
        with open('to-do-list.txt', 'w') as file_writer:
            file_writer.writelines(todo_list)
        print(f"Removed item {num}.")
    else:
        print("Invalid item number.")




main()