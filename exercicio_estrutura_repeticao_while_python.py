# -*- coding: utf-8 -*-
"""exercicio-de-while.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zj0WGz1YFWr63-HrK3Ex9sNmSJY4os1r
"""

# Faça um programa que peça uma nota, entre zero e dez.
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = float(input('Digite uma nota: '))

while nota < 0 or nota > 10:
  nota = float(input('VALOR INVÁLIDO! Digite uma nota entre 0 e dez: '))
print(f'O aluno tirou {nota:.1f} no exame.')

# Faça um programa que calcule o mostre a média aritmética de N notas.

resp = 'S'
media = contador = 0

while resp == 'S':
  nota = (float(input('Digite a nota do aluno: ')))
  media += nota
  contador += 1
  resp = str(input('Deseja continuar?\n[Sim] [Não]\n')).upper()[0]
  while resp != 'N' and resp != 'S':
    resp = (str(input('Digite uma resposta válida: '))).upper()[0]
  if resp == 'N':
    break

print(f'A média do aluno das notas inseridas foi {media/contador}')

# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

usuario = str(input('Usuário: '))
senha = str(input('Password: '))

while usuario.upper() == senha.upper():
  senha = str(input('ERRO! Digite uma senha válida: '))
print('Cadastramento concluído.')

# Um funcionário de uma empresa recebe aumento salarial anualmente.
# Sabe-se que: Esse funcionário foi contratado em 1995, com salário inicial de R$1.000,00;
# Em 1996 recebeu aumento de 1,5% sobre seu salário inicial; A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
# Faça um programa que determine o salário atual desse funcionário.
# Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.

salario = float(input('Digite o salário do funcionário: R$'))
ano = 1995
ano_atual = int (input('Digite o ano em que estamos: '))
aumento = 0.015

while ano < ano_atual:
  ano += 1
  salario =  salario + aumento
  aumento *= 2

print(f'O salário em: {ano} é de R${salario:.2f}')

# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

#Nome
nome = str(input('Digite o nome: ')).title()
while len(nome) <= 3:
  nome = str(input('ERROR! Digite um nome válido: ')).title()

#Idade
idade = int(input('Digite a idade: '))
while idade < 0 or idade > 150:
  idade = int(input('ERROR! Digite uma idade adequada: '))

#Salário
salario = float(input('Digite o salário: R$'))
while salario <= 0:
  salario = float(input('ERROR! Digite um salário válido: R$'))

#Sexo
sexo = str(input(f'Digite o sexo de {nome} (M/F): ')).upper()
while sexo != 'M' and sexo != 'F' and len(sexo) > 1:
  sexo = str(input('ERROR! Digite um gênero adequado: ')).upper()

#Estado Civil
estado = str(input('Digite o Estado Civil:\n[S] Solteiro\n[C] Casado\n[V] Víuvo\n[D] Divorciado\n\n')).lower()
while estado != 's' and estado != 'c' and estado != 'v' and estado != 'd' and len(estado) > 1:
  estado = str(input('ERROR! Digite um valor válido: ')).lower()

print(f'Nome: {nome}\nIdade: {idade}\nSalário: R${salario}\nSexo: {sexo}\nEstado Civil: {estado.upper()}')

# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%.
# E que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

a = 80000
b = 200000
year = 2023

percentualA = 3 / 100
percentualB = 1.5 / 100

while a != b and b > a:
  a = a + (a*percentualA)
  b = b + (b*percentualB)
  year += 1

print(f'Percentual alcançado em {year}. País A com {a}. País B com {b}.')

# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
# Ex.: 5!=5.4.3.2.1=120

num = int(input('Digite um número para ver o seu fatorial: '))
fatorial = 1
print(f'{num}! = ',end='')
while num > 0:
  print(num, end=' ')
  fatorial *= num
  num -= 1
print(f'= {fatorial}')

# Faça um programa que solicite ao usuário números indefinidamente até que ele digite 0.
# Em seguida, o programa deve imprimir a média dos números digitados.

soma = 0
contador = 0

while True:
  num = int(input('Digite um valor (Digite 0 para cancelar): '))
  if num == 0: break
  soma += num
  contador += 1

if contador > 0:
  print(f'A soma do número {soma}, resultou em uma média de {soma/contador}.')
