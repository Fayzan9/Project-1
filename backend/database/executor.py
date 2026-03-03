from database.connection import get_connection


def execute_query(
    query: str,
    params: tuple = (),
    fetchone: bool = False,
    fetchall: bool = False,
    commit: bool = False
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(query, params)

    data = None

    if fetchone:
        data = cursor.fetchone()

    if fetchall:
        data = cursor.fetchall()

    if commit:
        conn.commit()

    cursor.close()
    conn.close()

    return data