import requests


api_keys = {'client_id': 'MT3VHUDOIPPIF00TPOEMOUOV550MISJG21TM0U2RUZZP42XD',
            'client_secret': 'FZI4HLHMZ1U0IKFSHESG2BLAFMOPSU1T2XUMDIAKCWV0FO3C',
            'v': '20141101',
            }

categories = {'elementary_school': '4f4533804b9074f6e4fb0105',
              'high_school': '4bf58dd8d48988d13d941735',
              'bus_station': '4bf58dd8d48988d1fe931735',
              'college_university': '4d4b7105d754a06372d81259',
              'train_station': '4bf58dd8d48988d129951735',
              'light_rail': '4bf58dd8d48988d1fc931735',
              'mall': '4bf58dd8d48988d1fd941735',
              'petrol_station': '4bf58dd8d48988d113951735',
              'gym_fitness': '4bf58dd8d48988d175941735',
              'atm': '52f2ab2ebcbc57f1066b8b56'
              }


class Category(object):

    def __init__(self, name):
        if name not in categories:
            Exception()
        else:
            self.name = name
            self.id = categories[name]

    def full_results(self, latlong, radius, topfive=False):
        full_results = []
        initial_results = self.initial_results(latlong, radius)

        if topfive is True:
            initial_results = self.select_top_five(initial_results)

        initial_results.sort(key=lambda x: x.distance)

        for venue in initial_results:
            full_results.append(Venue(venue.id, venue.distance))

        return full_results

    def select_top_five(self, venues):
        if len(venues) > 5:
            venues = venues[0:5]
        return venues

    def initial_results(self, latlong, radius):
        response_from_api = self.search(latlong, radius)
        venues = self.extract_matches(response_from_api.json())
        venues.sort(key=lambda x: x.users_count)
        return venues

    def search(self, latlong, radius):
        parameters = {'categoryId': self.id,  'll': latlong, 'radius': radius}
        parameters.update(api_keys)

        response = requests.get('https://api.foursquare.com/v2/venues/search?', params=parameters)
        return response

    def number_of_matches(self, json):
        return len(json['response']['venues'])

    def extract_matches(self, json):
        venues = []
        for index in range(self.number_of_matches(json)):
            venues.append(Venue(json['response']['venues'][index]['id'],
                                distance=json['response']['venues'][index]['location']['distance'],
                                users_count=json['response']['venues'][index]['stats']['usersCount'],
                                prefetch=False)
                          )
        return venues


class Venue(object):

    def __init__(self, id_, distance=None, users_count=None, prefetch=True):
        self.id = id_
        self.distance = distance
        self.users_count = users_count

        if prefetch is True:
            self.response = self.fetch_info()
            self.url = self.get_venue_url(self.response.json())
            self.photo_url_thumb = self.get_photo_url(self.response.json(), "128")
            self.photo_url_full = self.get_photo_url(self.response.json())
            self.name = self.get_name(self.response.json())

    def fetch_info(self):
        response = requests.get('https://api.foursquare.com/v2/venues/' + self.id, params=api_keys)
        return response

    def get_venue_url(self, json):
        return json['response']['venue']['canonicalUrl']

    def get_photo_url(self, json, dimension=None):
        try:
            prefix = json['response']['venue']['photos']['groups'][0]['items'][0]['prefix']
            suffix = json['response']['venue']['photos']['groups'][0]['items'][0]['suffix']

        except IndexError:
            return "http://placehold.it/128&text=no.photo"

        if dimension is None:
            return prefix + "original" + suffix
        else:
            return prefix + dimension + suffix

    def get_name(self, json):
        return json['response']['venue']['name']
