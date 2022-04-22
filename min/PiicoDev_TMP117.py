_A=None
from PiicoDev_Unified import *
REG_TEMPC=0
_baseAddr=72
compat_str='\nUnified PiicoDev library out of date.  Get the latest module: https://piico.dev/unified \n'
class PiicoDev_TMP117:
	def __init__(self,bus=_A,freq=_A,sda=_A,scl=_A,address=_baseAddr,asw=_A):
		if type(asw)is list:assert max(asw)<=1 and min(asw)>=0 and len(asw)is 4,'asw must be a list of 1/0, length=4';self.addr=_baseAddr+1*asw[1]+2*asw[2]+3*asw[3];print(self.addr)
		else:self.addr=address
		try:
			if compat_ind>=1:0
			else:print(compat_str)
		except:print(compat_str)
		self.i2c=create_unified_i2c(bus=bus,freq=freq,sda=sda,scl=scl)
	def readTempC(self):
		try:data=self.i2c.readfrom_mem(self.addr,REG_TEMPC,2)
		except:print(i2c_err_str.format(self.addr));return float('NaN')
		tempDataRaw=int.from_bytes(data,'big')
		if tempDataRaw>=32768:return-256.0+(tempDataRaw-32768)*0.0078125
		else:return tempDataRaw*0.0078125
	def readTempF(self):return self.readTempC()*9/5+32
	def readTempK(self):return self.readTempC()+273.15