Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> sadef_yas = 19
... enes_yas = 20
... muharrem_yas = 21
... 
... 
... toplam_yas = sadef_yas + enes_yas + muharrem_yas
... ortalama = toplam_yas / 3
... 
... print("Grubun yaş ortalaması:", ortalama)
... 
... 
... if muharrem_yas > enes_yas and muharrem_yas > sadef_yas:
...     print("En büyük kişi: Muharrem")
... elif enes_yas > muharrem_yas and enes_yas > sadef_yas:
...     print("En büyük kişi: Enes")
... else:
...     print("En büyük kişi: Sadef")
... 
... if sadef_yas < enes_yas and sadef_yas < muharrem_yas:
