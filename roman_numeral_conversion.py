def romanToInt(s):
    r_numerals='M','D','C','L','X','V','I'
    bad_response=(f"Only Roman numerals {r_numerals}.\nPlease try again.")
    for let in s:
        if let not in r_numerals:
            return bad_response
            
    ans=0
    s=s+'a'
    for i,c in enumerate(s):
        try:
            if c=='I' and s[i+1]!='V' and s[i+1]!='X':
                ans+=1
            elif c=='I' and s[i+1]=='V':
                ans+=4
            elif c=='I' and s[i+1]=='X':
                ans+=9

            if c=='V' and s[i-1]!='I':
                ans+=5
            if c=='X' and s[i-1]!='I' and s[i+1]!='L' and s[i+1]!='C':
                ans+=10
            elif c=='X' and s[i+1]=='L':
                ans+=40
            elif c=='X' and s[i+1]=='C':
                ans+=90

            if c=='L' and s[i-1]!='X':
                ans+=50
            if c=='C' and s[i-1]!='X' and s[i+1]!='D' and s[i+1]!='M':
                ans+=100
            elif c=='C' and s[i+1]=='D':
                ans+=400
            elif c=='C' and s[i+1]=='M':
                ans+=900

            if c=='D' and s[i-1]!='C':
                ans+=500
            if c=='M' and s[i-1]!='C':
                ans+=1000
            else: ans+=0
        except IndexError: continue
    return ans

print(romanToInt(input('What is the Roman Numeral you want to convert?? ').upper()))
