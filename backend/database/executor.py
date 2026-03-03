from contextlib import contextmanager
from database.connection import get_connection
from core.logger import get_logger
import logging
logger = logging.getLogger(__name__)

def execute_query(
    query: str,
    params: tuple = (),
    fetchone: bool = False,
    fetchall: bool = False,
    commit: bool = False
):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(query, params)

        data = None

        if fetchone:
            data = cursor.fetchone()

        if fetchall:
            data = cursor.fetchall()

        if commit:
            conn.commit()

        return data
    except Exception as e:
        logger.error(f"Query failed: {query} | Params: {params} | Error: {e}")
        raise

    finally:
        cursor.close()
        conn.close()


@contextmanager
def get_db():
    """
    Transaction context manager.
    Commits if successful.
    Rolls back if exception occurs.
    """
    conn = get_connection()
    cursor = conn.cursor()

    try:
        yield cursor
        conn.commit()
        logger.info("Transaction committed sucessfully.")
    except Exception:
        conn.rollback()
        logger.error(f"Transaction failed. Rolled back. Error: {e}")
        raise
    finally:
        cursor.close()
        conn.close()