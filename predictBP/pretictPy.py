import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
from joblib import dump, load

class modelPredictMatrix:
    model = load_model(r'predictBP\model_NN_best')

class modelPredictModul:
    model = load(r'predictBP\model_reg\RandomForestRegressor.joblib')

def predict(params, method):
    list_param = []
    if get_params(params, list_param, method):
        if method == 'matrix':
            return modelPredictMatrix.model.predict(list_param)[0][0]
        else:
            return modelPredictModul.model.predict([list_param])[0]
    else:
        return 'Некорретный ввод данных!'

def get_params(params, list_param, method):

    try:

        if method == 'matrix': 
            list_param.append(int(params['plotnost']))
            list_param.append(int(params['modulUprugosti']))
            list_param.append(int(params['poverhPlotn']))
            list_param.append(int(params['modulUprugostiRast']))
            list_param.append(int(params['prochnRast']))
            list_param.append(int(params['shagNash']))
            list_param.append(int(params['plotNash']))   
            list_param.append(int(params['poverhPlotn'])/int(params['plotnost']))
        else:
            list_param.append(float(params['matr']))
            list_param.append(int(params['plotnost']))
            list_param.append(int(params['modulUprugosti']))
            list_param.append(int(params['poverhPlotn'])) 
            list_param.append(int(params['shagNash']))
            list_param.append(int(params['plotNash']))   
            list_param.append(int(params['poverhPlotn'])/int(params['plotnost']))
    except:
        return False

    return True
