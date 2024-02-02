#///////////////////////////////////GLOBALOFSET/////////////////////////////////////////////////////////
#kullanıcıdan girilen kelimenin basındaki ve sonundaki boslıkları silen ve kucuk harf yapan program
# cumle = input("bir cümle gir")
# tcumle = cumle.strip()
# kucuk_harf_cumle = tcumle.lower()
# print("sonuc",kucuk_harf_cumle)
#///////////////////////////////////GLOBALOFSET/////////////////////////////////////////////////////////
#Bir string içinde belirli bir karakterin kaç kez geçtiğini sayın
# kelime = input("bir kelime girin")
# ara_kelime = input("aradıgınız harfi girin")
# sayac = kelime.count(ara_harf)
# print(f"{ara_kelime}  kelimede {sayac}kadar var")
#///////////////////////////////////GLOBALOFSET/////////////////////////////////////////////////////////
#Kullanıcıdan bir kelime ve bir harf alın, kelimenin içindeki o harfi kaç kez içerdiğini kontrol edin
# kelime = input("Bir kelime girin: ")
# harf = input("Bir harf girin: ")
# sayac = kelime.count(harf)
# print(f"{kelime} kelimesinde {harf} harfi {sayac} kez geçiyor.")
#///////////////////////////////////GLOBALOFSET/////////////////////////////////////////////////////////
#İki string'i birleştirin ve ardından bir substring arayın ve konumunu bulun.
#Kullanıcıdan bir cümle alın ve cümlenin içindeki kelimeleri alfabetik sıraya göre sıralayın.
# string1 = input("Birinci string'i girin: ")
# string2 = input("İkinci string'i girin: ")
# birlesik_string = string1 + string2
# substring = input("Aranacak substring'i girin: ")
# konum = birlesik_string.find(substring)
# print(f"Birleştirilmiş string: {birlesik_string}")
# print(f"{substring} substring'i {konum} konumunda bulunuyor.\n")
# cumle = input("Bir cümle girin: ")
# siralanmis_kelimeler = sorted(cumle.split())
# print(f"Cümledeki kelimeler alfabetik sırayla: {', '.join(siralanmis_kelimeler)}")
#///////////////////////////////////GLOBALOFSET/////////////////////////////////////////////////////////
#Kullanıcıdan iki string alın, bu stringleri birleştirin ve tüm karakterleri küçük harfe çevirin
# string1 = input("İlk stringi gir ")
# string2 = input("İkinci stringi gir ")
# birlesik_string = string1 + string2
# kucuk_harf_string = birlesik_string.lower()
# print("Birleştirilmiş ve küçük harfe çevrilmiş string:", kucuk_harf_string)
#///////////////////////////////////GLOBALOFSET/////////////////////////////////////////////////////////
#Bir string içinde belirli bir alt dizeyi (substring) arayın ve yerine başka bir alt dize ekleyin
# ana_string = input("Bir string gir ")
# aranan_substring = input("Aranacak alt diziyi gir ")
# eklenecek_substring = input("Yerine ekleyeceğiniz alt diziyi gir ")
# yenilenmis_string = ana_string.replace(aranan_substring, eklenecek_substring)
# print("Yenilenmiş string", yenilenmis_string)
#///////////////////////////////////GLOBALOFSET/////////////////////////////////////////////////////////
#Kullanıcıdan bir kelime alın ve kelimenin içindeki tüm 'a' harflerini '@' ile değiştirin
# kelime = input("Bir kelime gir ")
# yenilenmis_kelime = kelime.replace('a', '@')
# print("Değiştirilmiş kelime", yenilenmis_kelime)
#///////////////////////////////////GLOBALOFSET/////////////////////////////////////////////////////////
#Kullanıcıdan bir kelime alın ve kelimenin palindrome (tersinden de okunduğunda aynı olan) olup olmadığını kontrol edin
# Kullanıcıdan bir kelime alın
# kelime = input("Bir kelime gir ")
# ters_kelime = kelime[::-1]
# if kelime == ters_kelime:
#     print("Girdiğiniz kelime bir palindromdur")
# else:
#     print("Girdiğiniz kelime bir palindrom değil")
#///////////////////////////////////GLOBALOFSET/////////////////////////////////////////////////////////
#Kullanıcıdan bir cümle alın, cümlede geçen kelimelerin içinde en uzun olanını bulun.
#Bir liste oluşturun ve listenin ortasındaki elemanı bulun
# cumle = input("Bir cümle girin: ")
# kelimeler = cumle.split()
# en_uzun_kelime = max(kelimeler, key=len)
# list = kelimeler.copy()
# orta_eleman = list[len(liste) // 2]
# print("Cümledeki en uzun kelime", en_uzun_kelime)
# print("Oluşturulan liste", list)
# print("Listenin ortasındaki eleman", orta_eleman)
#///////////////////////////////////GLOBALOFSET/////////////////////////////////////////////////////////
#Bir tuple oluşturun, tuplein 2. ve 4. elemanlarını yeni bir tuple olarak alın
# tuple = (10, 20, 30, 40, 50)
# yeni_tuple = (tuple[1], tuple[3])
# print("Oluşturulan tuple", tuple)
# print("Yeni tuple", yeni_tuple)
#///////////////////////////////////GLOBALOFSET/////////////////////////////////////////////////////////
# Bir set oluşturun
# set = {10, 20, 30, 40, 50}
# eklenen_sayi = 60
# set.add(eklenen_sayi)
# cikarilan_sayi = 30
# set.remove(cikarilan_sayi)
# print("Oluşturulan set", set)
# print(f"{eklenen_sayi} sayısı sete eklendi")
# print(f"{cikarilan_sayi} sayısı setten çıkarıldı")
#///////////////////////////////////GLOBALOFSET/////////////////////////////////////////////////////////
#Bir dictk oluşturun, dicte yeni bir anahtar-değer çifti ekleyin, ardından bir anahtarı silin
# Bir dictionary oluşturun
# dict = {'anahtar1': 'değer1', 'anahtar2': 'değer2', 'anahtar3': 'değer3'}
# yeni_anahtar = 'anahtar4'
# yeni_deger = 'değer4'
# dict[yeni_anahtar] = yeni_deger
# silinecek_anahtar = 'anahtar2'
# if silinecek_anahtar in dict:
#     del dict[silinecek_anahtar]
#     print(f"{silinecek_anahtar} anahtarı silindi")
# else:
#     print(f"{silinecek_anahtar} anahtarı bulunamadı")
# print("Oluşturulan dictionary", dict)
#///////////////////////////////////GLOBALOFSET/////////////////////////////////////////////////////////
#Bir liste oluşturun, listenin ortasına yeni bir sayı ekleyin
# liste = [10, 20, 30, 40, 50]
# yeni_sayi = 25
# orta_index = len(liste) // 2
# liste.insert(orta_index, yeni_sayi)
# print("Oluşturulan liste", liste)
# print(f"{yeni_sayi} sayısı listenin ortasına eklendi")
#///////////////////////////////////GLOBALOFSET/////////////////////////////////////////////////////////
#Bir liste oluşturun ve listenin ortasındaki elemanı bir tuplee ekleyin
# liste = [10, 20, 30, 40, 50]
# orta_index = len(liste) // 2
# orta_eleman = liste[orta_index]
# tuple_ekle = (orta_eleman,)
# print("Oluşturulan liste", liste)
# print("Tuple olarak eklenen eleman", tuple_ekle)
#///////////////////////////////////GLOBALOFSET/////////////////////////////////////////////////////////
#Bir set oluşturun ve setin elemanlarını içeren bir liste oluşturun, ardından bu liste elemanlarının toplamını hesaplayın
# set = {10, 20, 30, 40, 50}
# liste = list(set)
# toplam = sum(liste)
# print("Olusturulan set", set)
# print("Setin elemanlarını içeren liste", liste)
# print("Liste elemanlarının toplam", toplam)
#///////////////////////////////////GLOBALOFSET/////////////////////////////////////////////////////////
#Bir dict oluşturun ve dictin içindeki string türündeki değerlerin karakter sayılarının toplamını bulun
# dict = {'anahtar1': 'deger1', 'anahtar2': 'deger22', 'anahtar3': 'deger333'}
# toplam_karakter_sayisi = sum(len(deger) for deger in dict.values())
# print("Oluşturulan dictionary", dict)
# print("String değerlerin karakter sayılarının toplamı", toplam_karakter_sayisi)
#///////////////////////////////////GLOBALOFSET/////////////////////////////////////////////////////////
#Bir liste oluşturun ve listenin içindeki en büyük sayıyı bulun, ancak sadece aritmetik operatörler (+, -, *, /) kullanmadan yapın
# liste = [10, 45, 23, 67, 88, 42]
# en_buyuk_sayi = max(liste)
# print("Oluşturulan liste", liste)
# print("Listenin içindeki en büyük sayı", en_buyuk_sayi)
#///////////////////////////////////GLOBALOFSET/////////////////////////////////////////////////////////
#Bir dict oluşturun ve dictin içindeki string türündeki değerlerin hepsini birleştirerek tek bir string elde edin
# dict = {'anahtar1': 'deger1', 'anahtar2': 'deger2', 'anahtar3': 'deger3'}
# birlesik_string = ''.join(dict.values())
# print("Oluşturulan dictionary", dict)
# print("String değerlerin birleştirilmiş hali", birlesik_string)
#///////////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////GLOBALOFSET/////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////










