import _pickle as pickle

with open('./model.pkl', 'rb') as file:
    model = pickle.load(file)
    model.predict()

