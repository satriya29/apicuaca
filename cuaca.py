import requests
import json
from datetime import datetime,timezone

#mengambil api dari openweathermap.org, bisa dilakukan dengan reqister dulu ke webnya 
api_key = '04a8f79850dc73c4676e6f5b9f74cfbc'

#memasukan input nama kota
query = input("Nama kota : ")

# contoh api call
url = f'http://api.openweathermap.org/data/2.5/weather?q={query}&appid={api_key}'

#mengambil respon dari request url
response = requests.get(url)

#untuk mengecek apakah respon diterima
if response.status_code == 200:
    print('berhasil')
else:
    print('gagal mengambil data')
    exit()

#menagmbil data respon
data = response.json()
#menampilkan data respon
# print(data)
#menampilkan data respon dengan format JSON agar lebih mudah dibaca
jsonstring = json.dumps(data ,indent=3)
# print(jsonstring)

# mengambil data yang di inginkan dari data json
#  sintaks [0] untuk mengambil elemen pertama dari sebuah list objek. 
cuaca = data['weather'][0]['description'],data['weather'][0]['main']
suhu = data ['main']['temp'] -273/15 #merubah kelvin ke celcius
koordinat = data['name'],data['coord']['lon'],data['coord']['lat']
timestime = data['dt']

#mengubah timestamp menjadi waktu lokal
waktu_lokal = datetime.fromtimestamp(timestime,timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

print('cuaca :',cuaca)
print('suhu  :',suhu,' Celcius')
print(koordinat, waktu_lokal)
