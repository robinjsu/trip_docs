model_backend = 'datastore'

if model_backend == 'datastore':
    from .model_backend import model
else:
    raise ValueError("No appropriate databackend configured. ")

appmodel = model()

def get_model():
    return appmodel
