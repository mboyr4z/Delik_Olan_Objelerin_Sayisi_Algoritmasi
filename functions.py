def recu(tuple,noktalar,yon, kume , maxY, maxX):

    # print("TUPLE : " , tuple , end=" ")
    noktalar.remove(tuple)
    # if yon == 1:
    #     print("sol_alt")
    # elif yon == 2:
    #     print("alt")
    # elif yon == 3:
    #     print("sag_alt")
    # elif yon == 4:
    #     print("sol")
    # elif yon == 6:
    #     print("sag")
    # elif yon == 7:
    #     print("sol_ust")
    # elif yon == 8:
    #     print("ust")
    # elif yon == 9:
    #     print("sag_ust")
    # else:
    #     print("Başla")

    y = tuple[0]
    x = tuple[1]

    if (y == 0 or x == 0 or y == maxY or x == maxX):
        return 0


    sol_ust = (y - 1, x - 1)
    ust = (y - 1, x)
    sag_ust = (y - 1, x + 1)

    sol = (y, x - 1)
    sag = (y, x + 1)

    sol_alt = (y + 1, x - 1)
    alt = (y + 1, x)
    sag_alt = (y + 1, x + 1)


    if sol_ust in noktalar and yon != 3:
        yon = 7
        kume.append(sol_ust)
        recu(sol_ust, noktalar, yon,kume , maxY, maxX)

    if ust in noktalar and yon != 2:
        yon = 8
        kume.append(ust)
        recu(ust, noktalar, yon,  kume , maxY, maxX)

    if sag_ust in noktalar and yon != 1:
        yon = 9
        kume.append(sag_ust)
        recu(sag_ust, noktalar, yon,kume , maxY, maxX)

    if sol in noktalar and yon != 6:
        yon = 4
        kume.append(sol)
        recu(sol, noktalar, yon,kume , maxY, maxX)

    if sag in noktalar and yon != 4:
        yon = 6
        kume.append(sag)
        recu(sag, noktalar, yon,kume , maxY, maxX)

    if sol_alt in noktalar and yon != 9:
        yon = 1
        kume.append(sol_alt)
        recu(sol_alt, noktalar, yon, kume , maxY, maxX)

    if alt in noktalar and yon != 8:
        yon = 2
        kume.append(alt)
        recu(alt, noktalar, yon, kume , maxY, maxX)

    if sag_alt in noktalar and yon != 7:
        yon = 3
        kume.append(sag_alt)
        recu(sag_alt, noktalar, yon, kume , maxY, maxX)

def max_ve_min_bul(kume) -> object:
        maxY = kume[0][0]
        minY = kume[0][0]

        maxX = kume[0][1]
        minX = kume[0][1]

        for tuple in kume:
            y = tuple[0]
            x = tuple[1]

            if y > maxY:
                maxY = y
            if y < minY:
                minY = y
            if x > maxX:
                maxX = x
            if x < minX:
                minX = x

        return (maxY,minY,maxX,minX)

def kenarlari_ciz(img,maxY,maxX):
    for i in range(maxY):
        for j in range(maxY):
            if(i == 0 or i == maxY - 1 or j == 0 or j == maxX - 1):
                img[i][j] = (0,0,0)


def etrafCiz(img, tuple):
    maxY = tuple[0]
    minY = tuple[1]
    maxX = tuple[2]
    minX = tuple[3]

    for i in range(len(img)):
        for j in range(len(img[0])):
            if (i == maxY or i == minY) and (j <= maxX and j >= minX):
                img[i][j] = (255,0,150)
            elif (j == minX or j == maxX) and (i <= maxY and i >= minY):
                img[i][j] = (255,0,150)

def beyazlari_boya(y,x,img):
    img[y][x] = (0,255,0)
    #print(y,x)

    if img[y][x+1][0] == 255:       # SAĞ
        #print("SAĞ")
        beyazlari_boya(y,x+1,img)

    if img[y][x - 1][0] == 255:       # sol
        #print("SOL")
        beyazlari_boya(y,x - 1,img)

    if img[y + 1][x][0] == 255:         # aşağı
        #print("AŞAĞI")
        beyazlari_boya(y + 1,x,img)

    if img[y - 1][x][0] == 255:           #yukarı
        #print("YUKARI")
        beyazlari_boya(y - 1,x,img)






