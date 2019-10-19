budget = int(input("Enter budget: "))
scott=int(input("Enter number heads of scott: "))
bullPrice = 20
cowPrice = 10
calfPrice = 5

bullNumber = 0
cowNumber = 0
calfNumber = 0

for bullNumber in range(1, int(budget/bullPrice+1)):
#  print("bull: ", bullNumber) #otladka
  ostBudget=budget-bullNumber*bullPrice
  if ostBudget>0:
#    print("ostatok: ", ostBudget) #otladka
    for cowNumber in range (int(ostBudget/cowPrice+1),-1,-1 ):
#      print(" cow: ", cowNumber) #otladka
      finalBudget = ostBudget - cowNumber * cowPrice
#      print("ostatok: ", finalBudget) #otladka
      if finalBudget>0:
        for calfNumber in range (0,int(finalBudget / calfPrice)+1):
#          print("calf: ", calfNumber)#otladka
          if ((bullNumber+cowNumber+calfNumber)==scott) and ((bullNumber*bullPrice+cowNumber*cowPrice+calfNumber*calfPrice)==budget):
            print(bullNumber,cowNumber,calfNumber)
      elif  ((bullNumber+cowNumber+calfNumber)==scott) and ((bullNumber*bullPrice+cowNumber*cowPrice+calfNumber*calfPrice)==budget):
        print(bullNumber,cowNumber,calfNumber)
  elif ((bullNumber+cowNumber+calfNumber)==scott) and ((bullNumber*bullPrice+cowNumber*cowPrice+calfNumber*calfPrice)==budget):
    print(bullNumber,cowNumber,calfNumber)
