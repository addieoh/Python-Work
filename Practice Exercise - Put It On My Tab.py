debts = {}


def lend_money(debts, person, amount):
    if person in debts.keys():
        debts[person].append(amount)
    else:
        debts.update({person:[amount]})
    return None

def amount_owed_by(debts, person):
    if person in debts.keys():
        if debts == {}:
            return 0
        else:
            return sum(debts[person])
    else:
        return 0

def total_amount_owed(debts):
    i = 0
    for person in debts.keys():
        i += sum(debts[person])
    return i
