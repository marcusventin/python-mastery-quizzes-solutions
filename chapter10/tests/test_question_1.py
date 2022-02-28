from chapter10.questions.question_1 import Todo, TodoList

class TestQuestion1():
    def test_todo_create_new_todo_object(self):
        assert isinstance(Todo("get milk"), Todo)
    
    def test_todo_returns_text_stored_on_todo(self):
        assert Todo("get milk").text == "get milk"
    
    def test_TodoList_creates_new_TodoList_object(self):
        assert isinstance(TodoList(), TodoList)
    
    def test_adds_a_todo_without_raising_error(self):
        todo_list = TodoList()
        todo = Todo("get milk")

        todo_list.add(todo)
    
    def test_print_one_todo_with_a_bullet_point(self, capsys):
        todo_list = TodoList()
        todo = Todo("get milk")
        todo_list.add(todo)
        
        todo_list.print() 
        stdout = capture_stdout(capsys)
        
        expected_stdout = "* get milk"

        assert stdout[-1] == expected_stdout
    
    def test_print_many_todos_separated_by_new_lines(self, capsys):
        todo_list = TodoList()

        todo1 = Todo("get milk")
        todo2 = Todo("get the paper")
        todo3 = Todo("get orange juice")

        todo_list.add(todo1)
        todo_list.add(todo2)
        todo_list.add(todo3)

        todo_list.print()
        stdout = capture_stdout(capsys)

        expected_stdout = [
            "* get milk",
            "* get the paper",
            "* get orange juice"
        ]

        assert stdout == expected_stdout


def capture_stdout(capsys):
    """Capture the preceding stdout and stderr and convert the stdout to a list,
    with every item corresponding to a line of stdout.
    """
    stdout, stderr = capsys.readouterr()
    return(stdout.strip().split('\n'))

