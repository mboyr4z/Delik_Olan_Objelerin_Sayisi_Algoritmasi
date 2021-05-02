import cv2

from obje_adet_bulma.soru_2.functions import *



def resim_Al(konum):
    img = cv2.imread(konum)
    return img

def koordinatlari_al(img,gore):
    koordinatlar = []
    toplam = 0
    y = 0
    x = 0
    for i in range(1,len(img) - 1):
        for j in range(1,len(img[0]) - 1):
            if img[i][j][0] != gore:
                koordinatlar.append((i,j))

    return koordinatlar


if __name__ == "__main__":

    img = resim_Al(r"C:\Users\Muhammet\Desktop\Python Projelerim\obje_adet_bulma\soru_2\image.png")
    kenarlari_ciz(img,len(img),len(img[0]))
    cv2.imwrite("kenarlar.jpg",img)

    siyah_noktalar = koordinatlari_al(img,255)
    siyah_kumeler = []


    sayac = 0

    #SİYAHLARI KÜMELENDİR
    while(len(siyah_noktalar) != 0):
        siyah_kumeler.append([siyah_noktalar[0]])
        recu(siyah_noktalar[0], siyah_noktalar, 5, siyah_kumeler[sayac] , len(img) , len(img[0]))
        sayac += 1



    beyazlari_boya(1,1,img)

    sayac = 0
    for kume in siyah_kumeler:
        for pixel in kume:
            y = pixel[0]
            x = pixel[1]

            if img[y][x + 1][0] == 255:     #sağ
                sayac += 1
                break
            if img[y][x - 1][0] == 255:     #sol
                sayac += 1
                break
            if img[y + 1][x][0] == 255:    #aşağı
                sayac += 1
                break
            if img[y - 1][x][0] == 255:    # yukarı
                sayac += 1
                break

    print(sayac)


    


    




















