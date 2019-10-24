# Self Dividing Numbers


def self_dividing(n):
    for d in str(n):
        if d == '0' or n % int(d) > 0:
            return False
    return True


def self_dividing_numbers(left, right):
    row = []
    for n in range(left, right + 1):
        if self_dividing(n):
            row.append(n)
    return row


print(self_dividing_numbers(left=int(input("Enter left: ")), right=int(input("Enter right: "))))


