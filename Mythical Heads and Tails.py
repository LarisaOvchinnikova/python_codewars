# https://www.codewars.com/kata/5751aa92f2dac7695d000fb0
def beasts(heads, tails):
# --- How to solve:
# orthius * 2 + hydra * 5 = heads
# orthius + h = tails
# So, ... ===>
# orthius = tails- hydra
# (tails-hydra) * 2 + hydra * 5 = heads
# 2 * tails + hydra * 3 = heads
# so, ===>
# hydra = (heads - 2 * tails) / 3
    hydra = (heads - 2 * tails) / 3
    orthius = tails- hydra
    return [orthius, hydra] if orthius * hydra >=0 else "No solutions"