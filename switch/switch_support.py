import inspect


def switch_support(func):
    def wrapper(*args):
        args_name = inspect.getfullargspec(func)[0]
        args_dict = dict(zip(args_name, args))
        parsed_docstring = [s.replace(':', '').lstrip() for s in
                            func.__doc__.split('\n') if s.strip()]
        cases = {}
        while parsed_docstring:
            s = parsed_docstring.pop(0)
            if 'switch' in s:
                switch = s.split()[1]
            elif 'case' in s:
                case = s.split()[1]
                if case in args_dict.keys():
                    case = str(args_dict[case])
                result = parsed_docstring.pop(0)
                cases[case] = result.split()[1]
        if switch in args_dict.keys():
            switch = str(args_dict[switch])
        return print(cases[switch])
    return wrapper


@switch_support
def test_function(a, b, c, d):
    """
    switch a:
         case b:
              return 1
         case c:
              return 2
         case 14:
              return 3
         case d:
              return 4
    """


test_function(15, 12, 13, 15)
