from flask import Flask, jsonify, request, abort
import sqlite3
import os

DB_PATH = os.environ.get("DB_PATH", "/data/todo.db")


def get_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done INTEGER NOT NULL DEFAULT 0
        )
        """
    )
    conn.commit()
    conn.close()


def create_app():
    app = Flask(__name__)
    init_db()

    @app.get("/health")
    def health():
        return jsonify(status="ok")

    @app.get("/tasks")
    def list_tasks():
        conn = get_db()
        rows = conn.execute("SELECT * FROM tasks").fetchall()
        conn.close()
        return jsonify([dict(row) for row in rows])

    @app.post("/tasks")
    def create_task():
        data = request.get_json(silent=True) or {}
        title = data.get("title")
        if not title:
            abort(400, description="Field 'title' is required")
        conn = get_db()
        cursor = conn.execute("INSERT INTO tasks (title, done) VALUES (?, 0)", (title,))
        conn.commit()
        task_id = cursor.lastrowid
        conn.close()
        return jsonify(id=task_id, title=title, done=False), 201

    @app.put("/tasks/<int:task_id>")
    def update_task(task_id):
        data = request.get_json(silent=True) or {}
        done = bool(data.get("done", False))
        conn = get_db()
        result = conn.execute(
            "UPDATE tasks SET done = ? WHERE id = ?", (int(done), task_id)
        )
        conn.commit()
        conn.close()
        if result.rowcount == 0:
            abort(404, description="Task not found")
        return jsonify(id=task_id, done=done)

    @app.delete("/tasks/<int:task_id>")
    def delete_task(task_id):
        conn = get_db()
        result = conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        conn.close()
        if result.rowcount == 0:
            abort(404, description="Task not found")
        return "", 204

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
