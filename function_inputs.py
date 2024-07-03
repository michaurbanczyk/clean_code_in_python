def my_function(x, y, *args, kw1, kw2=0):
    print(f"{x=}, {y=}, {kw1=}, {kw2=}")


my_function(1, 2, kw1=3, kw2=4)


def my_function_with_slash(x, y, /):
    print(f"{x=}, {y=}")


# my_function_with_slash(x=1, y=2)


def my_function_with_kwargs(my_argument=None, **kwargs):
    print(my_argument)


my_function_with_kwargs(**{"my_argument": "This is My argument"})
