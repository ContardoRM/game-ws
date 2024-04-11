from sqlite3 import connect, Error

class Database:
    def __init__(self):
        self.filename = 'database.db'

    def initialize(self):
        if not self.initialized():
            print('Initializing database')
            queries = [
                """CREATE TABLE solo (
                    'username' VARCHAR(45) NOT NULL DEFAULT '',
                    'high' INT UNSIGNED DEFAULT NULL,
                    PRIMARY KEY ('username'));""",
                """CREATE TABLE duo (
                    'username' VARCHAR(45) NOT NULL DEFAULT '',
                    'high' INT UNSIGNED DEFAULT NULL,
                    PRIMARY KEY ('username'));"""
            ]
            for query in queries:
                self.executeQuery(query)
        else:
            print('Database already initialized')
        return True

    def initialized(self):
        result_solo = self.executeQuery('SELECT name FROM sqlite_master WHERE type="table" AND name="solo";')
        result_duo = self.executeQuery('SELECT name FROM sqlite_master WHERE type="table" AND name="duo";')
        return result_solo is not None and len(result_solo.fetchall()) == 1 and \
               result_duo is not None and len(result_duo.fetchall()) == 1

    def executeQuery(self, query, values=()):
        try:
            with connect(self.filename) as connection:
                cursor = connection.cursor()
                cursor.execute(query, values)
                result = cursor.fetchall()
                connection.commit()
        except Error as e:
            print(f'DATABASE ERROR: {e}')
            return None
        return result

    def printStatus(self):
        result_solo = self.executeQuery("SELECT * FROM solo;")
        result_duo = self.executeQuery("SELECT * FROM duo;")
        if result_solo is None or result_duo is None:
            return False
        print('DATABASE STATUS:')
        print('Table solo:')
        for row in result_solo:
            print(row)
        print('Table duo:')
        for row in result_duo:
            print(row)

    def getHighScore(self, username, mode):
        query = f"SELECT * FROM {mode} WHERE username=?;"
        result = self.executeQuery(query, (username,))
        if result is None:
            print(f'DATABASE ERROR: could not query current high score of username {username}, mode {mode}')
            return None
        return result[0][1] if result else None

    def submitHighScore(self, username, mode, score):
        if not all(isinstance(arg, (str, int)) for arg in (username, mode, score)):
            print('DATABASE ERROR: invalid arguments to insert high score')
            return False
        current_score = self.getHighScore(username, mode)
        if current_score is None:
            query = f"INSERT INTO {mode} (username, high) VALUES (?, ?);"
            self.executeQuery(query, (username, score))
        elif score > current_score:
            query = f"UPDATE {mode} SET high=? WHERE username=?;"
            self.executeQuery(query, (score, username))
        self.printStatus()
        return True

    def getScores(self, mode):
        query = f"SELECT * FROM {mode} ORDER BY high DESC;"
        return self.executeQuery(query)
