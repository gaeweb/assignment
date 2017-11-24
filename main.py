from base_controller import *
from time import gmtime, strftime
import datetime
import logging
import hashlib

from InformationPage import *

class MainHandler(BaseHandler):
	def get(self):
		self.ini()

	def getRequestParameter(parameters):
		string='?'
		isBegin=False
		for x in parameters:
			if isBegin:
				string+='&'
			string+=x[0]+'='+x[1]
			isBegin=True
		print(string)
		return string
		# print(str(self))
		# print(vars(self))
		# print(vars(self.request))
		self.ini()
		
		Place=[]
		c=0
		data=''
		
		def request_1():
			ses_Num='1'
			if self.session[ses_Num]!=None:
				return self.session[ses_Num]
			try:
				self.session['1'] = self.api('http://www2.lcsd.gov.hk/php/gen_xml_to_psi/xml/venues.xml','x')
				return self.session['1']
			except Exception as e:
				return request_1()
		data=request_1()
		for x in data._children:
			c+=1
			if c>10:
				break
			ar={}
			ar['venuec']=x.find('venuec').text
			ar['venuee']=x.find('venuee').text
			Place.append(ar)

		events=[]
		c=0
		try:
			def request_menu():
				ses_Num='2'
				if self.s(ses_Num)!=None:
					return self.s(ses_Num)
				try:
					self.session['2'] = self.api('http://www2.lcsd.gov.hk/php/gen_xml_to_psi/xml/events.xml','x')
					return self.session['2']
				except Exception as e:
					return request_menu()
			data=request_menu()
			
			#data=self.api('localhost:8080/events.xml','x')
			#data=self.api('http://www2.lcsd.gov.hk/php/gen_xml_to_psi/xml/even','x')

			for x in data._children:
				c+=1
				if c>10:
					break
				ar={}
				try:
					# ar['titlec']=x.find('titlec').text.replace("'",'',100).replace('"','',100)
					ar['titlee']=x.find('titlee').text.replace("'",'',100).replace('"','',100).replace('\u','',100)
					# ar['predateC']=x.find('predateC').text.replace("'",'',100).replace('"','',100)
					ar['predateE']=x.find('predateE').text.replace("'",'',100).replace('"','',100).replace('\u','',100)

					# ar['xml']=self.xe(x)
					# print('xml: '+ar['xml'])
					# ar['submitdate']=x.find('submitdate').text
					# ar['presenterorgc']=x.find('presenterorgc').text
					# ar['tagenturlc']=x.find('tagenturlc').text
					# ar['progtimec']=x.find('progtimec').text



					ar['href']=x.find('urlc').text.replace('\u','',100)
					ar['getrequestlink']='InformationPage/?md5='+hashlib.md5(ar['titlee']+ar['predateE']).hexdigest()

					ar['json']=self.je(ar)
						

				except Exception as e:
					# raise e
					pass
				


				# ar['getrequestlink']='/'+'?'+'titlec'+'='+ar['titlec']+'&'+'titlee'+'='+ar['titlee']+'&'+'predateC'+'='+ar['predateC']+'&'+'predateE'+'='+ar['predateE']
				# ar['getrequestlink'].encode('ascii')
				# print(ar['getrequestlink'])

				# getRequestParameter({
				#	 'titlec':ar['titlec'],
				#	 'titlee':ar['titlee'],
				#	 'predateC':ar['predateC'],
				#	 'predateE':ar['predateE'],
				#	 # 'submitdate':ar['submitdate'],
				#	 # 'presenterorgc':ar['presenterorgc'],
				#	 # 'presenterorge':ar['presenterorge'],
				#	 # 'urlc':ar['urlc'],
				#	 # 'tagenturlc':ar['tagenturlc'],
				#	 # 'progtimec':ar['progtimec'],
				#	 # 'progtimee':ar['progtimee']
				#	 })
				events.append(ar) 
				# print(self.je(events))
		except Exception as e:
			# raise e
			pass







		facility=[]
		def request_3():
			ses_Num='3'
			if self.session[ses_Num]!=None:
				return self.session[ses_Num]
			try:
				self.session['3'] = self.api('http://www.lcsd.gov.hk/datagovhk/facility/facility-bbqs.json','j')
				return self.session['3']
			except Exception as e:
				return request_3()
		data=request_3()
		c=0
		for a in data:
			c+=1
			if c>5:
				break
			ar={}
			ar['i']=str(c)
			ar['title']=a['Name_en']
			ar['content']=a['District_en']+'<br>'+'<br>'+a['Address_en']+'<br>'+a['Facilities_en']
			long_arr=a['Longitude'].split('-')
			ar['longitude']=str(long_arr[0])
			# +'.'+str(long_arr[1])
			# +str(long_arr[2])
			latit_arr=a['Latitude'].split('-')
			ar['latitude']=str(latit_arr[0])
			# +'.'+str(latit_arr[1])
			# +str(latit_arr[2])
			facility.append(ar)
		# print('facility: '+str(len(facility)))

		# print vars(self)
		qr_data='http://'
		request_arr=str(self.request).split('\n')
		for x in request_arr:
			
			ar=str(x).split(':')
			if ar[0]=='Host':
				print '[[['
				qr_data='http://'+(ar[1]+':'+ar[2]).replace(' ','')
				print ']]]'
		# print str(self.request)
		
		self.lp('page_main',{'Place':Place,'events':events,'facility':facility,'qr_data':qr_data})
		# self.redirect('/newsfeed/index.html')
		# self.response.write('''<center><h1 style="">Current Date Time: <br>'''+strftime("%Y-%m-%d %H:%M:%S", gmtime())+'''</h1></center>''')

		

app = webapp2.WSGIApplication([
	('/', MainHandler),
    ('/InformationPage/',InformationPage)
	# ('/p1', P1),
	# ('/p_book', p_book),
	# ('/p3', p3),
	# ('/name', RememberNameHandler),
	# ('/topic', RememberTopicHandler),
	# ('/location', LocationHandler),

], debug=True, config={'webapp2_extras.sessions':{'secret_key':'my-super-secret-key'}})
