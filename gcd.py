# Rahman ve Rahim olan ALLAH'ın Adıyla,
#
# Dayının Dut Yiyenine ;)

def ebob (a,b):
	if(a == b):
		return a
	if(a>b):
		return ebob(a-b,b) 
	else:
		return ebob(a,b-a) 

def gcd(a,b):
	print(str(a) + " ile " + str(b) + "'in ebobu : " + str(ebob(a,b)))

gcd(120,180)
gcd(150,200)
gcd(200,250)

devam = "y"

while(devam != "x"):
	a = int(input("Selam, ebobunu almak istediğin sayıların ilkini gir"))
	b = int(input("lkincisini gir: "))
	gcd(a,b)
	devam  = input("çıkmak için 'x' devam için 'd' gir: ")