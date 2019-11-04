#HW-2 task2
S=int(input("Enter your price of a croissant: ")) 
D=int(input("Enter days: "))
price = 50 # Стоимость круассана --- 50 р.
delivery = 500 #Разовая доставка неограниченного числа круассанов от дверей "Перекрестья" до школы №1 --- 500 р.
profit = 0 #прибыль
revenue=0 #выручка
cost = 0 #издержки 
cost_buy=0 #затраты на покупку 
cost_delivery = 0 #затраты на перевозку до школы
babka = 300 #Стоимость помощи бабки на входе с разгрузкой машины (за 1 коробку круассанов) --- 300 р. 
cost_babka = 0 #Затраты на бабку 
for i in range(D):
  AB=input("Enter the number of croissants bought and sold").split()
  A = int(AB[0])     #количество купленных круассанов
  B = int(AB[1])     #количество проданных круассанов
  revenue+=S*B  #прибавление выручки за каждый день
  cost_buy += A * price
  cost_delivery+=delivery
  boxes = A//25
  cost_babka += boxes * babka 
cost = cost_buy + cost_delivery + cost_babka
profit = revenue - cost
if (profit/revenue>0.3):
  print("YES")
else:
  print("NO")
