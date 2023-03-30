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



def rotateList(voters):
    voters.append(voters.pop(0))   ###this function will rotate the list of voters
    return voters


def banzaf(voters, quota):
    t = [[0 for x in range(quota+1)] for x in range(len(voters)+1)]  ##this is the table that will be used to calculate the banzaf power index
    t[0][0] = 1  ###this is the base case thing that we need to do
    for i in range(1, len(voters)+1):
        for j in range(0, quota+1):
            if voters[i-1] > j:
                t[i][j] = t[i-1][j]  ### this is all charlie's idea 
            else:
                t[i][j] = t[i-1][j] + t[i-1][j-voters[i-1]]   ### other given for the algorithm by charlie 
    print(t)
    result = 0
    pointer = -1
    while(voters[0] > 0):
        result = result + t[-2][pointer]  ## adding the numbers to get the result
        voters[0]= voters[0]-1
        pointer-=1
   
         ###this part isnt right i need to return the more specific thing that i need to calculate the banzaf power index i forgot
     #### i return the sum from t[-2][right to left counting based on their power and add it up]



def simulation(voters, quota):
    for i in range(len(voters)):
        banzaf(voters, quota)
        rotateList(voters)
    return 



simulation(voters, quota)


    



    




  
 






