def get_2020():
    """get two values that equal 2020 and then their multiple."""
    input=open('input.txt','r')
    numbers=[]
    for line in input:
        numbers.append(int(line.strip('\n')))

    for num,i in enumerate(numbers):
        target=2020-num
    
        for j in range(num+1,len(numbers)):
            if j == target:
                print(j,num)
