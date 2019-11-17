import os
os.system('rm -rf t.txt')
f1 = open('data/src-temp.txt')
for l in f1:
	l1 = l.rstrip()[12:]
	print(l1)
	os.system('sed -n /'+l1+'/= data/src-train.txt >> t.txt')
f1.close()

l2=''
f2 = open('t.txt')
for l in f2:
	l1 = l.rstrip()
	l2 += l1 + 'd;'
l2 = l2[:-1]
print(l2)
os.system('sed -i "'+l2+'" data/tgt-train.txt')
os.system('sed -i "'+l2+'" data/src-train.txt')
f2.close()
