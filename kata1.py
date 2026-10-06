# Scanner Health Checks
# A Medline branch checks its handheld scanners every 15 minutes. Print the first 10 check times.
# Expected: Check 1: 15 minutes after shift start … Check 10: 150 minutes after shift start

Time = 150 #runnning checks for 1-150 minutes

for Time in range (1, Time + 1, 15):   #range that tests will be ran
    if Time % 15 == 0:                # number must be divisible by 15 to run (every 15 mins)
        print(f"min: Running Scanner Check") #notify user that check is running