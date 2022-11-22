import unittest
from robo import *


class TesteInformacoesBasicas(unittest.TestCase):

    def setUp(self):
        self.robo = iniciar()

    def testar_pg(self):
        mensagens = ["quantas vezes o brasil foi campeão?", "quantos títulos o brasil possui?", "quantas copas o brasil ganhou?"]

        for mensagem in mensagens:
            print(f"testando a mensagem: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn(
                "O Brasil é campeão do mundo cinco vezes", resposta.text)

    def testar_pg2(self):
        mensagens = [ "qual o ano do último título conquistado?", "qual o último ano que o brasil ganhou?", "qual foi a última vez que o brasil ganhou a copa?", "brasil ganhou em que ano?" ]

        for mensagem in mensagens:
            print(f"testando a mensagem: {mensagem}")

            resposta = self.robo.get_response(mensagem)
            self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
            self.assertIn("Seu último título foi conquistado em 2002, contra a a Alemanha, por 2 x 0", resposta.text)

    def testar_pg3(self):
            mensagens = [ "qual o placar da final da copa de 1958?","brasil ganhou de quantos gols na copa de 1958?","qual foi o placar do jogo de 1958 quando brasil ganhou?" ]

            for mensagem in mensagens:
                print(f"testando a mensagem: {mensagem}")

                resposta = self.robo.get_response(mensagem)
                self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
                self.assertIn("A seleção brasileira conquistou a vitória por 5 x 2 em cima dos suecos, com gols de Vavá, Pelé e Zagallo. Três jogadores que, até os dias de hoje, tem expressividade na história do futebol brasileiro.", resposta.text)
                
    def testar_pg3_2(self):
            mensagens = [ "qual o placar da final da copa de 1962?","brasil ganhou de quantos gols na copa de 1962?","qual foi o placar do jogo de 1962 quando brasil ganhou?" ]

            for mensagem in mensagens:
                print(f"testando a mensagem: {mensagem}")

                resposta = self.robo.get_response(mensagem)
                self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
                self.assertIn("A final da Copa do Mundo FIFA de 1962 foi disputada pela Tchecoslováquia, que havia eliminado a Iugoslávia e a Hungria; e o Brasil, que havia eliminado o Chile e a Inglaterra. A partida foi realizada em 17 de junho às 14h30min, Estádio Nacional do Chile, com um público estimado em 68 679 pessoas. Sob o apito do árbitro soviético Nikolay Latyshev, Josef Masopust abriu o placar aos 15 minutos, porém, 2 minutos depois, Amarildo empata o jogo, que termina o primeiro tempo no 1 a 1. Aos 24 minutos do segundo tempo, Zito vira o jogo para a equipe brasileira e Vavá, 9 minutos depois, amplia a diferença, fechando o placar em 3 x 1.", resposta.text)            
    def testar_pg3_3(self):
            mensagens = [ "qual o placar da final da copa de 1970?","brasil ganhou de quantos gols na copa de 1970?","qual foi o placar do jogo de 1970 quando brasil ganhou?" ]

            for mensagem in mensagens:
                print(f"testando a mensagem: {mensagem}")

                resposta = self.robo.get_response(mensagem)
                self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
                self.assertIn("A Copa de 70 é um marco na memória dos brasileiros. O Brasil virou a primeira seleção com três títulos na Copa do Mundo, superando a Itália e o Uruguai que já tinham dois Mundiais nas costas. A conquista foi ainda mais emocionante porque o título de campeão veio na final contra a Itália, por 4 x 1, com gols de Pelé, Gérson, Jairzinho e Carlos Alberto.", resposta.text)            
    def testar_pg3_4(self):
            mensagens = [ "qual o placar da final da copa de 1994?","brasil ganhou de quantos gols na copa de 1994?","qual foi o placar do jogo de 1994 quando brasil ganhou?" ]

            for mensagem in mensagens:
                print(f"testando a mensagem: {mensagem}")

                resposta = self.robo.get_response(mensagem)
                self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
                self.assertIn("Na Copa de 1994, o Brasil conquistou o tetracampeonato na disputa de pênaltis contra a Itália, terminando as cobranças com a vitória por 3 x 2. A Copa foi sediada nos Estados Unidos e bateu todos os recordes de público.", resposta.text)            
    def testar_pg3_5(self):
            mensagens = [ "qual o placar da final da copa de 2002?","brasil ganhou de quantos gols na copa de 2002?","qual foi o placar do jogo de 2002 quando brasil ganhou?" ]

            for mensagem in mensagens:
                print(f"testando a mensagem: {mensagem}")

                resposta = self.robo.get_response(mensagem)
                self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
                self.assertIn("O último título da seleção canarinho foi garantido na Copa do Japão e da Coreia do Sul, em 2002, jogando contra a Alemanha na final e ganhando por 2 x 0.", resposta.text)            
                            
    def testar_pg4(self):
            mensagens = [ "qual a copa do mundo que o brasil não participou?","brasil deixou de participar em alguma copa?","o brasil não participou de qual copa?" ]

            for mensagem in mensagens:
                print(f"testando a mensagem: {mensagem}")

                resposta = self.robo.get_response(mensagem)
                self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
                self.assertIn("A seleção brasileira é a única que participou de todas as edições da Copa do Mundo, desde 1930. Em 2022, a competição chega a sua 22ª edição e o Brasil joga como a seleção mais bem cotada a receber o título de campeã do mundo, segundo o ranking da FIFA.", resposta.text)
                
    def testar_pg5(self):
            mensagens = [ "qual foi a pior participação do Brasil em copas do mundo?","qual foi a pior copa que o brasil participou?","qauais foram as piores copas que o brasil participou?" ]

            for mensagem in mensagens:
                print(f"testando a mensagem: {mensagem}")

                resposta = self.robo.get_response(mensagem)
                self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
                self.assertIn("As Copas de 1934 e 1966 demarcam as piores campanhas brasileiras. A primeira delas foi disputada na Itália, com um formato de mata-mata desde o início. E foi logo na estreia que o Brasil já deu adeus. Outro ano muito conhecido pelo fraco desempenho brasileiro foi o de 1966. Apesar de contar com os craques Pelé e Garrincha, o Brasil caiu na primeira fase. A Copa do Mundo de 1966 ficou conhecida como a última de Garrincha e pela lesão precoce de Pelé, contundido ainda no primeiro jogo. No ranking final daquela edição, o Brasil terminou em 11°.", resposta.text)
                
    def testar_pg6(self):
            mensagens = [ "quantas vezes a seleção brasileira foi vice?","o brasil ficou em segundo lugar em alguma copa?","quantas vezes o brasil ficou na segunda colocação na copa do mundo?" ]

            for mensagem in mensagens:
                print(f"testando a mensagem: {mensagem}")

                resposta = self.robo.get_response(mensagem)
                self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
                self.assertIn("O Brasil foi vice apenas duas vezes na sua história, uma em 1950, quando perdeu para o Uruguai em uma triste derrota no Maracanã, e outra em 1998, quando perdeu para a França por 3x0, em jogo super polêmico.", resposta.text)
                
    def testar_pg7(self):
            mensagens = [ "qual jogador foi mais vezes campeão na copa?","qual jogador venceu mais copas do mundo?" ]

            for mensagem in mensagens:
                print(f"testando a mensagem: {mensagem}")

                resposta = self.robo.get_response(mensagem)
                self.assertGreaterEqual(resposta.confidence, CONFIANCA_MINIMA)
                self.assertIn("O jogador que mais vezes foi campeão na história da Copa do Mundo foi o brasileiro Pelé (Edson Arantes do Nascimento). Pelé foi campeão mundial nas copas de 1958, 1962 e 1970", resposta.text)
                
if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()

    testes.addTest(carregador.loadTestsFromTestCase(TesteInformacoesBasicas))

    executor = unittest.TextTestRunner()
    executor.run(testes)

