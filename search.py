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
        response = requests.get('https://api.foursquare.com/v2/venues/search?' +
                                'll=' + latlong +
                                '&radius=' + radius +
                                '&categoryId=' + self.id,
                                params=api_keys)
        return response


class Venue(object):

    def __init__(self, id_):
        self.id = id_
