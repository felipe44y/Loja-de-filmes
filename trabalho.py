filmes = ['Carros','20','Need for Speed','30','Jurassic World','40']
while True:
    print('='*60)
    print('[1] - COMPRAR\n'
'[2] - CADASTRAR')
    print('='*60)
    opcao = int(input('Você quer comprar ou cadastra? [1/2]: '))
    if opcao == 1:
        print('='*60)
        for c,e in enumerate(filmes):
            if c % 2 == 0:
                print(f'Nome do Filme => {filmes[c]} >> Seu preço R${filmes[c+1]}')
        print('='*60)
        op = input('Qual você quer comprar: ')
        if op in filmes:
            print('ÓTIMA ESCOLHA!!!')          
        else:
            print('o filme não está disponivel')
        op = input('Deseja continuar na loja? [S/N]: ').upper()
        while op not in'SN':
            op = input('Opção invalida! Escolha novamente [S/N]: ').upper()
        if op == 'N':
            break
    else:
        if opcao == 2:
            nome = input('Digite o nome do filme: ')
            if nome in filmes:
                print('/'*26)
                print('O filme já foi cadastrado.')
                print('/'*26)
            else:
                preco = input('preço: ')
                filmes.append(nome)
                filmes.append(preco)
                print('='*60)
                print('Cadrastado com SUCESSO!!!!')
                print('='*60)
print('-='*10)
print('    VOLTE SEMPRE')
print('=-'*10)
