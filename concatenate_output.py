with open('parent_gu_brnn_10000.txt') as f:
    with open('concat_op.txt', 'w') as g:
        for i in f:
            print(i)
            op = i.split()
            print(op)
            tmp = ''
            for j in op:
                if j != "<space>":
                    tmp = tmp + j
                else:
                    tmp = tmp + " "
            print(tmp)
            g.write(tmp+'\n')
         
