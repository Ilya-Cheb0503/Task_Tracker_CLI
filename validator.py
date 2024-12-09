from datetime import datetime

from exceptions import TaskError


def validate_task(title: str, description: str, category: str, due_date: str, priority: str) -> None:
    """Валидация вводимых данных для задачи."""
    if not title or not description or not category or not due_date or not priority:
        raise TaskError("Все поля должны быть заполнены.")
    
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise TaskError("Неправильный формат даты. Используйте YYYY-MM-DD.")
