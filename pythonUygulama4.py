import requests

api_key="b21021e5140323145d1ce2e2"
# Where USD is the base currency you want to use
url=f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"
bozulan_doviz_turu=input("Bozulacak döviz türü: ")
alinacak_doviz_turu=input("Alınacak döviz türü: ")
miktar=int(input(f"Ne kadar {bozulan_doviz_turu} bozdurmak istiyorsunuz."))
# Making our request
sonuc =requests.get(url+bozulan_doviz_turu)
sonuc_json=sonuc.json()

print(f"1 {bozulan_doviz_turu} = {sonuc_json['conversion_rates'][alinacak_doviz_turu]}")
print(f"{miktar} {bozulan_doviz_turu} = "
      f"{miktar*sonuc_json['conversion_rates'][alinacak_doviz_turu]}, {alinacak_doviz_turu}")


