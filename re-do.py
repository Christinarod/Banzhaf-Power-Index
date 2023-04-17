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

# initializing number of swing votes 
freshmanSwing = 0
freshman_deansSwing = 0
sophmoreSwing = 0
sophmore_deansSwing = 0
juniorSwing = 0
junior_deansSwing = 0
seniorSwing = 0
senior_deansSwing = 0


voters = [freshman, freshman_deans, sophmore, sophmore_deans, junior, junior_deans, senior, senior_deans]
votersSwing = [freshmanSwing, freshman_deansSwing, sophmoreSwing, sophmore_deansSwing, juniorSwing, junior_deansSwing, seniorSwing, senior_deansSwing]

q = 13;
sumOfVotes = 0

# 0-255 in bcd (2^8 - 1)
for num in range(256):
    sumOfVotes = 0
    x = bin(num)[2:].zfill(8); # skips the 0b and pads it to eight digits 
    print(x); # bin number : x[0] = first digit 
    for i in range(8):
      if x[i] == "1":
        sumOfVotes += voters[i];
      i+=1
    print(sumOfVotes);

    if (sumOfVotes >= q):
          print("The bill has PASSED!!!");
          # check for swing votes 
          # you only want to check ones that voted yes (1's)
          for n in range(8):
           if (x[n] == "1"):
            if (sumOfVotes - voters[n] < q):
            # this means voters[n] is a swing vote 
             votersSwing[n]+=1;
    else: 
          print("failed");
print("");

# below adds up all times a voter was a swing vote
totalSwings = 0
for x in range(8):
     totalSwings += votersSwing[x]

     
print("Total Swings: ", totalSwings)

print("Freshman have been a swing vote ", freshmanSwing, " times.")
print("The banzhaf power index for Freshman is ", round(freshmanSwing/totalSwings, 2))
print("")
print("Freshman Deans have been a swing vote ", freshman_deansSwing, " times.");
print("The banzhaf power index for Freshman Deans is ", round(freshman_deansSwing/totalSwings, 2));
print("")
print("Sophmores have been a swing vote ", sophmoreSwing, " times.");
print("The banzhaf power index for Sophmores is ", round(sophmoreSwing/totalSwings, 2));
print("")
print("Sophmore Deans has been a swing vote ", sophmore_deansSwing, " times.");
print("The banzhaf power index for Sophmore Deans is ", round(sophmore_deansSwing/totalSwings, 2));
print("")
print("Juniors have been a swing vote ", juniorSwing, " times.");
print("The banzhaf power index for juniors is ", round(juniorSwing/totalSwings, 2));
print("")
print("Juniors Deans have been a swing vote ", junior_deansSwing, " times.");
print("The banzhaf power index for Junior Deans is ", round(junior_deansSwing/totalSwings, 2));
print("")
print("Seniors have been a swing vote ", seniorSwing, " times.");
print("The banzhaf power index for Seniors is ", round(seniorSwing/totalSwings, 2));
print("")
print("Senior Deans have been a swing vote ", senior_deansSwing, " times.");
print("The banzhaf power index for Senior Deans is ", round(senior_deansSwing/totalSwings, 2));
          