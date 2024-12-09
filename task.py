class Task:
    def __init__(self, id: int, title: str, description: str, category: str, due_date: str, priority: str):
        self.id = id
        self.title = title
        self.description = description
        self.category = category
        self.due_date = due_date
        self.priority = priority
        self.status = "не выполнена"

    def mark_as_completed(self):
        self.status = "выполнена"
