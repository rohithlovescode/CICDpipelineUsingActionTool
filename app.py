from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# In-memory list to store tasks.
tasks = []

# HTML template defined as a string.
template = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Todo List App</title>
  </head>
  <body>
    <h1>Todo List</h1>
    <form method="POST" action="{{ url_for('add') }}">
      <input type="text" name="task" placeholder="New Task" required>
      <input type="submit" value="Add">
    </form>
    <ul>
      {% for task in tasks %}
        <li>
          {{ task }}
          <a href="{{ url_for('delete', index=loop.index0) }}">Delete</a>
        </li>
      {% endfor %}
    </ul>
  </body>
</html>
"""

@app.route("/", methods=["GET"])
def index():
    return render_template_string(template, tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    if task:
        tasks.append(task)
    return redirect(url_for("index"))

@app.route("/delete/<int:index>", methods=["GET"])
def delete(index):
    if 0 <= index < len(tasks):
        del tasks[index]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
