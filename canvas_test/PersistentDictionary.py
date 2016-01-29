import os
import uuid
import sqlite3
import cPickle as pickle

class PersistentDictionary(object):
    """
    A sqlite based key,value storage.
    The value can be any pickleable object.
    Similar interface to Python dict
    Supports the GLOB syntax in methods keys(),items(), __delitem__()
    Usage Example:
    >>> p = PersistentDictionary(path='test.sqlite')
    >>> key = 'test/' + p.uuid()
    >>> p[key] = {'a': 1, 'b': 2}
    >>> print p[key]
    {'a': 1, 'b': 2}
    >>> print len(p.keys('test/*'))
    1
    >>> del p[key]
    """

    CREATE_TABLE = "CREATE TABLE persistence (pkey, pvalue)"
    SELECT_KEYS = "SELECT pkey FROM persistence WHERE pkey GLOB ?"
    SELECT_VALUE = "SELECT pvalue FROM persistence WHERE pkey GLOB ?"
    INSERT_KEY_VALUE = "INSERT INTO persistence(pkey, pvalue) VALUES (?,?)"
    DELETE_KEY_VALUE = "DELETE FROM persistence WHERE pkey LIKE ?"
    SELECT_KEY_VALUE = "SELECT pkey,pvalue FROM persistence WHERE pkey GLOB ?"

    def __init__(self,
                 path='persistence.sqlite',
                 autocommit=True):
        self.path = path
        self.autocommit = autocommit
        create_table = not os.path.exists(path)
        self.connection  = sqlite3.connect(path)
        self.connection.text_factory = str # do not use unicode
        self.cursor = self.connection.cursor()
        if create_table:
            self.cursor.execute(self.CREATE_TABLE)
            self.connection.commit()

    def uuid(self):
        return str(uuid.uuid4())

    def keys(self,pattern='*'):
        "returns a list of keys filtered by a pattern, * is the wildcard"
        self.cursor.execute(self.SELECT_KEYS,(pattern,))
        return [row[0] for row in self.cursor.fetchall()]

    def __contains__(self,key):
        return True if self[key] else False

    def __iter__(self):
        for key in self:
            yield key

    def __setitem__(self,key,value):
        if value is None:
            del self[key]
            return
        self.cursor.execute(self.INSERT_KEY_VALUE,
                            (key, pickle.dumps(value)))
        if self.autocommit: self.connection.commit()

    def __getitem__(self,key):
        self.cursor.execute(self.SELECT_VALUE, (key,))
        row = self.cursor.fetchone()
        return pickle.loads(row[0]) if row else None

    def __delitem__(self,pattern):
        self.cursor.execute(self.DELETE_KEY_VALUE, (pattern,))
        if self.autocommit: self.connection.commit()

    def items(self,pattern='*'):
        self.cursor.execute(self.SELECT_KEY_VALUE, (pattern,))
        return [(row[0],pickle.loads(row[1])) \
                    for row in self.cursor.fetchall()]
