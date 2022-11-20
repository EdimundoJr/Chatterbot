from chatterbot import ChatBot
from difflib import SequenceMatcher

CONFIANCA_MINIMA = 0.65


def comparar_mensagens(mensagem_digitada, mensagem_candidata):
    confianca = 0.0

    digitada = mensagem_digitada.text
    candidata = mensagem_candidata.text
    if digitada and candidata:
        confianca = SequenceMatcher(None, digitada, candidata)
        confianca = round(confianca.ratio(), 2)

    return confianca

def iniciar():
    robo = ChatBot("Robô de Atendimento Sobre Curiosidades da Copa ",
                   read_only=True,
                   logic_adapters=[
                       {
                           "import_path": "chatterbot.logic.BestMatch"
                       }
                   ])

    return robo


def executar_robo(robo):
    while True:
        mensagem = input("Faça sua pergunta... \n")
        resposta = robo.get_response(mensagem.lower())
        if resposta.confidence >= CONFIANCA_MINIMA:
            print(">>", resposta.text)
        else:
            print("Infelizmente, não sei a resposta")
            print("Pergunte outra coisa sobre o Brasil na copa do mundo")


if __name__ == "__main__":
    robo = iniciar()

    executar_robo(robo)
