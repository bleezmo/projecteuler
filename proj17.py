belowtwenty = ["zero","one","two","three","four","five",\
				"six","seven","eight","nine","ten","eleven","twelve",\
				"thirteen","fourteen","fifteen","sixteen","seventeen",\
				"eighteen","nineteen"]#this counts the zero
bytens = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
hundred = 7
onethousand = 11
def belowhundred(tensplace,onesplace):
	return tensplace + belowtwenty[onesplace]
def abovehundred(hundredsplace,tensplace,onesplace):
	return belowtwenty[hundredsplace]+"hundred"+"and"+belowhundred(tensplace,onesplace)
def main():
	total = 0
	for i in range(1,len(belowtwenty)):
		print("length of:",belowtwenty[i])
		total = total + len(belowtwenty[i])
	for tensplace in bytens:
		print("length of:",tensplace)
		total = total + len(tensplace)
		for onesplace in range(1,10):
			print("length of:",belowhundred(tensplace,onesplace))
			total = total + len(belowhundred(tensplace,onesplace))
	for hundredsplace in range(1,10):
		print("length of:"+belowtwenty[hundredsplace]+"hundred")
		total = total + len(belowtwenty[hundredsplace]+"hundred")
		for i in range(1,len(belowtwenty)):
			print("length of:",belowtwenty[hundredsplace]+"hundred"+"and"+belowtwenty[i])
			total = total + len(belowtwenty[hundredsplace]+"hundred"+"and"+belowtwenty[i])
		for tensplace in bytens:
			print("length of:",belowtwenty[hundredsplace]+"hundred"+"and"+tensplace)
			total = total + len(belowtwenty[hundredsplace]+"hundred"+"and"+tensplace)
			for onesplace in range(1,10):
				print("length of:",abovehundred(hundredsplace,tensplace,onesplace))
				total = total + len(abovehundred(hundredsplace,tensplace,onesplace))
	total = total + len("onethousand")
	print(total)

main()