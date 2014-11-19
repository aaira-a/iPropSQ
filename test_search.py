import unittest
from search import Category, Venue
import json


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

    @unittest.skip("minimise number of api calls")
    def test_search_api_call_using_lat_long_should_return_200(self):
        latlong = '3.1175,101.6773'
        radius = '1000'
        response = Category('train_station').search(latlong, radius)
        self.assertEqual(response.status_code, 200)

    def test_number_of_matches_method_should_return_correct_venue_number_from_json(self):
        category = Category('elementary_school')
        with open("fixtures/test_category_search.json") as json_file:
            json_loaded = json.load(json_file)
            self.assertEqual(category.number_of_matches(json_loaded), 3)


class VenueTest(unittest.TestCase):

    def test_venue_class_instantiation_using_id_should_pass(self):
        myvenue = Venue('4bd69f68637ba5939977f870')
        self.assertIsInstance(myvenue, Venue)

    def test_venue_class_should_save_id(self):
        myvenue = Venue('4bd69f68637ba5939977f870')
        self.assertEqual(myvenue.id, '4bd69f68637ba5939977f870')

    @unittest.skip("minimise number of api calls")
    def test_venue_fetch_info_should_return_200(self):
        myvenue = Venue('4cb7c677a33bb1f76f687cfd')
        self.assertEqual(myvenue.fetch_info().status_code, 200)

    def test_venue_fetch_info_should_return_url_from_json(self):
        myvenue = Venue('4cb7c677a33bb1f76f687cfd')
        expected_url = 'https://foursquare.com/v/sekolah-kebangsaan-bangsar/4cb7c677a33bb1f76f687cfd'
        with open("fixtures/test_venue_details.json") as json_file:
            json_loaded = json.load(json_file)
            self.assertEqual(myvenue.get_venue_url(json_loaded), expected_url)

    def test_venue_get_photo_should_return_photo_url_from_json(self):
        myvenue = Venue('4cb7c677a33bb1f76f687cfd')
        expected_photo_url = 'https://irs0.4sqi.net/img/general/original/6586420_CMoiV9Fy5EwoFxKuRfm2n_u7MQ86rrHuURB0NwGbV6k.jpg'
        with open("fixtures/test_venue_details.json") as json_file:
            json_loaded = json.load(json_file)
            self.assertEqual(myvenue.get_photo_url(json_loaded), expected_photo_url)


if __name__ == '__main__':
    unittest.main()
