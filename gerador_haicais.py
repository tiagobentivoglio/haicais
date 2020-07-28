import requests
from bs4 import BeautifulSoup
import re
import random
!pip install -U spacy
!python -m spacy download pt_core_news_lg
import spacy
import pt_core_news_lg
import tweepy
import time

arquivo = open('/content/drive/My Drive/Colab Notebooks/haicais.txt')
raw = arquivo.read().lower()
arquivo.close()


base = raw.split('\n')


semente = open('/content/drive/My Drive/Colab Notebooks/sertanejo.txt')
seed = semente.read().lower()
semente.close()

nlp = pt_core_news_lg.load()


def gerador_verso(texto_inicial):

    # escolhe verso aleatório da base de haicais
    rand_linha = random.choice(texto_inicial)

    # cria os objetos spacy
    doc_base = nlp(rand_linha)
    doc_semente = nlp(seed)

    # cria o padrão sintático para ser a base de um novo verso
    tagline  = [(i, i.tag_) for i in doc_base if 'PUNCT' not in i.tag_]

    # lista de novas palavras escolhidas que se tornarão o verso
    novas_palavras = []

    for (word, bla) in tagline:

        # escolhe palavras que se enxaixem no padrão morfológico de cada palavra do verso original
        possibilidades = [i for i in doc_semente if i.tag_ == bla]

        # se não encontrar nenhuma possibilidade, use a palavra do verso original
        if len(possibilidades) == 0:
            possibilidades.append(word)


        # a primeira palavra do novo verso é randômica
        if len(novas_palavras) == 0:
            novas_palavras.append(random.choice(possibilidades))

        # a partir da segunda, é levada em conta a similaridade semântica com a anterior
        else:

            # gera lista de tuplas com palavra candidata à próxima posição e sua similaridade com a anterior
            candidatas = [(i, i.similarity(novas_palavras[-1])) for i in possibilidades]

            try:
                # escolhe aleatoriamente três das candidatas e seleciona a com maior similaridade
                semi = random.choices(candidatas, k=3)
                escolhida = max(semi)

            except IndexError:
                # escolhe a mais próxima semanticamente
                escolhida = max(candidatas)

            finally:    
                # seleciona só a palavra, sem o valor da similaridade            
                novas_palavras.append(escolhida[0])

    # pega todos os elementos da lista e cria um novo verso
    novo_verso = ' '.join([str(i) for i in novas_palavras])

    return novo_verso
            



def proximo_verso(anterior):

    # o próximo verso leva em conta a similaridade semântica com o anterior

    proximo = gerador_verso(base)

    while nlp(proximo).similarity(nlp(anterior)) < 0.6:
        proximo = ''
        proximo = gerador_verso(base)

    return proximo



# gera um poema de teste

um = gerador_verso(base)

dois = proximo_verso(um)

tres = proximo_verso(dois)

print(um)
print(dois)
print(tres)
