import sys
import re
token = ""
numerico = ""
estado = 0
separadores = [';', '[', ']', ')', '(', ')', '{', '}', ',', '=', '.']
operadores = ['-', '+', '/', '*', '^']
lista_erros = []
token_geral = []
tabela_token = {}
linha = 0
coluna = 0
id_tabela = 0
acumula = ""

def verifica_erro(elemento, token_geral, lista_erros, linha, coluna):
  """Se não encontrar um erro retorna 1"""
  separadores = [';', '[', ']', ')', '(', ')', '{', '}', ',', '=', '.', '-', '+', '/', '*', '^', '!', '&', '|', '>', '<']
  if not re.match("[\w]", elemento):
    if elemento not in separadores:
      if not re.search(r"\s", elemento):
        token_geral.append("[Token Inválido]")
        lista_erros.append([elemento, add_linha_coluna(elemento, linha, coluna)])
      return 0
  return 1

def add_linha_coluna(token, linha, coluna):
  """Adiciona linha e coluna"""
  p_inicio = coluna - len(token)
  return "L:" + str(linha) + " C:(" + str(p_inicio) + "," + str(coluna) + ")"

def ver_iden(elemento):
  """Verifica se o elemento é um separador dos numeros"""
  if(re.match(r"[\w]", elemento)):
    return 0
  else:
    return 1

def ver_num(elemento):
  """Verifica se o elemento pertence ao grupo das constantes numericas"""
  if(re.match(r"[\d.]", elemento)):
    return 0
  else:
    """Se ele não pertence retorna 1"""
    return 1

def verifica_reservada(token):
  """Verifica se determinado token é
  reservado e retorna um código para o mesmo"""
  reservada_list = [
    'int',
    'float',
    'double',
    'char',
    'long',
    'signed',
    'unsigned',
    'if',
    'else',
    'printf',
    'for',
    'while',
    'return',
    'continue',
    'break',
    'read',
    'case',
    'const',
    'do',
    'switch',
    'void'
    'default'
    'static',
    'struct',
    'typedef'
  ]
  cont = 0
  for i in reservada_list:
    cont = cont + 1
    if (token == i):
      return cont

def imprime_token(lista):
  """Imprime a lista de tokens"""
  arq = open('token_saida', "w")
  if(len(lista) == 0):
    arq.write("Lista vazia\n")
  for i in lista:
    print(i)
    arq.write(str(i) + "\n")

  arq.close()

def imprime_erros(lista_erros):
  """Imprime a lista de erros"""
  arq_tabela = open("lista_erros", "w")
  arq_tabela.write("Erros\n")
  for i in sorted(lista_erros):
    arq_tabela.write("Linha/Coluna: " + i[1] + ", Erro:" + i[0])
  arq_tabela.close()

def imprime_tabela(tabela_token):
  """Imprime a tabela de tokens"""
  arq_tabela = open("tabela_simbolos", "w")
  arq_tabela.write("Tabela de Simbolos\n")
  for i in sorted(tabela_token):
    arq_tabela.write("Chave:" + str(i) + " " + str(tabela_token[i]) + "\n")
  arq_tabela.close()

def open_file():
  """Abre o arquivo de entrada"""
  try:
    nome = sys.argv[1]
    arquivo = open(nome, "r")
  except Exception as e:
    arquivo = open("teste.c", "r")
  return arquivo

