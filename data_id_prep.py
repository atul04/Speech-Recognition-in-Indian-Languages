with open('temp.txt') as f:
    with open('/home/suraj/Downloads/azcopy_linux_amd64_10.3.1/microsoftspeechcorpusindianlanguages/data_ms/speech/src-train.txt','w') as g:
        for i in f:
            g.write('train/ms/wav/'+i)

