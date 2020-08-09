import json
import pandas
import matplotlib.pyplot as plot

x = [-1., -0.7777, -0.55455, -0.366556, -0.11111254, 0.11111254, 0.366556, 0.55455, 0.7777, 1.]
y = [-1.135468, -0.5754618, -0.21698458, 0.5426548, 0.495425346, 1.149756543, 1.642258454, 2.17465325, 2.64775468, 2.9546548]

plot.figure(figsize=(10, 5))
plot.plot(x, y, 'o', label='dados originais')
plot.legend()
plot.xlabel('X')
plot.ylabel('Y')
plot.grid()
plot.show()
