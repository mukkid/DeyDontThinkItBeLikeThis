import wikipedia
import requests
import re
import os

def getSummary():
	query = raw_input('What you want fo\' rizzle?  ')
	summary = str(wikipedia.summary(query).encode('utf-8'))
	return summary

def jiveIt(summary):

	credentials = {
	"translatetext":summary,
	"translate":"Tranzizzle Dis Shiznit"
	}
	s = requests.session()
	raw = s.post('http://www.gizoogle.net/textilizer.php', data=credentials).content
	keys = re.compile(r"height:250px;\"/>(.*)",re.MULTILINE)
	clean = re.findall(keys, raw)
	return clean[0]

def sayIt(jivizzle):
	os.system("espeak \""+jivizzle+"\"")

if __name__ == "__main__":
	sayIt(jiveIt(getSummary()))