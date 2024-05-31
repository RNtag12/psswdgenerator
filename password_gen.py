#Python3 program to generate all passwords for given keywords

#Recursive helper function
#Adds/removes characters
#Until len is reached

def generate(arr, i, s, length):

#Base case
    if (i == 0): # when len has
                 # been reached
        #Print it out/write to a file
        #print(s)
        with open('passwords.txt', 'a') as out_file: 
            out_file.write(s+'\n')
        return
        
    #Iterate through the array
    for j in range(0, length):
        # Create new string with # next character Call
        # generate again until
        # string has reached its len
        appended = s + arr[j]
        generate(arr, i - 1, appended, length)
        return

#Function to generate all possible passwords
def crack(arr, length):

    #Call for all required lengths
    for i in range(1 , length + 1):
        a = generate(arr, i, "", length)
    return

arr = ['red', 'car', 'rivera','1996','Corvette', 'john']
length = len(arr)
possible_passwords=crack(arr, length)
