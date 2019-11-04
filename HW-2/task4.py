#task4 try 1
budget = int(input("Enter budget: "))
scott=int(input("Enter number heads of scott: "))
bullPrice = 20
cowPrice = 10
calfPrice = 5
bullNumber = 0
cowNumber = 0
calfNumber = 0
for bullNumber in range(1, int(budget/bullPrice+1)):
  calfNumber = int((10*bullNumber+10*scott-budget)/5)
  if (calfNumber>0) and (bullNumber+calfNumber<scott):
    cowNumber = scott - bullNumber - calfNumber
    if ((bullNumber+cowNumber+calfNumber)==scott) and ((bullNumber*bullPrice+cowNumber*cowPrice+calfNumber*calfPrice)==budget):
      print(bullNumber,cowNumber,calfNumber) 
