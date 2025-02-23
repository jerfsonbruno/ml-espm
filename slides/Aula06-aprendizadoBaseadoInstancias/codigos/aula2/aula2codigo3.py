#
# Neste exemplo eh utilizado a distribuicao de frequencia condicional
# para prever qual eh a palavra X com maior probabilidade de ocorrer apos
# uma palavra Y
#

from nltk.token import *
from nltk.tokenizer import WhitespaceTokenizer
from nltk.probability import ConditionalFreqDist
corpus = Token(TEXT=open('dados/may2001_pdf.torto').read())
WhitespaceTokenizer().tokenize(corpus)
cfdist = ConditionalFreqDist()

context = None # Condicao
for token in corpus['SUBTOKENS']:
	outcome = token['TEXT']
	#dado a condicao context o que vem depois (outcome)
	cfdist[context].inc(outcome)
	print context , outcome
	context = token['TEXT']

# Depois de construido uma distribuicao condicional para o corpus de 
# treinamento, nos podemos usar os valores para encontrar a palavra 
# que mais se adequa ao contexto.

cfdist['form'].max()
cfdist['problems'].max()
cfdist['in'].max()

cfdist['the'].max()
cfdist['the'].freq('form')

