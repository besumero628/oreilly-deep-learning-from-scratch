import gate as gt

def Perceptron_test(data, gate):
  if gate == "AND":
    print("AND Gate Selected...")
    for d in data:
      print(gt.AND(d[0], d[1]))
  elif gate == "NAND":
    print("NAND Gate Selected...")
    for d in data:
      print(gt.NAND(d[0], d[1]))
  elif gate == "OR":
    print("OR Gate Selected...")
    for d in data:
      print(gt.OR(d[0], d[1]))
  elif gate == "XOR":
    print("XOR Gate Selected...")
    for d in data:
      print(gt.XOR(d[0], d[1]))

sample = gt.np.array([[0,0], [1,0], [0,1], [1,1]])
Perceptron_test(sample, "AND")
Perceptron_test(sample, "NAND")
Perceptron_test(sample, "OR")
Perceptron_test(sample, "XOR")