def is_prime(n:int)->bool:
    '''check prime'''
    if n<=1:
        return False
    else:
        for d in range(2,int(n**0.5)+1):
            if n%d==0:
                return False
    return True 

def get_word_fre(text:str, normalize = True)->dict:
    """docstring"""
    text_nor = text
    if normalize:
        text_nor = text_nor.lower()
        for char in {'.',',','!','-','*'}:
            text_nor = text_nor.replace(char, ' ')
    fre_dict = dict()
    for w in text_nor.split():
        if w in fre_dict:
            fre_dict[w] += 1
        else:
            fre_dict[w] = 1
    return fre_dict


digits = list(range(100))
print('The module is imported')
print('--------')