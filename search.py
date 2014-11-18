
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
