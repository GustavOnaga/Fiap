
import streamlit as st
import pandas as pd
from graficos import family_history, favc
from train.ml import random_forest



st.set_page_config('Tech Challange 04')


st.title('Tech Challange 04')
st.subheader('Tech Challange 04')


file_upload = st.file_uploader(label = 'Faça o upload da base de treino para o modelo de machine learning: ', type = ['csv'])

if file_upload:
    
  #Leitura dos dados
  df = pd.read_csv(file_upload)
  expa1 = st.expander('Base de treino')  
  expa1.dataframe(df,hide_index= True)

  with st.expander('Análises'):
      
    tab_family_history,tab_fav = st.tabs(['Historico familiar','Fav'])

    with tab_family_history:
      
      st.write('Relação entre histórico familiar e condição de obesidade')
      plt = family_history(df)  # chama a função do outro arquivo
      st.pyplot(plt)  # exibe o gráfico no Streamlit

    with tab_fav:
      
      st.write('Relação fav e condição de obesidade')
      plt = favc(df)  # chama a função do outro arquivo
      st.pyplot(plt)  # exibe o gráfico no Streamlit

  st.markdown("""
  ----
    #### Aplicação do algoritmo de Machine learning
    ##### Selecione os parametros do paciente para obter um pré diagnostico para a pré disposição para a obesidade:  

  """)
  
  #Botões
  age = st.slider('Idade do paciente:',
              min_value=int(df['Age'].min()),
              max_value=int(df['Age'].max()),
              value=int(df['Age'].min()))   
  
  Weight= st.slider('Altura do paciente [cm]:',
              min_value=float(df['Weight'].min()),
              max_value=float(df['Weight'].max()),
              value=float(df['Weight'].min()))    
  
  FAF = st.select_slider('FAF: ',
                    options = df['FAF'].unique().tolist())

  col1,col2 = st.columns(2)

  with col1:
      family_history = st.selectbox('Possui historico familiar de obsidade: ' ,
                                      options = df['family_history'].unique().tolist())
  
      favc = st.selectbox('FAVC: ' ,
                              options = df['FAVC'].unique().tolist())
  
  with col2:
      caec = st.selectbox('CAEC: ' ,
                          options = df['CAEC'].unique().tolist())
  
      smoke = st.selectbox('O paciente é fumante: ',
                            options = df['SMOKE'].unique().tolist())
  
  x = random_forest(df)
  print(x)


