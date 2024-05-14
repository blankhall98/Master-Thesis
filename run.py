# Import Local Modules
from scripts.modules import API
from data.data import data_inputs

# Inputs
### (This might be a dictionary in a different file that must be imported)
inputs = {
    'world': {
        'sample_countries': ['Argentina','Chile','Mexico']
    },
    'data': data_inputs
}

# Initiaize app
app = API(inputs)

# Run application
if __name__ == '__main__':
    app.run()
    