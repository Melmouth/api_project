import joblib

def load_model(model_path:str = 'model.pkl'):
    model = joblib.load(model_path)
    return model