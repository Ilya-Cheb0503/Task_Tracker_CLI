import pytest

from exceptions import (EmptyFieldError, InvalidDateFormatError,
                        TaskNotFoundError)
from task_tracker import TaskTracker


@pytest.fixture
def tracker(tmp_path):
    test_file = tmp_path / "test_tasks.json"
    return TaskTracker(filename=str(test_file))

def test_add_task(tracker):
    tracker.add_task("Задача 1", "Описание задачи 1", "Работа", "2024-12-31", "высокий")
    tasks = tracker.get_tasks()
    assert len(tasks) == 1
    assert tasks[0].title == "Задача 1"

def test_mark_task_as_completed(tracker):
    tracker.add_task("Задача 1", "Описание задачи 1", "Работа", "2024-12-31", "высокий")
    tracker.mark_task_as_completed(1)
    tasks = tracker.get_tasks()
    assert tasks[0].status == "выполнена"

def test_edit_task(tracker):
    tracker.add_task("Задача 1", "Описание задачи 1", "Работа", "2024-12-31", "высокий")
    tracker.edit_task(1, title="Обновленная задача", description="Обновленное описание")
    tasks = tracker.get_tasks()
    assert tasks[0].title == "Обновленная задача"
    assert tasks[0].description == "Обновленное описание"

def test_invalid_date(tracker):
    with pytest.raises(InvalidDateFormatError):
        tracker.add_task("Задача 1", "Описание задачи 1", "Работа", "31-12-2024", "высокий")

def test_empty_fields(tracker):
    with pytest.raises(EmptyFieldError):
        tracker.add_task("", "Описание задачи 1", "Работа", "2024-12-31", "высокий")

    with pytest.raises(EmptyFieldError):
        tracker.add_task("Задача 1", "", "Работа", "2024-12-31", "высокий")

    with pytest.raises(EmptyFieldError):
        tracker.add_task("Задача 1", "Описание задачи 1", "", "2024-12-31", "высокий")

    with pytest.raises(EmptyFieldError):
        tracker.add_task("Задача 1", "Описание задачи 1", "Работа", "", "высокий")

    with pytest.raises(EmptyFieldError):
        tracker.add_task("Задача 1", "Описание задачи 1", "Работа", "2024-12-31", "")

def test_task_not_found(tracker):
    with pytest.raises(TaskNotFoundError):
        tracker.mark_task_as_completed(999)  # ID, который не существует
