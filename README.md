
## PROBLEM:
Elimizde siyah-beyaz fotoğraf ve siyah olan noktalar kümesi objelerimizdir. Amacımız siyah kümelerden delik olanları bulmaktır. 

### Orneğimizin İlk Hali
<p align="center" id="id_1">
  <img src="https://user-images.githubusercontent.com/82450697/116828362-e7fd7380-aba6-11eb-8c63-420808ba9e7f.png" width="350" title="hover text">
</p>

## Algoritma Adımlarım

<ul type="square">
  <li>İlk önce, birbiriyle komşu olan siyah noktalar gruplanır "functions.recu fonksiyonu"</li>
  <li>Gruplar Belli olduktan sonra, resmin etrafı siyah noktalarla çevrelenir ki obje ortasında olmayan beyaz noktalarla işimiz olmadığı için farklı renge boyarken "functions.beyazlari_boya()" fonksiyonu taşmaya uğramasın <a href = "#id_2">Kenarları Boyanmış Hali</a></li>
  <li>Artık İşimize yaramayan beyaz noktalar dışarıdaki siyah kenar ile gruplamış olduğumuz noktalar arasında kalır</li>
  <li>Bu aşamadan sonra işimize yaramayan beyazları boyayabiliriz "functions.beyazlari_boya()" <a href = "#id_3">Boş Beyazlar Boyandı</a></li>
  <li>Geriye Sadece gruplanmış olduğumuz siyah kümeler ve bu kümelerden herhangi bir pixelinin komşusunun beyaz olup olmaması önemli, eğer bi tane bile komşusu varsa o kümenin ortası deliktir. (Kenarlar JPG yumuşatmasından ötürü renk kaybına uğramış belirgin olsun diye kırmızılaştırdım) <a href = "#id_4">Gruplarımız ve beyaz delikler</a></li>
  
  <li> <a href = "#id_45">Delik Sayma Kodumuz</a></li>
  
</ul>
 
 <h3 id="id_2"> Kenarları Çizilmiş Hali</h3>
<p align="center">
  <img src="https://user-images.githubusercontent.com/82450697/116828368-f21f7200-aba6-11eb-89ab-032f16751aab.png" width="350" title="hover text">
</p>

 <h3 id="id_3"> Boş Beyazlar Boyandı</h3>
<p align="center">
  <img src="https://user-images.githubusercontent.com/82450697/116828373-fc417080-aba6-11eb-94a1-396ea7b97720.jpg" width="350" title="hover text">
</p>

 <h3 id="id_4"> Gruplarımız ve Delik Oluşturan Beyazlar</h3>
<p align="center" >
  <img src="https://user-images.githubusercontent.com/82450697/116828386-0f544080-aba7-11eb-942b-0c0935af4acd.jpg" width="350" title="hover text">
</p>


 <h3  id="id_45"> Çıktımız </h3>
<p align="center">
  <img src="https://user-images.githubusercontent.com/82450697/116828788-a3bfa280-aba9-11eb-999c-8da08d304f19.PNG" width="500" title="hover text">
</p>


 <h3  id="id_5"> Çıktımız </h3>
<p align="center">
  <img src="https://user-images.githubusercontent.com/82450697/116828392-17ac7b80-aba7-11eb-99de-918577e82927.PNG" width="1000" title="hover text">
</p>


 
