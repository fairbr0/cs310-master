from summarize import *
import nltk

orig = open('../resources/bodies/article1processed.txt', 'r').read()

print orig

tokens = getWordsAsTokens(orig)

nonstops = removeStopWords(tokens, stop_words)

normalized = normalize(nonstops)

tagged = nltk.pos_tag(normalized)

filtered = wfilter(normalized)

graph = buildWordGraph(filtered, 2)

ranked = getRankedKeyphrases(orig)

r = ranked[:10]

recovered = recoverKeywords(r, orig)

output = orig + '\n\n' + str(tokens) + '\n\n' + str(nonstops) + '\n\n' + str(normalized) + '\n\n' + str(tagged) + '\n\n' + str(filtered) + '\n\n' + str(ranked) + '\n\n' + str(recovered)

out = open('./demo.txt', 'w')
out.write(output)

