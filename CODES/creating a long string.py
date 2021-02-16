def long_string(s):
    if(len(s) == 0):
        return 'enough thushani'
    else:    
        return s + "\n" + long_string(s[1:])



s = 'asitha'

print(long_string(s))