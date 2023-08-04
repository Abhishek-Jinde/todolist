from flask import Flask, render_template, request, redirect

app = Flask(__name__)

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

todo_list = TodoList()

@app.route('/')
def index():
    return render_template('index.html', tasks=todo_list.tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        todo_list.add_task(task)
    return redirect('/')

@app.route('/remove/<task>', methods=['POST'])
def remove_task(task):
    todo_list.remove_task(task)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
