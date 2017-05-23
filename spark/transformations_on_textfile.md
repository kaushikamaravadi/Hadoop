# Transformations on textFile

### Convert all words in a rdd to lowercase and split the lines of a document using space.

>>> def func(lines): 
...     lines = lines.lower()
...     lines = lines.split()
...     return lines
... 
>>> use1 = use.map(func)

>>> use2 = use.flatMap(func)
>>> use2.take(2)
[u'all', u'of']

###  Next, I want to remove the words, which are not necessary to analyze this text. We call these words as “stop words”; Stop words do not add much value in a text. For example, “is”, “am”, “are” and “the” are few examples of stop words.

>>> stopwords = ['is','am','are','the','for','a','of']
>>> use3 = use2.filter(lambda x: x not in stopwords)
>>> use3.take(5)
[u'all', u'above', u'explains', u'why', u'it\u2019s']

## Transformation: groupBy

### After getting the results into rdd3, we want to group the words in rdd3 based on which letters they start with. For example, suppose I want to group each word of rdd3 based on first 3 characters.

>>> use4 = use3.groupBy(lambda w: w[0:3])
>>> print [(k, list(v)) for (k,v) in use4.take(1)]
[(u'all', [u'all'])]
>>> use3_mapped =use3.map(lambda x: (x,1))
>>> use3_grouped = use3_mapped.groupByKey()
>>> print(list((j[0], list(j[1])) for j in use3_grouped.take(5)))
[(u'all', [1]), (u'rdds.', [1]), (u'have', [1]), (u'type-safety', [1]), (u'when', [1, 1])]
>>> use3.filter(lambda x: x == 'all').collect()
[u'all']
>>> use3.filter(lambda x: x == 'when').collect()
[u'when', u'when']
>>> use3.filter(lambda x: x == 'rdds.').collect()
[u'rdds.']
>>> use3_freq_of_words = use3_grouped.mapValues(sum).map(lambda x: (x[1],x[0])).sortByKey(False)
>>> use3_freq_of_words.take(10)
[(4, u'you'), (4, u'to'), (4, u'that'), (3, u'use'), (3, u'in'), (2, u'when'), (2, u'want'), (2, u'api,'), (2, u'might')
, (2, u'python')]
