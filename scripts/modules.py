#Modules
import time

#Class: Country
class Country:

    def __init__(self,country_name):
        self.name = country_name

    #Load country's data
    def load_country(self):
        print(self.name)

# Class: World
class World:

    def __init__(self,data,inputs):
        self.inputs = inputs
        self.data = data
        self.load_sample()

    #Load sample of countries and load their data
    def load_sample(self):
        print('Loading Sample Countries')
        t = time.time()
        self.countries = {}
        for country in self.inputs['sample_countries']:
            self.countries[country] = Country(country)
            self.countries[country].load_country()
        print(f'Sample Countries Loaded - Loading Time: {time.time()-t}')

# Class: Routes
class Data:

    def __init__(self,inputs):
        self.inputs = inputs

# Class: Model
class Model:

    def __init__(self,inputs):
        self.inputs = inputs
        self.load_data()
        self.load_world()

    def load_data(self):
        print('Loading Data')
        t = time.time()
        self.data = Data(self.inputs)
        print(f'Data Loaded - Loading Time: {time.time()-t}')

    def load_world(self):
        print('Loading World')
        t = time.time()
        self.world = World(self.data,self.inputs['world'])
        print(f'World Loaded - Loading Time: {time.time()-t}')

# Class: API
class API:

    def __init__(self,inputs):
        self.inputs = inputs

    def run(self):
        #Greeting
        self.greeting()
        #start model instance, with inputs for model
        self.start_model()
        #start interaction
        self.start_interaction()

    def start_model(self):
        #Start Model
        print('Starting Model')
        t = time.time()
        self.model = Model(self.inputs)
        print(f'Model Loaded - Loading Time: {time.time()-t}')

    ### Interaction Functions

    #Print a straight line with dashes
    def print_line(self):
        print('\n'+'--------------------------------------------'+ '\n')

    #First greeting for first starting the API
    def greeting(self):
        self.print_line()
        print('Welcome, this is the API for the model!'+'\n'+'I will load the model, and then you will be able to interact with it through me.')
        self.print_line()

    #Start interaction with the API after the Model is loaded
    def start_interaction(self):
        self.print_line()
        print('The model is now loaded, you can interact with it through me using the API menu.')
        self.print_line()
