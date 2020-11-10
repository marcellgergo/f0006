név = input('Mi a kedves vezetékneved? ')
 
nem = input('Lány vagy, avagy fiú vagy-é? (l/f) ')
if nem == 'l':
    előtag = 'Ms.'
elif nem == 'f':
    előtag = 'Mr.'
else:
    print('Íly nemet sajna nem ismerek. Nem fogok rendesen köszönni.')
    előtag = 'M?.'
 
napszak = input('Milyen napaszak van? (r/du/e/é) ')
# r = reggel, du = délután, e = este, é = éjjel
if napszak == 'r':
    angol_napszak = 'morning'
elif napszak == 'du':
    angol_napszak = 'afternoon'
elif napszak == 'e':
    angol_napszak = 'evening'
elif napszak == 'é':
    angol_napszak = 'night'
else:
    print('E napszakot sajnos nincs szerencsém ismerni. Aú! Revoár!')
    angol_napszak = 'i-don\'t-know'
 
print('Good ', angol_napszak, ', ', előtag, ' ', név, '!', sep='')