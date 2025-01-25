# def detect_if_vowel(letter):
#     vowels=['a','e','y','u','i','o']
#     for vowel in vowels:
#         if(letter==vowel):
#             return True         
#     return False

# def splice_word(word,vowel_active=True):
#     temp=[]
#     for i in range (len(word)):
#         for j in range (1,len(word)+1):
#             if(i+j>len(word)):
#                 pass
#             else:
#                 if(vowel_active and detect_if_vowel(word[i])==True or vowel_active==False 
#                 and detect_if_vowel(word[i])==False):
#                     temp.append(word[i:i+j])             
#     return temp

# n=str(input())
# consumn_count=len(splice_word(n,False))
# vowel_count=len(splice_word(n))
# if(consumn_count>vowel_count):
#     print('This letter contains more consumn '+str(consumn_count)+' than vowels '+str(vowel_count))
# else:
#     print('This letter contains less consumn '+str(consumn_count)+' than vowels '+str(vowel_count))

def minion_games(word):
    vowels="AEYUIO"
    consumn_count=0
    vowel_count=0
    for i in range (len(word)):
        if word[i] in vowels:
            vowel_count+=len(word)-i
        else:
            consumn_count+=len(word)-i
    if(consumn_count>vowel_count):
        print('Kevin '+str(consumn_count))
    elif(consumn_count==vowel_count):
        print("Draw")
    else:
        print('Stuart '+str(vowel_count))


n=input()
minion_games(n)

