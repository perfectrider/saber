Для запуска приложения выполнить следующие шаги:
1. Создать виртуальное окружение
2. Установить зависимости:
```python
pip install -r requirements.txt
```
3. Выполнить запуск сервера:
```python
python3 manage.py runserver
```
4. Оправить *POST*-запрос на `localhost:8000/builds/`:
```json
{
"build": "make_tests"
}
```

Пример ответа:
```JSON
"tasks": [
        "write_fuchsia_golems",
        "write_blue_ogres",
        "upgrade_navy_ogres",
...
```