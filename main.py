from funcoes import *
opcao = -1
menu()
   
while(opcao != 0 ):
  opcao = int(input("escolha uma das opcoes do menu: "))
  if(opcao == 1):
    armador()
  elif(opcao ==2):
    if(jogador1["funcao"] != 'indefinada'):
      imprimeMapa()
      print("você pode esconder até 3 ovos podres por linha do terreno.")
      poeOvo(maxOvos)
      limpaTela()
    else:
      print("defina armador primeiro")
  elif(opcao == 3):
      if(jogador1["funcao"] != 'indefinada'):
        movimetacaoAndarilho() 
      else:
        print("defina o armador")       
  elif(opcao == 4):
    mostraPlacar()
  elif(opcao == 0):
    print("opcao 0")
  else:
    print("opcao invalida")