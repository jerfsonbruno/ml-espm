#
# Para todo algoritmo de classificacao (entre eles, algoritmos de tag)
# eh necessario uma medida ou metedo de avaliacao.
#
# Felizemente, os atomos dos corpus utilizados para a tarefa de
# aprendizado jah estao demarcados com as suas tags. Sendo assim,
# estes corpus podem ser utilizados tambem para a avaliacao dos
# algoritmos de tags.
#

# um exemplo simples

from nltk.tokenizer import *
from nltk.tagger import *
from nltk.corpus import brown

# fase de treinamento

train_tokens = []
for item in brown.items()[:10]:
    train_tokens.append(brown.read(item))

mytagger = UnigramTagger(SUBTOKENS='WORDS')
for tok in train_tokens: mytagger.train(tok)

# utilizacao

text_token = Token(TEXT="John saw the book on the table")
WhitespaceTokenizer(SUBTOKENS='WORDS').tokenize(text_token)
mytagger.tag(text_token)
print text_token

#
# depois de criado o mytagger podemos testa-lo
# com um corpus. Por exemplo, train_tokens
#

acc = tagger_accuracy(mytagger, train_tokens)
print 'Accuracy = %4.1f%%' % (100 * acc)

#
# Eh claro que ao utilizarmos o mesmo corpus para
# treinamento e testes a performance do algoritmo
# serah alta e nao real
#
# Para realmente validarmos o algoritmo de taggers
# temos que utilizar um corpus para treinamento e 
# outro para testes.
#

train_tokens = []
for item in brown.items()[:10]: # texts 0-9
	train_tokens.append(brown.read(item))
unseen_tokens = []
for item in brown.items()[10:12]: # texts 10-11
	unseen_tokens.append(brown.read(item))	

for tok in train_tokens: mytagger.train(tok)
acc = tagger_accuracy(mytagger, unseen_tokens)
print 'Accuracy = %4.1f%%' % (100 * acc)

