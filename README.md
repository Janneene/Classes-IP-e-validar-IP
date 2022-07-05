# Classes-IP-e-validar-IP

Tarefas

1) Pesquise sobre as Classe A, B e C dos endereços de rede IPv4 e suas faixas de endereços. Descreva as características dessas Classes em até 10 linhas. Informe a fonte. Resultados Pretendidos da Aprendizagem Conteúdos envolvidos Tarefas

2) Armazene uma lista de IPs informados pelo usuário com 10 ou mais endereços de IPs que testem casos de IPs válido e inválido para cada tipo de Classe para atribuição a hosts, seguindo as regras específicas de atribuição da Figura1. Para isso, considerar:

a) Cada IP informado deve ser verificado se é válido ou não, verificando os valores de cada octeto.

Obs.: Se for inválido só dar a mensagem e continuar com o seguinte. Dica1: usar list[] e str.split() usando algum separador no split() no caso de digitar os endereços em linha única ou criar um bloco de repetição com while para adicionar na lista.

Dica2: Verificar se o usuário digitou pelo menos a quantidade de endereços solicitada.

Dica3: Verificar se o usuário digitou 4 octetos para cada IP.

Dica4: Verificar se digitou números em cada octeto. Estudamos a função .isdigit()

Dica5: Os endereços IPs que passaram pelas verificações mencionadas armazene em outra estrutura list[] auxiliar.

b) Eliminar os IPs repetidos dessa lista Dica: usar set()

c) Verifique os IPs que sobraram e separe em classes A, B e C. Repare bem nas “obs.1 e 2” para as Classes A e B informadas na Figura1.

Imprimir lista completa que informe para cada (IP, classe válida) por linha Dica6: Usar os condicionais compostos (if..elif..else) e operadores lógicos (and/or), caso precise.

Dica7: usar dict { } para armazenar a tupla (IP, classe válida )

Dica8: use um list[] separado para armazenar por classe.

d) Exibir uma lista só com a Classe C em ordem crescente.

3) Dentro das classes A, B e C foram reservadas redes conhecidas como endereços de redeprivada.

a) Pesquisar sobre as três faixas de endereçamento IP reservadas para redes privadas.

b) Para cada IPs válido da classe C, informar ao cliente se é um endereço público ou privado.
