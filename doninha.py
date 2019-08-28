import random
characters = [" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
static_size = 28
high_score = -100
id_high_score = 0
target_string = 'METHINKS IT IS LIKE A WEASEL'
probability = [("CHANGE", 5), ("CONTINUE", 95)]
probability_list = [prob for prob, p in probability for i in range(p)]
aux_list = []
cont = 0 

def _calcutating(string_copies):#string == cópias
    high_score = -100
    for k in range(len(string_copies)):
        score = 0
        aux_list.clear()
        aux_text = ""
        for i in range(static_size):
            aux_list.append(random.choice(probability_list))

        #conferindo as posicoes que contem "CHANGE" para mudar o caracter naquela mesma posição
        for j in range(28):
            if(aux_list[j] == "CHANGE"):
                aux_char = random.choice(characters)
                aux_text+=aux_char
            else:
                aux_text+=string_copies[k][j]

        string_copies[k] = aux_text

        #Compare cada nova seqüência de caracteres com a frase alvo "METHINKS IT IS LIKE A WEASEL", 
        #e dê a cada cópia gerada uma pontuação (número de letras na sequência e na posição correta).
        for l in range(28):
            if (target_string[l] == string_copies[k][l]):
                score += 1

        if score > high_score:
            high_score = score
            id_high_score = k
            random_string = string_copies[k]
        
    
    if (high_score == 28):
        print(string_copies[id_high_score])
    else:
        _reproduce(random_string)
    
    print("Generation =", string_copies[k])


#criando 100 cópias dessa sequência
def _reproduce(string):
    string_copies = []
    for i in range(100):
        string_copies.append(string)
    _calcutating(string_copies)


#iniciando com uma sequencia aleatoria
random_string = ""
for i in range(static_size):
    random_string += random.choice(characters)
_reproduce(random_string)

