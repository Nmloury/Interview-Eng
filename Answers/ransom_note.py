from collections import Counter


def ransom_note(magazine, ransom):
    answer = True
    if len(magazine) < len(ransom):
        answer = False
        return answer
    else:
        mag_count = Counter(magazine)
        ransom_count = Counter(ransom)
        mag_count.subtract(ransom_count)
        if min(mag_count.values()) < 0:
            answer = False
    return answer


#######
# Tests
#######

mag = "you are so amazing".split()
ransom = "you are amazing".split()

print "Magazine: ", mag
print "Ransom Note", ransom
print "Can we create the ransom note?: ", ransom_note(mag, ransom)

mag = "you are so amazing".split()
ransom = "You are amazing".split()

print "Magazine: ", mag
print "Ransom Note", ransom
print "Can we create the ransom note?: ", ransom_note(mag, ransom)

mag = "you are so amazing".split()
ransom = "you".split()

print "Magazine: ", mag
print "Ransom Note", ransom
print "Can we create the ransom note?: ", ransom_note(mag, ransom)

mag = "".split()
ransom = "you are amazing".split()

print "Magazine: ", mag
print "Ransom Note", ransom
print "Can we create the ransom note?: ", ransom_note(mag, ransom)

mag = "you are so amazing".split()
ransom = "you are amazing amazing".split()

print "Magazine: ", mag
print "Ransom Note", ransom
print "Can we create the ransom note?: ", ransom_note(mag, ransom)
