
#Importação das bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from matplotlib.typing import LineStyleType

from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay

from xgboost import XGBClassifier

def random_forest(obesity):

    #Tratameto dos dados
    obesity['condition'] = obesity['Obesity'].str.contains('Obesity', case=False, na=False).astype(int)

    obesity['Age'] = obesity['Age'].astype(int)
    obesity['FCVC'] = obesity['FCVC'].astype(int)
    obesity['NCP'] = obesity['NCP'].astype(int)
    obesity['CH2O'] = obesity['CH2O'].astype(int)
    obesity['FAF'] = obesity['FAF'].astype(int)
    obesity['TUE'] = obesity['TUE'].astype(int)
    obesity['Height_roud'] = obesity['Height'].round(1)
    obesity['Weight_round'] = obesity['Weight'].round(1)


    #Seleção das colunas
    df_obesity = obesity[['Age','Weight_round','family_history','FAVC','CAEC','SMOKE','FAF','condition']]

    df_obesity['family_history'] = obesity['family_history'].str.contains('yes', case=False, na=False).astype(int)
    df_obesity['FAVC'] = obesity['FAVC'].str.contains('yes', case=False, na=False).astype(int)
    df_obesity['SMOKE'] = obesity['SMOKE'].str.contains('yes', case=False, na=False).astype(int)

    df_obesity['CAEC'] = df_obesity['CAEC'].replace({'no': 0, 'Sometimes': 1,'Frequently':2,'Always':3})
    

    encoder = OneHotEncoder(sparse_output=False)
    encoded = encoder.fit_transform(df_obesity[['CAEC']])

    # Transforma em DataFrame com nomes das colunas
    df_encoded = pd.DataFrame(encoded, columns=encoder.get_feature_names_out(['CAEC']))

    # Junta com o DataFrame
    df_obesity = pd.concat([df_obesity.drop(columns=['CAEC']), df_encoded.drop(columns=['CAEC_3'])], axis=1)


    # Separação em treino e teste
    x = df_obesity.drop(columns=['condition'])
    y = df_obesity['condition']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30)


    #Modelo
    # Criar e treinar o modelo
    model_rf = RandomForestClassifier(random_state=42)
    model_rf.fit(x_train, y_train)

    # Fazer previsões
    y_pred = model_rf.predict(x_test)

    return 'teste'