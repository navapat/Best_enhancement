import random as rd
import os
def do_enhance(percent):
    pick = rd.random()*100
    if pick <= percent:
        return "S"
    else:
        return "F"
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
        status,scrolls = loop_enhance(enh_1_rate,enh_1)
        all_scrolls += scrolls
        if status == 'F':
            continue
        status,scrolls = loop_enhance(enh_2_rate,enh_2)
        all_scrolls += scrolls
        if status == 'F':
            continue
        status,scrolls = loop_enhance(enh_3_rate,enh_3)
        all_scrolls += scrolls
        if status == 'F':
            continue        
        status,scrolls = loop_enhance(enh_4_rate,enh_4)
        all_scrolls += scrolls
        if status == 'F':
            continue        
        
        all_status = 'S'
    return round, all_scrolls

def do_cost_collection(cost):
    if cost <= 1500:
        cost_range['1500b'] += 1
    elif cost <= 2500:
        cost_range['2500b'] += 1
    elif cost <= 3500:
        cost_range['3500b'] += 1
    elif cost <= 4000:
        cost_range['4000b'] += 1
    elif cost <= 5000:
        cost_range['5000b'] += 1
    else:
        cost_range['5001b+'] += 1
        
if __name__ == "__main__":
    """
        main input 
    """
    limit = 10000
    re_price = 90
    enh_price = 95
    enh_1 = 1
    enh_2 = 0
    enh_3 = 3
    enh_4 = 7
    budget = 5000
    
    """
        main fix variable
    """
    enh_1_rate = 24.2 
    enh_2_rate = 48.4
    enh_3_rate = 72.6
    enh_4_rate = 96.8
    max_e = -1
    min_e = 99999
    count_save = 0
    re_budget = 0
    enh_budget = 0
    max_re_1 = -999
    max_re_2 = -999
    max_re_3 = -999
    max_netprice = -99999
    cost_range = {'1500b':0, '2500b':0, '3500b':0, '4000b':0, '5000b':0, '5001b+':0}
    """
        Start process
    """
    for i in range(limit):
        if (i % (limit/100)) == 0:
            os.system('cls')
            print('Progress: {}{:.0f}%'.format('.'*int(i/1000),i/100))
            
        round, all_scrolls = finish_one()
        re_scroll = round - 1
        enh_scroll = abs(round-1-all_scrolls)
        net_price = re_scroll*re_price + enh_scroll*enh_price
        do_cost_collection(net_price)
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
    """
        Display summary
    """
    print('',"Simulation summary for {:,} rounds".format(limit), sep = '\n')
    print("*All Min-Max cost: ","{:,}".format(min_e),"<----> {:,}".format(max_e))
    print("Not over budget {:,} BAHT: {:.3f}%".format(budget, count_save/limit*100))
    print("Max cost      --> Re-scrolls: {}, Enhancement scrolls: {}, Price: {:,} BAHT".format(re_budget, enh_budget, max_netprice))
    print("Max re-scroll --> Re-scrolls: {}, Enhancement scrolls: {}, Price: {:,} BAHT".format(max_re_1, max_re_2, max_re_3))
    print("Option: {:+d}".format((enh_1*20)+(enh_2*15)+(enh_3*12)+(enh_4*9)))
    print("Weapon Slot: {}".format(enh_1+enh_2+enh_3+enh_4))
    """
        Display cost range
    """
    print('-'*79)
    print('| {:^10} | {:^10} | {:^10} | {:^10} | {:^10} | {:^10} |'
    .format('1500 BAHT', '2500 BAHT', '3500 BAHT', '4000 BAHT', '5000 BAHT', '5001+ BAHT'))
    print('-'*79)
    print('| {:^10} | {:^10} | {:^10} | {:^10} | {:^10} | {:^10} |'
    .format(cost_range['1500b'],cost_range['2500b'],cost_range['3500b'], cost_range['4000b'], cost_range['5000b'], cost_range['5001b+']))
    print('-'*79)
    print('| {:^9.2f}% | {:^9.2f}% | {:^9.2f}% | {:^9.2f}% | {:^9.2f}% | {:^9.2f}% |'
    .format(cost_range['1500b']/limit*100,
            cost_range['2500b']/limit*100,
            cost_range['3500b']/limit*100,
            cost_range['4000b']/limit*100,
            cost_range['5000b']/limit*100,
            cost_range['5001b+']/limit*100))
    print('-'*79)
