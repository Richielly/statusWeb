import requests
import streamlit as st
from time import sleep as s
import os.path
from conexao import TransactionObject

#with st.form(key='my_form'):
 #   text_input = st.text_input(label='Enter your name')
  #  submit_button = st.form_submit_button(label='Submit')

dados = TransactionObject()
urls = dados.view()
sistemas = ['esadmin','stp','scf','srh','stm']

if st.sidebar.checkbox("Cadastrar"):
    with st.beta_expander("Cadastrar Url"):
        entidade = st.number_input("Código Entidade",max_value=999)
        nome = st.text_input("Nome Entidade")
        url = st.text_input('Url')
        if st.button("Gravar"):
            dados.insert(str(entidade),nome,url)

if st.sidebar.checkbox("Cadastrados"):
    st.header('Lista de entidades cadastradas:')

    for url in urls:
        if st.sidebar.checkbox(str(url[1])):
            for sistema in sistemas:
                resposta = requests.get(str(url[3]) + sistema)
                if (resposta.status_code == 200):
                    st.success("Sistema " + sistema.upper() + " no Ar.")
                else:
                    st.error("Sistema " + sistema.upper() + " fora do Ar ou sem licença.")

if st.button("Verificação Geral") :
    for url in urls:
        resposta = requests.get(str(url[3]) +'esadmin')
        if (resposta.status_code == 200):
            st.success("Entidade: " + url[3] + " no Ar.")
        else:
            st.error("Entidade: " + url[3] + " fora do Ar ou sem licença encontrada.")