import numpy as np

class Self_organizing_map():

    neurons = []

    def __init__(self, number_of_neurons, learning_rate, epochs, learning_rate_decay=False, radius_decay=False):
        #neurons
        self.neurons = np.random.rand(number_of_neurons, 2)

        #learning rate
        self.current_learning_rate = learning_rate

        #training epochs
        self.epochs = epochs

        #training radius
        self.current_radius

    def train_neurons(self, input):
        for i in range(self.epochs):
            for input_element in input: #trains nearest neurons towards input_element
                output_signals = self.integrate_and_fire(input_element)
                winning_neuron_pos = output_signals.tolist().index(min(output_signals))
                self.update_neurons(winning_neuron_pos, input_element)
    
    def integrate_and_fire(self, input_element):
        #returns distance of all elements to current element
        return np.apply_along_axis(self.dist, 1, self.neurons, input_element)
    
    def dist(self, neuron, input_element):
        #euclidian distance from neuron to input_element
        return np.linalg.norm(input_element, neuron)
    
    def update_neurons(self, winning_neuron_pos, input_element):
        #train neurons in neighborhood where neighborhood is neurons within radius in neuron chain including winning neuron
        neurons_pos = [((winning_neuron_pos + i) % len(self.neurons)) \ 
            for i in range(-self.current_radius, self.current_radius + 1)]
        for neuron_pos in neurons_pos:
            self.apply_learning(neuron_pos, input_element)
    
    def apply_learning(self, neuron_pos, input_element):
        #apply learning to neuron with a factor based on radius
        updated_neuron = self.learning(self.neurons[neuron_pos], input_element, 1.0)
        self.neurons[neuron_pos] = updated_neuron.tolist()

    def learning(self, neuron, input_element, factor):
        #regulate learning by learning formula: Wij = Wij + f*(Pj-Wij)
        return np.asarray(neuron) + \
            (self.current_learning_rate * \
                factor * (np.array(input_element) - np.array(neuron)))
    

