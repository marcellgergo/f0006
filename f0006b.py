egyik = int(input('Mi az egyik szám? '))
másik = int(input('Mi a másik szám? '))
if egyik > másik:
    kiírandó = 'Az ' + str(egyik) + ' a nagyobb.'
elif egyik == másik:
    kiírandó = 'Egyenlőek.'
else:
    kiírandó = 'A ' + str(másik) + ' a nagyobb.'
print(kiírandó)