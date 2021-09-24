_A=None
from PiicoDev_Unified import *
REG_TEMPC=0
compat_str='\nUnified PiicoDev library out of date.  Get the latest module: https://piico.dev/unified \n'
class PiicoDev_TMP117:
	def __init__(self,bus=_A,freq=_A,sda=_A,scl=_A,addr=72):
		try:
			if compat_ind>=1:0
			else:print(compat_str)
		except:print(compat_str)
		self.i2c=create_unified_i2c(bus=bus,freq=freq,sda=sda,scl=scl);self.addr=addr
	def readTempC(self):
		try:data=self.i2c.readfrom_mem(self.addr,REG_TEMPC,2)
		except:print(i2c_err_str.format(self.addr));return float('NaN')
		tempDataRaw=int.from_bytes(data,'big')
		if tempDataRaw>=32768:return-256.0+(tempDataRaw-32768)*0.0078125
		else:return tempDataRaw*0.0078125
	def readTempF(self):return self.readTempC()*9/5+32
	def readTempK(self):return self.readTempC()+273.15