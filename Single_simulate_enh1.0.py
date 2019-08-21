import random as rd
def do_enhance(percent):
    pick = rd.random()*100
    if pick <= percent:
        return "S -->{:.2f}:::{:.2f}%".format(pick, percent)
    else:
        return "F -->{:.2f}:::{:.2f}%".format(pick, percent)
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

    enh_1 = 1
    enh_2 = 0
    enh_3 = 2 
    enh_4 = 9

    all_status = 'F'
    round = 0
    score = 0
    all_score = 0
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
    print('='*30)
    print("Round: "+ str(round))
    print("Baht: "+ str((all_score)*90))
    print("option: "+str((enh_1*20)+(enh_2*15)+(enh_3*12)+(enh_4*9)))                