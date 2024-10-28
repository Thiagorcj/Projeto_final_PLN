import joblib

# Carregar o modelo
modelo = joblib.load('modelo/modelo.pkl')

# Carregar o vectorizer e o label encoder
vectorizer = joblib.load('modelo/vectorizer.pkl')
label_encoder = joblib.load('modelo/label_encoder.pkl')



def retorna_acao(comando):
    # Pré-processar o comando
    novo_comando_vectorizado = vectorizer.transform(comando)

    # Fazer a predição
    predicao = modelo.predict(novo_comando_vectorizado)

    # Decodificar a predição
    acao_predita = label_encoder.inverse_transform(predicao)

    # Imprimir o comando e a ação prevista
    print(f"Comando: {comando[0]} --> Ação prevista: {acao_predita[0]}")

    return acao_predita[0]



if __name__ == '__main__':
    # Testar a função com um comando
    comando = ["Vire a direita!"]
    acao = retorna_acao(comando)
    print(acao)
