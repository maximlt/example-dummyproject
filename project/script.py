def foo(a, b):
    """Foo

    Parameters
    ----------
    a : str
        a
    b : str
        b

    Returns
    -------
    str
        a + b
    """
    return a + b


def bar(j, k):
    """bar

    Parameters
    ----------
    j : int
        j
    k : int
        k

    Returns
    -------
    int
        substraction
    """
    return j - k


def voila():
    x = 2
    if x > 5:
        print("Test branch coverage")
    return "voila"


def tag_2():
    pass
