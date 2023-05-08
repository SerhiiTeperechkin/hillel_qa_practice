import unittest
from recordbook import Record, Directory


class TestRecord(unittest.TestCase):
    def test_init(self):
        r = Record('John', '123456')
        self.assertEqual(r.name, 'John')
        self.assertEqual(r.surname, '')
        self.assertEqual(r.phone, '123456')
        self.assertEqual(r.birth_date, '')

        r = Record('John', '123456', 'Doe', '1990-01-01')
        self.assertEqual(r.name, 'John')
        self.assertEqual(r.surname, 'Doe')
        self.assertEqual(r.phone, '123456')
        self.assertEqual(r.birth_date, '1990-01-01')

    def test_str(self):
        r = Record('John', '123456', 'Doe', '1990-01-01')
        self.assertEqual(str(r), 'John Doe 123456 1990-01-01')


class TestDirectory(unittest.TestCase):
    def test_init(self):
        d = Directory()
        self.assertEqual(len(d.records), 3)

    def test_add_record(self):
        d = Directory()
        d.add_record('John', '123456')
        self.assertEqual(len(d.records), 4)
        self.assertEqual(d.records[-1].name, 'John')
        self.assertEqual(d.records[-1].surname, '')
        self.assertEqual(d.records[-1].phone, '123456')
        self.assertEqual(d.records[-1].birth_date, '')

    def test_remove_record(self):
        d = Directory()
        d.remove_record(0)
        self.assertEqual(len(d.records), 3)

        # Emergency services cannot be removed
        d.remove_record(2)
        self.assertEqual(len(d.records), 3)

    def test_edit_record(self):
        d = Directory()
        d.edit_record(0, 'Jane', '654321', 'Doe', '1990-01-01')
        self.assertEqual(d.records[0].name, 'Jane')
        self.assertEqual(d.records[0].surname, 'Doe')
        self.assertEqual(d.records[0].phone, '654321')
        self.assertEqual(d.records[0].birth_date, '1990-01-01')

        # Emergency services cannot be edited
        d.edit_record(2, 'Fire department', '101', '', '')
        self.assertEqual(d.records[2].name, 'Fire department')
        self.assertEqual(d.records[2].phone, '101')


if __name__ == '__main__':
    unittest.main()
