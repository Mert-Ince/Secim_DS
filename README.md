# 2024 belediye seçimleri, kazananlar ve kaybedenler:
31 mart 2024te gerçekleşen ve "muhalefet için bir zafer" olarak değerlendirilen bu seçimi biraz daha derinden incelemek ve geçtiğimiz yıllardaki seçimlerden ne kadar farklı sonuçlar alındığına objektif bir biçimde bakmak istedim. İnternette hazır bir veri seti bulamasam da detaylı sonuçlar birçok sitede bulunuyordu. Ben de Anadolu Ajansı'nın paylaştığı sonuçları secim.ntv.com.tr adresinden, python kullanarak scrapelemeye ve kendi veri setimi oluşturmaya karar verdim. Bu veri setine "https://www.kaggle.com/datasets/mertinc/2024-turkish-local-elections" adresinden ulaşabilirsiniz. Aklıma gelen ve cevaplamak istediğim bazı soruları yazarak başlayayım.

### Cevaplamak istediğim ana sorular:
1- Partiler geçen seçime kıyasla ne kadar oy/belediye kazandı veya kaybetti? Ortada muhalefet için ne kadar büyük bir zafer olduğunu görmek istiyorsam tabii ki merak ettiğim ilk şey bu. <br/>
2- Geçen seçime kıyasla en büyük farklılık hangi şehirlerde yaşandı? Geçen seçimden bu yana fikri büyük oranda değişmiş şehirleri görmek isterim. Bunu yazarken bir şeyi daha merak ettim, acaba fikri en az değişen şehirler hangileri? <br/>
3- Geçmiş seçimlerde yerel ve genel seçimler arasında nasıl bir bağlantı vardı? Belediye seçimlerinden önde çıkmış olmak, bir sonraki seçimler için gerçekten bir anlam ifade ediyor mu? 

### Bu seçimle alakasız, elimdeki veriye bakarak aklıma gelen sorular:
1- En yüksek oy oranı alınan ilçeler hangileri? Bunun çok önemli bir istatistik olduğunu düşünmüyorum fakat %80 tarzı ezici bir üstünlükle alınmış ilçeler varsa bunu görmek isterim. <br/>
2- Bölgeler arasında(Ege, Marmara, Karadeniz) oy verme eğilimi açısından nasıl bir fark var? Büyük şehirler ve diğer şehirler arasında nasıl bir fark var? Elimde bu veri yok fakat 81 şehri bölgelerine ve şehir/büyük şehir olarak ayırmak fazla zor olmayacağından bunu da incelemek isterim.

## Analiz
#### Alınan belediye sayısı
İlk soruya partilerin 2019 seçimlerinde kazandıkları belediye sayılarını grafiğe döküp inceleyerek başlayalım. Bu seçim için muhtemelen en önemlisi olan bu metrikte CHP, kazandığı belediye sayısını, kendileri için yine iyi geçen bir yıl olan 2019a kıyasla neredeyse ikiye katlayarak iktidar partisi AKP ile yer değiştirmiş. DEM Parti ve Yeniden Refah Partisi'de bu konuda iyi performans gösteren diğer partiler.
<br/><br/>

