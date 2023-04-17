# Banzhaf Power Index - Binary Method
# ctrl + alt + n to run code

# Voting power 
freshman = 4
freshman_deans = 5
sophmore = 3
sophmore_deans = 4
junior = 2
junior_deans = 3
senior = 1
senior_deans = 2

freshmanSwing = 0
freshman_deansSwing = 0
sophmoreSwing = 0
sophmore_deansSwing = 0
juniorSwing = 0
junior_deansSwing = 0
seniorSwing = 0
senior_deansSwing = 0


freshman = False
freshman_deans = False
sophmore = False
sophmore_deans = False
junior = False
junior_deans = False
senior = False
senior_deans = False

voters = [freshman, freshman_deans, sophmore, sophmore_deans, junior, junior_deans, senior, senior_deans]

A = 4;
B = 3;
C = 2;
D = 1;
q = 6;


# 0-255 in bcd (2^8 - 1) (8 is the number of voters)
for num in range(256):

# below is to reinitialize
    freshman = False
    freshman_deans = False
    sophmore = False
    sophmore_deans = False
    junior = False
    junior_deans = False
    senior = False
    senior_deans = False

    x = bin(num)[2:].zfill(4); # skips the 0b and pads it to four digits 
    print(x); # bin number 
    # print(x[0]); # first digit 

    if x[0] == "0":
            a = False;
    else:
            a = True;
    if x[1] == "0":
            b = False;
    else:
            b = True;
    if x[2] == "0":
            c = False;
    else:
            c = True;
    if x[3] == "0":
            d = False;
    else:
            d = True;


    sumOfVotes = 0;
    if a == True:
        sumOfVotes += A;
        #print("The sum is ", sumOfVotes);
    if b == True:
        sumOfVotes += B;
        #print("The sum is now ", sumOfVotes);
    if c == True:
        sumOfVotes += C;
    if d == True:
        sumOfVotes += D;
    print(sumOfVotes);

    if (sumOfVotes >= q):
          print("The bill has PASSED!!!");
          # check for swing votes 
          # you only want to check ones that voted yes (1's)
          if (x[0] == "1"):
            if (sumOfVotes - A < q):
            # this means A is a swing vote 
                numA_Swing+=1;
          if (x[1] == "1"):
            if (sumOfVotes - B < q):
            # this means B is a swing vote 
             numB_Swing+=1;
          if (x[2] == "1"):
            if (sumOfVotes - C < q):
            # this means C is a swing vote 
             numC_Swing+=1;
          if (x[3] == "1"):
            if (sumOfVotes - D < q):
            # this means D is a swing vote 
             numD_Swing+=1;
    else: 
          print("failed");
print("");

totalSwings = numA_Swing + numB_Swing + numC_Swing + numD_Swing;

print("A has been a swing vote ", numA_Swing, " times.");
print("The banzhaf power index for A is ", round(numA_Swing/totalSwings, 2));
print("B has been a swing vote ", numB_Swing, " times.");
print("The banzhaf power index for B is ", round(numB_Swing/totalSwings, 2));
print("C has been a swing vote ", numC_Swing, " times.");
print("The banzhaf power index for C is ", round(numC_Swing/totalSwings), 2);
print("D has been a swing vote ", numD_Swing, " times.");
print("The banzhaf power index for D is ", round(numD_Swing/totalSwings), 2);
          