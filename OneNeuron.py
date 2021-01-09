import random

#SetUp
input1list = [0,1,0,1]
input2list = [0,0,1,1]

# generate the 3 Gates output from the two input lists
ORlist  = [a|b for a,b in zip(input1list, input2list)]
ANDlist = [a&b for a,b in zip(input1list, input2list)]
XORlist = [a^b for a,b in zip(input1list, input2list)]

outputlist = ORlist

input_output_matrix = list(zip(input1list, input2list, outputlist))

# Setup the HyperParameters
max_epoch = 500 # to avoid infinite loop
LR = 0.7 # learning rate

# Setup random weights and bias
weight1 = random.uniform(-1,1)
weight2 = random.uniform(-1,1)
bias = random.uniform(-1,1)

Total = 0
Loop = 1
errorFreeRunLength = 0

print('')
print('Program Name: ONE Neuron')
print('Start')
print('')

while errorFreeRunLength < len(input_output_matrix):

    count = Loop%len(input_output_matrix)
    input1, input2, Wanted = input_output_matrix[count]

#Neuron Result (Kernal Of Learning)
    NeuronResult = ((input1 * weight1)+(input2 * weight2) + bias)
# The TEST
    if NeuronResult < 0:
      Output = 0
    else:
      Output = 1
    error = Wanted - Output
# LOOP Control
    if Output is Wanted:
      errorFreeRunLength += 1
      Correct = 1
      Total += 1
    else:
      errorFreeRunLength = 0
      Correct = 0
      Total -= 1
# Applying The Whip (Changing The Weights)
    weight1new = (weight1  + (input1 * LR) * error)
    weight1 = weight1new

    weight2new = (weight2  + (input2 * LR) * error)
    weight2 = weight2new

    biasnew = (bias  + ( 1 *  LR) * error)
    bias = biasnew

    print('Loop: ', Loop)
    Loop += 1
    print('Total',Total)
    print('Correct', Correct)
    print('errorFreeRunLength: ', errorFreeRunLength)
    print('input1:',input1 ,' input2:', input2)
    print('Wanted: ',Wanted ,'Output: ', (Output))
    print('NeuronResult: ', NeuronResult)
    print('error: ' , (error))
    print(weight1)
    print(weight2)
    print(bias)
    print('')

    if Loop >= max_epoch:
      print(f'Max Epoch of {max_epoch} epochs reached')
      break

print('The End')
