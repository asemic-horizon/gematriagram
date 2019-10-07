from gematria import gematria, gematrix
from random import choice, randint
import sys
from itertools import product
sys.setrecursionlimit(3000)
with open('milleplateaux.txt') as f: corpus = f.readlines()
corpus = ''.join(corpus)
corpus = corpus.strip("\n")
corpus = corpus.replace(",","#").replace(".","#").replace(";","#")
corpus = corpus.split("#")

filter_word = lambda word: ''.join([i for i in word if i.isalpha()])
corpus = ['$'.join([filter_word(word).lower() for word in phrase]) for phrase in corpus]
corpus = [phrase.replace("$$"," ").replace("$","") for phrase in corpus]
first_corpus = corpus
corpus +=[f"{p} {q}" for p,q in zip(first_corpus,first_corpus[1:])]
corpus +=[f"{p} {q} {r}" for p,q,r in zip(first_corpus,first_corpus[1:],first_corpus[2:])]

max_len = max(len(phrase) for phrase in corpus)
min_word_len = min(len(phrase) for phrase in corpus)

async def get_similar(candidate: str):
    code = gematrix(candidate)
    ans = [phrase for phrase in corpus if gematrix(candidate) == code]
    return ans

async def make_similar(candidate: str):
    similar = await get_similar(candidate)
    m = len(candidate.split(' '))
    alevel = 0
    while similar ==[] and m>3:
        alevel +=1
        print(f"Attempt: {alevel}")
        m -= 1
        words = candidate.split(' ')
        candidate = ' '.join(words[:m])
        similar = get_similar(candidate)
    if len(similar)>0:
        return choice(list(similar))
    else:
        return None

async def find_similar(candidate: str, rlevel = 0):

    p = len(candidate)
    if p< max_len:
        similar = await make_similar(candidate)
    else:
        rlevel +=1

        m = len(candidate.split(' '))
        r=1;s=1;

        words = candidate.split(' ')
        left_candidate = ' '.join(words[:r*m//s])
        right_candidate = ' '.join(words[r*m//s:])
        left =  await find_similar(left_candidate, rlevel)
        right = await find_similar(right_candidate, rlevel)
        p = min(len(left),len(right))
        if left and right:
            similar = f"{left}; {right}"
        elif left and not right:
            similar = left
        elif not left and right:
            similar = right
    if similar == [] or similar is None: 
        return ["Silence."]
    else: 
        return similar