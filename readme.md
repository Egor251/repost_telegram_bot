Телеграм бот делающий репосты из каналов по ключевым словам

Прежде чем запускать нужно зайти на сайт https://my.telegram.org/apps и создать приложение. Скопировать api_hash и api_id в файл config.py</br>
Так же в config.py можно указать канал в котором бот будет принимать команды.

установка:

cd repost_bot </br>
python -m pip install -r requirements.txt</br>

Запуск:</br>
python main.py

Команды:</br>
Важно! Для корректной работы бота необходимо чтобы пользователь с телефонным номероом и api выше был подписан на каналы!</br>
</br>
Добавить слово/канал/пользователь - добавляет слово/канал/пользователя</br>
Удалить слово/канал/пользователь - удаляет слово/канал/пользователя</br>
Список слово/канал/пользователь - показывает список слов/каналов/пользователей</br>
Помощь - показывает это сообщение</br>
</br>
Примеры:</br>
"Добавить пользователь 12345678" - Бот будет пересылать сообщения и этому пользователю. По умолчанию он пересылает их в управляющий канал</br>
</br>
"Добавить слово привет" - Бот будет пересылать сообщения из списка каналов со словом привет</br>
</br>
"Добавить канал chanel_name" - Бот будет слушать и пересылать сообщения из канала chanel_name</br>
</br>
"Список каналов" - показывает список каналов, за которыми бот сейчас следит</br>