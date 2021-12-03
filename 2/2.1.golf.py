a,b=zip(*[[int(x[-2]),0]if x[0]=='f'else[0,int(x[-2])*-1]if x[0]=='u'else[0,int(x[-2])] for x in open('i')])
print(sum(a)*sum(b))