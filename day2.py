from collections import Counter

def validpasswords(database):
    valid_count = 0
    for policy, password in [line.split(":") for line in database]:
        freq_min, freq_max = int(policy.split(" ")[0].split("-")[0]), int(policy.split(" ")[0].split("-")[1])
        char = policy[-1]
        password = password[1:] # take of begining space
        test = Counter(password)
        if freq_min <= test[char] <= freq_max:
            valid_count += 1
    return valid_count


def validpasswordspt2(database):
    valid_count = 0
    for policy, password in [line.split(":") for line in database]:
        pos1, pos2 = int(policy.split(" ")[0].split("-")[0]), int(policy.split(" ")[0].split("-")[1])
        char = policy[-1]

        p1 = password[pos1] == char
        p2 = password[pos2] == char
        if p1:
            if not p2:
                valid_count +=1
        elif p2:
            valid_count += 1


    return valid_count

file = open('input', 'r')
data = []
for line in file:
    data.append(line.strip())

result = validpasswordspt2(data)
print(result)

