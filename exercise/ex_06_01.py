str = 'X-DSPM-Confidence: 0.8475'

ipos = str.find(':')
#print(ipos)
piece = str[ipos+1:]
#print(piece.strip())
value = float(piece)
print(value)
