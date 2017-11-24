# import webapp2
# from webapp2_extras import sessions

# from google.appengine.api import users
# import logging
# from jinja2 import *

# import xml.etree.ElementTree as ET
# # import dicttoxml

# # import requests
# import urllib2 as urllib

# import json
# class BaseHandler(webapp2.RequestHandler):
# 	def ini(self):
# 		u=self.google_users()
# 		self.loadPage('menu',{})
# 		return u
# 	# def dispatch(self):
# 	# 	self.session_store = sessions.get_store(request=self.request)
# 	# 	try:
# 	# 		webapp2.RequestHandler.dispatch(self)
# 	# 	finally:
# 	# 		self.session_store.save_sessions(self.response)
# 	@webapp2.cached_property
# 	def session(self):
# 		return self.session_store.get_session()

# 	def html(self,html):
# 		env = Environment(loader=PackageLoader('main', 'templates'))
# 		template = env.get_template(page_name+'.html')
# 		string = template.render(page_value)
# 		return string
# 	def loadPage(self,page_name,page_value):
# 		env = Environment(loader=PackageLoader('main', 'templates'))
# 		template = env.get_template(page_name+'.html')
# 		string = template.render(page_value)
# 		self.response.out.write(string)
# 	def p(self,page_name,page_value):
# 		self.loadPage(page_name,page_value)
# 	# def post(self):
# 	# 	self.response.out.write('empty post response')
# 	def google_users(self):
# 		user = users.get_current_user()
# 		if user:
# 			url = users.create_login_url(self.request.path)
# 			self.response.write('<a href="'+url+'">Log out</a>')
# 		else:
# 			logging.info('No user currently logged in')
# 			uri = users.create_login_url(self.request.uri)
# 			self.redirect(uri)
# 		return user
# 	def get_Login_user(self):
# 		user = users.get_current_user()
# 		if user:
# 			return user
# 		else:
# 			return 'UnknownUser'
# 	def get_login_email(self):
# 		user = users.get_current_user()
# 		if user:
# 			return user
# 		else:
# 			return None

# 	def xml_decode(self,xml_str):
# 		return ET.fromstring(xml_str)
# 	def xd(self,xml_str):
# 		return self.xml_decode(xml_str)
# 	# def xml_encode(self,arr):
# 	# 	xml_str = dicttoxml.dicttoxml(arr)
# 	# 	return xml_str
# 	# def xe(self,arr):
# 	# 	self.xml_encode(arr)

# 	def getRequest(self,url):
# 		try:
# 			content = urllib.urlopen(url).read()
# 			return content
# 		except Exception:
# 			msg_error = 'URL Error occurred'

# 	def gr(self,url):
# 		self.getRequest(url)

# 	def lo_url(self):
# 		return users.create_logout_url(self.request.path)

# 	def jd(self,jt):
# 		# print jt
# 		return json.loads(str(jt))
# 	def je(self,array):
# 		return json.dumps(array, sort_keys=True,indent=4, separators=(',', ': '))


import webapp2
from webapp2_extras import sessions

from google.appengine.api import users
import logging
from jinja2 import *

import xml.etree.ElementTree as ET
# import dicttoxml

# import requests
import urllib2 as urllib

import json
class BaseHandler(webapp2.RequestHandler):
	def p(self,str):
		self.response.out.write(str)
	def ini(self):
		u=self.google_users()
		self.loadPage('menu',{})
		return u
	# def dispatch(self):
	# 	self.session_store = sessions.get_store(request=self.request)
	# 	try:
	# 		webapp2.RequestHandler.dispatch(self)
	# 	finally:
	# 		self.session_store.save_sessions(self.response)
	@webapp2.cached_property
	def session(self):
		return self.session_store.get_session()
	def s(self,k='',v=''):
		if v=='':
			self.session.get(k)
		else:
			self.session[k]=v

	def html(self,html):
		env = Environment(loader=PackageLoader('main', 'templates'))
		template = env.get_template(page_name+'.html')
		string = template.render(page_value)
		return string
	def loadPage(self,page_name,page_value):
		env = Environment(loader=PackageLoader('main', 'templates'))
		template = env.get_template(page_name+'.html')
		string = template.render(page_value)
		self.response.out.write(string)
	def lp(self,page_name,page_value):
		self.loadPage(page_name,page_value)
	# def post(self):
	# 	self.response.out.write('empty post response')
	def google_users(self):
		user = users.get_current_user()
		if user:
			url = users.create_login_url(self.request.path)
			self.response.write('<a href="'+url+'" style="color: yellow;">Log out</a>')
		else:
			logging.info('No user currently logged in')
			uri = users.create_login_url(self.request.uri)
			self.redirect(uri)
		return user
	def get_Login_user(self):
		user = users.get_current_user()
		if user:
			return user
		else:
			return 'UnknownUser'
	def get_login_email(self):
		user = users.get_current_user()
		if user:
			return user
		else:
			return None

	def xml_decode(self,xml_str):
		return ET.fromstring(xml_str)
	def xd(self,xml_str):
		return self.xml_decode(xml_str)
	# def xml_encode(self,arr):
	# 	xml_str = dicttoxml.dicttoxml(arr)
	# 	return xml_str
	# def xe(self,arr):
	# 	self.xml_encode(arr)

	def getRequest(self,url):
		try:
			content = urllib.urlopen(url).read()
			return content
		except Exception:
			msg_error = 'URL Error occurred'

	def gr(self,url):
		return self.getRequest(url)

	def lo_url(self):
		return users.create_logout_url(self.request.path)

	def jd(self,jt):
		# print jt
		return json.loads(str(jt))
	def je(self,array):
		return json.dumps(array, sort_keys=True,indent=4, separators=(',', ': '))

	def api(self,url,_type='j'):
		r=self.gr(url)

		# print(r)
		if _type=='j':
			return self.jd(r)
		if _type=='x':
			return self.xd(r)
	def p_api(self,url,_type='j'):
		if _type=='j':
			self.p(str(self.api(url,_type)))
		else:
			return self.api(url,_type)
	def para(self,value):
		return self.request.get(value)
	def d(self,value):
		return self.para(value)
			# print(vars())





















