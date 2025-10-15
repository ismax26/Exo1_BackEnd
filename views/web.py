from flask import Flask, render_template, request, redirect, url_for
from controllers.task_controller import TaskController

app = Flask(__name__)
controller = TaskController()


@app.route('/')
def home():
    tasks = controller.list_tasks()
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title', '').strip()
    if title:
        controller.add_task(title)
    return redirect(url_for('home'))


@app.route('/delete/<int:index>')
def delete_task(index):
    controller.delete_task(index)
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
