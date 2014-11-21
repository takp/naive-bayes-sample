# -*- coding: utf-8 -*-
import urllib
import urllib2
from bs4 import BeautifulSoup

appid = 'YOUR_APP_ID'
pageurl = "http://jlp.yahooapis.jp/MAService/V1/parse" # yahoo API

# Return the result of Yahoo Japanese Morphological Anaylysis API
def split(sentence, appid=appid, results="ma", filter="1|2|3|4|5|9|10"):
	sentence = sentence.encode("utf-8")
	params = urllib.urlencode({'appid':appid, 'results':results, 'filter':filter, 'sentence':sentence })
	# 形態素解析の結果をresultsに入れる
	results = urllib2.urlopen(pageurl, params)
	# 結果をBeautifulSoupでパース
	soup = BeautifulSoup(results.read())

	return [w.surface.string for w in soup.ma_result.word_list] # Return List
