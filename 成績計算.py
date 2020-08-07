while True:
    a = int(input('how many question you are right in chinese:'))
    if 44 <= a <= 48:
        sa = 7
        print('your chinese score:',sa)
        break
    elif a == 42 or a == 43:
        sa = 6
        print('your chinese score:',sa)
        break
    elif a  == 40 or a == 41:
        sa = 5
        print('your chinese score:',sa)
        break
    elif 35 <= a <= 39:
        sa = 4
        print('your chinese score:',sa)
        break
    elif 31 <= a <= 34:
        sa = 3
        print('your chinese score:',sa)
        break
    elif 20 <= a <= 30:
        sa = 2
        print('your chinese score:',sa)
        break
    elif 0<= a <= 19:
        sa = 1
        print('your chinese score:',sa)
        break
    else :
        print('fill in the right number')
while True:
    b = int(input('how many points you get in math:'))
    if 93.46 <= b <= 100.00:
        sb = 7
        print('your math score:',sb)
        break
    elif 87.69 <= b <= 93.45 :
        sb = 6
        print('your math score:',sb)
        break
    elif 78.46 <= b <= 87.68:
        sb = 5
        print('your math score:',sb)
        break
    elif 67.88 <= b <= 78.45:
        sb = 4
        print('your math score:',sb)
        break
    elif 57.31 <= b <= 67.87:
        sb = 3
        print('your math score:',sb)
        break
    elif 36.92 <= b <= 57.30:
        sb = 2
        print('your math score:',sb)
        break
    elif 0.00 <= b <= 36.91:
        sb = 1
        print('your math score:',sb)
        break
    else :
        print('fill in the right number')
while True:
    c = int(input('how many question you are right in english:'))
    if c == 41 or c == 40:
        sc = 7
        print('your english score:',sc)
        break
    elif c == 39 or c == 38:
        sc = 6
        print('your english score:',sc)
        break
    elif c == 37 or c == 36:
        sc = 5
        print('your english score:',sc)
        break
    elif 31 <= c <= 35:
        sc = 4
        print('your english score:',sc)
        break
    elif 25 <= c <= 30:
        sc = 3
        print('your english score:',sc)
        break
    elif 14 <= c <= 24:
        sc = 2
        print('your english score:',sc)
        break
    elif 13 <= c <= 0:
        sc = 1
        print('your english score:',sc)
        break
    else :
        print('fill in the right number')
while True:    
    d = int(input('how many question you are right in social studies:'))
    if 60 <= d <= 63:
        sd = 7
        print('your social studies score:',sd)
        break
    elif d == 59:
        sd = 6
        print('your social studies score:',sd)
        break
    elif 55 <= d <= 58:
        sd = 5
        print('your social studies score:',sd)
        break
    elif 47 <= d <= 54:
        sd = 4
        print('your social studies score:',sd)
        break
    elif 39 <= d <= 46:
        sd = 3
        print('your social studies score:',sd)
        break
    elif 24 <= d <= 38:
        sd = 2
        print('your social studies score:',sd)
        break
    elif 0 <= d <= 23:
        sd = 1
        print('your social studies score:',sd)
        break
    else :
        print('fill in the right number')
while True:
    e = int(input('how many question you are right in science:'))
    if 52 <= e <= 54:
        se = 7
        print('your science score:',se)
        break
    elif e == 51 or e == 50:
        se = 6
        print('your science score:',se)
        break
    elif 47 <= e <= 49:
        se = 5
        print('your science score:',se)
        break
    elif 39 <= e <= 46:
        se = 4
        print('your science score:',se)
        break
    elif 31 <= e <= 38:
        se = 3
        print('your science score:',se)
        break
    elif 20 <= e <= 30:
        se = 2
        print('your science score:',se)
        break
    elif 0 <= e <= 19:
        se = 1
        print('your science score:',se)
        break
    else :
        print('fill in the right number')
while True:
    f = float(input('how many points you get in writing:'))
    if 0.1 <= f <= 1:  
        break
    else:
        print('fill in the right number')
        break
total = sa+sb+sc+sd+se+f
print('your total',total)

gob = input('girl or boy:')
if gob == 'girl':
    if total >= 33.8:
        print('your high school is 北一女中')        
    elif 33.6 <= total < 33.8:
        print('your high school is 師大附中')        
    elif 30.6 <= total < 33.6:
        print('your high school is 中山女高')
    elif 30.4 <= total < 30.6:
        print('your high school is 松山高中')        
    elif 29.8 <= total < 30.4:
        print('your high school is 大同高中 or 政大附中')    
    elif 29.6 <= total < 29.8: 
        print('your high school is 中崙高中')
    elif 28.8 <= total < 29.6:
        print('your high school is 麗山高中')       
    elif 28.6 <= total < 28.8:
        print('your high school is 板橋高中')
    elif 27.8 <= total < 28.6:
        print('your high school is 大直高中')
    elif 27.6 <= total < 27.8:
        print('your high school is 成淵高中 or 和平高中 or 海山高中')
    elif 25.6 <= total < 27.6:
        print('your high school is 內湖高中 or 西松高中')
    elif 24.8 <= total < 25.6:
        print('your high school is 中正高中')
    elif 24.6 <= total < 24.8:
        print('your high school is 明倫高中 or 景美女中')
    elif 23.8 <= total < 24.6:
        print('your high school is 南湖高中')
elif gob == 'boy':
    if total >= 34.6:
        print('your high school is 建國中學')
    elif 33.6 <= total < 34.6:
        print('your high school is 師大附中')
    elif 31.6 <= total < 33.6:
        print('your high school is 成功高中')
    elif 30.8 <= total < 31.6:
        print('your high school is 松山高中')
    elif 29.8 <= total < 30.8:
        print('your high school is 大同高中 or 政大附中')
    elif 29.6 <= total < 29.8: 
        print('your high school is 中崙高中')
    elif 28.8 <= total < 29.6:
        print('your high school is 麗山高中')
    elif 28.6 <= total < 28.8:
        print('your high school is 板橋高中')
    elif 27.8 <= total < 28.6:
        print('your high school is 大直高中')
    elif 27.6 <= total < 27.8:
        print('your high school is 成淵高中 or 和平高中 or 海山高中')
    elif 25.8 <= total < 27.6:
        print('your high school is 內湖高中 or 西松高中')
    elif 24.8 <= total < 25.8:
        print('your high school is 中正高中')
    elif 24.6 <= total < 24.8:
        print('your high school is 明倫高中')
    elif 23.8 <= total < 24.6:
        print('your high school is 南湖高中')

        
        
        
        
        
        
        
        
        