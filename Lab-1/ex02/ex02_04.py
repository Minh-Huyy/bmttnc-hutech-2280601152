#tao list
j = []
#Duyet tu 2000 -> 3200 kiem tra xem i co chia het cho 7 va la` boi. cua 5 hay khong
for i in range(2000 , 3201):
    if(i % 7 ==0 ) and (i % 5 !=0):
        j.append(str(i))
print (','.join(j))