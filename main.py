import argparse

from task_tracker import TaskTracker


def main():
    parser = argparse.ArgumentParser(description="Управление задачами в трекере задач.")
    parser.add_argument("command", choices=["add", "list", "complete", "edit", "delete", "search", "delete_category"], help="Команда для выполнения")
    
    # Аргументы для команды "add"
    parser.add_argument("--title", type=str, help="Название задачи")
    parser.add_argument("--description", type=str, help="Описание задачи")
    parser.add_argument("--category", type=str, help="Категория задачи")
    parser.add_argument("--due_date", type=str, help="Срок выполнения задачи")
    parser.add_argument("--priority", type=str, help="Приоритет задачи")

    # Аргументы для команды "complete", "edit", "delete"
    parser.add_argument("--id", type=int, help="ID задачи")

    # Аргументы для команды "search"
    parser.add_argument("--keyword", type=str, help="Ключевое слово для поиска")
    parser.add_argument("--status", type=str, help="Статус задачи для фильтрации")
    
    # Аргументы для команды "delete_category"
    parser.add_argument("--delete_category", type=str, help="Категория для удаления задач")

    args = parser.parse_args()

    tracker = TaskTracker()

    if args.command == "add":
        if not all([args.title, args.description, args.category, args.due_date, args.priority]):
            print("Ошибка: необходимо указать все параметры для добавления задачи.")
        else:
            tracker.add_task(args.title, args.description, args.category, args.due_date, args.priority)
            print("Задача добавлена.")

    elif args.command == "list":
        tasks = tracker.get_tasks()
        for task in tasks:
            print(f"ID: {task.id}, Title: {task.title}, Description: {task.description}, Category: {task.category}, Due_date: {task.due_date}, Priority: {task.priority}, Status: {task.status}")

    elif args.command == "complete":
        if args.id is None:
            print("Ошибка: необходимо указать ID задачи для завершения.")
        else:
            tracker.mark_task_as_completed(args.id)
            print("Задача помечена как выполненная.")

    elif args.command == "edit":
        if args.id is None:
            print("Ошибка: необходимо указать ID задачи для редактирования.")
        else:
            tracker.edit_task(args.id, args.title, args.description, args.category, args.due_date, args.priority)
            print("Задача отредактирована.")

    elif args.command == "delete":
        if args.id is None:
            print("Ошибка: необходимо указать ID задачи для удаления.")
        else:
            tracker.delete_task(args.id)
            print("Задача удалена.")

    elif args.command == "search":
        results = tracker.search_tasks(args.keyword, args.category, args.status)
        for task in results:
            print(f"ID: {task.id}, Title: {task.title}, Description: {task.description}, Category: {task.category}, Due_date: {task.due_date}, Priority: {task.priority}, Status: {task.status}")


    elif args.command == "delete_category":
        if args.delete_category is None:
            print("Ошибка: необходимо указать категорию для удаления задач.")
        else:
            tracker.delete_tasks_by_category(args.delete_category)
            print("Задачи в категории удалены.")

if __name__ == "__main__":
    main()