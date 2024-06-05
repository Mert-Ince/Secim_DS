# 2024 belediye seçimleri, kazananlar ve kaybedenler:
31 mart 2024te gerçekleşen ve "muhalefet için bir zafer" olarak değerlendirilen bu seçimi biraz daha derinden incelemek ve geçtiğimiz yıllardaki seçimlerden ne kadar farklı sonuçlar alındığına objektif bir biçimde bakmak istedim. İnternette hazır bir veri seti bulamasam da detaylı sonuçlar birçok sitede bulunuyordu. Ben de Anadolu Ajansı'nın paylaştığı sonuçları secim.ntv.com.tr adresinden, python kullanarak scrapelemeye ve kendi veri setimi oluşturmaya karar verdim. Bu veri setine "koymayı unutmamışsam burada link olacak" adresinden ulaşabilirsiniz. Aklıma gelen ve cevaplamak istediğim bazı soruları yazarak başlayayım.

### Cevaplamak istediğim ana sorular:
1- Partiler geçen seçime kıyasla ne kadar oy/belediye kazandı veya kaybetti? Ortada muhalefet için ne kadar büyük bir zafer olduğunu görmek istiyorsam tabii ki merak ettiğim ilk şey bu.
2- Geçen seçime kıyasla en büyük farklılık hangi şehirlerde yaşandı? Geçen seçimden bu yana fikri büyük oranda değişmiş şehirleri görmek isterim. Bunu yazarken bir şeyi daha merak ettim, acaba fikri en az değişen şehirler hangileri?
3- Geçmiş seçimlerde yerel ve genel seçimler arasında nasıl bir bağlantı vardı? Belediye seçimlerinden önde çıkmış olmak, bir sonraki seçimler için gerçekten bir anlam ifade ediyor mu?

### Bu seçimle alakasız, elimdeki veriye bakarak aklıma gelen sorular:
1- En yüksek oy oranı alınan ilçeler hangileri? Bunun çok önemli bir istatistik olduğunu düşünmüyorum fakat %80 tarzı ezici bir üstünlükle alınmış ilçeler varsa bunu görmek isterim.
2- Bölgeler arasında(Ege, Marmara, Karadeniz) oy verme eğilimi açısından nasıl bir fark var? Büyük şehirler ve diğer şehirler arasında nasıl bir fark var? Elimde bu veri yok fakat 81 şehri bölgelerine ve şehir/büyük şehir olarak ayırmak fazla zor olmayacağından bunu da incelemek isterim.

## Analiz
#### Alınan belediye sayısı
İlk soruya partilerin 2019 seçimlerinde kazandıkları belediye sayılarını grafiğe döküp inceleyerek başlayalım. Bu seçim için muhtemelen en önemlisi olan bu metrikte CHP, kazandığı belediye sayısını, kendileri için yine iyi geçen bir yıl olan 2019a kıyasla neredeyse ikiye katlayarak iktidar partisi AKP ile yer değiştirmiş. DEM Parti ve Yeniden Refah Partisi'de bu metrikte iyi performans gösteren diğer partiler.
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
Sıra,geçen seçime kıyasla şehirlerde en çok oy değişiminin nerelerde ve hangi partilerde görüldüğünü bulmaya geldi. Bunu gerçekleştirmek için önce partilerin,geçen seçimden her şehirdeki oylarını bu seçimde topladıkları oylardan çıkardım ve aradaki farka göre sıraladıktan sonra en yüksek 5 sonucu grafiğe döktüm. Fakat bunu yaptıktan sonra fark ettimki elde ettiğim sonuçlar hep en büyük şehirlerdendi. Bekleneceği üzere en yüksek farklar en yüksek miktarda oyun kullanıldığı şehirlerden çıkıyordu. Benim asıl bulmak istediğim "fikri en çok değişen şehirler" olduğu için farklı bir yöntem kullanmam gerekiyordu. Ben de elimdeki diğer bir veri olan yüzdelik oyları kullandım ve bunların geçen seçime göre ne kadar değiştiğine baktım.
![image](https://github.com/Mert-Ince/Secim_DS/assets/120698325/850cbef8-727a-4a74-8724-af05e9e45802)
![image](https://github.com/Mert-Ince/Secim_DS/assets/120698325/a0492bf4-66c8-4df4-adcc-a70ba65a20e6)
![image](https://github.com/Mert-Ince/Secim_DS/assets/120698325/affd2c10-70ed-4f92-926d-f9c0a1348ed7)
![image](https://github.com/Mert-Ince/Secim_DS/assets/120698325/cd583828-5cd8-4605-a7b5-aea30690b344)
![image](https://github.com/Mert-Ince/Secim_DS/assets/120698325/eb378370-a1d8-403e-bf1d-f31c1236187a)
![image](https://github.com/Mert-Ince/Secim_DS/assets/120698325/7d73c157-39bd-4928-a690-d4cf1f58a150)
![image](https://github.com/Mert-Ince/Secim_DS/assets/120698325/c37d621f-8505-47d5-98d6-47d1a9f6b3a2)
![image](https://github.com/Mert-Ince/Secim_DS/assets/120698325/cbebde3b-b8bd-4a1f-bc83-4c72930846e9)










