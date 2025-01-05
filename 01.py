import os

restaurantes = [{'nome':'Temakin', 'categoria':'Japonesa', 'ativo':False}, 
                    {'nome':'Pizzaria Suprema', 'categoria':'Pizza', 'ativo':True},
                    {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}] 


def show_program_name():
    print('Sabor Express\n')

def show_options():
    print('1. cadastrar restaurante')
    print('2. listar restaurantes')
    print('3. alternar estado de restaurante')
    print('4. sair\n')

def end_app():
    show_subtitle('Finalizando app\n')


def invalid_option():
    print('Opção Inválida!\n')
    back_to_menu()


def back_to_menu():
    input('\nDigite uma tecla para voltar ao menu principal')
    main()


def show_subtitle(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_restaurante():
    show_subtitle('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}:')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    back_to_menu()


def restaurants_list():
    show_subtitle('Listando os restaurantes\n')
    
    print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    back_to_menu()



def change_restaurant_state():
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
    os.system('cls')
    show_program_name()
    show_options()
    escolher_opcao()

if __name__ == '__main__':
    main()












