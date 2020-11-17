from collections import MutableMapping # from collection.abc если python >= 3.8



def flatten(dct, p_key ='', sep='.'): 
    if isinstance(dct, MutableMapping): 
        pairs = []
        for key, value in dct.items(): 
            new_key = p_key + sep + key if p_key else key
            if isinstance(value, MutableMapping): 
                pairs.extend(flatten(value, p_key = new_key).items())
            else: 
                pairs.append((new_key, value))
        return dict(pairs)
    else:
        raise TypeError('Неверный формат словаря.')

