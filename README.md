# Верный помощник в учебе

Этот набор скриптов для изменения данных электронного дневника. Скрипты помогут тебе изменить оценки, удалить замечания учителя, добавить похвалу учителя.

## Описание скриптов

- `get_schoolkid` - Принимает ФИО ученика и вовзращает его объект в БД  
- `fix_marks` - Принимает объект-ученик, находит плохие оценки(2,3) и исправляет их на 5  
- `remove_chastisements` - Принимает объект-ученик и удаляет все замечания учителей  
- `create_commendation` - Принимает объект-ученик, название предмета, находит рандомный урок и создает похвалу от учителя  

## Запуск

- Скачайте код
- Положите файл `scripts.py` в директорию с репозиторием электронного дневника
- Запустите `Django shel` командой:  
  ```bash
     python manage.py shell
  ```
- Импортируйте и запускайте нужные вам функции из модуля `scripts`  


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
