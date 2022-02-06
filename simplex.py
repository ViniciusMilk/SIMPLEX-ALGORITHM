
# * Portuguese: Importação da biblioteca os
# * ENGLISH:    Import from the library
import os

# *  Portuguese: Classe que contem todas as funções do método SIMPLEX
# *  ENGLISH:    Class that contains all functions of the SIMPLEX method


class Simplex:

    # *  Portuguese: Inicia a tabela
    # *  ENGLISH:    start the table
    def __init__(self):
        self.table = []

    # *  Portuguese: Coloca a função objetivo na tabela
    # *  ENGLISH:    Put the objective function in the table
    def set_objective_function(self, fo: list):
        self.table.append(fo)

    # *  Portuguese: Coloca as restrições na tabela
    # *  ENGLISH:    Put constraints on the table
    def add_restrictions(self, rst: list):
        self.table.append(rst)

    # *  Portuguese: Retorna o índice coluna que vai entra na base
    # *  ENGLISH:    Returns the column index that will enter the base
    def get_entry_column(self) -> int:
        aux_list = self.table[-1].copy()
        aux_list.pop()
        entry_column = min(aux_list)
        index = aux_list.index(entry_column)
        return index

    # *  Portuguese: Retorna o índice da linha que vai sair da base
    # *  ENGLISH:    Returns the index of the row that will leave the base
    def get_exit_line(self, entry_column: int) -> int:
        results = {}
        for line in range(len(self.table)):
            if line < len(self.table)-1:
                if self.table[line][entry_column] != 0:
                    division = self.table[line][-1] / \
                        self.table[line][entry_column]
                    # *  Portuguese: Se o resultado da divisão for positivo, guarda o resultado e o índice no dicionário results
                    # *  ENGLISH:    If division result is positive, store result and index in results dictionary
                    if division > 0:
                        results[line] = division
        # *  Portuguese: Se o tamanho do dicionário results for maior que 0, retorna a chave que é o índice da linha que irá sair da base
        # *  ENGLISH:    If the size of the results dictionary is greater than 0, it returns the key that is the index of the row that will leave the base
        if len(results) > 0:
            index = min(results, key=results.get)
            return index
        # *  Portuguese: Caso não seja maior que zero ele informa que é um PPL ILIMITADO e encerra o programa
        # *  ENGLISH:    If it is not greater than zero, it informs that it is an UNLIMITED PPL and closes the program
        else:
            print('SORRY, NÃO CONSEGUI ACHAR UMA SOLUÇÃO ÓTIMA, PPL ILIMITADO!')
            exit('ENCERRANDO...')

    # *  Portuguese: Retorna a lista da coluna que vai sair da base com todos os seu elementos divididos pelo elemento pivô
    # *  ENGLISH:    Returns the list of the column that will leave the base with all its elements divided by the pivot element
    def calculate_new_pivot_line(self, entry_column: int, exit_line: int) -> list:
        line = self.table[exit_line]

        pivot = line[entry_column]

        new_pivot_line = [value / pivot for value in line]

        return new_pivot_line

    # *  Portuguese: Calcula as novas linhas que irão substituir as linhas que não são a linha do pivô
    # *  ENGLISH:    Calculates the new lines that will replace the lines that are not the pivot line
    def calculate_new_line(self, line: list, entry_column: int, pivot_line: list) -> list:
        # *  Portuguese: atribui a variável aux, o negativo do elemento na linha que será substituída na coluna do pivô
        # *  ENGLISH:    assigns the variable aux, the negative of the element in the row that will be replaced in the pivot column
        aux = line[entry_column] * -1
        # *  Portuguese: Percore a linha do pivô, multiplicando seus elementos por aux e guarda os resultado na lista result line
        # *  ENGLISH:    Traverse the pivot line, multiplying its elements by aux and store the results in the result line list
        result_line = [value * aux for value in pivot_line]
        # *  Portuguese: Declaração de um nova linha
        # *  ENGLISH:    Declaration of a new line
        new_line = []
        # *  Portuguese: Soma a linha result_line com a linha que será substituída e atribui seus resultados a new_line
        # *  ENGLISH:    Adds the result_line line to the line to be replaced and assigns its results to new_line
        for i in range(len(result_line)):
            sum_value = result_line[i] + line[i]
            new_line.append(sum_value)
        # *  Portuguese: Retorna new_line
        # *  ENGLISH:    Returns new_line
        return new_line

    # *  Portuguese: Retorna verdadeiro caso haja algum número negativo na linha da função objetivo
    # *  ENGLISH:    Returns true if there is any negative number in the objective function line
    def is_negative(self) -> bool:
        # *  Portuguese: Se houver número negativo na função objetivo, coloca esse número na lista negative
        # *  ENGLISH:    If there is a negative number in the objective function, put that number in the negative list
        negative = list(filter(lambda x: x < 0, self.table[-1]))
        # *  Portuguese: Se a lista nagative for maior que 0 retorna true, se não retorna false
        # *  ENGLISH:    If the nagative list is greater than 0, it returns true, otherwise it returns false
        return True if len(negative) > 0 else False

    # *  Portuguese: Função que imprimi a tabela
    # *  ENGLISH:    Function that prints the table
    def print_table(self):
        for i in range(len(self.table)):
            for j in range(len(self.table[-1])):
                print(round(self.table[i][j], 2), '\t', end='')
            print()

    # *  Portuguese: Função que imprimi as variáveis que estão na base
    # *  ENGLISH:    Function that prints the variables that are in the base
    def print_base(self, base: dict):
        base_list = sorted(base.values())
        print('Estão na base: ')
        for i in base_list:
            print('X', i+1)

    # *  Portuguese: Função que atualiza a lista das variáveis que estão na base a cada novo pivotamento
    # *  ENGLISH:    Function that updates the list of variables that are in the base with each new pivot
    def update_base(self, base: dict, entry_column: int, exit_line: int) -> dict:
        base[exit_line] = entry_column
        return base

    # *  Portuguese: Função que ira fazer os cálculo, (Obs: está função além de efetuar os cálculos, também irá retornar a lista atualizada das variáveis que estão na base)
    # *  ENGLISH:     Function that will do the calculations, (Note: this function, in addition to performing the calculations, will also return the updated list of variables that are in the base)
    def calculate(self, base: dict) -> dict:
        # *  Portuguese: entry_column recebendo o índice da coluna que irá entrar na base
        # *  ENGLISH:    entry_column receiving the column index that will enter the base
        entry_column = self.get_entry_column()
        # *  Portuguese: exit_line o índice recebendo a linha que ira sair da base
        # *  ENGLISH:    exit_line the index receiving the line that will leave the base
        exit_line = self.get_exit_line(entry_column)
        # *  Portuguese: pivot_line recebendo a linha do pivô(linha que irá sair da base) com todos os seus elementos divididos pelo elemento pivô
        # *  ENGLISH:    pivot_line receiving the pivot line (line that will leave the base) with all its elements divided by the pivot element
        pivot_line = self.calculate_new_pivot_line(entry_column, exit_line)
        # *  Portuguese: Substituindo a linha que sai pela nova linha do pivô(já com o pivô sendo = 1 )
        # *  ENGLISH:     Substituindo a linha que sai pela nova linha do pivô(já com o pivô sendo = 1 )
        self.table[exit_line] = pivot_line
        # *  Portuguese: table_copy recebendo uma cópia da tabela original (isto será necessário para poder multiplicar os elementos da linhas pivô pelo negativo dos elementos que estão na mesma coluna do pivô sem alterá a linha do elemento pivô e depois soma-lá com as sua respectiva linha, assim gerando uma nova tabela já pivotada)
        # *  ENGLISH:    table_copy receiving a copy of the original table (this will be necessary to be able to multiply the elements of the pivot row by the negative of the elements that are in the same column of the pivot without changing the row of the pivot element and then add it to its respective row, thus generating a new table already pivoted)
        table_copy = self.table.copy()

        index = 0
        # *  Portuguese: As multiplicações e somas citadas no comentário acima irão ser feita na mesma quantidade de linhas que a tabela menos na linha do elemento pivô
        # *  ENGLISH:    The multiplications and sums mentioned in the comment above will be done in the same number of rows as the table minus the row of the pivot element
        while index < len(self.table):
            if index != exit_line:
                line = table_copy[index]
                new_line = self.calculate_new_line(
                    line, entry_column, pivot_line)
                self.table[index] = new_line
            index += 1

        base = self.update_base(base, entry_column, exit_line)
        return base

    # *  Portuguese: Função que verifica se o PPL tem múltiplas soluções
    # *  ENGLISH:    Function that checks if the PPL has multiple solutions
    def multi_solutions(self, base: dict):
        # *  Portuguese: aux recebe uma cópia da função objetivo e depois remove seu o último elemento, já que este corresponde ao elemento da coluna de resultado
        # *  ENGLISH:    aux receives a copy of the objective function and then removes its last element as it corresponds to the element of the result column
        aux = self.table[-1].copy()
        aux.pop()
        # *  Portuguese: aux_list receber uma lista que corresponde aos valores(índices das colunas que estão na base) organizada em ordem decrescente.
        # *  ENGLISH:    aux_list receive a list that corresponds to the values (indices of the columns that are in the base) organized in descending order.
        aux_list = sorted(base.values(), reverse=True)
        # *  Portuguese: Retira também os elementos que estão na base(Obs: isso é necessário porque quem está na base tem o valor 0 na função objetivo, mais também pode haver alguma variável com valor 0 que não está na base)
        # *  ENGLISH:    It also removes the elements that are in the base (Note: this is necessary because whoever is in the base has the value 0 in the objective function, but there may also be some variable with value 0 that is not in the base)
        for i in aux_list:
            aux.pop(i)
        # *  Portuguese: Verifica se tem alguma variável que não está na base com valor 0, se houver informa que o PPL tem múltiplas soluções
        # *  ENGLISH:    Checks if there is any variable that is not in the base with a value of 0, if there is, it informs that the PPL has multiple solutions
        if min(aux) == 0:
            print('\nPPL COM MÚLTIPLAS SOLUÇÕES!!!')

    # *  Portuguese: Função que resolve o problema de programação linear
    # *  ENGLISH:    Function that solves the linear programming problem
    def solve(self, base: dict):
        # *  Portuguese: A lista que contém a variáveis que estão na base recebe a nova lista das variáveis que estarão na base após o pivotamento, nesta linha a função calculate já irá fazer o primeiro pivotamento
        # *  ENGLISH:    The list that contains the variables that are in the base receives the new list of the variables that will be in the base after pivoting, in this line the calculate function will already do the first pivot
        base = self.calculate(base)
        # *  Portuguese: enquanto Houver candidados a entrarem na base, a função calculate que faz o pivotamento será chamada, e essa função irá sempre retornar a lista atualizada das variáveis que estarão na base
        # *  ENGLISH:    while there are candidates to enter the base, the calculate function that makes the pivot will be called, and this function will always return the updated list of variables that will be in the base
        while self.is_negative():
            base = self.calculate(base)
        # *  Portuguese: Verifica se o PPL tem múltiplas soluções
        # *  ENGLISH:    Checks if the PPL has multiple solutions
        self.multi_solutions(base)
        # *  Portuguese: chamada da função para imprimir a tabela
        # *  ENGLISH:    function call to print the table
        print('TABELA FINAL!')
        self.print_table()
        # *  Portuguese: Chamada da função que imprimi quem está na base
        # *  ENGLISH:    Call of the function that prints who is in the base
        self.print_base(base)

    # *  Portuguese: retorna os índices de quem inicia na base
    # *  ENGLISH:    returns the indexes of who starts at the base
    def base_init(self, rst: int) -> dict:
        aux = self.table[-1].copy()
        aux.pop()
        base = []
        for i in range(rst):
            base.append(len(aux)-1)
            aux.pop()

        base_dictionary = {}

        for i in range(len(base)):
            base_dictionary.update({i: base[-1]})
            base.pop()

        return base_dictionary


