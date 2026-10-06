# Scanner Health Checks
# A Medline branch checks its handheld scanners every 15 minutes.
# Print the first 10 check times.
# Expected: Check 1: 15 minutes after shift start ... Check 10: 150 minutes after shift start

for check_number in range(1, 11): #range with number of checks to be run (+1)
    minutes = check_number * 15  #number of minutes between each check
    print(f"Check {check_number}: {minutes} minutes after shift start") #check number and run time