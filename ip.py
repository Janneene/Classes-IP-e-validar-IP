#Criação das Listas para armazenar os IPs dividido por classe
listaA = []
listaB = []
listaC = []
#Lista para verificar os octetos de cada IP
verificador = [] 
#Dicionário para IPs na Classe C e para os IPs no geral
dicIPC = {}
dicIPs = {}


#IP = input("Coloque 10 ou mais IPs dividido por vírgulas (,): \n").strip() #Recebendo um STRING de IPs do usuário
#listaIP = IP.split(",") #Dividindo a STRING em diversos itens de uma lista

listaIP = input("Coloque 10 ou mais IPs dividido por vírgulas (,): \n").strip().split(",") #Recebendo um STRING de IPs do usuário


print("\n Lista IP recebida: \n", listaIP, "\n") #printando a minhha lista de IPs
conjuntoIP = set(listaIP)
for x in conjuntoIP: #percorre a lista de IPs
  verificador = x.split(".") #Aqui eu pego um IP por vez e divido em outra lista com os octetos separados

  #verificando se tem 4 octetos
  if(len(verificador) != 4):
    print("IP", x ," tem menos (ou mais) que 4 octetos")
    dicIPs.update({x:'inválido'})
  #verificando se os 4 octetos são numeros
  elif((verificador[0].isdigit() == False)) or ((verificador[1].isdigit()) == False) or ((verificador[2].isdigit()) == False) or ((verificador[3].isdigit() == False)):
    print("IP", x ,"tem algum integrante que não é numeral!")
    dicIPs.update({x:'inválido'})
  #verificando se a lista de IPs tem 10 ou mais IPs
  elif(len(listaIP) < 10):
    print("Faltou adicionar mais IPs na sua lista de IPs :-)")
  #entra no else se tudo tiver válido
  else:
    #como a gente recebeu uma STRING la no início e não um inteiro, logo abaixo convertemos para INTEIRO para fazer as verificações nos IFs
    oct1 = int(verificador[0])
    oct2 = int(verificador[1])
    oct3 = int(verificador[2])
    oct4 = int(verificador[3])

    if(oct2 >= 0 and oct2 <= 255 and oct3 >= 0 and oct3 <= 255): #semelhança entre as 3 classes coloquei em um IF só. 
      if(oct4 >= 0 and oct4 <= 255):       
        if(oct1 >= 0 and oct1 <= 127): #Classe A
          if((oct2 == 0 and oct3 == 0 and oct4 == 0) or (oct2 == 255 and oct3 == 255 and oct4 == 255)):
            dicIPs.update({x:'inválido'})
          else:
            listaA.append(x)
            dicIPs.update({x:'válido'})
        elif(oct1 >= 128 and oct1 <= 191): #Classe B
          if((oct3 == 0 and oct4 == 0) or (oct3 == 255 and oct4 == 255)):
            dicIPs.update({x:'inválido'})
          else:
            listaB.append(x)
            dicIPs.update({x:'válido'})
        elif(oct1 >= 192 and oct1 <= 223 and oct4 >= 1 and oct4 <= 254): #Classe C
          if((oct3 == 0 and oct4 == 0) or (oct3 == 255 and oct4 == 255)):
            dicIPs.update({x:'inválido'})
          else:
            listaC.append(x)
            dicIPs.update({x:'válido'}) 
            if(oct1 == 192 and oct2 == 168):
              dicIPC.update({x:'privado'})
            else:
              dicIPC.update({x:'publico'})
        else:
          dicIPs.update({x:'invalido'})
    else:
      dicIPs.update({x:'invalido'})

# exibir lista de classes
print("\n ##### Exibição das listas de IP ##### \n")
print("IPs classe A: \n", listaA)
print("IPs classe B: \n", listaB)
print("IPs classe C: \n", listaC)
print("\n #################################### \n")

#print("\n Sua lista de IP ordenados é: ",sorted(listaIP))

#print("\n Sua Lista de IP de Classe C sem números repetidos: \n", set(listaIP))

print("\n \n #### LISTAGEM DE IPs VÁLIDOS E INVÁLIDOS ####")
for chave, valor in dicIPs.items(): #método items (nesse contexto) é como se fosse o len() do list 
#Se fosse fazer apenas print(dicIPs.items()) iria sair mal formatado, colocando dentro do for podemos formatar a exibição bonitinha
  print(f"-> O IP = {chave} é {valor}")
print("\n #################################### \n")

#print(dicIPs.items())


print("\n \n #### IPs CLASSE C PUBLICOS E PRIVADOS ####")
for chave, valor in dicIPC.items():
    print(f"-> O IP = {chave} é {valor}")
print("\n #################################### \n")

