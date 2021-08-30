# Analisador Léxico

Código que simular um analisador léxico da linguagem C

## Requisitos

- Python 3.8

## Como roda o código

Para rodar o código existem duas formas. A primeira você pode rodar apenas:

```
python analisador_lexico.py
```

Desta forma o programa utilizará o arquivo `teste-geral.c` localizado dentro de `/testes/geral` para fazer a análise léxica. A outra forma de rodar o 
programa é passando como argumento o caminho do arquivo `.c` que se de seja analisar:

```
python analisador_lexico.py testes/geral/teste-geral-2.c
```

Desta forma o programa fará a análise léxica do arquivo `teste-geral-2.c` localizado dentro de `/testes/geral`

No Windows é possível rodar o programa utilizando o arquivo executável em `/dist/`, para isso você deve especificar o caminho do arquivo de teste você deseja utilizar. No exemplo abaixo, será rodando o executável utilizando o arquivo de testes `teste-geral-2.c` que está dentro de `/testes/geral/`.

```
analisador_lexico.exe ./testes/geral/teste-geral-2.c
```

## Resultados

O analisador gerará 3 arquivos: um arquivo contendo os erros achados na análise léxica, uma tabela de simbolos e uma tabela com os tokens de saída.
Os arquivos são respectivamente: `lista_erros`, `tabela_simbolos` e `token_saida`
