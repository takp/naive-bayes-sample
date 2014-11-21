# naive-bayes-sample

Naive Bayes sample program.

infer the category of the document. 

### Before Run

It's needed to install the "BeautifuSoup" : http://www.crummy.com/software/BeautifulSoup/

This App using "Yahoo morphological analysis API".
http://developer.yahoo.co.jp/webapi/jlp/ma/v1/parse.html

If you want to use in English, please modify the 'morphological.py'.

### Run

	$ python naivebayes.py

### Reference

http://gihyo.jp/dev/serial/01/machine-learning/0003?page=1

### Naive Bayes

	P(cat, doc) = P(cat|doc)P(doc) = P(doc|cat)P(cat)

	=> P(cat|doc) = P(doc|cat)P(cat) / P(doc)

now, we can get the P(cat|doc) by calculationg (1) P(doc|cat) and (2) P(cat).

(1) P(doc|cat)

	p(doc|cat) = P(word1|cat)P(word2|cat)...P(wordn|cat)

By the assumption of independence, it is possible to approximate to this function, as documents is the aggregation of the words.

	P(word|cat) = ( number of word shows up in the category ) / ( number of all words )

(2) P(cat)

	P(cat) = ( number of (this) category shows up (in train data) ) / ( number of all train data )

* Using Logarithm

It is needed to use logarithm because the value of every P() is so small that it may cause Underflow.

So we convert the multiply to sum of logs.

	P(doc|cat)P(cat)
	= P(word1|cat)P(word2|cat)...P(wordn|cat)P(cat)
	= log P(word1|cat) + log P(word2|cat) + ... + log P(wordn|cat) + log P(cat)
