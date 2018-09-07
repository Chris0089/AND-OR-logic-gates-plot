import pylab
import numpy
import matplotlib.pyplot as plt

x = numpy.linspace(-2, 2, 4)  # range: (initial, last, iteration)

AND_FORMULA = eval('(0.5/1) - x')
OR_FORMULA = eval('(1.5/1) - x')

plt.plot([0, 0, 1, 1], [0, 1, 0, 1], 'ro', color="green")
pylab.plot(x, AND_FORMULA)
pylab.plot(x, OR_FORMULA)
plt.axis([-2, 2, -2, 2])
pylab.show()

plt.plot([1, 0, 1], [1, 1, 0], 'ro', color="red")
plt.plot([0], [0], 'ro', color="green")
pylab.plot(x, AND_FORMULA)
plt.axis([-2, 2, -2, 2])
pylab.show()

plt.plot([0, 0, 1], [0, 1, 0], 'ro', color="green")
plt.plot([1], [1], 'ro', color="red")
pylab.plot(x, OR_FORMULA)
plt.axis([-2, 2, -2, 2])
pylab.show()
