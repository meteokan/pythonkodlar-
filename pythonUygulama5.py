import json

# Örnek JSON verisi
json_data = '''
{
    "name": "John",
    "age": 30,
    "city": "New York",
    "is_student": false,
    "courses": ["Math", "Science", "History"],
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "zipcode": "10001"
    }
}
'''

# JSON verisini Python sözlüğüne dönüştürme
data = json.loads(json_data)

# JSON verisini işleme
print("Name:", data["name"])         # Düz metin değeri
print("Age:", data["age"])           # Sayısal değer
print("City:", data["city"])         # Düz metin değeri
print("Is Student:", data["is_student"])  # Boolean değer
print("Courses:", data["courses"])   # Liste değeri
print("First Course:", data["courses"][0])  # Liste içindeki bir öğe
print("Address:", data["address"])   # İç içe geçmiş sözlük (dictionary)
print("Street:", data["address"]["street"])  # İç içe geçmiş sözlük içindeki bir değer
