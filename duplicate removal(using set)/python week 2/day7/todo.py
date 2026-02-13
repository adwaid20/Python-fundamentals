import sys
import json
from pathlib import Path

DB_FILE = Path("tasks.json")


def load_tasks():
    if DB_FILE.exists():
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def add_task(desc):
    tasks = load_tasks()
    task = {"id": len(tasks) + 1, "desc": desc, "done": False}
    tasks.append(task)
    save_tasks(tasks)
    print(f"Added task #{task['id']}: {desc}")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet!")
        return
    for t in tasks:
        status = "[x]" if t["done"] else "[ ]"
        print(f"{status} {t['id']}. {t['desc']}")


def mark_done(task_id):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            save_tasks(tasks)
            print(f"Marked task #{task_id} as done")
            return
    print(f"Task #{task_id} not found")


def main():
    if len(sys.argv) < 2:
        print("Usage: python todo.py [add|list|done] ...")
        return

    cmd = sys.argv[1]

    if cmd == "add":
        if len(sys.argv) < 3:
            print("Usage: python todo.py add <task description>")
            return
        desc = " ".join(sys.argv[2:])
        add_task(desc)

    elif cmd == "list":
        list_tasks()

    elif cmd == "done":
        if len(sys.argv) < 3:
            print("Usage: python todo.py done <task id>")
            return
        try:
            task_id = int(sys.argv[2])
            mark_done(task_id)
        except ValueError:
            print("Task id must be a number")

    else:
        print(f"Unknown command: {cmd}")


if __name__ == "__main__":
    main()
