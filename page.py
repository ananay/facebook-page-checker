# -*- coding: utf-8 -*-
# @Author: ananayarora
# @Date:   2017-02-11 11:55:52
# @Last Modified by:   ananayarora
# @Last Modified time: 2017-02-11 13:12:41

import urllib2
from flask import Flask, render_template, request, url_for



def process(url):
	try:
		response = urllib2.urlopen('https://facebook.com/'+url)
		page_source = response.read()
		arr = page_source.split('entity_id')
		pageid = arr[1][3:50].split('"}]')[0]
		count = page_source.count(pageid)
		if (count > 1):
			return "The page is live."
		else:
			return "The page exists, but is hidden."
		pass
	except urllib2.HTTPError, e:
		if (e.code == 404):
			return "The page doesn't exist."

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/check', methods = ['POST', 'GET'])
def check():
	return process(request.form['url'])

if __name__ == "__main__":
	app.run()