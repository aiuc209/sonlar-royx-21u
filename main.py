def sonlarni_ayirma(sonlar):
    yangi_sonlar = [round(son, 2) for son in sonlar]
    return yangi_sonlar

sonlar = [12.3456, 78.9012, 34.5678, 90.1234]
print(sonlarni_ayirma(sonlar))
