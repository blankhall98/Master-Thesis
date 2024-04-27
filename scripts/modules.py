class Country:

    def __init__(self,country_name):
        self.name = country_name

    #Load country's data
    def load_country(self):
        print(self.name)

class World:

    def __init__(self,sample_countries):
        self.countries = sample_countries
        self.sample = {}
        self.load_sample()

    #Load sample of countries and load their data
    def load_sample(self):
        for country in self.countries:
            self.sample[country] = Country(country)
            self.sample[country].load_country()


class Model:

    def __init__(self,inputs):
        self.inputs = inputs

    def load_world(self):
        self.world = World(self.inputs['sample_countries'])
