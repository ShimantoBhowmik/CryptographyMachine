def cryptomachine():
    keys = 'abcdefghijklmnopqrstuvwxyz !'
    values = keys[-1] + keys[0:-1]

    encryptDict = dict(zip(keys,values))

    decryptDict = dict(zip(values,keys))

    message = input("Please enter your desired message:\n")
    mode = input("Please enter the mode : Encode(E)pr Decode(D)\n")

    while mode.upper() =='D'or mode.upper() =='E':
        if mode.upper() == 'E':
            new_message = ''.join([encryptDict[letter] for letter in message.lower()])
        elif mode.upper() == 'D' :
            new_message = ''.join([decryptDict[letter] for letter in message.lower()])
        return new_message
print(cryptomachine())


    

