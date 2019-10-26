import sklearn.model_selection as sms
import os
X = []
Y = []
with open('wav.txt', 'r') as f:
    with open('txt.txt', 'r') as t:    
        for i in f.readlines():
            X.append(i)
        for i in t.readlines():
            Y.append(i)

X_train, X_test, Y_train, Y_test = sms.train_test_split(X,Y,test_size=0.2,random_state=1)
X_train, X_val, Y_train, Y_val = sms.train_test_split(X_train,Y_train,test_size=0.2,random_state=1)

R = []
_dict = {}
def Merge(dict1, dict2): 
    res = {**dict1, **dict2} 
    return res 

val = {}      
with open('line_index.tsv','r') as f:
    D = f.readlines()
    for i in D:
        R.append(i.split('\t'))
        val[i.split('\t')[0]] = i.split('\t')[1]
        _dict = Merge(_dict, val)
        val.clear()
    #print(_dict)
#_dict['a'] = '1'
#print(_dict)
#print(_dict['a'])

with open('src-train.txt', 'w') as f:
    with open('tgt-train.txt', 'w') as f2:
        for i in X_train:
            #line = i.rstrip()+ ' ' + _dict[i[:-5]]
            f.write(i)
            f2.write(_dict[i[:-5]])

with open('src-val.txt', 'w') as f:
    with open('tgt-val.txt', 'w') as f2:
        for i in X_val:
            #line = i.rstrip()+ ' ' + _dict[i[:-5]]
            f.write(i)
            f2.write(_dict[i[:-5]])

with open('src-test.txt', 'w') as f:
    with open('tgt-test.txt', 'w') as f2:
        for i in X_train:
            #line = i.rstrip()+ ' ' + _dict[i[:-5]]
            f.write(i)
            f2.write(_dict[i[:-5]])

#for i in X_train:
 #   os.system('mv '+i.rstrip()+' train/wav/')

#for i in X_val:
 #   os.system('mv '+i.rstrip()+' val/wav/')

#for i in X_test:
    #os.system('mv '+i.rstrip()+' test/wav/')
