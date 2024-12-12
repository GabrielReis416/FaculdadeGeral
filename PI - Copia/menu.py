import sqlite3

def escolher_tabela():
    print('''Escolha qual tabela você quer inserir os dados: 
    [1] Tabela Local (contém os locais das amostras)
    [2] Tabela Amostras (contém os dados das amostras)''')
    opcao = input(F'{YELLOW}Digite a opcao escolhida: {END}')
    if opcao == '1':
        return 'local'
    else:
        return 'amostra'
    
def selecionar_todos_dados_tabela(tabela: str):
    conn = sqlite3.connect('dados.db')
    cursor = conn.cursor()
    print('-' * 100)
    print(f'Tabela {tabela}')
    print('-' * 100)
    cursor.execute(f'SELECT * FROM {tabela};')
    linhas = cursor.fetchall()
    for linha in linhas:
        print(linha, sep=' - ')
    print('-' * 100)    
    conn.commit()
    conn.close()



def inserir_dado_tabela_local():
    conn = sqlite3.connect('dados.db')
    cursor = conn.cursor()

    if tabela == 'local':
        latitude = float(input('Digite a latitude do local: '))
        longitude = float(input('Digite a longitude do local: '))
        descricao = float(input('Digite a descrição do local: '))
        cursor.execute(f'''
            INSERT INTO local (latitude, longitude, descricao_local) VALUES
            ({latitude}, {longitude}, '{descricao}')''')
    print('Dado incluído com sucesso!')
    conn.commit()
    conn.close()

def apagar_registro(tabela: str):
    conn = sqlite3.connect('dados.db')
    cursor = conn.cursor()
    id = float(input('Qual ID você quer apagar? : '))
    cursor.execute(f'''
        DELETE FROM {tabela} WHERE id = {id}''')
    print(f'{YELLOW}Registro apagado com sucesso!{END}')
    conn.commit()
    conn.close()


def inserir_dado_tabela_amostra():
    conn = sqlite3.connect('dados.db')
    cursor = conn.cursor()

    data = input('Digite a data do local no formato DD-MM-AA: ')
    descricao = input('Digite a descricao da amostra: ')
    temperatura = float(input('Digite a temperatura da amostra: '))
    ph = float(input('Digite a ph da amostra: '))
    condutividade = float(input('Digite a condutividade da amostra: '))
    turbidez = float(input('Digite a turbidez da amostra: '))
    acidez = float(input('Digite a acidez da amostra: '))
    alcalinidade_parcial = float(input('Digite a alcalinidade_parcial da amostra: '))
    alcalinidade_total = float(input('Digite a alcalinidade_total da amostra: '))
    cursor.execute(f'''
        INSERT INTO amostra(data, descricao, temperatura, ph, condutividade,turbidez,alcalinidade_parcial, acidez, alcalinidade_total) VALUES
        ('{data}', '{descricao}', {temperatura}, {ph}, {condutividade},{turbidez},{alcalinidade_parcial}, {acidez}, {alcalinidade_total})''')
    conn.commit()
    conn.close()

def inserir_dados(tabela):
    if tabela == 'local':
        inserir_dado_tabela_local()
    elif tabela == 'amostra':
        inserir_dado_tabela_amostra()

def atualizar_registro(tabela: str):
    conn = sqlite3.connect('dados.db')
    cursor = conn.cursor()
    id = float(input('Qual [é o ID do registro que você quer editar? : '))
    latitude = float(input('Digite a latitude do local: '))
    longitude = float(input('Digite a longitude do local: '))
    descricao = float(input('Digite a descrição do local: '))
    cursor.execute(f'''
        UPDATE {tabela} SET latitude = {latitude}, longitude = {longitude}, descricao_local = {descricao} WHERE id = {id}''')
    print(f'{YELLOW}Registro apagado com sucesso!{END}')
    conn.commit()
    conn.close()

YELLOW = '\033[93m'
END = '\033[0m'

while True:
    print(f'''
{YELLOW}Escolha uma opção:{END}
[1] Visualizar uma tabela
[2] Adicionar um novo dado em uma tabela
[3] Apagar o dado de uma tabela
[4] Editar o dado de uma tabela
[5] Sair do programa''')
    opcao = input(F'{YELLOW}Digite a opcao escolhida: {END}')
    if opcao == '1':
        tabela = escolher_tabela()
        selecionar_todos_dados_tabela(tabela)
    elif opcao == '2':
        tabela = escolher_tabela()
        inserir_dados(tabela)
    elif opcao == '3':
        tabela = escolher_tabela()
        apagar_registro(tabela)
    elif opcao == '4':
        tabela = escolher_tabela()
        atualizar_registro(tabela)
    elif opcao == '5':
        print('Programa enceerrado.')
        break

        



    
