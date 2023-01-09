for killer in ['A', 'B', 'C', 'D']:
    if (killer != 'A') + (killer == 'C') \
        + (killer == 'D') + (killer != 'D') == 3:
        print(killer)