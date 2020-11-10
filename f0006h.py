#!/usr/bin/onv python3

gondolt_szám = 3
tipp = input('Szerinted melyik számra gondolok 1 és 5 között')
tipp = int(tipp)
if gondolt_szám == tipp: #a gondolt szám egyenlő a tippel?
  print('Eltaláltad!') 
  print('Kis ügyes!')
elif abs (tipp - gondolt_szám) == 1:
  print('Majdnem...')
else: #különben
  print('Ez most sajnos nem sikerült!')
  print('De majd legközelebb ha nagyobb szerencséd lesz.')
print('Pápá!')
