# Веб-приложение для обнаружения форм  

## Описание
Приложение принимает на вход по url /get_form POST запросом данные в `x-www-form-urlencoded` формате и возвращает имя 
формы соответствующей входящим данным, если она найдена в базе данных, или словарь с типами входящих данных.  

ссылка на задание:  
https://docs.google.com/document/d/1fMFwPBs53xzcrltEFOpEG4GWTaQ-5jvVLrNT6_hmC7I/edit?tab=t.0#heading=h.pieurecv5l1j

## Добавление шаблонов
Путь к загружаемым в базу данных шаблонам устанавливается в `config.py` в параметре `templates_path`.  
`templates_path=None` будет работать с загруженными ранее шаблонами.

## Запуск
для запуска веб-приложения введите команду:
```sh
docker-compose up --build
```

## Тестирование

Для тестовых запросов запустите скрипт:  
```sh
python tests/test.py
```  

в файле `tests/test_templates.json` задаётся список данных для тестовых запросов.

## Зависимости
`MongoDB`
`fastapi`
`uvicorn`
`pydantic`
`motor`