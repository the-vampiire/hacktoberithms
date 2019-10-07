def compute_earnings(expenditures):
    expenditures = expenditures.split(",")
    sum = 0

    for item in expenditures:
        if not item.strip().lstrip('-').replace('.','',1).isdigit():
            return 0

        exp = int(item.strip())
        sum += exp

        if sum < 0:
            sum = 0

    return sum

if __name__ == '__main__':
    expenditures = input("Enter expenditures: ")
    print(compute_earnings(expenditures))