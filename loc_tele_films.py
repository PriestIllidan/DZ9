from random import *
import json
films = []

def save():
    with open("films.json", "w", encoding="utf-8") as fm:
        fm.write(json.dumps(films, ensure_ascii=False))
    print("Фильм добавлен в файл films.json")

def load():
    global films
    with open("films.json", "r", encoding="utf-8") as fm:
         films = json.load(fm)
    print("Фильмотека успешно загружена!")


while True:
    command = input("Введите команду ")
    if command == "/start":
        print("Бот фильмотека начал свою работу")
    elif command == "/stop":
        save()
        print("Бот остановил свою работу. Заходите еще, будем рады!")
        break
    elif command == "/all":
        print("Вот текущий список фильмов: ", films)
    elif command == "/add":
        film = input("Введите название нового фильма: ")
        films.append(film)
        print("Фильм был успешно добавлен в коллекцию!")
    elif command == "/help":
        print("Здесь какой-то мануал!")
    elif command == "/del":
        film = input("Введите название фильма, который надо удалить: ")
        if film in films:
            films.remove(film)
            print("Фильм был удален!")
        else:
            print("Такого фильма нет в коллекции.")
    elif command == "/random":
        rand = randint(0, len(films)-1)
        print("Случайный фильм: ", films[rand])
    elif command == "/save":
        save()
    elif command == "/load":
        load()
    else:
        print("Неопознанная команда, просьба изучить мануал через /help")
