# Doninha

Embora Dawkins não forneceu o código-fonte de seu programa, um algoritmo no estilo "Weasel" pode ser executado da seguinte maneira:

Inicie com uma seqüência aleatória de 28 caracteres (frase).
Faça 100 cópias da seqüência inicial de caracteres (reprodução).
Para cada caracteres, em cada uma das 100 cópias, substituía (mutação), com uma probabilidade de 5%, o caracteres por um novo caractere aleatório.
Compare cada nova seqüência de caracteres com a frase alvo "METHINKS IT IS LIKE A WEASEL", e dê a cada cópia gerada uma pontuação (número de letras na sequência e na posição correta).
Se alguma das novas sequências de caracteres (frases) tiver uma pontuação perfeita (28, todas as letras na sequência e posição corretas), pare. Caso contrário, pegue a frase de maior pontuação e recomece da etapa 2.
Nest algoritmo, uma "caractere" é qualquer letra maiúscula ou um espaço. O número de cópias por geração, e a chance de mutação por caractere não são especificados no livro do Dawkins. 100 cópias e 5% de taxa de mutação são exemplos. Letras corretas não são "travadas". Cada letra correta pode tornar-se incorreta em gerações subsequentes. Os termos do programa e a existência da frase alvo não significa que  'mutações negativas" vão ser 'corrigidas' rapidamente.
