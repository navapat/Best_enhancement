import random as rd
def do_enhance(percent):
    pick = rd.random()*100
    if pick <= percent:
        return "S -->{:6.2f}:--:{:.2f}%".format(pick, percent)
    else:
        return "F -->{:6.2f}:--:{:.2f}%".format(pick, percent)
def loop_enhance(percent, round):
    score = 0
    flag = 'S'
    for i in range(round):
        status = do_enhance(percent)
        print(status)
        score += 1
        if status[0] == 'F':
            flag = 'F'
            score+=1
            return flag, score
    return flag, score
if __name__ == "__main__":
    # target_enh = int(input("Target:"))

    re_price = 95
    enh_price = 95
    enh_1 = 2
    enh_2 = 0
    enh_3 = 0 
    enh_4 = 0

    all_status = 'F'
    round = 0
    score = 0
    all_score = 0
    re_scroll = 0
    enh_scroll = 0
    while all_status == 'F':
        round += 1
        print('='*30)
        status,score = loop_enhance(24.2,enh_1)
        all_score += score
        if status == 'F':
            continue
        status,score = loop_enhance(48.4,enh_2)
        all_score += score
        if status == 'F':
            continue
        status,score = loop_enhance(72.6,enh_3)
        all_score += score
        if status == 'F':
            continue        
        status,score = loop_enhance(96.8,enh_4)
        all_score += score
        if status == 'F':
            continue        
        
        all_status = 'S'
    re_scroll = round - 1
    enh_scroll = all_score - re_scroll
    print('='*30)
    print("Round: "+ str(round))
    print("Cost: {:,} BAHT  Re-scrolls:{}  Enh-scrolls:{}".format( re_scroll* re_price + enh_scroll * enh_price, re_scroll, enh_scroll))
    print("option: "+str((enh_1*20)+(enh_2*15)+(enh_3*12)+(enh_4*9)))                