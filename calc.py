bill_period = []
presence = []
n = 3

for date in range(1, 21):
    bill_period.append(date)
    presence.append(0)

total_days = len(bill_period)
bill_cost = 300

per_day_cost = bill_cost/total_days
cost_matrix = []

for day_cost in range(1, n + 1):
    cost_matrix.append(per_day_cost/day_cost)

print(cost_matrix)

def attendance(ankit, vipin, ismail):
    for date in bill_period:
        if date in ankit:
            presence[date - 1] += 1
        if date in ismail:
            presence[date - 1] += 1
        if date in vipin:
            presence[date - 1] += 1

ankit_stay = [1,2,3,4,5,6,7,8,15,16,17,18,19]
vipin_stay = [1,2,3,4,5]
ismail_stay = [15,16,17,18,19,20]

attendance(ankit_stay, vipin_stay, ismail_stay)

availability = zip(bill_period, presence)

def calculate_bill(person_stay):
    total = 0.0
    for date, freq in iter(availability):
        if date in person_stay:
            print(date)
            if freq == 1:
                total += cost_matrix[0]
            elif freq == 2:
                total += cost_matrix[1]
            elif freq == 3:
                total += cost_matrix[2]
    return total

if __name__ == '__main__':

    ismail = calculate_bill(ismail_stay)
    print('ismail: ' + str(ismail))
    
    ankit = calculate_bill(ankit_stay)
    print('ankit: ' + str(ankit))

    vipin = calculate_bill(vipin_stay)    
    print('vipin: ' + str(vipin))