arquivo = open_file()
for i in arquivo:
  linha = linha + 1
  coluna = 0
  for k in i:
    id_tabela = (id_tabela + 1)
    coluna = coluna + 1
    if estado == 0:
      """Define o estado inicial"""
      if k == "/" and i[coluna] == "*" and estado == 0 and estado != 4:
        """Comentario"""
        estado = 4
        token_geral.append(["*/"])
      if re.search(r"^(#)|[/]{2}", i) and estado == 0 and estado != 4:
        """ignora o stdio e linha comentada"""
        break
      if re.match(r"([A-Za-z_])", k) and estado == 0 and estado != 4:
        """Pesquisa por identificadores validos"""
        estado = 1  # Identificador
      if re.match(r"[0-9]", k) and estado == 0 and estado != 4:
        """Pesquisa por Constante Numérica"""
        estado = 2  # Constante Numérica
      if re.match(r"[\"]", k) and estado == 0 and estado != 4:
        """Pesquisa por Literal"""
        estado = 3 # Literal

      if ver_num(k) and ver_iden(k) and estado == 0 and estado != 4:
        """Se não for um identificador valido então é um separador"""
        if verifica_erro(k, token_geral, lista_erros, linha, coluna):
          token_geral.append([k])

    if estado == 1:
      """Valida Identificador"""
      if re.match(r"([\w])", k):
        token = token + k
      if ver_iden(k):
        """Lista com separadores"""
        estado = 0
        if verifica_reservada(token):
          tabela_token[id_tabela] = ["Res Cod: " + str(verifica_reservada(token)), token, add_linha_coluna(token, linha, coluna)]
          token_geral.append(["Res Cod: " + str(verifica_reservada(token)), token, id_tabela])

          if k != " ":
            if verifica_erro(k, token_geral, lista_erros, linha, coluna):
              token_geral.append([k])
          token = ""
        else:

          tabela_token[id_tabela] = ["ID ", token, add_linha_coluna(token, linha, coluna)]
          token_geral.append(["ID ", token, id_tabela])

          if ver_iden(k):

            """Vai inserir o k como separador """
            if k != re.match(r"\s", k):
              if verifica_erro(k, token_geral, lista_erros, linha, coluna):
                """Se não encontrar um erro insere"""
                token_geral.append([k])
            estado = 0
          token = ""

    if estado == 2:
      """Estado de indentificacao de constante numerica"""
      if re.match(r"[\w.]", k):
        numerico = numerico + k
      if ver_num(k):
        if(re.match(r"(^[0-9]*$|[0-9]+.[0-9]+)", numerico)):
          valor = re.match(r"(^[0-9]*$|[0-9]+.[0-9]+)", numerico)
          if valor != None:
            tabela_token[id_tabela] = ["NUM", valor.group(), add_linha_coluna(valor.group(), linha, coluna)]
            token_geral.append(["NUM", valor.group(), id_tabela])
            if k != " ":
              if verifica_erro(k, token_geral, lista_erros, linha, coluna):
                token_geral.append([k])
            estado = 0
            numerico = ""
        else:
          if k in separadores or re.match(r"\s|\n", k) or k in operadores:
            """Identifica o token inválido"""
            token_geral.append("[Token Inválido]")
            lista_erros.append([numerico, add_linha_coluna(numerico, linha, coluna)])
            numerico = ""
            estado = 0
      else:
        if ver_num(k):
          "Armazena token de separadores"
          if k != " ":
            if verifica_erro(k, token_geral, lista_erros, linha, coluna):
              token_geral.append([k])
          estado = 0

    if estado == 3:
      """Identifica Literal"""
      if re.match(r"[%a-zA-z0-9\"\s]", k):
        token = token + k
        if re.match(r"[\"]", k):
          lit = re.match(r"[\"]+[%\w\s]+[\"]*", token)
          if lit != None:
            tabela_token[id_tabela] = ["Literal", lit.group(), add_linha_coluna(lit.group(), linha, coluna)]
            token_geral.append(["Literal", lit.group(), id_tabela])
            token = ""
            estado = 0

    if estado == 4:
      """Incrementa comentarios"""
      acumula = acumula + k
      if re.search(r"(\*\/)", acumula):
        token_geral.append("[*/]")
        estado = 0

if __name__ == '__main__':
  imprime_token(token_geral)
  imprime_tabela(tabela_token)
  imprime_erros(lista_erros)
