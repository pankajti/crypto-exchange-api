import talib
import numpy
c = numpy.random.randn(100)

# this is the library function
#k, d = talib.STOCHRSI(c)
#print(d)

from talib import abstract

# directly
SMA = abstract.SMA
abstract.Function()
# or by name
SMA = abstract.Function('sma')