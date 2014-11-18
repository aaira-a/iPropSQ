import unittest
from search import Category, Venue


class CategoryTest(unittest.TestCase):

    def test_category_class_instantiation_using_myparams_dict_should_pass(self):
        high_school_category = Category('high_school')
        self.assertIsInstance(high_school_category, Category)

    def test_category_class_should_save_name_and_id(self):
        bus_station_category = Category('bus_station')
        self.assertEqual(bus_station_category.name, 'bus_station')
        self.assertEqual(bus_station_category.id, '4bf58dd8d48988d1fe931735')

    def test_category_class_should_raise_exception_if_category_does_not_exist_in_dict(self):
        undefined_category = Category('undefined')
        self.assertRaises(Exception, undefined_category)


class VenueTest(unittest.TestCase):

    def test_venue_class_instantiation_using_id_should_pass(self):
        myvenue = Venue('4bd69f68637ba5939977f870')
        self.assertIsInstance(myvenue, Venue)

    def test_venue_class_should_save_id(self):
        myvenue = Venue('4bd69f68637ba5939977f870')
        self.assertEqual(myvenue.id, '4bd69f68637ba5939977f870')


if __name__ == '__main__':
    unittest.main()
