import sqlite3
from flask import current_app, g


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(current_app.config['DATABASE'],
                               detect_types=sqlite3.PARSE_DECLTYPES
                               )
        g.db.row_factory = sqlite3.Row
    return g.db


class DatabaseObject:
    def __init__(self):
        super(DatabaseObject, self).__init__()
        self.db = None
        self.app = None
        self.cursor = None

    def init_db(self):
        self.db = get_db()
        with current_app.open_resource('db/schema.sql') as f:
            self.db.executescript(f.read().decode('utf8'))

    def close_db(self, e=None):
        self.db = g.pop('db', e)
        if self.db is not e:
            self.db.close()

    def get_objects_from_table(self, table):
        cursor = self.db.cursor()
        cursor.execute(f'select * from {table}')
        objects = []
        for row in cursor:
            objects.append(row)
        return objects

    def add_object_to_table(self, table, *args):
        cursor = self.db.cursor()
        argValues = str()
        if len(args) > 1:
            for arg in range(len(args)):
                if arg + 1 != len(args):
                    argValues += '?,'
                else:
                    argValues += '?'
        else:
            argValues += '?'

        cursor.execute(f'INSERT INTO {table}(name,password) VALUES({argValues})', *args)
        self.db.commit()
