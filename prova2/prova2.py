class Wookie:
    def __init__(self, id):
        self.carga = []
        self.id = id

    def topo(self):
        return self.carga[-1] if len(self.carga) > 0 else None

    def get_carga(self):
        return self.carga

    def empilha_carga(self,carga):
        self.carga.append(carga)
        return self.topo()

    def desempilha_carga(self):
        return self.carga.pop()

    def has_load(self):
        return len(self.carga) != 0

    def peso_total_das_cargas(self):
        pass

    def __str__(self):
        return f" Wookie {self.id}. O topo da minha lista é {self.topo()}."

class FilaDeWookies:
    def __init__(self, numero_wookies, lista_cargas):
        self.numero_wookies = int(numero_wookies)
        self.wookies = []
        self.lista_cargas = lista_cargas.split()
        self.sobras = []
        self.init_wookies()

    def get_lista_cargas(self):
        return self.lista_cargas

    def get_numero_de_wookies(self):
        return self.numero_wookies

    def desempilha_carga(self):
        return self.lista_cargas.pop(0)

    def get_lista_de_wookies(self):
        return self.wookies

    def init_wookies(self):
        for i in range(self.numero_wookies):
            self.wookies.append(Wookie(i))

    def wookie_without_load(self):
        for wookie in self.wookies:
            if not wookie.has_load:
                return wookie
        return False

    def get_cargas_por_wookie(self):
        result = []
        for wookie in self.wookies:
            result.append(wookie.get_carga())
        return result

    def start_check_list(self):
        return [False]*self.numero_wookies

    def place_cargas_in_wookies(self):
        w_counter = 0 #wookie counter
        check_list = self.start_check_list()
        carga_atual = self.desempilha_carga()
        while(self.lista_cargas):
            check_list[w_counter] = True
            curr_wookie = self.wookies[w_counter] #
            # se o wookie estiver sem carga, entrega para ele
            if not curr_wookie.topo():
                curr_wookie.empilha_carga(int(carga_atual)) # [Wookie0<4>, Wookie1<4>, Wookie2<1>]
                check_list[w_counter] = False
                carga_atual = self.desempilha_carga()
            # se ele ja tiver carga, verifica se há algum wookie sem carga
            elif self.wookie_without_load():
                free_wookie = get_first_wookie_without_load()
                free_wookie.empilha_carga(int(carga_atual))
                check_list[w_counter] = False
                carga_atual = self.desempilha_carga()
            # se nenhum wookie estiver sem carga, verifica se carga atual é menor que topo da pilha do woookie atual
            elif int(carga_atual) <= int(curr_wookie.topo()):
                curr_wookie.empilha_carga(int(carga_atual))
                check_list[w_counter] = False
                carga_atual = self.desempilha_carga()
            # se nenhum dos casos se aplicar, coloca carga na lista de sobras
            elif all(check_list) == True:
                self.sobras.append(carga_atual)
                carga_atual = self.desempilha_carga()
                check_list = self.start_check_list()
                w_counter += 1
            #atualiza iteração dos wookies
            if w_counter < self.numero_wookies-1:
                w_counter += 1
            else:
                w_counter = 0
        return self.get_cargas_por_wookie()


    def get_lista_decrescente_por_peso(self):
        pass

if __name__ == 'main':
    numero_wookies = int(input())
    lista_cargas = input().split()
    fila_de_wookies = FilaDeWookies(numero_wookies, lista_cargas)
    fila_de_wookies.place_cargas_in_wookies()

# lista_wookie = []
# for i in range(numero_wookies):
#     lista_wookie.append([])
# posicao=0
# while lista_carga:
#     elemento = int(lista_carga.pop(0))
#     for i in range (numero_wookies-1):
#         tamanho = len(lista_wookie[i])
#         if not lista_wookie[i]:
#             lista_wookie[i].append(elemento)
#             elemento = int(lista_carga.pop(0))
#         elif lista_wookie[i][tamanho-1]>=elemento:
#             lista_wookie[i].append(elemento)
#             elemento = int(lista_carga.pop(0))
#
#
#
# print (lista_wookie)
