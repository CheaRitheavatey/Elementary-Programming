def atomic_number(electrons):
    shellnum = 1
    list = []
    remain = electrons
    while remain > 0:
        formula = 2* (shellnum**2)
        if remain >= formula:
            list.append(formula)
            remain -= formula
        else:
            list.append(remain)
            remain =0
        shellnum +=1
    return list
print(atomic_number(11))

# We are given a (big big) array a of n numbers (n>0 assumed).
# example
# sum_of_products([12,13]) = 12 + 13 + 12*13 = 181
# sum_of_products([2,3,7]) = 2 + 3 + 7 + 2*3 + 2*7 + 3*7 + 2*3*7 = 95 

def sum_of_products(a):
    result = 1
    for i in a:
        result *= (1+i)
    return result - 1




# Example usage
# print(sum_of_products([-9, 17, 21, 35, 6, 4, 2, 1, 0, 1, 1, 1, 2, 3, 4, 7, 129]))  # Output: -11955879936001

# # Example usage
# print(sum_of_products([12, 13]))  # Output: 181
# print(sum_of_products([2, 3, 7])) # Output: 95

# print(sum_of_products([-9,17,21,35,6,4,2,1,0,1,1,1,2,3,4,7,129]))

def range_bit_count(a, b):
#     store the range a,b
    array = []
    for i in range(a,b+1):
        array.append(i)
    print(array)

    # binary array
    # pointer j 
    binaryarr = []
    for i in array:
        while i >0:
            remainder = i % 2
            i = i// 2
            binaryarr.append(remainder)
    print(binaryarr)

    # count all the 1s in the binaryarr
    count = 0
    for i in binaryarr:
        if i == 1:
            count +=1
    print(count)




# range_bit_count(2,7)

# In this kata, your task is to replace all of the irregular characters with regular ones, following such example:

# 'ťēхţ' -> 'text'
# 'ĵõľĺÿ' -> 'jolly'
# 'sØMetНiпǦ' -> 'sOMetHinG'
# IRREGULAR = [
    # 'aàáâäæãɑå', 'AÀÁÂÄÆÅА', #A
    # 'вбbβ', 'BВ', #B
    # 'çĉċčćс', 'CÇĆČĈС', #C
    # 'dðďд', 'DÐĎ', #D
    # 'eèéêëėęēе', 'EÈÉÊËĘĖĒЕ', #E
    # 'ʄϝᶂᶠ', 'F𝕱Ꞙ', #F
    # 'gğĝġǧģ', 'GĞĜĠǦ', #G
    # 'ĥнħĥ', 'HĦĤН', #H
    # 'iìíīîïįıі', 'IÌÍÎÏĮİІ', #I
    # 'jĵ', 'JĴJ̃', #J
    # 'kķǩк', 'KĶǨК', #K
    # 'llłĺľ', 'LŁĹĽ', #L
    # 'мϻm', 'MМ', #M
    # 'nñńņňnп', 'NÑŃŅŇ', #N
    # 'oòóőоôõơoōöøœ', 'OÒÓÔÖØŒО', #O
    # 'ppþр', 'PÞР', #P
    # 'q𐞥q̃q̇', 'QꞯɊꟴ', #Q
    # 'rřŗŕг', 'RŘŖŔ', #R
    # 'sßśşšŝ', 'SŚŠŜ', #S
    # 'tŧţťт', 'TŦŢŤТ', #T
    # 'uùúûüųűů', 'UÙÚÛÜŲŰŮ', #U
    # '۷ࡐʋv̇ṽ', 'VV̇ṾṼꝞ', #V
    # 'ԝաŵ', 'WŴ', #W
    # 'хx', 'XХ', #X
    # 'yÿýŷу', 'УYŸÝŶ', #Y
    # 'zźžż', 'ZŹŽŻ', #Z
    
# ]