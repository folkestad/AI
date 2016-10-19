from math import exp as e

def Integrate(outputs, weights):
    net = 0
    for i in range(len(outputs)):
        net += outputs[i]*weights[i]
    return net

def Activate(net):
    output = float(1)/(1+e(-net))
    return output
