def get_todos(filepath='todos.txt'):
    """Read a text file and return a list of
        todo items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath='todos.txt'):
    """update the changes to the
       todo list to the text file"""
    with open (filepath, 'w') as file_write:
        file_write.writelines(todos_arg)