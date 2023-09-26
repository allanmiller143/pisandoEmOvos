from funcoes import *
opcao = -1
menu()
   
while(opcao != 0 ):
  opcao = int(input("escolha uma das opcoes do menu: "))
  if(opcao == 1):
    armador()
  elif(opcao ==2):
    if(jogador1["funcao"] != 'indefinida'):
      imprimeMapa()
      print("você pode esconder até 3 ovos podres por linha do terreno.")
      poeOvo(maxOvos)
      limpaTela()
    else:
      print("defina armador primeiro")
  elif(opcao == 3):
      print(jogador1["funcao"])
      if(jogador1["funcao"] != 'indefinida'):
        movimetacaoAndarilho() 
      else:
        print("defina o armador primeiro")       
  elif(opcao == 4):
    mostraPlacar()
  elif(opcao == 0):
    print("opcao 0")
  else:
    print("opcao invalida")
