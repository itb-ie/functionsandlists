def dragon(heat, damage=10):
    """
    Creates a mean dragon
    :param heat: potency of dragon fire (1-100)
    :param damage: how hard the dragon bites (1-50)
    :return: the sum of heat and damage
    """
    try:
        heat = int(heat)
        damage = int(damage)
    except ValueError:
        print("You must use numbers for the dragon attributes")
        return
    # here comes the body of the function
    print(f"You are creating a dragon with a fire power of {heat} and bite power of {damage}")
    return heat+damage


dragon1 = dragon(7, 10)
dragon2 = dragon(damage=17, heat=45)
if dragon1 > dragon2:
    print("Dragon1 is stronger")
else:
    print("Dragon2 is stronger")
dragon3 = dragon(40)