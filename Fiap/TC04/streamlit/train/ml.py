# Importação das bibliotecas
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def random_forest(obesity,age=None,Height=None,family_history=None,favc=None,caec=None,smoke=None,scc=None,faf=None):

    df_obesity = obesity.copy()

    df_obesity['condition'] = (df_obesity['Obesity'].str.contains('Obesity', case=False, na=False).astype(int))

    df_obesity['Age'] = df_obesity['Age'].astype(int)
    df_obesity['Height_round'] = df_obesity['Height'].round(1)

    df_obesity['family_history'] = (df_obesity['family_history'].str.contains('yes', case=False, na=False).astype(int))

    df_obesity['FAVC'] = (df_obesity['FAVC'].str.contains('yes', case=False, na=False).astype(int))

    df_obesity['CAEC'] = df_obesity['CAEC'].replace({'no': 0,'Sometimes': 1,'Frequently': 2,'Always': 3})

    df_obesity['SMOKE'] = (df_obesity['SMOKE'].str.contains('yes', case=False, na=False).astype(int))

    df_obesity['SCC'] = (df_obesity['SCC'].str.contains('yes', case=False, na=False).astype(int))

    df_obesity['FAF'] = df_obesity['FAF'].astype(int)

    # Seleção de colunas
    df_obesity = df_obesity[['Age', 'Height_round', 'family_history', 'FAVC','CAEC', 'SMOKE','SCC' ,'FAF', 'condition']]

    # One-Hot Encoding
    encoder = OneHotEncoder(sparse_output=False)
    encoded = encoder.fit_transform(df_obesity[['CAEC']])

    df_encoded = pd.DataFrame(encoded,columns=encoder.get_feature_names_out(['CAEC']))

    # Remove uma categoria para evitar multicolinearidade
    df_obesity = pd.concat([df_obesity.drop(columns=['CAEC']),df_encoded.drop(columns=['CAEC_3'])],axis=1)

    # Treino e teste
    X = df_obesity.drop(columns=['condition'])
    y = df_obesity['condition']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.30, random_state=42
    )

    # Modelo
    model_rf = RandomForestClassifier(random_state=42)
    model_rf.fit(X_train, y_train)

    acc = accuracy_score(y_test, model_rf.predict(X_test))

    # Previsão para novo paciente
    pred = None
    if all(param is not None for param in [age, Height,family_history, favc, caec,scc, smoke,faf]):

        novo_paciente = pd.DataFrame([{
            'Age': age,
            'Height_round': round(Height, 1),
            'FAF': faf,
            'family_history': 1 if str(family_history).lower() == 'yes' else 0,
            'FAVC': 1 if str(favc).lower() == 'yes' else 0,
            'SMOKE': 1 if str(smoke).lower() == 'yes' else 0,
            'CAEC': caec,
            'scc': 1 if str(scc).lower() == 'yes' else 0,

        }])

        novo_paciente['CAEC'] = novo_paciente['CAEC'].replace({
            'no': 0,
            'Sometimes': 1,
            'Frequently': 2,
            'Always': 3
        })

        encoded_new = encoder.transform(novo_paciente[['CAEC']])
        df_encoded_new = pd.DataFrame(
            encoded_new,
            columns=encoder.get_feature_names_out(['CAEC'])
        )

        novo_paciente = pd.concat(
            [novo_paciente.drop(columns=['CAEC']),
             df_encoded_new.drop(columns=['CAEC_3'], errors='ignore')],
            axis=1
        )

        novo_paciente = novo_paciente.reindex(
            columns=X.columns,
            fill_value=0
        )

        resultado = int(model_rf.predict(novo_paciente)[0])

        pred = (
            'Possui predisposição para obesidade'
            if resultado == 1
            else 'Não possui predisposição para obesidade'
        )

    return {
        'predicao': pred,
        'acuracia': acc
    }
