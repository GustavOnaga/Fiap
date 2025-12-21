
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

def random_forest(obesity,age=None, weight=None, faf=None, family_history=None, favc=None, caec=None, smoke=None):

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

    # Avaliação da acuracia
    acc = accuracy_score(y_test, model_rf.predict(x_test))

# Previsão para novo paciente (se parâmetros forem informados)
    pred = None
    if all(param is not None for param in [age, weight, faf, family_history, favc, caec, smoke]):

        novo_paciente = pd.DataFrame([{
            'Age': age,
            'Weight_round': round(weight, 1),
            'FAF': faf,
            'family_history': 1 if str(family_history).lower() == 'yes' else 0,
            'FAVC': 1 if str(favc).lower() == 'yes' else 0,
            'SMOKE': 1 if str(smoke).lower() == 'yes' else 0,
            'CAEC': caec
        }])

        # One-hot encoding da coluna CAEC do novo paciente

        novo_paciente['CAEC'] = novo_paciente['CAEC'].replace({'no': 0, 'Sometimes': 1,'Frequently':2,'Always':3})

        encoded_new = encoder.transform(novo_paciente[['CAEC']])
        df_encoded_new = pd.DataFrame(encoded_new, columns=encoder.get_feature_names_out(['CAEC']))

        novo_paciente = pd.concat([novo_paciente.drop(columns=['CAEC']), df_encoded_new.drop(columns=['CAEC_3'], errors='ignore')], axis=1)

        # Garante que o novo paciente tenha as mesmas colunas do treino
        novo_paciente = novo_paciente.reindex(columns=x.columns, fill_value=0)

        # Predição

        pred = 'Possui pré disposição para a obesidade' if int(model_rf.predict(novo_paciente)[0]) == 0 else 'Não possui pré disposição para a obesidade'

    return {'predicao': pred, 'acuracia': acc}