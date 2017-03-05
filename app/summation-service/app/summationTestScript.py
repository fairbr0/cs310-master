import summarize

for i in range(1, 2):
    print 'processing ' + str(i)
    f = open('../resources/bodies/article' + str(i) + '.txt', 'r')
    content = f.read()

    summary, reduction, keywords = summarize.summarizeTest(content)
    f = open('../resources/summaries/_article' + str(i) + '.txt', 'w')
    f.write(summary + '\n\n' + str(reduction) + '\n\n' + str(keywords))
