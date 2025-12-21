def render():
    import streamlit as st
    import pandas as pd
    import matplotlib.pyplot as plt
    from graficos import family_history, favc, smoke
    from train.ml import random_forest

    st.set_page_config(
        page_title='Tech Challenge 04',
        page_icon='🏥',
        layout='wide'
    )

    st.title('Tech Challenge 04')
    st.subheader('Análise da pré-disposição para obesidade')

    file_upload = st.file_uploader(
        label='Faça o upload da base de treino para o modelo de Machine Learning:',
        type=['csv']
    )

    if file_upload is not None:
        # Leitura dos dados
        df = pd.read_csv(file_upload)

        with st.expander('Base de treino'):
            st.dataframe(df, hide_index=True)

        # with st.expander('Análises'):
        #     tab_family_history, tab_fav, tab_smoke = st.tabs(
        #         ['Histórico familiar', 'FAVC', 'Smoke']
        #     )

        #     with tab_family_history:
        #         st.write('Relação entre histórico familiar e condição de obesidade')
        #         fig = family_history(df)
        #         st.pyplot(fig)
        #         plt.close(fig)
        #         plt.tight_layout()

        #     with tab_fav:
        #         st.write('Relação FAVC e condição de obesidade')
        #         fig = favc(df)
        #         st.pyplot(fig)
        #         plt.close(fig)
        #         plt.tight_layout()

        #     with tab_smoke:
        #         st.write('Relação Smoke e condição de obesidade')
        #         fig = smoke(df)
        #         st.pyplot(fig)
        #         plt.tight_layout()
        #         plt.close(fig)
        

        st.markdown("""
        ---
        #### Aplicação do algoritmo de Machine Learning
        ##### Selecione os parâmetros do paciente para obter um pré-diagnóstico
        """)

        # Sliders
        age = st.slider(
            'Idade do paciente:',
            min_value=int(df['Age'].min()),
            max_value=int(df['Age'].max()),
            value=int(df['Age'].min())
        )

        height = st.slider(
            'Altura do paciente:',
            min_value=float(df['Height'].min()),
            max_value=float(df['Height'].max()),
            value=float(df['Height'].min())
        )

        col1, col2 = st.columns(2)

        with col1:
            family_history_input = st.selectbox(
                'O paciente possui histórico familiar de obesidade?',
                options=df['family_history'].unique().tolist()
            )

            favc_input = st.selectbox(
                'O paciente come alimentos altamente calóricos com frequência?',
                options=df['FAVC'].unique().tolist()
            )

            FAF_input = st.selectbox(
                'Qual a frequência que o paciente pratica atividade física?',
                options = [0,1,2,3]
            )

        with col2:
            caec_input = st.selectbox(
                'O paciente come alguma coisa entre as refeições?',
                options=df['CAEC'].unique().tolist()
            )

            smoke_input = st.selectbox(
                'O paciente é fumante?',
                options=df['SMOKE'].unique().tolist()
            )

            scc_input = st.selectbox(
                'O paciente monitora calorias ingeridas?',
                options=df['SCC'].unique().tolist()
            )

        if st.button("Executar modelo"):
            try:
                resultado = random_forest(
                    df,
                    age,
                    height,
                    family_history_input,
                    favc_input,
                    caec_input,
                    smoke_input,
                    scc_input,
                    FAF_input
                )

                st.success("📈 Modelo executado com sucesso!")
                st.write("Resultado do modelo:", resultado['predicao'])
                st.write(f"Acurácia: {resultado['acuracia'] * 100:.2f}%")

            except Exception as e:
                st.error(f"📉 Erro ao executar o modelo: {e}")
