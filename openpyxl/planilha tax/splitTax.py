import openpyxl
import re
import nltk


workbook = openpyxl.load_workbook('SCC-CouncilTax-Variances.xlsx')
workbook2 = openpyxl.Workbook()

sheet1 = workbook.active
sheet2 = workbook2.active
_max=200000
ic=3
lines=[]
files=[]
defs_ln=[]
lines_pattern=['','']
ult_cache_nm=[]
caches_call=[]
lista = []
lista_perguntas = []

ic2=2

sheet2['A1']='Question'
sheet2['B1']='Utterences'

utt=[]

while ic < _max:
  #print 'Process utterences:',str(ic)
  #print workbook.get_sheet_names()
  #w==============
  ask1=sheet1['B'+str(ic)].value

  lista_perguntas.append(ask1)
  #a = list(ask1)
  print map(list, ask1)
  stop = nltk.corpus.stopwords.words('english')
  #stemmer = nltk.stem.RSLPStemmer() #extrai o radical da palavra
  splitter = re.compile('\\W+')
  lista_palavra = []
  for i in lista_perguntas:
    listaW = [p for p in splitter.split(a[2]) if p != '']
    for p in listaW:
      if p.lower() not in stop:
        if len(p) > 1:
            lista_palavra.append(p.lower())
            ic2+=1

  #print lista_palavra 



  if ask1== None:
        break
  if ask1.replace(' ','')=='':
        break
  if ask1 in utt:
    pass
  else:
   utt.append(ask1)
  sheet2['A' + str(ic2)].value = ask1
  
  #
  ic += 1
  ic2 += 1

workbook2.save('SCC-CouncilTax-Variances-Done2005.xlsx')