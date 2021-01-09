import random

#SetUp
input1list = [0,1,0,1]
input2list = [0,0,1,1]

# generate the 3 Gates output from the two input lists
ORlist  = [a|b for a,b in zip(input1list, input2list)]
ANDlist = [a&b for a,b in zip(input1list, input2list)]
XORlist = [a^b for a,b in zip(input1list, input2list)]

LR = 0.7
weight1 = 0
weight2 = 0
bias = 0.7
Total = 0
Loop = 1

errorFreeRunLength = 0

print('')
print('Program Name: ONE Neuron')
print('Start')
print('')

while errorFreeRunLength is not 20:

    count = random.randint(0,3)
    input1 = input1list[count]
    input2 = input2list[count]
    Wanted = ORlist[count]

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
      errorFreeRunLength = (errorFreeRunLength + 1)
      Correct = 1
      Total = (Total + 1)
    else:
      errorFreeRunLength = 0
      Correct = 0
      Total = (Total - 1)
# Applying The Whip (Changing The Weights)
    weight1new = (weight1  + (input1 * LR) * error)
    weight1 = weight1new

    weight2new = (weight2  + (input2 * LR) * error)
    weight2 = weight2new

    biasnew = (bias  + ( 1 *  LR) * error)
    bias = biasnew

    print('Loop: ', Loop)
    Loop = (Loop + 1)
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

print('The End')
