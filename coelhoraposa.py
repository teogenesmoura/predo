import math

def flush_result(indice, target):
    COELHO_GANHOU = "O coelho pode escapar pelo buraco "
    RAPOSA_GANHOU = "O coelho nao pode escapar."
    if(indice > 1):
        print(COELHO_GANHOU + str(target) + '.')
    else:
        print(RAPOSA_GANHOU)

def dist_dois_pontos(p1, p2):
    p1_x = float(p1[0])
    p1_y = float(p1[1])
    p2_x = float(p2[0])
    p2_y = float(p2[1])
    return math.sqrt(((p1_x-p2_x)**2)+((p1_y-p2_y)**2))

def calc_target(animal_coord, lista_buracos):
    target = ()
    optimal_dist = math.inf
    for buraco in lista_buracos:
        curr_dist = dist_dois_pontos(animal_coord, buraco)
        if(curr_dist < optimal_dist):
            optimal_dist = curr_dist
            target = buraco
    return target

def is_fuga_possivel(lista_buracos, coelho_coord, raposa_coord):
    COELHO_GANHOU = "O coelho pode escapar pelo buraco "
    RAPOSA_GANHOU = "O coelho nao pode escapar."
    target = calc_target(coelho_coord, lista_buracos)
    dist_coelho_target = dist_dois_pontos(coelho_coord, target)
    dist_raposa_target = dist_dois_pontos(raposa_coord, target)
    print('target')
    print(target)
    print('dist_coelho_target')
    print(dist_coelho_target)
    print('dist_raposa_target')
    print(dist_raposa_target)
    if(dist_coelho_target > (dist_raposa_target * 2)):
        print(COELHO_GANHOU + str(target) + '.')
    else:
        print(RAPOSA_GANHOU)
    print(indice)
    flush_result(indice, target)

def input_str_to_dict(str):
    separate = str.split(" ")
    return (separate[0], separate[1])

def recebe_input():
    numero_buracos = int(input())
    coelho_coord = input_str_to_dict(input())
    raposa_coord = input_str_to_dict(input())
    lista_buracos = []
    i = 0
    while (i < numero_buracos):
        lista_buracos.append(input_str_to_dict(input()))
        i += 1
    is_fuga_possivel(lista_buracos, coelho_coord, raposa_coord)

recebe_input()

#1
#1.000 1.000
#2.000 2.000
#1.500 1.500
