# Warehouse Audit Calendar
# For days 1–30, apply these rules:

# Every 3rd day → Cycle count
# Every 5th day → Scanner audit
# Days that are both → FULL AUDIT
# Any other day → Normal operations

# Expected: Day 3: Cycle count, Day 5: Scanner audit, Day 15: FULL AUDIT, Day 30: FULL AUDIT

Days = 30 #number of days in 30 day month

for Days in range(1,Days +1):
    if Days % 3 == 0 and Days % 5 == 0:
        print(f"Day", Days, f"FULL AUDIT")
    elif Days % 5 == 0:
        print(f"Day", Days, f"Scanner Audit")
    elif Days % 3 == 0:
        print(f"Day", Days, f"Cycle Count")
    else: print(f"Day", Days, f"Normal Day")