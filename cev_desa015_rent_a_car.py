"""Exercício Python 015: Escreva um programa que pergunte
a quantidade de Km percorridos por um carro alugado e
a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$80 por dia e R$0,15 por Km rodado."""


from uteis import abre, divide, encerra, decima, natura, words


titulo = 'CÁLCULO PARA LOCAÇÃO DE VEÍCULO'

abre(titulo)

while True:

    segue = ' '

    km_rodados    = decima('Digite a quilometragem rodada:          ')
    dias_locados  = natura('Digite o número de dias locados:                  ')

    print()

    preco_km_rodado = decima('Digite o custo por quilômetro rodado:   ')
    preco_diaria = decima('Digite o custo por dia locado:     ')

    print()

    total_km   = km_rodados * preco_km_rodado
    total_dias = dias_locados * preco_diaria

    print()

    print(f'Você rodou {km_rodados:.1f} km em {dias_locados:.0f} dias e deverá pagar R$ {total_dias+total_km:.2f} no total, sendo')
    print(f'R$ {total_km:.2f} pelos quilômetros rodados e R$ {total_dias:.2f} pelos dias ocupados.')

    divide()

    while segue not in 'SN':

        segue = words('Outra locação?   [S/N] ').strip().upper()[0]

    if segue in 'N':
        encerra(80, 'Encerrando...')
        print('On github.com visit leonardinobre')
        break
