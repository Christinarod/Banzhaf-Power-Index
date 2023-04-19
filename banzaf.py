##  
## t[i][j]  t[i-1][j] when p[i] > j
##          t[i-1][j] + t[i-1][j-p[i]]




# Path: banzaf.py

# Compare this snippet from banzhaf-binary.py:

freshman = 4
freshman_deans = 5
sophmore = 3
sophmore_deans = 4
junior = 2
junior_deans = 3
senior = 1
senior_deans = 2

voters = [freshman, freshman_deans, sophmore, sophmore_deans, junior, junior_deans, senior, senior_deans]

quota = 13

# voters = [4,3,2,1]

# quota = 6



def rotateList(voters):
    voters.append(voters.pop(0))   ###this function will rotate the list of voters
    return voters


def banzaf(voters, quota):
    t = [[0 for x in range(quota)] for x in range(len(voters)+1)]  ##this is the table that will be used to calculate the banzaf power index
    t[0][0] = 1  ###this is the base case thing that we need to do
    for i in range(1, len(voters)+1):
        for j in range(0, quota):
            if voters[i-1] > j:
                t[i][j] = t[i-1][j]  
            else:
                t[i][j] = t[i-1][j] + t[i-1][j-voters[i-1]]   
    
    print(voters[-1])

    for i in range(len(voters)+1):
        print(t[i]) 
    
         ###this is just to print the table so i can see it
    print('')
    sum = 0

    for i in range((quota-voters[-1]), quota):
        sum += t[-2][i]

    print(f'Voting power: {sum}\n')

    return sum


   
         ###this part isnt right i need to return the more specific thing that i need to calculate the banzaf power index i forgot
     #### i return the sum from t[-2][right to left counting based on their power and add it up]



def simulation(voters, quota):
    powers = []
    for i in range(len(voters)):
        powers.append(banzaf(voters, quota))
        rotateList(voters)
      
    print(powers)
    print(sum(powers))





simulation(voters, quota)


    



    




  
 






