def is_singleton(factory):
    a = factory()
    b = factory()
    return (a is b)