else:
  print('Nenhum valor foi definido.')

# A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,...
# Faça um programa capaz de gerar a série até o n−ésimo termo.

limite = int(input('Digite o n-ésimo termo: '))
x = 1
y = 1
contagem = 0

while contagem < limite:
  print(y, end=' ')
  soma = x + y
  y = x
  x = soma
  contagem += 1

print('-'*50)
print('Loja Tabajara'.center(50))
print('-'*50)

produto = 0
total = 0

while True:
  produto += 1
  valor = float(input(f'Digite o preço do Produto {produto}: R$'))
  total += valor
  if valor == 0:
    print(f'O Total da compra foi R${total:.2f}.')
    dinheiro = float(input('Pagamento: R$'))
    while dinheiro < total:
      dinheiro = float(input('Preço inválido. Digite o valor novamente: R$'))
    print(f'Troco: {dinheiro - total:.2f}')
    valor = produto = total = 0

#  O cardápio de uma lanchonete é o seguinte:
# Especificação Código Preço
# Cachorro Quente 100 R$ 1,20
# Bauru Simples 101 R$ 1,30
# Bauru com ovo 102 R$ 1,50
# Hambúrguer 103 R$ 1,20
# Cheeseburguer 104 R$ 1,30
# Refrigerante 105 R$ 1,00
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
# Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
# Considere que o cliente deve informar quando o pedido deve ser encerrado.

cachorroQuente = 1.20
bauruSimples = 1.30
bauruComOvo = 1.50
hamburguer = 1.20
cheeseburguer = 1.30
refrigerante = 1.00

v100 = v101 = v102 = v103 = v104 = v105 = quantidade = total = 0

while True:
  codigo = int(input('Digite o código do produto: (0 para encerrar) '))
  if codigo == 0: break
  quantidade = int(input('Digite a quantidade do produto: '))
  if codigo == 100:
    preco = cachorroQuente * quantidade
    total += preco
    print(f'Cachorro Quente   {quantidade}x   Total: R${preco:.2f}')
  elif codigo == 101:
    preco = bauruSimples * quantidade
    total += preco
    print(f'Bauru Simples   {quantidade}x   Total: R${preco:.2f}')
  elif codigo == 102:
    preco = bauruComOvo * quantidade
    total += preco
    print(f'Bauru Simples   {quantidade}x   Total: R${preco:.2f}')
  elif codigo == 103:
    preco = hamburguer * quantidade
    total += preco
    print(f'Bauru Simples   {quantidade}x   Total: R${preco:.2f}')
  elif codigo == 104:
    preco = cheeseburguer * quantidade
    total += preco
    print(f'Bauru Simples   {quantidade}x   Total: R${preco:.2f}')
  elif codigo == 105:
    preco = refrigerante * quantidade
    total += preco
    print(f'Bauru Simples   {quantidade}x   Total: R${preco:.2f}')
print(f'A compra no total resultou em R${total:.2f}')

# Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código.
# Os códigos utilizados são:
# 1, 2, 3, 4 - Votos para os respectivos candidatos
# (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos.
# Para finalizar o conjunto de votos tem-se o valor zero.



print('Tabela de Votação\n\n[ 1 ] Boca de 09\n[ 2 ] Julius\n[ 3 ] Spliknot\n[ 4 ] Ruyter\n[ 5 ] Voto Nulo\n[ 6 ] Voto Branco\n\n')
n1 = n2 = n3 = n4 = n5 = n6 = total = 0

while True:
  votos = int(input('Digite o número para votação: '))
  while votos < 0 or votos > 6:
    votos = int(input('ERRO! Digite novamente: '))
  if votos == 1: n1 =+ 1
  elif votos == 2: n2 =+ 1
  elif votos == 3: n3 =+ 1
  elif votos == 4: n4 =+ 1
  elif votos == 5: n5 =+ 1
  elif votos == 6: n6 =+ 1
  else: break
  total += 1

  print(f'Boca de 09: {n1} votos.\nJulius: {n2} votos.\nSpliknot: {n3} votos.\nRuyter: {n4} votos.\nVoto Nulo: {n5} votos.\nVoto Branco: {n6} votos.')
  print(f'{(n5*100) / total:.2f}% de votos nulos sobre o total.\n{(n6*100) / total:.2f} votos em branco sobre o total.')