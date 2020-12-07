def combat(health, damage):
    if health - damage > 0:
        return health - damage
    else:
        return 0