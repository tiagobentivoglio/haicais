# gerador de haicais

Trata-se de um programa para mimetizar haicais, poemas tradicionais japoneses caracterizados pela forma breve e pelas imagens que evocam fenômenos da natureza e estados de espírito.

Há duas funções: uma que gera o primeiro verso e outra que gera um verso que não é o primeiro (ou seja, é usada para gerar o segundo e o terceiro).
A primeira função seleciona aleatoriamente um verso da base de versos de haicais e mapeia seu padrão morfossintático. Usamos uma list comprehention de forma que cada elemento da lista seja a tag com informações morfológicas de cada palavra do verso original. Como a lista gerada tem a mesma ordem que as palavras do verso, consideramos que a lista contém também informações sintáticas.

A partir desse padrão (variável tagline), são criadas listas de possibilidades de palavras que se encaixam em cada uma das tags da lista tagline. A primeira palavra do verso é escolhida aleatoriamente entre as possibilidades para aquela posição. A partir da segunda palavra da tagline, inserimos um filtro de similaridade semântica, usando a função similarity do pacote Spacy. A ideia aqui é filtrar as palavras que são muito diferentes da palavra anterior e excluí-las. O parâmetro escolhido foi similaridade acima de 0.3. As palavras que têm similaridade menor que 0.3 são descartadas para aquela posição.

Assim é criado um verso. Com o filtro de similaridade semântica, cria-se alguma coerência interna no verso. É verdade que essa tarefa é relativamente fácil, pois os versos de haicais são em geral curtos, contendo um sintagma ou trechos curtos de orações. Assim, quase sempre obtemos um resultado satisfatório em termos de coerência interna do verso.

A partir do segundo verso, a função para geração muda um pouco. Um passo a mais é adicionado: após seguir todos os passos anteriores para a criação de um verso, inserimos outro filtro para selecionar o primeiro verso que tenha similaridade semântica maior que 0.6 (ou 0.7) que o anterior. Enquanto o novo verso gerado não satisfaz essa condição, o programa fica gerando versos indefinidamente. É esse passo que faz o programa demorar para rodar de vez em quando. O mesmo procedimento é feito para gerar o terceiro verso.

A lista de palavras candidatas a ocupar as posições na tagline vem de outro corpus, que pode ser selecionado de acordo com o tema que se espera do poema gerado. Para o bot no twitter, inserimos uma base de letras de música da Marília Mendonça e outros cantores de sertanejo sofrência. O objetivo foi criar um resultado engraçado para a forma de haicai que foi proposta. Além disso, é necessário considerar que o corpus deve ter um tamanho relativamente longo e, de preferência, ter unidade de temas. Um ótimo exemplo é o conjunto dos sonetos de Camões. São quase duzentos sonetos (ou seja, mais de 2000 versos) falando principalmente sobre um único assunto: amor. O fato de ser de um único autor também ajuda na coerência linguística, que é igualmente importante.

Este modelo foi criado a partir de estudos do pacote Spacy e das possibilidades de uso das informações contidas nas POS tags.

Perfil no Twitter:
https://twitter.com/haicaisofrencia
