with open('transcription.txt') as f:
    for i in f:
        #print(i)
        id_txt = i.split()
        txt = ''
        for j in id_txt[1:]:
            txt = txt + j + ' '
        txt = txt[:-1]
        with open('/home/suraj/Downloads/azcopy_linux_amd64_10.3.1/microsoftspeechcorpusindianlanguages/data_ms/speech/ms_dataset/train/ms/txt/'+id_txt[0]+'.txt', 'w') as t:
            t.write(txt)
        #for j in id_txt:    
            #print(j)
        #break

