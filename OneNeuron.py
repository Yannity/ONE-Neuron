import random

#SetUp
input1list = [0,1,0,1]
input2list = [0,0,1,1]

# generate the 3 Gates output from the two input lists
ORlist  = [a|b for a,b in zip(input1list, input2list)]
ANDlist = [a&b for a,b in zip(input1list, input2list)]
XORlist = [a^b for a,b in zip(input1list, input2list)]

# make it a list of choice for the CLI
choices = [
  ['an OR',  ORlist],
  ['an AND', ANDlist],
  ['a XOR', XORlist],
]

# Start of Rudimentary CLI User Interface
happy = False
while not happy:
    print('Which Gate do You Want to Train?')
    for i, (name,*_) in enumerate(choices):
        print(f'  Enter {i+1} For {name} Gate')
    try:
        user_choice = int(input('\n> ')) - 1
        happy = 0 <= user_choice < len(choices)
    except ValueError:
        print(f'Please Enter a Valid Number Between 1 and {len(choices)+1}')

name, outputlist = choices[user_choice]

input_output_matrix = list(zip(input1list, input2list, outputlist))

# We Display the input_output Matrix for the User
print(f'A\tB\t{name.split(" ")[1]}')
for a, b, o in input_output_matrix:
  print(f'{a}\t{b}\t{o}')

input('\nPress Enter to Start Training your Neuron!')

# Setup the HyperParameters
max_epoch = 500 # to avoid infinite loop
LR = 0.7 # learning rate

# Setup random weights and bias
weight1 = random.uniform(-1,1)
weight2 = random.uniform(-1,1)
bias = random.uniform(-1,1)

Total = 0
Loop = 0
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

    print('Loop: ', Loop + 1)
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
