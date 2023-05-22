import unittest
from recordbook import Record, Directory


class RecordTestCase(unittest.TestCase):
    def test_valid_record(self):
        record = Record("John", "1234567890")
        self.assertEqual(record.name, "John")
        self.assertIsNone(record.surname)
        self.assertEqual(record.phone, "1234567890")
        self.assertIsNone(record.date_of_birth)

    def test_valid_record_with_optional_fields(self):
        record = Record("John", "1234567890", "Doe", "1990-01-01")
        self.assertEqual(record.name, "John")
        self.assertEqual(record.surname, "Doe")
        self.assertEqual(record.phone, "1234567890")
        self.assertEqual(record.date_of_birth, "1990-01-01")

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            Record("John1", "1234567890")

    def test_invalid_phone(self):
        with self.assertRaises(ValueError):
            Record("John", "12345a67890")

    def test_invalid_date_of_birth(self):
        with self.assertRaises(ValueError):
            Record("John", "1234567890", "Doe", "1990-01-xx")


class DirectoryTestCase(unittest.TestCase):
    # [FIXED] Повторяющееся создание записи в тесте должно быть вынесено в setUp метод
    def setUp(self):
        self.directory = Directory()

    def test_initial_records(self):
        records = self.directory.get_all_records()
        self.assertEqual(len(records), 3)

    def test_add_record(self):
        record = Record("Test", "9876543210")
        self.directory.add_record(record)
        records = self.directory.get_all_records()
        self.assertEqual(len(records), 4)
        self.assertIn(record, records)

    def test_remove_record(self):
        record = self.directory.get_all_records()[0]
        self.directory.remove_record(record)
        records = self.directory.get_all_records()
        self.assertEqual(len(records), 2)
        self.assertNotIn(record, records)

    def test_remove_nonexistent_record(self):
        record = Record("Nonexistent", "9999999999")
        with self.assertRaises(ValueError):
            self.directory.remove_record(record)

    def test_edit_record(self):
        record = self.directory.get_all_records()[0]
        new_name = "New Name"
        new_surname = "New Surname"
        new_phone = "1111111111"
        new_date_of_birth = "1990-02-02"
        self.directory.edit_record(record, new_name, new_surname, new_phone, new_date_of_birth)
        updated_record = self.directory.get_all_records()[0]
        self.assertEqual(updated_record.name, new_name)
        self.assertEqual(updated_record.surname, new_surname)
        self.assertEqual(updated_record.phone, new_phone)
        self.assertEqual(updated_record.date_of_birth, new_date_of_birth)


if __name__ == "__main__":
    unittest.main()
