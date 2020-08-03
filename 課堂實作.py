scoreeng = int(input('fill in your ehglish score:'))
scoremath = int(input('fill in your math score:'))
if scoreeng == 100 or scoremath == 100:
    print('有獎學金')
elif scoreeng >= 90 and scoremath >= 90:
    print('有獎學金')
elif scoreeng < 60 and scoremath < 60:
    print('有處罰')
else:
    print('keep going!')
