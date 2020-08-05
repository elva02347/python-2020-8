import os.path
elva = {}
if not os.path.isfile('elva.txt'):
    fo = open('elva.txt','w')
    print('new file')
else:
    fo = open('elva.txt','r')
    print('old file')
for r in fo.readlines():
    data = r.spilt(':')
    key = data[0]
    value = data[1]
    elva[key] = value
print(elva)
fo.close()
while True:
    print('1.fill in words')
    print('2.print data')
    print('3.english to chinese')
    print('4.chinese to english')
    print('5.short test')
    print('6.leave system')
    sel = input('choose a option:')
    if sel  == '1' :
        eng = input('enter your words in ehglish:')
        ch = input('enter your words in chinese:')
        elva[eng] = ch
        elva[ch] = eng
        fo = open('elva.txt','a')
        for k,v in elva.items():
            fo.write(k)
            fo.write('=')
            fo.write(v)
            fo.write('\n')
        fo.close()
    elif sel == '2':
        for k,v in elva.items():
            print(k,':',v)
    elif sel == '3':
        search = input('enter your words in ehglish:')
        print(search,'=',elva[search])
    elif sel == '4':
        search1 = input('enter your words in chinese:')
        print(search1,'=',elva[search1])
        #for k,v in elva.items():
            #if search1 == v:
                #print(k)
    elif sel == '5':
        score = 0
        for k,v in elva.items():
            print(v,':')
            ans = input('fill in your answer:')
            if ans == k :
                print('you are right!!')
                score = score + 1
        print ('you score:',score)
    elif sel == '6':
        break

