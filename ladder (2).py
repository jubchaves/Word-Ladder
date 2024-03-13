
def cria_dicionario(inicio):
    dicionario = []
    with open("dicionario.txt", "r") as texto:
        for palavra in texto:
            if len(palavra)-1 == len(inicio):
                dicionario.append(palavra.strip("\n"))
        dicionario = set(dicionario)
    return dicionario


def semelhanca(fim, palavra):
    s = 0
    for i in range(len(palavra)):
        if palavra[i] == fim[i]:
            s +=1
    return s

def caminho(genealogia, inicio, fim):
    caminho = []
    palavra = fim
    while palavra != inicio:
        caminho.insert(0,palavra)
        #puxar palavra mãe
        palavra = genealogia[palavra]
    caminho.insert(0,inicio)
    
    return caminho

def print_caminho(caminho):
    for i in range(len(caminho)):
        print(caminho[i], end="")
        if i < len(caminho) -1:
            print("->", end="")

def vizinhas(palavra, dicionario):
    alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    vizinhas = []
    for i in range(len(palavra)):
        for letra in alfabeto:    
            nova = str(palavra[:i] + letra + palavra[i+1:])
            if nova in dicionario:
                vizinhas.append(nova)
    
    return vizinhas

def wordladder(inicio, fim, dicionario):
    fila = [] #falta visitar
    visitados = set()  
    genealogia = {}  #dicionario com maes e filhas
    
    fila.append(inicio) 
    visitados.add(inicio)
    
    while len(fila) > 0:
        ind = -1
        palavra = fila.pop(0)
        ind+=1
        if palavra == fim:
            print_caminho(caminho(genealogia, inicio, fim))
            return True
        
        for vizinha in vizinhas(palavra, dicionario):
            if vizinha not in visitados:
                visitados.add(vizinha)  
                fila.append(vizinha)  
                genealogia[vizinha] = palavra
                
    
    #Se não houver caminho possível
    print("Não existe caminho possível")
    return False

def main():
    inicio = str(input("Início:")).upper()
    fim = str(input("Fim:")).upper()
    dicionario = cria_dicionario(inicio)
     
    wordladder(inicio, fim, dicionario)
    
main()
    
