import os
os.system('rm -rf t.txt')
f1 = open('data/src-temp.txt')
for l in f1:
	l1 = l.rstrip()[12:]
	print(l1)
	os.system('sed -n /'+l1+'/= data/src-train.txt >> t.txt')
f1.close()

f2 = open('t.txt')
for l in f2:
	l1 = l.rstrip()
	print(l1)
	os.system('sed -i '+l1+'d data/tgt-train.txt')
	os.system('sed -i '+l1+'d data/src-train.txt')
f2.close()
