def example(a, b=10, *args, **kwargs):
    print(a, b, args, kwargs)

example(1, 2, 3, 4, name="Ali")