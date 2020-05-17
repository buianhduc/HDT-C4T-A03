def HanoiTower(NumberOfDisks):
    if(NumberOfDisks == 1): return 1
    elif(NumberOfDisks == 2): return 7
    else:
        return 2*HanoiTower(NumberOfDisks-1)+1
print(HanoiTower(1000))