import requests


api_keys = {'client_id': 'MT3VHUDOIPPIF00TPOEMOUOV550MISJG21TM0U2RUZZP42XD',
            'client_secret': 'FZI4HLHMZ1U0IKFSHESG2BLAFMOPSU1T2XUMDIAKCWV0FO3C',
            'v': '20141101',
            }

categories = {'elementary_school': '4f4533804b9074f6e4fb0105',
              'high_school': '4bf58dd8d48988d13d941735',
              'bus_station': '4bf58dd8d48988d1fe931735',
              'train_station': '4bf58dd8d48988d129951735',
              'light_rail': '4bf58dd8d48988d1fc931735',
              }


class Category(object):

    def __init__(self, name):
        if name not in categories:
            Exception()
        else:
            self.name = name
            self.id = categories[name]

    def search(self, latlong, radius):
        parameters = {'categoryId': self.id,  'll': latlong, 'radius': radius}
        parameters.update(api_keys)

        response = requests.get('https://api.foursquare.com/v2/venues/search?', params=parameters)
        return response

    def number_of_matches(self, json):
        return len(json['response']['venues'])


class Venue(object):

    def __init__(self, id_, prefetch=True):
        self.id = id_
        if prefetch is True:
            self.response = self.fetch_info()
            self.url = self.get_venue_url(self.response.json())
            self.photo_url = self.get_photo_url(self.response.json())

    def fetch_info(self):
        response = requests.get('https://api.foursquare.com/v2/venues/' + self.id, params=api_keys)
        return response

    def get_venue_url(self, json):
        return json['response']['venue']['canonicalUrl']

    def get_photo_url(self, json):
        prefix = json['response']['venue']['photos']['groups'][0]['items'][0]['prefix']
        suffix = json['response']['venue']['photos']['groups'][0]['items'][0]['suffix']
        return prefix + "original" + suffix
