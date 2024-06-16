import sqlite3
import os

class DB:

    table_name ='main_db'
    db_path = ''
    #conn = sqlite3.connect(db_path)  # или :memory: чтобы сохранить в RAM
    #cursor = conn.cursor()

    conn = None
    cursor = None

    def __init__(self):

        """# Проблема была в том, что при обращении к этому классу из файла не в корневой папке создавалась новая БД. Решение ниже
        if os.path.exists('trading_db.db'):  # Проверяем, есть ли в нашей папке файл с БД
            self.db_path = 'trading_db.db'  # Если есть, то указываем путь
        elif os.path.exists('../trading_db.db'):  # Если не в нашей, значит уровнем выше
            self.db_path = '../trading_db.db'  # Если есть, то указываем путь"""

        self.db_path = "repost.db"

        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

        check = 0
        if os.stat(self.db_path).st_size:  # файл может создаваться с ошибками и быть просто пустым файлом
            check = self.select('SELECT EXISTS(SELECT * FROM test_db)')  # Проверяем есть ли хоть что-то в таблице
        if not check:
            print('Creating DB file')
            self.create_db('test_db')
            self.create_db('channels')
            self.create_db('words')
            self.create_db('users')
            #self.refresh_db()

    def refresh_db(self):

        self.select("select 'drop table ' || name || ';' from sqlite_master where type = 'table';")  # Конструкция роняет все таблицы даже не зная из названий

    def create_db(self, table_name='main_db'):

        # Создание таблицы
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table_name}
                          (item text UNIQUE)
                       """)
        if table_name =='test_db':
            self.insert('test_db', ['test'])
        self.conn.commit()

    def select(self, sql):  # Выполнение select к БД
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result  # Возращает список со списком записей

    def insert(self, table, data):

        try:
            self.cursor.executemany(f"INSERT INTO {table} VALUES (?)", (data,))  # Количество ? должно совпадать с количеством элементов во входном массиве
        except sqlite3.IntegrityError:
            pass
        self.conn.commit()

    def test_connection(self):  # Проверка соединения. Хотя применяется эта функция для инициализации init класса
        return self.select('SELECT EXISTS(SELECT * FROM main_db)')

    def exec(self, sql):  # Просто обёртка для запросов к БД
        self.cursor.execute(sql)
        self.conn.commit()

    def delete(self, table, data):
        self.cursor.executemany(f"DELETE FROM {table} WHERE item =?", (data,))
        self.conn.commit()


if __name__ == '__main__':
    pass