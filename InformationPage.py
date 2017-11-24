from base_controller import *
import hashlib

class InformationPage(BaseHandler):
	def get(self):
		try:
			# self.p('Error')
			try:
				arr=self.jd(u' '.join(self.d('json')).encode('utf-8').strip())
				print(str(arr))
				for x in arr:
					print(x+' '+arr[x])
			except Exception as e:
				# raise e
				# print('')
				pass
			self.lp('InformationPage',{'title':self.d('title'),'content':self.d('content'),'json':self.d('json').replace('\n','').replace(' ','')})
		except Exception as e:
			raise e