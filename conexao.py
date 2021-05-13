import sqlite3 as sql

class TransactionObject():
    database = "webdb.db"
    conn = None
    cur = None
    connected = False

    def initDB(self):
        trans = TransactionObject()
        trans.connect()
        trans.execute(
            "CREATE TABLE IF NOT EXISTS cadastros (id INTEGER PRIMARY KEY , codigo TEXT, nome TEXT, url TEXT)")
        trans.persist()
        trans.disconnect()

    def connect(self):
        TransactionObject.conn = sql.connect(TransactionObject.database)
        TransactionObject.cur = TransactionObject.conn.cursor()
        TransactionObject.connected = True

    def disconnect(self):
        TransactionObject.conn.close()
        TransactionObject.connected = False

    def execute(self, sql, parms=None):
        if TransactionObject.connected:
            if parms == None:
                TransactionObject.cur.execute(sql)
            else:
                TransactionObject.cur.execute(sql, parms)
            return True
        else:
            return False

    def fetchall(self):
        return TransactionObject.cur.fetchall()

    def persist(self):
        if TransactionObject.connected:
            TransactionObject.conn.commit()
            return True
        else:
            return False

    def view(self):
        trans = TransactionObject()
        trans.connect()

        trans.execute("SELECT * FROM cadastros")

        rows = trans.fetchall()
        trans.disconnect()
        return rows

    def insert(self, codigo, nome, url):
        trans = TransactionObject()
        trans.connect()
        trans.execute("INSERT INTO cadastros VALUES(NULL, ?,?,?)", (codigo, nome, url))
        trans.persist()
        trans.disconnect()

    def search(self, codigo="", nome="", url=""):
        trans = TransactionObject()
        trans.connect()
        trans.execute("SELECT * FROM cadastros WHERE codigo=? or nome=? or url=? ",
                      (codigo, nome, url))
        rows = trans.fetchall()
        trans.disconnect()
        return rows

    def update(self, id, codigo, nome, url):
        trans = TransactionObject()
        trans.connect()
        trans.execute("UPDATE cadastros SET codigo =?, nome=?, url=? WHERE id = ?",
                      (codigo, nome, url,id))
        trans.persist()
        trans.disconnect()

    def delete(self, id):
        trans = TransactionObject()
        trans.connect()
        trans.execute("DELETE FROM cadastros WHERE id = ?", (id,))
        trans.persist()
        trans.disconnect()

dados = TransactionObject()

