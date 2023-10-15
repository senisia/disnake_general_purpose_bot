import sqlite3
conn = sqlite3.connect(database='C:\\coding\\python\\kl\\kl_disnake_tools_bot\\utils\\sqlite3\\dbs\\users.db')

def increase_currency(id):
    cursor = conn.cursor()
    sql_query = """--sql
        UPDATE users
        SET user_xp = user_xp + 10
        WHERE user_id = (?);
    """
    cursor.execute(sql_query,(id,))
    conn.commit()
    return cursor.fetchall()

def get_user_xp_by_id(id):
    cursor = conn.cursor()
    sql_query = """--sql
        SELECT user_xp
        FROM users
        WHERE user_id = (?)
    """
    cursor.execute(sql_query, (id,))
    result = cursor.fetchone()

    if result:
        return result[0]
    else:
        return None


def check_user_id_exists(id):
    cursor = conn.cursor()
    sql_query = """--sql
        SELECT 1 FROM users WHERE user_id = ?
    """
    cursor.execute(sql_query, (id,))
    result = cursor.fetchone()
    return result is not None