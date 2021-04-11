# lê a primeira linha, pega tamanho total
# lê primeiros cinco segundos
# soma a quantidade de bytes enviados, divide por 5
# pega o que resta e faz a regra de três (e.g se transmite 12 bytes por segundo, quantos segundos leva para transmitir 40bytes)
# printa resultado
# pega os próximos cinco dados, faz a mesma coisa
# se a leitura dos proximos 5 inputs for zero, printa pendente

def process_stream(bytes_stack):
    print('bytes stack')
    print(bytes_stack)

def le_input():
    filesize = int(input())
    bytes_stack = []
    aux = input()
    while(aux):
        if(len(bytes_stack) <= 5):
            bytes_stack.append(aux)
        if(len(bytes_stack) == 5 or not aux):
            process_stream(bytes_stack)
            bytes_stack = []
        aux = input()

le_input()
