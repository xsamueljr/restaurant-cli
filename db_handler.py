import sqlite3

# Custom exceptions
class PlateNotFound(Exception):
    pass


class DBHandler:

    def __init__(self, database: str = "data.db") -> None:
        """
        Creates the database if it doesn't exist
        :param database: database path
        """
        self.con = sqlite3.connect(database)
        self.__create_table()
    
    def __create_table(self) -> None:
        cursor = self.con.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS plates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                plate TEXT NOT NULL
            )
        """)
        self.con.commit()
        cursor.close()

    def list_plates(self) -> list[str]:
        cursor = self.con.cursor()
        cursor.execute("SELECT plate FROM plates")
        plates = [row[0] for row in cursor.fetchall()]
        cursor.close()
        return plates
    
    def create_plate(self, plate: str) -> None:
        cursor = self.con.cursor()
        cursor.execute("INSERT INTO plates (plate) VALUES (?)", (plate,))
        self.con.commit()
        cursor.close()
    
    def find_plate(self, plate: str) -> bool:
        cursor = self.con.cursor()
        result = cursor.execute("SELECT plate FROM plates WHERE plate = ?", (plate,)).fetchone()
        cursor.close()

        return result is not None
    
    def delete_plate(self, plate: str) -> None:
        if not self.find_plate(plate):
            raise PlateNotFound()

        cursor = self.con.cursor()
        cursor.execute("DELETE FROM plates WHERE plate = ?", (plate, ))
        self.con.commit()
        cursor.close()
    
    def update_plate(self, old_plate: str, new_plate: str) -> None:
        if not self.find_plate(old_plate):
            raise PlateNotFound()

        cursor = self.con.cursor()
        cursor.execute("UPDATE plates SET plate = ? WHERE plate = ?", (new_plate, old_plate))
        self.con.commit()
        cursor.close()
