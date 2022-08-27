import time
import datetime
print("Lütfen 3 saniye sonra demek istediklerinizi yazınız")
print("3")
time.sleep(0.5)#geçen süreyi askıya alıyor tek tek 3-2-1 yazdırmamızı sağladı
print("2")
time.sleep(0.5)
print("1")
time.sleep(0.5)
simdikizaman=datetime.datetime.now() # şimdiki zamanı gösteren fonk.
input("Lütfen yazmak istediklerinizi giriniz:")
sonrakizaman=datetime.datetime.now()#yazma işlemi bittikten sonraki süre
hesaplananzaman=sonrakizaman-simdikizaman#toplam yazma süresini hesaplar
print(hesaplananzaman)
