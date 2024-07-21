f = open("1.txt")
a = [list(map(str, s.split())) for s in f]

maxd10 = 0 #макс детали среди ID, начинающихся на 10
maxr10 = 0 #ID рабочего с макс деталями
maxd50 = 0 #макс детали среди ID, начинающихся на 50
maxr50 = 0 #ID рабочего с макс деталями

for x in range(len(a)):
    if a[x][0][:2] == "10":
        if int(a[x][1]) > maxd10:
            maxd10 = max(maxd10, int(a[x][1]))
            maxr10 = max(maxr10,int(a[x][0]))
    if a[x][0][:2] == "50":
        if int(a[x][1]) > maxd50:
            maxd50 = max(maxd50, int(a[x][1]))
            maxr50 = max(maxr50,int(a[x][0]))
print(maxr50,maxr10)
