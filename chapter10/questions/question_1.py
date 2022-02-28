# Write a program that keeps a list of todos. It should:
# * Have two classes:
#   * `Todo`
#     * Has two methods:
#       * `__init__`: Creates a new todo object. Takes a string as a
#         parameter and stores it on the todo object.
#       * `text`: Takes no parameters. Returns the string that was
#         stored when the todo object was created.
#   * `TodoList`
#     * Has three methods:
#       * `__init__`: Creates a new todo list object. Takes no parameters.
#       * `add`: Takes a todo object as a parameter.  Stores it on the
#         todo list object.
#       * `print`: Takes no parameters.  Creates a string of all the
#         stored todos, one per line.  Each line should start with a
#         `* `.  Prints the string.
#         * e.g.
#           ```
#           * get milk
#           * get the papers
#           ```

# * Note: When you run the automated tests, make sure to remove from
#   the top level of the file any calls to any methods.

class Todo():
    def __init__(self, text):
        self.text = text

class TodoList():
    def __init__(self):
        self.list = []
    
    def add(self, todo):
        self.list.append(todo)
    
    def print(self):
        for todo in self.list:
            print(f"* {todo.text}")