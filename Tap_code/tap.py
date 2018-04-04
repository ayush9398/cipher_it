def tap(message):
    string=''
    for k in message:
        if(k!=' '):
            l=ord(k.upper())-65
            if(l>9):
                l-=1
            i=(l//5)+1
            j=l%5 +1
            string+='.'*i+' '+'.'*j+' '
        else:
            string+='/ '
    return string
