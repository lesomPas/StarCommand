
def checking(dictionary: dict, pattern: dict) -> None:
    if not isinstance(dictionary, dict): #pattern同理
        raise TypeError
    
    sequence = [pattern]    
    dict_sequence = [dictionary]
    # breakpoint()
    
    while (sequence != []):
        l = sequence.pop()
        r = dict_sequence.pop()
        if len(l) < len(r):
            raise ValueError("too many parameters")
            
        for key, value in l.items():
            if key not in r:
                raise ValueError("missing value")
            data = r[key]   
            
            if isinstance(value, dict) and isinstance(data, dict):
                sequence.insert(0, l[key])
                dict_sequence.insert(0, data)
                continue
                
            match value:
                case "string":
                    if not isinstance(data, str):
                        return TypeError("str Argument")
                
                case "integer":
                    if not isinstance(data, int):
                        return TypeError("int Argument")    
                
                case _:
                    raise ValueError("nothing")           
            

checking({"a": 1}, {"a": "string"})        