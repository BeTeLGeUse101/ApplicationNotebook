import csv
import os
from datetime import datetime

NOTES_FILE = "notes.csv"

def display_menu():
    print("*********************")
    print("Консольный блокнот")
    print("*********************")
    print("1. Просмотреть все заметки")
    print("2. Просмотреть заметку")
    print("3. Поиск заметки по дате")
    print("4. Добавить новую заметку")
    print("5. Редактировать заметку")
    print("6. Удалить заметку")
    print("7. Выйти")

def show_notes():
    with open(NOTES_FILE, "r", encoding="utf-8" , newline="") as file:
        reader = csv.reader(file, delimiter=";")
        notes = list(reader)
        if notes:
            print("---------------------")
            print("Список заметок:")
            for note in notes:
                print(f"Идентификатор: {note[0]}")
                print(f"Заголовок: {note[1]}")
                print(f"Тело заметки: {note[2]}")
                print(f"Дата/время создания: {note[3]}")
                print(f"Дата/время последнего изменения: {note[4]}")
                print("---------------------")
        else:
            print("Заметок пока нет.")

def show_note():
    note_id = input("Введите идентификатор заметки для просмотра: ")
    with open(NOTES_FILE, "r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file, delimiter=";")
        notes = list(reader)
        for note in notes:
            if note[0] == note_id:
                print("---------------------")
                print(f"Идентификатор: {note[0]}")
                print(f"Заголовок: {note[1]}")
                print(f"Тело заметки: {note[2]}")
                print(f"Дата/время создания: {note[3]}")
                print(f"Дата/время последнего изменения: {note[4]}")
                print("---------------------")
                break
        else:
            print("Заметка с указанным идентификатором не найдена.")

def add_note():
    id = generate_id()
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = [id, title, body, timestamp, timestamp]
    with open(NOTES_FILE, "a",encoding="utf-8" , newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(note)
    print("Заметка добавлена.")

def edit_note():
    show_notes()
    note_id = input("Введите идентификатор заметки для редактирования: ")
    notes = []
    with open(NOTES_FILE, "r", encoding="utf-8" , newline="") as file:
        reader = csv.reader(file, delimiter=";")
        notes = list(reader)
        for i, note in enumerate(notes):
            if note[0] == note_id:
                edited_title = input("Введите новый заголовок заметки: ")
                edited_body = input("Введите новый текст заметки: ")
                notes[i][1] = edited_title
                notes[i][2] = edited_body
                notes[i][4] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                break
    with open(NOTES_FILE, "w", encoding="utf-8" , newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(notes)
    print("Заметка отредактирована.")

def search_notes_by_date():
    date_str = input("Введите дату для поиска заметок (в формате ГГГГ-ММ-ДД): ")
    try:
        search_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Неверный формат даты. Попробуйте снова.")
        return

    with open(NOTES_FILE, "r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file, delimiter=";")
        notes = list(reader)
        found_notes = []
        for note in notes:
            note_date = datetime.strptime(note[3], "%Y-%m-%d %H:%M:%S").date()
            if note_date == search_date:
                found_notes.append(note)
        
        if found_notes:
            print(f"Найдено заметок по дате {date_str}: {len(found_notes)}")
            for note in found_notes:
                ("---------------------")
                print(f"Идентификатор: {note[0]}")
                print(f"Заголовок: {note[1]}")
                print(f"Тело заметки: {note[2]}")
                print(f"Дата/время создания: {note[3]}")
                print(f"Дата/время последнего изменения: {note[4]}")
                print("---------------------")
        else:
            print(f"Заметки по дате {date_str} не найдены.")

def delete_note():
    show_notes()
    note_id = input("Введите идентификатор заметки для удаления: ")
    notes = []
    with open(NOTES_FILE, "r", encoding="utf-8" , newline="") as file:
        reader = csv.reader(file, delimiter=";")
        notes = list(reader)
        for i, note in enumerate(notes):
            if note[0] == note_id:
                del notes[i]
                break
    with open(NOTES_FILE, "w", encoding="utf-8" , newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerows(notes)
    print("Заметка удалена.")

def generate_id():
    notes = []
    if os.path.isfile(NOTES_FILE):
        with open(NOTES_FILE, "r", encoding="utf-8" , newline="") as file:
            reader = csv.reader(file, delimiter=";")
            notes = list(reader)
    if notes:
        last_id = int(notes[-1][0])
        return str(last_id + 1)
    return "1"

def main():
    if not os.path.isfile(NOTES_FILE):
        with open(NOTES_FILE, "w", encoding="utf-8", newline="") as file:
            pass
    while True:
        display_menu()
        choice = input("Выберите действие (1-5): ")
        if choice == "1":
            show_notes()
        elif choice == "2":
            show_note()
        elif choice == "3":
            search_notes_by_date()
        elif choice == "4":
            add_note()
        elif choice == "5":
            edit_note()
        elif choice == "6":
            delete_note()
        elif choice == "7":
            print("Спасибо за использование блокнота. До свидания!")
            break
        else:
            print("Недопустимый ввод. Попробуйте еще раз.")

if __name__ == "__main__":
    main()