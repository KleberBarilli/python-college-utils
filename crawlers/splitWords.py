# -*- coding: utf-8 -*-
import re
import nltk
#nltk.download()


stop = nltk.corpus.stopwords.words('portuguese')
stop.append('é')
splitter = re.compile('\\W+')
lista_palavra = []
lista = [p for p in splitter.split('este lugar é apavorante') if p != '']
for p in lista:
    if p.lower() not in stop:
        if len(p) > 1:
                lista_palavra.append(p)

print(len(stop))
print(lista_palavra)    