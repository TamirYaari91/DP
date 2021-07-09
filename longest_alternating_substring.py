# Given a string of digits, return the longest substring with alternating odd/even or even/odd digits.
# If two or more substrings have the same length, return the substring that occurs first.

main_string = "225424272163254474441338664823"


def is_alt(curr, prev):
    if (int(curr) % 2 == 1 and int(prev) % 2 == 0) or (int(prev) % 2 == 1 and int(curr) % 2 == 0):
        return True
    return False


def longest_substring(string):
    cand = str(string[0])
    out = str(string[0])

    for i in range(1, len(string)):
        if is_alt(string[i], string[i - 1]):
            cand = cand + string[i]
            if len(cand) > len(out):
                out = cand
        else:
            cand = string[i]
    return out


print(longest_substring(main_string))
