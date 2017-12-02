import cmake_example as m

assert m.__version__ == '0.0.1'
assert m.add(1, 2) == 3
assert m.subtract(1, 2) == -1

from cmake_example.mult import mult
assert mult(2, 2) == 4

assert False
