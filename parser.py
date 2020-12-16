while True:
    _input = input("parse ")

    _type = _input.split(" ")[0]

    if _type == "identifier":
        _str = _input.split(" ", 1)[1]

        if _str[0] == '"' and _str[-1:] == '"':
            _str = _str[1:-1]
            
            identifier = ""
            remaining = ""
            start = True
            awaiting_alphanum = False

            for char in _str:
                if char is " ":
                    start = True
                    awaiting_alphanum = False
                    remaining = remaining + char
                
                else:
                    if start is True and identifier == "":
                        if char.isalpha():
                            awaiting_alphanum = True
                            identifier = identifier + char
                        
                        else:
                            remaining = remaining + char

                    else:
                        if awaiting_alphanum is True:
                            if char.isalnum():
                                identifier = identifier + char
                            
                            else:
                                remaining = remaining + char
                        
                        else:
                            remaining = remaining + char

                    start = False

            print([(identifier, remaining)]) if identifier else print([])

        else:
            print("Syntax error. Try again.")
            break

    elif _type == "natural":
        _str = _input.split(" ", 1)[1]

        if _str[0] == '"' and _str[-1:] == '"':
            _str = _str[1:-1]
            
            natural = ""
            remaining = ""
            start = True
            awaiting_num = False

            for char in _str:
                if char is " ":
                    start = True
                    awaiting_num = False
                    remaining = remaining + char
                
                else:
                    if start is True and natural == "":
                        if char.isdigit():
                            awaiting_num = True
                            natural = natural + char
                        
                        else:
                            remaining = remaining + char

                    else:
                        if awaiting_num is True:
                            if char.isdigit():
                                natural = natural + char
                            
                            else:
                                remaining = remaining + char
                        
                        else:
                            remaining = remaining + char

                    start = False

            print([(natural, remaining)]) if natural else print([])

        else:
            print("Syntax error. Try again.")
            break

    elif _type == "(symbol":
        _given = _input.split(" ")[1]

        if _given[0] == '"' and _given[-2:] == '")':
            _given = _given[1:-2]
            
            _str = _input.split(" ", 2)[2]

            if _str[0] == '"' and _str[-1:] == '"':
                _str = _str[1:-1]
                
                print([(_given, _str.replace(_given, ""))]) if _str.find(_given) != -1 else print([])
            
            else:
                print("Syntax error. Try again.")
                break
        
        else:
            print("Syntax error. Try again.")
            break

    else:
        print("Syntax error. Try again.")
        break