# *  Portuguese: Método main
# *  ENGLISH:    main method
if __name__ == '__main__':
    # *  Portuguese: simplex recebendo a classe Simplex
    # *  ENGLISH:    simplex getting the Simplex class
    simplex = Simplex()
    # *  Portuguese: Recebendo o número de variáveis que tem o PPL do usuário
    # *  ENGLISH:    Getting the number of variables that the user's PPL has
    n_variables = int(input('\nLembre-se adicionar os índices das variáveis de folga e/ou excesso no final das restrições e também no final da função objetivo.\n\nQuantas variáveis tem seu PPL?\n(Obs: não inclua a coluna de resultado como uma variável): '))
    os.system('clear') or None
    # *  Portuguese: Recebendo a função objetivo do usuário
    # *  ENGLISH:    Getting the objective function from the user
    n_restriction = int(input('Quantas restrições tem seu problema? '))
    os.system('clear') or None
    # *  Portuguese: Recendo as restrições do usuário
    # *  ENGLISH:    Receiving user restrictions
    for i in range(n_restriction):
        print('Informe as variáreis da restrição ', i+1)
        rst = []
        for j in range(n_variables):
            print('índice de x', j+1)
            rst.append(int(input()))
            os.system('clear') or None
        rst.append(int(input('Igual a: ')))
        os.system('clear') or None
        simplex.add_restrictions(rst)

    fo = []
    # *  Portuguese: Recebendo a função objetivo do usuário
    # *  ENGLISH:    Getting the objective function from the user
    print('Informe as variáreis da função objetivo')
    for i in range(n_variables):
        print('índice de x', i+1)
        fo.append(int(input()))
        os.system('clear') or None
    fo.append(int(input('Igual a: ')))
    os.system('clear') or None
    simplex.set_objective_function(fo)
    # *  Portuguese: base recebendo os índices da coluna das variáveis que iniciarão na base
    # *  ENGLISH:    base receiving the column indexes of the variables that will start in the base
    base = simplex.base_init(n_restriction)
    os.system('clear') or None
    print('Tabela Original')
    simplex.print_table()
    # *  Portuguese: Chamada da função que irá resolver o PPL. (Obs: esta função irá receber a lista das variáveis que iniciarão na base)
    # *  ENGLISH:    Call of the function that will resolve the PPL. (Note: this function will receive the list of variables that will start in the base)
    simplex.solve(base)
