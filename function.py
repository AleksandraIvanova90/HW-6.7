from Stack import Stack



def cheking_brackets(bracket_str):
    brackets = Stack()
    brackets_dict = {'(':')','[':']', '{':'}'}
    for i in bracket_str:
        if brackets.is_empty() == False:
            if i not in brackets_dict.keys():
                return f'Несбалансированно'
                break
            brackets.push(i)
        if brackets.is_empty() == True:
            if i in brackets_dict.keys():
                brackets.push(i)
            else:
                k = brackets.peek()
                if brackets_dict[k] == i:
                    brackets.pop()
                else:
                    return f'Несбалансированно'
                    break
    else:
        return f'Cбалансированно'