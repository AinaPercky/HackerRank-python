def merge_the_tools(string, k):
    split_number=len(string)//k
    unique_chars=[]
    for i in range(0,len(string),k):
        sub_string=string[i:i+k]
        unique_sub_string=[]
        for sub_string_item in sub_string:
            if( not(sub_string_item in unique_sub_string)):
                unique_sub_string.append(sub_string_item)
        unique_chars.append(unique_sub_string)
    for letters in unique_chars:
        print(''.join(letters))



string, k = input(), int(input())
merge_the_tools(string, k)