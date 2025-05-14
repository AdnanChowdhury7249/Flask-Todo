from flask import Blueprint, render_template, request, redirect
from models.todo import Todo
from extensions import db

main = Blueprint("main", __name__)


@main.route("/")
def index():
    todo_list = Todo.query.all()
    return render_template("base.html", todo_list=todo_list)


@main.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect("/")


@main.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.get(todo_id)
    todo.complete = not todo.complete
    db.session.commit()
    return redirect("/")


@main.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")
