text = ' learning Machine learning models are get rules from data  data'

fre_dict = dict()
for w in text.split():
    if w in fre_dict:
        fre_dict[w] += 1
    else:
        fre_dict[w] = 1
print(fre_dict)

