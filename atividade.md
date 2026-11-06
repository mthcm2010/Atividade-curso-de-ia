1) ele devolve uma String (C)

2) API tem que ser armazenada no arquivo .env pra proteger as informações privadas e evitar que fique direto no código. Desse jeito, diminui o risco de vazar a chave quando compartilhar o projeto ou publicar ele no github
se ninguém tiver acesso, vai poder fazer alguma solicidação usando sua conta e causar gastos não autorizados

3) Uma lista de dicionários (B)

4) 

total = 0
while True:
 n = int(input("Número (0 para sair): "))
 if n == 0:

    break

 total += n

print(f"Soma: {total}")

5) 

a) Acontece pq sem histórico o código não guarda as mensagens de antes, então se mandar uma mensagem em um novo chat, o código não vai conseguir buscar as informações anteriores

b) A gente colocou uma variável histórico ao código, usando uma lista de dicionários para armazenar as mensagens de antes e enviar junto com a nova mensagem ao modelo.

6) Pega o primeiro item da lista choices (b)

7) 

def carregar_contexto(caminho="contexto.txt"):
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return arquivo.read().strip()

    except FileNotFoundError:
        print("Aviso: arquivo de contexto não encontrado.")
        return ""


8) 

a) 

import streamlit as st
 
if "historico" not in st.session_state:
    st.session_state.historico = []
 
pergunta = st.chat_input("Digite...")
 
if pergunta:
    st.session_state.historico.append({"role": "user", "content": pergunta})

b) Se usa st.session_state para manter o histórico de mensagens mesmo quando o streamlit executa novamente o códico. se usar apenas histórico = [], a lista vai ser reiniciada a cada execução, perdendo as mensagens anteriores.