from math import exp as e

class Neuron:

    def __init__(self):
        pass
    
    def integrate(outputs, weights):
        net = 0
        for i in range(len(outputs)):
            net += outputs[i]*weights[i]
        return net

    def activate(net):
        output = float(1)/(1+e(-net))
        return output