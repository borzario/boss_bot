import sqlite3 as sq

def db_start():
    global base, cur
    base = sq.connect("boss.db")
    cur = base.cursor()
    if base:
        print("Connected to bd is OK!")
    base.execute('CREATE TABLE IF NOT EXISTS users(user_id TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS master_at_work(master_id TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS bron(user TEXT, time TEXT, user_name TEXT)')
    base.execute('CREATE TABLE IF NOT EXISTS all_masters(id TEXT, photo TEXT, about TEXT)')
    base.commit()

async def user_add(message):
    try:
        await cur.execute("INSERT INTO users VALUES (?)", (message.from_user.id,))
    except:
        pass
    base.commit()

async def set_master(message):
    try:
        await cur.execute("INSERT INTO master_at_work VALUES (?)", (message.from_user.id,))
    except:
        pass
    base.commit()

async def master():
    nobr = cur.execute("SELECT MAX(ROWID) FROM master_at_work").fetchall()
    tobr = cur.execute(f"SELECT master_id FROM master_at_work WHERE ROWID == {nobr[0][0]} ").fetchall()
    photo = cur.execute(f"SELECT photo FROM all_masters WHERE id == {tobr[0][0]} ").fetchall()
    about = cur.execute(f"SELECT about FROM all_masters WHERE id == {tobr[0][0]} ").fetchall()
    return (tobr[0][0], photo[0][0], about[0][0])

async def bron(message):
    cur.execute("INSERT INTO bron VALUES (?, ?, ?)", (message.from_user.id, message.text, message.from_user.username))
    base.commit()
    nobr = cur.execute("SELECT MAX(ROWID) FROM bron").fetchall()
    tobr = cur.execute(f"SELECT time FROM bron WHERE ROWID == {int(nobr[0][0])} ").fetchall()
    uobr = cur.execute(f"SELECT user FROM bron WHERE ROWID == {int(nobr[0][0])} ").fetchall()
    name = cur.execute(f"SELECT user_name FROM bron WHERE ROWID == {int(nobr[0][0])} ").fetchall()
    return (nobr, tobr, uobr, name)

async def bronselect(message):
    user = cur.execute(f"SELECT user FROM bron WHERE ROWID == {message.text} ").fetchall()
    return user