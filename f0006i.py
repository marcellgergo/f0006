#!/usr/bin/onv python3

#6.i:Kérdezd meg a felhasználó korát és
#ha hat év alatti, akkor mondd meg neki, hogy nézze a piroska és a farkast,
#ha legalább hat de legfeljebb 16, akkor nézze a Zootropoliszt,
#ha meg 16 múlt, akkor közöld vele, hogy már elég nagy hozzá, hogy bármit megnézhessen

kor = int(input('Hány éves vagy?'))
if kor < 6:
  print('Nézzél piroska és a farkast!')
elif 6 <= kor <= 16: #kor >= 6 and kor <= 16
  print('Nézzél Zootropoliszt!')
else kor > 16:
  print('Nézzél bármit, mert már jól megnőttél!')