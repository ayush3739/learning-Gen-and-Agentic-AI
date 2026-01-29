import arrow

brew_time=arrow.utcnow()
print(brew_time)
print(brew_time.to('Europe/Rome'))


from collections import namedtuple

carProfiles=namedtuple("carProfile",['Flavor','aroma'])
print(carProfiles)