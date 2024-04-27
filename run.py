from scripts.modules import Model

inputs = {
    'sample_countries': ['Argentina','Chile','Mexico'],
    'data': {}
}

app = Model(inputs)

#load world information
app.load_world()