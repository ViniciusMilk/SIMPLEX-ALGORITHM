# ALGORITMO SIMPLEX

# SIMPLEX ALGORITHM

## DESCRIÇÃO: Este é um algoritmo feito em python com a finalidade de resolver problemas de programação linear, ele recebe um problema na forma padrão, calcula e efetua os pivotamentos necessários e exibi a tabela final após a resolução do problema, e informa quais variáveis estarão na base após resolver o problema.

## DESCRIPTION: This is an algorithm made in python with the purpose of solving linear programming problems, it receives a problem in standard form, calculates and performs the necessary pivots and displays the final table after solving the problem, and informs which variables will be on the base after solving the problem.

- ### Algoritmo
- ### Algorithm

  - \* Portuguese: Importação da biblioteca os
  - \* ENGLISH: Import from the library
  - import os

  - \* Portuguese: Classe que contem todas as funções do método SIMPLEX
  - \* ENGLISH: Class that contains all functions of the SIMPLEX method
  - class Simplex:
    - \* Portuguese: Inicia a tabela
    - \* ENGLISH: start the table
    - def **init**(self):

    - \* Portuguese: Coloca a função objetivo na tabela
    - \* ENGLISH: Put the objective function in the table
    - def set_objective_function(self, fo: list):

    - \* Portuguese: Coloca as restrições na tabela
    - \* ENGLISH: Put constraints on the table
    - def add_restrictions(self, rst: list):

    - \* Portuguese: Retorna o índice coluna que vai entra na base
    - \* ENGLISH: Returns the column index that will enter the base
    - def get_entry_column(self) -> int:

    - \* Portuguese: Retorna o índice da linha que vai sair da base
    - \* ENGLISH: Returns the index of the row that will leave the base
    - def get_exit_line(self, entry_column: int) -> int:

    - \* Portuguese: Retorna a lista da coluna que vai sair da base com todos os seu elementos divididos pelo elemento pivô
    - \*\ ENGLISH: Returns the list of the column that will leave the base with all its elements divided by the pivot element
    - def calculate_new_pivot_line(self, entry_column: int, exit_line: int) -> list:

    - \* Portuguese: Calcula as novas linhas que irão substituir as linhas que não são a linha do pivô
    - \* ENGLISH: Calculates the new lines that will replace the lines that are not the pivot line
    - def calculate_new_line(self, line: list, entry_column: int, pivot_line: list) -> list:

    - \* Portuguese: Retorna verdadeiro caso haja algum número negativo na linha da função objetivo
    - \* ENGLISH: Returns true if there is any negative number in the objective function line
    - def is_negative(self) -> bool:

    - \* Portuguese: Função que imprimi a tabela
    - \* ENGLISH: Function that prints the table
    - def print_table(self):

    - \* Portuguese: Função que imprimi as variáveis que estão na base
    - \* ENGLISH: Function that prints the variables that are in the base
    - def print_base(self, base: dict):

    - \* Portuguese: Função que atualiza a lista das variáveis que estão na base a cada novo pivotamento
    - \* ENGLISH: Function that updates the list of variables that are in the base with each new pivot
    - def update_base(self, base: dict, entry_column: int, exit_line: int) -> dict:

    - \* Portuguese: Função que ira fazer os cálculo, (Obs: está função além de efetuar os cálculos, também irá retornar a lista atualizada das variáveis que estão na base)
    - \* ENGLISH: Function that will do the calculations, (Note: this function, in addition to performing the calculations, will also return the updated list of variables that are in the base)
    - def calculate(self, base: dict) -> dict:

    - \* Portuguese: Função que verifica se o PPL tem múltiplas soluções
    - \* ENGLISH: Function that checks if the PPL has multiple solutions
    - def multi_solutions(self, base: dict):

    - \* Portuguese: Função que resolve o problema de programação linear
    - \* ENGLISH: Function that solves the linear programming problem
    - def solve(self, base: dict):

    - \* Portuguese: retorna os índices de quem inicia na base
    - \* ENGLISH: returns the indexes of who starts at the base
    - def base_init(self, rst: int) -> dict:
  - \* Portuguese: Método main
  - \* ENGLISH: main method
  - if **name** == '**main**':
