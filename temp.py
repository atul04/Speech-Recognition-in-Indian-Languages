'''How to run:

put temp.py parallel to data folder
|-data/
|-temp.py

python3 temp.py txt
python3 temp.py wav
'''
import os, sys
txt_or_wav = sys.argv[1]
os.system('mkdir -p data/ms_dataset/temp/ms/txt')
os.system('mkdir -p data/ms_dataset/temp/ms/wav')
f1 = open('data/src-temp.txt', 'w')
f2 = open('data/tgt-temp.txt', 'w')
os.system('ls data/ms_dataset/train/ms/' + txt_or_wav + ' > temp.txt')
count = 0
for file in open('temp.txt'):
	count += 1
	if count < 2000:
		#print('mv data/ms_dataset/train/ms/' + txt_or_wav + '/' + file.rstrip() + ' data/ms_dataset/temp/ms/'+ txt_or_wav + '/')
		
		if txt_or_wav == 'wav':		
			f1.write('temp/ms/wav/'+file)
			os.system('mv data/ms_dataset/train/ms/' + txt_or_wav + '/' + file.rstrip() + ' data/ms_dataset/temp/ms/'+ txt_or_wav + '/')
		elif txt_or_wav == 'txt':
			os.system('mv data/ms_dataset/train/ms/' + txt_or_wav + '/' + file.rstrip() + ' data/ms_dataset/temp/ms/'+ txt_or_wav + '/')
			t1 = open('data/ms_dataset/temp/ms/txt/'+file.rstrip())
			t2 = t1.read()
			print(t2)
			f2.write(t2+'\n')
			t1.close()
			

f1.close()
f2.close()


		
