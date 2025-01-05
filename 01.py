import os

restaurantes = [{'nome':'Temakin', 'categoria':'Japonesa', 'ativo':False}, 
                    {'nome':'Pizzaria Suprema', 'categoria':'Pizza', 'ativo':True},
                    {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}] 


def show_program_name():
    ''' Exibe o nome estilizado do programa na tela '''
    print('Sabor Express\n')

def show_options():
    ''' Exibe as opções disponíveis no menu principal '''
    print('1. cadastrar restaurante')
    print('2. listar restaurantes')
    print('3. alternar estado de restaurante')
    print('4. sair\n')

def end_app():
    ''' Exibe mensagem de finalização do aplicativo '''
    show_subtitle('Finalizando app\n')


def invalid_option():
    ''' Exibe mensagem de opção inválida e retorna ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''
    print('Opção Inválida!\n')
    back_to_menu()


def back_to_menu():
    ''' Solicita uma tecla para voltar ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''
    input('\nDigite uma tecla para voltar ao menu principal')
    main()


def show_subtitle(texto):
    ''' Exibe um subtítulo estilizado na tela 
    
    Inputs:
    - texto: str - O texto do subtítulo
    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_restaurante():
    ''' Essa função é responsável por cadastrar um novo restaurante 
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes

    '''
    show_subtitle('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}:')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    back_to_menu()


def restaurants_list():
    ''' Lista os restaurantes presentes na lista 
    
    Outputs:
    - Exibe a lista de restaurantes na tela
    '''
    show_subtitle('Listando os restaurantes\n')
    
    print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    back_to_menu()



def change_restaurant_state():
    ''' Altera o estado ativo/desativado de um restaurante 
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    '''
    show_subtitle('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')
    back_to_menu()


def escolher_opcao():
    ''' Solicita e executa a opção escolhida pelo usuário 
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    '''
    try:
        option_choose = int(input('Escolha uma opção: '))    
    
        if option_choose == 1:
            cadastrar_restaurante()
        elif option_choose == 2:
            restaurants_list()
        elif option_choose == 3:
            change_restaurant_state()
        elif option_choose == 4:
            end_app()
        else:
            invalid_option()

    except:
        invalid_option()


def main():
    ''' Função principal que inicia o programa '''
    os.system('cls')
    show_program_name()
    show_options()
    escolher_opcao()

if __name__ == '__main__':
    main()












