def bond_a_name(first="James", last="Bond"):
    """
    Bond, James Bond
    :param first: first name
    :param last: last name
    :return: last, first last
    """
    return f"{last}, {first} {last}"


def greet(name):
    """
    print: the name is {name}
    :param name: the name to use
    :return: nothing
    """
    print(f"The name is: {name}")


greet(bond_a_name())
greet(bond_a_name("Padi", "Brown"))
greet("Brown, Padi Brown")