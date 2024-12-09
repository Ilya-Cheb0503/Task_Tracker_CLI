import json
import os
from datetime import datetime
from typing import List, Optional

from exceptions import (EmptyFieldError, InvalidDateFormatError,
                        TaskNotFoundError)
from task import Task


class TaskTracker:
    def __init__(self, filename: str = 'tasks.json'):
        """Инициализация трекера задач с загрузкой задач из файла."""
        self.filename: str = filename
        self.tasks: List[Task] = self.load_tasks()

    def load_tasks(self) -> List[Task]:
        """Загрузка задач из файла JSON."""
        tasks_list = []
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                tasks_data = json.load(file)
                
                for task in tasks_data:
                    status = task.pop('status')
                    a_task = Task(**task)
                    a_task.status = status
                    tasks_list.append(a_task)
                    
        return tasks_list

    def save_tasks(self) -> None:
        """Сохранение текущих задач в файл JSON."""
        with open(self.filename, 'w') as file:
            json.dump([task.__dict__ for task in self.tasks], file, indent=4)

    def add_task(self, title: str, description: str, category: str, due_date: str, priority: str) -> None:
        """Добавление новой задачи с проверкой обязательных полей и формата даты."""
        for attribute_name, attribute_value in locals().items():
            if attribute_name.__eq__('self'):
                pass
            elif attribute_value.__eq__(''):
                raise EmptyFieldError(attribute_name)
        
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            raise InvalidDateFormatError()

        task_id: int = len(self.tasks) + 1
        task = Task(task_id, title, description, category, due_date, priority)
        self.tasks.append(task)
        self.save_tasks()

    def get_tasks(self) -> List[Task]:
        """Получение списка всех задач."""
        return self.tasks

    def mark_task_as_completed(self, task_id: int) -> None:
        """Отметка задачи как завершенной по идентификатору."""
        for task in self.tasks:
            if task.id == task_id:
                task.mark_as_completed()
                self.save_tasks()
                return
        raise TaskNotFoundError()

    def edit_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None,
                  category: Optional[str] = None, due_date: Optional[str] = None,
                  priority: Optional[str] = None) -> None:
        """Редактирование существующей задачи по идентификатору."""
        for task in self.tasks:
            if task.id == task_id:
                if title is not None:
                    task.title = title
                if description is not None:
                    task.description = description
                if category is not None:
                    task.category = category
                if due_date is not None:
                    try:
                        datetime.strptime(due_date, "%Y-%m-%d")
                        task.due_date = due_date
                    except ValueError:
                        raise InvalidDateFormatError()
                if priority is not None:
                    task.priority = priority
                self.save_tasks()
                return
        raise TaskNotFoundError()

    def search_tasks(self, keyword: Optional[str] = None, category: Optional[str] = None,
                     status: Optional[str] = None) -> List[Task]:
        """Поиск задач по ключевому слову, категории или статусу."""
        results = self.tasks
        if keyword:
            results = [task for task in results if keyword.lower() in task.title.lower() or keyword.lower() in task.description.lower()]
        if category:
            results = [task for task in results if task.category == category]
        if status:
            results = [task for task in results if task.status == status]
        return results

    def delete_task(self, task_id: int) -> None:
        """Удаление задачи по идентификатору."""
        self.tasks = [task for task in self.tasks if task.id != task_id]
        self.save_tasks()

    def delete_tasks_by_category(self, category: str) -> None:
        """Удаление всех задач из указанной категории."""
        self.tasks = [task for task in self.tasks if task.category != category]
        self.save_tasks()