import unittest

from db_handler import DBHandler


class TestDBHandler(unittest.TestCase):
    def setUp(self) -> None:
        self.db = DBHandler(":memory:")

    def test_create_plate(self):
        self.db.create_plate("test")

        plates = self.db.list_plates()

        self.assertEqual(len(plates), 1)
        self.assertIn("test", plates)
    
    def test_delete_plate(self):
        self.db.create_plate("test")
        self.db.delete_plate("test")

        plates = self.db.list_plates()

        self.assertEqual(len(plates), 0, msg=f"The following list should be empty: {plates}")
    
    def test_update_plate(self):
        self.db.create_plate("test")
        self.db.update_plate("test", "new_test")

        plates = self.db.list_plates()
        self.assertEqual(len(plates), 1)
        self.assertNotIn("test", plates)
        self.assertIn("new_test", plates)


if __name__ == '__main__':
    unittest.main()
