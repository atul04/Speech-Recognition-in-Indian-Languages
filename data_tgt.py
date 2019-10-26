with open('transcription.txt') as f:
    with open('/home/suraj/Downloads/azcopy_linux_amd64_10.3.1/microsoftspeechcorpusindianlanguages/data_wo_space/speech/tgt-train.txt', 'w') as op:
        for i in f:
            #print(i)
            id_txt = i.split()
            #txt = ''
            for j in range(len(id_txt[1:])):
                #for ch in id_txt[j+1]:
                    #op.write(ch+' ')
                op.write(id_txt[j+1]+' ')

                #if j != len(id_txt[1:])-1:
                    #op.write(' <space> ')
            op.write('\n')

