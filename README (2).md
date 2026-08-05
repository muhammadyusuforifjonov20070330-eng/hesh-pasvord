# Password Hasher

Terminal orqali ism va parol qabul qilib, parolni **bcrypt** algoritmi bilan heshlab qaytaruvchi oddiy Python skripti.

## O'rnatish

```bash
pip install -r requirements.txt
```

## Ishga tushirish

```bash
python main.py
```

## Namuna

```
Ismingizni kiriting: Ali
Parolni kiriting: myPassword123

Ism: Ali
Parol (hash): $2b$12$iIJUKhIjVKWHBRrZkF3ZmOMnwiQ/1gm5TDyLpX4o8G5b8EnUKPWuC
```

## Nima uchun bcrypt?

- Har bir heshlash uchun tasodifiy **salt** qo'shiladi — bir xil parol har safar boshqacha hash beradi
- Qaytarib bo'lmaydigan (one-way) heshlash algoritmi
- Parollarni ochiq holda saqlashning oldini oladi
