# Roman numerals module

def roman(n):   # return roman numeral for integer n as a string
    result = (n // 1000) * 'M'
    remainder = n % 1000
    
    hundredsCounter = remainder // 100
    hundreds=['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
    result= result + hundreds[hundredsCounter]
    remainder = remainder % 100
    
    tensCounter = remainder // 10
    tens=['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
    result= result + tens[tensCounter]
    remainder = remainder % 10

    onesCounter = remainder
    ones=['','I','II','III','IV','V','VI','VII','VIII','IX']
    result= result + ones[onesCounter]
    
    return result


