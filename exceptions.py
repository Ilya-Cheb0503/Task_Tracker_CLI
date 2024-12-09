class TaskError(Exception):
    """Общее исключение для ошибок, связанных с задачами."""
    pass

class EmptyFieldError(TaskError):
    """Исключение для пустых полей."""
    def __init__(self, field_name: str):
        super().__init__(f"Ошибка: поле '{field_name}' не должно быть пустым.")

class InvalidDateFormatError(TaskError):
    """Исключение для некорректного формата даты."""
    def __init__(self):
        super().__init__("Ошибка: вы передали некорректный формат даты. Пожалуйста, исправьте дату в формате 'YYYY-MM-DD'.")

class TaskNotFoundError(TaskError):
    """Исключение для случаев, когда задача не найдена."""
    def __init__(self):
        super().__init__("Ошибка: задача не найдена.")

class ValidationError(TaskError):
    """Исключение для ошибок валидации."""
    def __init__(self, message: str):
        super().__init__(f"Ошибка валидации: {message}")