data = open('input2.txt','r')

passwords_valid=0
for line in data:
    entry=line.strip('\n')
    
    rule = entry.split(":")[0]

    rule_range = rule.split(" ")[0]
    rule_start=int(rule_range.split("-")[0])
    rule_end=int(rule_range.split("-")[1])
    rule_letter= rule.split(" ")[1]
    password = entry.split(":")[1]

    
    count=0
    position=-1
    hits_position=False
    print(password,rule_letter)
    for letter in password:
        position=position+1
        print(position,'***',letter,rule_range)

        if letter == rule_letter and position == rule_start:
            # count=count+1
            hits_position=True
            print(position,rule_start,rule_end)
            print(f'{position} at rule start')

            
        
        if letter == rule_letter and hits_position==False and position==rule_end:
            print(f'valid, {position} at rule end')
            passwords_valid = passwords_valid+ 1
        elif letter != rule_letter and hits_position==True and position==rule_end:
            print(f'valid, {position} at rule start')
            passwords_valid = passwords_valid+ 1
        elif letter == rule_letter and hits_position==True and position==rule_end:
            print('not valid')
        #yay!! this worked. position starts at -1 because password was passing in
        # an empty space at start of iteration
        
        
            

    # print(password,letter,count, rule_start,rule_end)
    # if count in range(rule_start,rule_end+1):
        # passwords_valid = passwords_valid+ 1
        # if (count == rule_start and count != rule_end) or (count != rule_start and count == rule_end): 
            # passwords_valid = passwords_valid+ 1
print(passwords_valid)

     



