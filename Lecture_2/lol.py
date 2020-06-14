def remove_at(i, s):
    return s[:i] + s[i+1:]
def true_parentheses(str):
    i = 0
    while(i<len(str)-1):
        if(str[i]=='(' and str[i+1]==')'):
            str = remove_at(i,str)
            str = remove_at(i,str)
        else: i+=1
    if(len(str)==0): return True
    else: return False

str = input()
print (true_parentheses(str))