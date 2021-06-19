# -*- coding: utf-8 -*-
import urllib3
from bs4 import BeautifulSoup
#from urlparse import urlparse 
#from urlparse import urljoin 
from urllib.parse import urljoin
import re
import nltk
import pymysql

def inserePalavraLocalizacao(idurl,idpalavra,localizacao):
    conexao = pymysql.connect(host='localhost',user='root',passwd='',db='indice',autocommit=True)
    cursor = conexao.cursor()
    cursor.execute('insert into palavra_localizacao (idurl,idpalavra,localizacao) values (%s,%s,%s)')
    idpalavra_localizacao = cursor.lastrowid
    cursor.close()
    conexao.close()
    return idpalavra_localizacao




def inserePalavra(palavra):
    conexao = pymysql.connect(host='localhost',user='root',passwd='',db='indice')
    cursor = conexao.cursor()
    cursor.execute('insert into palavras (palavra) values (%s)',palavra)
    idpalavra = cursor.lastrowid
    cursor.close()
    conexao.close()
    return idpalavra

def palavraIndexada(palavra):
    retorno = -1
    conexao = pymysql.connect(host='localhost',user='root',passwd='',db='indice')
    cursor = conexao.cursor()
    cursor.execute('select idpalavra from palavras where palavra =  %s',palavra)
    if cursor.rowcount > 0:
        retorno = cursor.fetchone()[0]
    cursor.close()
    conexao.close()
    return retorno


def inserePagina(url):
    conexao = pymysql.connect(host='localhost',user='root',passwd='',db='indice')
    cursor = conexao.cursor()
    cursor.execute('insert into urls (url) values (%s)',url)
    idpagina = cursor.lastrowid
    cursor.close()
    conexao.close()
    return idpagina



def paginaIndexada(url):
    retorno = -1
    conexao = pymysql.connect(host='localhost',user='root',passwd='',db='indice')
    cursorUrl = conexao.cursor()
    cursorUrl.execute('select idurl from urls where url = %s ',url)
    if cursorUrl.rowcount > 0:
        idurl = cursorUrl.fetchone()[0]
        cursorPalavra = conexao.cursor()
        cursorPalavra.execute('select idurl from palavra_localizacao where idurl = %s',idurl)
        if cursorPalavra.rowcount > 0:
            retorno = -2
        else:
            retorno = idurl
        cursorPalavra.close()


    cursorUrl.close()
    conexao.close()
def separaPalavras(texto):
    stop = nltk.corpus.stopwords.words('portuguese')
    stemmer = nltk.stem.RSLPStemmer() #extrai o radical da palavra
    splitter = re.compile('\\W+')
    lista_palavra = []
    lista = [p for p in splitter.split('Este lugar é apavorante abc c++') if p != '']
    for p in lista:
        if p.lower() not in stop:
            if len(p) > 1:
                lista_palavra.append(stemmer.stem(p).lower())


    return lista_palavra


def getTexto(sopa):
    for tags in sopa(['script','style']):
        tags.decompose()
    return ' '.join(sopa.stripped_strings)

def indexador(url, sopa):
    indexada = paginaIndexada(url)
    if indexada == -2:
        print('url já indexada')
        return
    elif indexada == -1:
        idnova_pagina = inserePagina(url)
    elif indexada > 0:
        idnova_pagina = indexada
    print('indexando'+url)
    texto = getTexto(sopa)
    palavras = separaPalavras(texto)
    for i in range(len(palavras)):
        palavra = palavras[i]
        idpalavra = palavraIndexada(palavra)
        if idpalavra == -1:
            idpalavra = inserePalavra(palavra)
        inserePalavraLocalizacao(idnova_pagina,idpalavra,i)




def crawl(paginas):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    novas_paginas = set()
    for pagina in paginas:
        http = urllib3.PoolManager()
        try:
            dados_pagina = http.request('GET',pagina)
        except:
            print('Erro ao acessar a página: ' + pagina)
        sopa = BeautifulSoup(dados_pagina.data,'lxml') #python2 remove lxml
        links = sopa.find_all('a')
        contador = 1
        for link in links:
            if('href' in link.attrs):
                url = urljoin(pagina, str(link.get('href')))

                if url.find("'") != -1:
                    continue
                url = url.split('#')[0]

                if url[0:4] == 'http':
                    novas_paginas.add(url)
                print(url)
                contador +=1

        paginas = novas_paginas
        print("Count:",contador)
        print(paginas)
        print("Nº de Links:",len(paginas))



teste = set()


teste.add('a')
teste.add('b')
teste.add('a')

print(type(teste))

listapaginas = ['https://pt.wikipedia.org/wiki/Linguagem_de_programa%C3%A7%C3%A3o']
crawl(listapaginas)


