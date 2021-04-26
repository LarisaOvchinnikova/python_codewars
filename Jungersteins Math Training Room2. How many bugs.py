# https://www.codewars.com/kata/58cf479f87c2e967250000e4
def cal_n_bug(head, leg, wing):
    for butt in range(head+1):
        for sp in range(head+1):
            for dr in range(head+1):
                if butt + sp + dr == head and (butt+dr)*6+sp*8 == leg and butt + dr*2 == wing:
                    return [sp, butt, dr]
    return [-1,-1,-1]