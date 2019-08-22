import random as rd
def do_enhance(percent):
    pick = rd.random()*100
    if pick <= percent:
        return "S -->{:.2f}:::{:.2f}%".format(pick, percent)
    else:
        return "F -->{:.2f}:::{:.2f}%".format(pick, percent)
def loop_enhance(percent, round):
    scrolls = 0
    flag = 'S'
    for i in range(round):
        status = do_enhance(percent)
        # print(status)
        scrolls += 1
        if status[0] == 'F':
            flag = 'F'
            scrolls+=1
            return flag, scrolls
    return flag, scrolls
def finish_one():
    all_status = 'F'
    round = 0
    scrolls = 0
    all_scrolls = 0    
    while all_status == 'F':
        round += 1
        status,scrolls = loop_enhance(24.2,enh_1)
        all_scrolls += scrolls
        if status == 'F':
            continue
        status,scrolls = loop_enhance(48.4,enh_2)
        all_scrolls += scrolls
        if status == 'F':
            continue
        status,scrolls = loop_enhance(72.6,enh_3)
        all_scrolls += scrolls
        if status == 'F':
            continue        
        status,scrolls = loop_enhance(96.8,enh_4)
        all_scrolls += scrolls
        if status == 'F':
            continue        
        
        all_status = 'S'
    return round, all_scrolls

if __name__ == "__main__":
    """
        main input 
    """
    limit = 10000
    re_price = 85
    enh_price = 90
    enh_1 = 0
    enh_2 = 1
    enh_3 = 3
    enh_4 = 8
    budget = 3500
    

    max_e = -1
    min_e = 99999
    count_save = 0
    re_budget = 0
    enh_budget = 0
    max_re_1 = -999
    max_re_2 = -999
    max_re_3 = -999
    max_netprice = -99999
    for i in range(limit):
        round, all_scrolls = finish_one()
        re_scroll = round - 1
        enh_scroll = abs(round-1-all_scrolls)
        net_price = re_scroll*re_price + enh_scroll*enh_price
        # print("{}:".format(i), "{:,}".format(net_price) , "Baht", 
        #     "Re-scroll:", re_scroll, "Scroll:", enh_scroll)
        if net_price < min_e:
            min_e = net_price
        if  net_price > max_e:
            max_e = net_price
        if net_price <= budget:
            count_save += 1
            if net_price > max_netprice:
                max_netprice = net_price
                re_budget = re_scroll
                enh_budget = enh_scroll
            if re_scroll > max_re_1:
                max_re_1 = re_scroll
                max_re_2 = enh_scroll
                max_re_3 = net_price
    print('',"Simulation summary for {:,} rounds".format(limit), sep = '\n')
    print("*All Min-Max price: ","{:,}".format(min_e),"<----> {:,}".format(max_e))
    print("Not over budget {:,} BAHT: {:.3f}%".format(budget, count_save/limit*100))
    print("Max price     --> Re-scrolls: {}, Enhancement scrolls: {}, Price: {:,} BAHT".format(re_budget, enh_budget, max_netprice))
    print("Max re-scroll --> Re-scrolls: {}, Enhancement scrolls: {}, Price: {:,} BAHT".format(max_re_1, max_re_2, max_re_3))
    print("Option: "+str((enh_1*20)+(enh_2*15)+(enh_3*12)+(enh_4*9)))
    print("Weapon Slot: {}".format(enh_1+enh_2+enh_3+enh_4))