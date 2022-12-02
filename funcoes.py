jogador1 = {'pontos':0,'funcao':'indefinida'}
jogador2 = {'pontos':0,'funcao':'indefinida'}
maxOvos = 0
dados = [jogador1,jogador2,maxOvos]
maxOvosLinha = 0

mapa = [["0","1","2","3","4", "5" ,"6" ,"7"],
        ["1","A","A","A","A" ,"A" ,"A" ,"A"],
        ["2","A","A","A","A" ,"A" ,"A" ,"A"],
        ["3","A","A","A","A" ,"A" ,"A" ,"A"],
        ["4","A","A","A","A" ,"A" ,"A" ,"A"],
        ["5","A","A","A","A" ,"A" ,"A" ,"A"],
        ["6","A","A","A","A" ,"A" ,"A" ,"A"],
        ["7","A","A","A","A" ,"A" ,"A" ,"A"],]

def menu():
  print("Opções:\n1 - Definir Armador\n2 - Plantar Armadilhas\n3 - Iniciar com Andarilho\n4 - Mostrar o placar\n0 - Finalizar o Jogo\n")


def imprimeMapa():
  print("\nmapa para plantar bombas\n")
  for i in range(8):
    for j in range(8):
      print(mapa[i][j], end = " ")
    print("")
  print("")

def armador():
  armador = int(input("quem será o armador(jogador 1 ou 2): "))
  print("\no armador é o jogador",armador)
  if(armador == 1):
    jogador1["funcao"] = 'armador'
    jogador2['funcao'] = 'andarilho'
    print("o andarilho é o jogador 2\n")
  elif(armador == 2):
    jogador1["funcao"] = 'andarilho'
    jogador2['funcao'] = 'armador'
    print("o andarilho é o jogador 1\n")

def poeOvo(maxOvos):
  for i in range(1,8):
    maxOvosLinha = 0  
    resposta = str(input("deseja colocar ovos podres na linha " + str(i) + " ?(s/n): "))
    if(maxOvosLinha <3 and maxOvos <15):  
      while(resposta == 's'):
        coluna = int(input("Em qual colunada linha " + str(i) + " você quer esconder ovos podres? [1 a 7]"))
        if((coluna > 0 and coluna <=7) and mapa[i][coluna] == 'A'):
          mapa[i][coluna] = 'X'
          maxOvos += 1
          maxOvosLinha +=1
          print()
          if(maxOvosLinha == 3):
            print("limite de ovos atingido nessa linha, vamos para a proxima")
            resposta = 'n'
          elif(maxOvos == 15):
            print("maximo de ovos atingidos")
            resposta = 'n'
          else:  
            resposta = str(input("deseja continuar nessa linha?(s/n): "))
        else:
          print("valor invalido ou ja possui um ovo podre nessa coluna")
  if(maxOvos > 0):    
    print("ovos colocados com sucesso")
    imprimeMapa()
    redefinir = str(input("deseja redefinir os ovos?(s/n): "))
    
    if(redefinir == 's'):
      redefinirMapa()
      maxOvos = 0
      poeOvo(maxOvos)  
  else:
    print("armador precisa por pelo menos um ovo podre no mapa")
    poeOvo(maxOvos)
    
def redefinirMapa():
  for i in range(8):
    for j in range(8):
      if(mapa[i][j] == 'X'):
        mapa[i][j] = 'A'
def possiveisMovimentos(posy):
  movimentos = []
  if(posy == 1):
    movimentos = [1,2]
  elif(posy == 7):
    movimentos = [6,7]
  elif(posy >1 or posy < 7):
    movimentos = [posy-1,posy,posy+1]
  else:
    return 0
  return movimentos  

  
def limpaTela():
  for i in range(100):
    for j in range(i):
      print('=',end = " ")
    print()  

      
def movimetacaoAndarilho():
  posx = 1
  print("\nandarilho, ande com bastante cuidado, muitos ovos podres o esperam hahahaha\n")
  posy = int(input("escolha uma opcao entre 1 e 7"))
  pisou = pisouEmOvo(posx,posy)
  if(pisou == 0):
    print("armador faz ponto")
    ponto("armador")
    
  else:
    print("andarilho conseguiu passar da primeira, tome bastante cuidado!!!")
    posx +=1
    while(pisou == 1 and posx < 7):
      print("posy :   ",posy)
      print("posx:    ",posx)
      movimentos = possiveisMovimentos(posy)
      posy = int(input("escolha uma opcao dentre as seguintes opcoes " + str(movimentos) +": "))
      if(posy in movimentos):
        pisou = pisouEmOvo(posx,posy)
        if(pisou == 0):
          print("armador faz ponto")
          ponto("armador")
        else:
          print("andarilho conseguiu andar mais um linha, tome bastante cuidado!!!")
          posx += 1
          if(posx ==7):
            print("andarilho faz ponto")
            ponto("armador")
      else:
        print("posicao invalida")
        while(posy not in possiveisMovimentos(posy)):
          posy = int(input("escolha uma opcao dentre as seguintes opcoes " + str(movimentos) +": "))
  
        
def pisouEmOvo(posx,posy):
  if(mapa[posx][posy] == 'X'):
    return 0
  else:
    return 1 
        
def ponto(funcao):
  if(funcao == 'armador'):
    if(jogador1['funcao'] == 'armador'):
      jogador1['pontos'] += 1
    else:
      jogador2['pontos'] += 1
  else:
    if(jogador1['funcao'] == 'andarilho'):
      jogador1['pontos'] += 1
    else:
      jogador2['pontos'] += 1
  
def mostraPlacar():
  print("\n------------------PLACAR------------------")
  print("pontução do jogador 1: ",jogador1['pontos'])
  print("pontução do jogador 2: ",jogador2['pontos'])

