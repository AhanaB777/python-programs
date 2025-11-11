"""
    A machine is purchased which will produce earning of Rs. 1000 per year while it lasts. The
    machine costs Rs. 6000 and will have a salvage of Rs. 2000 when it is condemned. If 12 percent
    per annum can be earned on alternate investments what would be the minimum life of the
    machine to make it a more attractive investment compared to alternative investment?
"""
# machine_min_life.py
# Compute minimum life (years) for machine to be attractive at 12% interest

r = 0.12            # interest rate
cost = 6000.0       # initial cost
annual = 1000.0     # yearly earning
salvage = 2000.0    # salvage at end

max_years = 50      # safety upper bound for search
found = False

# Try integer n from 1 to max_years
for n in range(1, max_years + 1):
    # compute present worth using loops (no pow, no functions)
    discount = 1.0
    pw = -cost
    # sum discounted annual earnings
    for t in range(1, n + 1):
        discount = discount * (1.0 + r)   # discount holds (1+r)^t
        pw += annual / discount
    # add discounted salvage
    pw += salvage / discount

    # print intermediate debug (optional)
    # print("n =", n, "PW =", round(pw, 4))

    if pw >= 0:
        print("Minimum life n (years) required:", n)
        print("Present worth at n =", n, "is approximately", round(pw, 4))
        found = True
        break

if not found:
    print("No feasible life <= {} years found (try increasing max_years).".format(max_years))
