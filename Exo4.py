#NE PAS TOUCHER
co2 = [58, 80, 83, 53, 51, 60, 66, 68]
water = [611, 544, 889, 476, 479, 947, 358, 657, 447, 577, 783]
deforestation = [7107, 5027, 9688, 7173, 5765, 7375, 7716, 8585, 7196, 9169]
agricultural = [8, 9, 11, 15, 11, 11, 8, 5]
plastic = [1392, 2246, 2017, 1336, 2971, 846, 1210, 796, 2426]
renewable = [20, 14, 8, 17, 5, 12, 18, 13]
#NE PAS TOUCHER


import math as m

d = [co2, water, deforestation, agricultural, plastic, renewable]

d_new = [[],[],[],[],[],[]]

#Suppression max et min (creation d'une nouvelle liste sans les max et min)

for i in range(len(d)):

    for k in range(len(d[i])):

        if d[i][k]!=max(d[i]) and d[i][k] != min(d[i]):
            
            d_new[i].append(d[i][k])

#Calcul de moyenne

d_moy = []

for j in range(len(d_new)):

    d_moy.append(sum(d_new[j])/len(d_new[j]))


#Moyennes respectives

co2_moy = m.floor(d_moy[0])
water_moy = m.floor(d_moy[1])
deforestation_moy = m.floor(d_moy[2])
agricultural_moy = m.floor(d_moy[3])
plastic_moy = m.floor(d_moy[4])
renewable_moy = m.floor(d_moy[5])

#Calcul de P et R

P = (co2_moy + (plastic_moy/1000))/2 * (1 - (renewable_moy/100))

R = ((100 - (water_moy/10)) + (100 - (deforestation_moy/100)) + agricultural_moy + renewable_moy)/4


print(str(m.floor(min(P,R))) + "_" + str(m.floor(max(P,R))))