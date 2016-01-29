from PersistentDictionary import *
from Canvas import *

storage = PersistentDictionary('sp100.sqlite')
appl = storage['AAPL/2011']
points = [(x,y['adjusted_close']) for(x,y) in enumerate(appl)]
Canvas(title='apple stock(2011)',xlab='trading day',ylab='adjusted_close').plot(points,legend='AAPL').save('appl2011.png')
