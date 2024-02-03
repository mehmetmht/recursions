# Rahman ve Rahim olan ALLAH'ın Adıyla,
#
# Dayının Dut Yiyenine ;)

def toplam (n):
	if(n == 0):
		return 0
	if(n>0):
		return toplam(n-1) + n 
	else:
		return toplam(n+1) + n 

def topla(n):
	if(n>0):
		print("0'dan " + str(n) + "'e kadar olan sayıların toplamı: " + str(toplam(n)))
	else:
		print(str(n) + "'den 0 kadar olan sayıların toplamı: " + str(toplam(n)))
		
topla(10)

topla(-9)