![image](https://github.com/Mert-Ince/Secim_DS/assets/120698325/822ee742-f766-4b54-a289-550e566d100d)
![image](https://github.com/Mert-Ince/Secim_DS/assets/120698325/e8e92b14-923a-4a41-b523-99cbd684e52c)
#### Alınan oy sayısı
Partilerin aldığı oy sayısını bulmak için ilk önce partilerin her şehirde "belediye başkanlığı" seçimi için aldığı oyları topladım. Fakat bunu yaptıktan sonra bulduğum sonucun diğer kaynaklardan bulduğum sonuç ile eşleşmediğini gördüm. Biraz araştırma yaptıktan sonra, toplam oy hesaplanırken, büyükşehir olmayan şehirlerde il genel meclisi oylarının hesaba katıldığını öğrendim. İkinci grafikte hesabı bu şekilde yaptım. Grafiklerin sol üstündeki "1e7", Y eksenindeki sayıların 10*7 yani 10,000,000 ile çarpılması gerektiğini gösteriyor. Grafiklere baktığımızda ise durumun alınan belediye sayısından biraz farklı olduğunu görüyoruz. CHP, AKP'den sadece %6 fazla oy alarak %45 daha fazla şehir almayı başarmış. Bu durum CHP'nin küçük şehirlerde daha popüler olduğunu veya CHP'nin aldığı şehirlerde, aralarındaki oy farkının düşük olduğunu gösteriyor olabilir. Seçim sonucu haritasını gördüğüm için ilk önermenin doğru olmadığını biliyorum fakat bu 2 olasılığı da ileride daha derinden inceleyebiliriz. Grafikte görebileceğimiz bir başka durum ise DEM Parti ve MHP'nin oylarının kıyasla düşük olmasına rağmen aldıkları belediye sayılarının yüksek olması. Bu durum yine belki bu partilerin küçük şehirlerde daha popüler olduklarını gösteriyor olabilir. 2019'da alınan oylara bakacak olursak CHP'nin ne kadar yüksek miktarda oy kazandığını, AKP'nin ve İYİ Parti'nin yüksek miktarda oy kaybettiğini, DEM Parti'nin iyi miktarda oy kazanıp MHP'nin de bir okadar kaybettiğini görebiliriz. 
<br/><br/>
 
![image](https://github.com/Mert-Ince/Secim_DS/assets/120698325/e34c1782-c1a2-4da5-925d-559114f7e289)<br/><br/>
Büyükşehir olmayanlar şehirler için il meclisi verisi hesaba alındığında: <br/><br/>
![image](https://github.com/Mert-Ince/Secim_DS/assets/120698325/b9b9a323-e36b-47a9-9ff0-146947402443)
![image](https://github.com/Mert-Ince/Secim_DS/assets/120698325/d549def5-ed9d-483f-81b2-eef15c9fee40)
#### En çok ve en az değişim görülen şehirler
Sıra, geçen seçime kıyasla şehirlerde en çok oy değişiminin nerelerde ve hangi partilerde görüldüğünü bulmaya geldi. Bunu gerçekleştirmek için önce partilerin,geçen seçimden her şehirdeki oylarını bu seçimde topladıkları oylardan çıkardım ve aradaki farka göre sıraladıktan sonra en yüksek 5 sonucu grafiğe döktüm. Fakat bunu yaptıktan sonra fark ettim ki elde ettiğim sonuçlar hep en büyük şehirlerdendi. Bekleneceği üzere en yüksek farklar en yüksek miktarda oyun kullanıldığı şehirlerden çıkıyordu. Benim asıl bulmak istediğim "fikri en çok değişen şehirler" olduğu için farklı bir yöntem kullanmam gerekiyordu. Ben de elimdeki diğer bir veri olan yüzdelik oyları kullandım ve bunların geçen seçime göre ne kadar değiştiğini inceledim. Bu istediğime çok daha yakın bir sonuç verse de belki daha iyi bir sonuç elde edebileceğimi düşünerek geçen seçimin oy yüzdelerini bu seçiminkilere oranlayarak son bir grafik daha oluşturdum. Bu da istediğime daha uygun bir sonuç vererek örneğin Kayseri'de AKP'nin geçen seçime oranla %40a yakın oy kaybettiğini bize göstermiş oldu. En yüksek 5 değişiklik yaşayanların tamamı AKP'den ve negatif değişiklikler olduğu için herhangi bir renklendirme yapma gereği duymadım. Hatta AKP olmayan ve pozitif olan ilk sonucu 27. sırada Tunceli'de CHP'nin oyunu %26 arttırmasıyla görüyoruz. 
<br/>
##### Not: Her şehirde sadece en yüksek değişiklik gören parti dikkate alınmıştır.
![image](https://github.com/Mert-Ince/Secim_DS/assets/120698325/850cbef8-727a-4a74-8724-af05e9e45802)
![image](https://github.com/Mert-Ince/Secim_DS/assets/120698325/a0492bf4-66c8-4df4-adcc-a70ba65a20e6)
![image](https://github.com/Mert-Ince/Secim_DS/assets/120698325/9d328a4c-c235-4972-b81e-33e1dc787ba9)
![image](https://github.com/Mert-Ince/Secim_DS/assets/120698325/db5125fb-3682-4b49-828c-edb3d74e4060)
![image](https://github.com/Mert-Ince/Secim_DS/assets/120698325/cd583828-5cd8-4605-a7b5-aea30690b344)
#### Yerel ve genel seçimlerin arasındaki bağlantı
Bu soruyu cevaplayabilmek için biraz araştırma yaptım fakat cevaplanamayacağında karar kıldım. Seçimler uzun aralıklarla tekrarlanıyor ve birkaç seçim öncesi ile günümüz şartları arasında büyük farklar var. Dolayısıyla yapılacak çıkarımlar pek sağlıklı olmayacaktır ve bu soruyu es geçiyorum.
#### En yüksek oranla alınan ilçeler
En yüksek oranla alınan ilçelere baktığımızda ise bu konuda DEM Parti ve AKP'nin önde olduğunu görüyoruz. Dediğim gibi çok önemli bir istatistik olmasa da, bir ilçenin %80inden fazlasının tek bir partiye oy atması bence ilginç bir durum.
<br/><br/>
![image](https://github.com/Mert-Ince/Secim_DS/assets/120698325/4f03ceef-7037-4579-be29-575ec2a8ddde)
![image](https://github.com/Mert-Ince/Secim_DS/assets/120698325/eb378370-a1d8-403e-bf1d-f31c1236187a)
#### Bölgeler ve büyükşehirler ile şehirler arasında nasıl bir fark var
Daha önce yaptığımız çıkarımlardan "CHP'nin küçük şehirlerde daha popüler olma ihtimali" nin kesinlikle doğru olmadığını görüyoruz. İlginç bir diğer durum ise muhtemelen AKP'nin oralarda aday göstermemesinden dolayı MHP'nin küçük şehirlerde 10 kata yakın daha popüler olması. HÜDA PAR ve DEM Parti de MHP kadar olmasa da küçük şehirlerde daha popülerler.
<br/><br/>
![image](https://github.com/Mert-Ince/Secim_DS/assets/120698325/56ab7025-2c1e-4878-ad41-217841d5a2e9)
![image](https://github.com/Mert-Ince/Secim_DS/assets/120698325/cbebde3b-b8bd-4a1f-bc83-4c72930846e9)
---
![image](https://github.com/Mert-Ince/Secim_DS/assets/120698325/3fc659f8-5359-4efc-8518-dcd77ce694d5)
![image](https://github.com/Mert-Ince/Secim_DS/assets/120698325/71236ef9-87ac-49f6-81fa-f9af58c61e8e)
![image](https://github.com/Mert-Ince/Secim_DS/assets/120698325/322a794b-7251-4ae3-aff8-156e02b5ca90)
![image](https://github.com/Mert-Ince/Secim_DS/assets/120698325/cd66ba05-6834-4da1-8ad3-f4dd1cce8ace)
![image](https://github.com/Mert-Ince/Secim_DS/assets/120698325/171657d1-3b7a-4d39-81ab-1570f71a4dda)
![image](https://github.com/Mert-Ince/Secim_DS/assets/120698325/6d8bf449-5b16-452c-8c77-c34ac4d468aa)
![image](https://github.com/Mert-Ince/Secim_DS/assets/120698325/8fae3c85-4fae-4d4d-91c7-a253a3e8eb8b)














