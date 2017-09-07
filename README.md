# Описание
Скрипт получает в качестве параметра командной строки ссылку на веб-сайт.
Далее приложение должно получить содержимое HTML документа по ссылке и во всех тэгах убрать атрибуты style.
Результат выводит на экран.

Например, скрипт получает HTML документ следующего содержания
```
<body>
  <p style="font-size: 12pt">Example</p>
</body>
```

Результат должен быть такой:
```
<body>
  <p>Example</p>
</body>
```

# Как использовать
Необходимо установить виртуальное окружения и необходимые модули

``` #!bash

virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
```

Запустить
``` #!bash
python fetch_page_no_style.py
```

# Run unit-tests
``` #!bash
python tests.py

```