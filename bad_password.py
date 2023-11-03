# Read input
n = int(input())
sequences = []
for _ in range(n):
    _, *sequence = input().split()
    sequences.append(set(sequence))

p = int(input())
password_changes = [input().split() for _ in range(p)]

# Function to check if two passwords have common words from the same list
def have_common_words_from_list(password1, password2):
    modified_password1 = password1
    modified_password2 = password2
    for seq in sequences:
        count = 0
        for word in seq:
            if word in password1:
                modified_password1 = password1.replace(word, "")
                count += 1
            elif word in password2:
                modified_password2 = password2.replace(word, "")
                count += 1
    if count >= 2:
        return True, modified_password1, modified_password2
    else:
        return False, modified_password1, modified_password2

# Function to check if two strings can be expressed as per the given rules
def can_express(s1, s2):
    prefix, suffix = "", ""
    for i in range(min(len(s1), len(s2))):
        if s1[i] == s2[i]:
            prefix += s1[i]
        else:
            break

    for i in range(1, min(len(s1), len(s2)) + 1):
        if s1[-i] == s2[-i]:
            suffix = s1[-i] + suffix
        else:
            break
    
    if len(suffix) == 0:
        ps1 = s1[len(prefix):]
        ps2 = s2[len(prefix):]
    else:    
        ps1 = s1[len(prefix):-len(suffix)] 
        ps2 = s2[len(prefix):-len(suffix)]    

    for seq in sequences:
        if ps1 in seq and ps2 in seq:
            return True
        # if len(prefix) == 0:
        #     for str in seq:
        #         if ps1 in str and ps2 in str:
        #             return True
    return False

# Check password changes and output the result
for old_password, new_password in password_changes:
    if old_password == new_password:
        print("REJECT")

    result,pass1,pass2 = have_common_words_from_list(old_password, new_password)
    if result:
        print("REJECT")
    else:
        print("OK")

    
