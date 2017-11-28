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
			self.lp('InformationPage',{
				'titlee':self.d('titlee'),
				'predateE':self.d('predateE')
				,'submitdate':self.d('submitdate')
				,'presenterorgc':self.d('presenterorgc')
				,'tagenturlc':self.d('tagenturlc')
				,'progtimec':self.d('progtimec')
				,'href':self.d('href')

				,'presenterorge':self.d('presenterorge')

				,'pricee':self.d('pricee')
				,'remarkc':self.d('remarkc')
				,'remarke':self.d('remarke')
				,'enquiry':self.d('enquiry')

				,'desce':self.d('desce')
				})
		except Exception as e:
			raise e