# Warehouse Audit Calendar
# For days 1–30, apply these rules:

# Every 3rd day → Cycle count
# Every 5th day → Scanner audit
# Days that are both → FULL AUDIT
# Any other day → Normal operations

# Expected: Day 3: Cycle count, Day 5: Scanner audit, Day 15: FULL AUDIT, Day 30: FULL AUDIT

Days = 30 #number of days in 30 day month

for Days in range(1,Days +1): #30 day month range that sudits will be run
    if Days % 3 == 0 and Days % 5 == 0: #full audit test runs every 15 days
        print(f"Day {Days} FULL AUDIT")
    elif Days % 5 == 0:                 #Scanner Audit Test runs every 5 days
        print(f"Day {Days} Scanner Audit")
    elif Days % 3 == 0:                 #Cycle Count Check runs every 3 days
        print(f"Day {Days} Cycle Count")
    else: print(f"Day {Days} Normal Day")#every other day runs normal