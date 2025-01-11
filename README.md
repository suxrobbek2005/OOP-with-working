7-dars. OOP(Object Oriented Programming). Class and objects. Inheritance.

—------------------------------------------------------------------------------------------------------------------------

Oson  

1-masala ⇒

Student class yarating. Har bir talabaning ism-familiyasi, kursi va o'rtacha bahosi bo'lsin. Talabaning to'liq ismini chiqaruvchi metod yozing.

2  -  masala   ⇒

Employee class yarating. Har bir xodimning ismi va oylik maoshi bo'lsin. Xodimning yillik maoshini hisoblovchi metod yozing.

3  -  masala   ⇒ 

   Movie Class (Film):

    Movie nomli class yarating, quyidagi atributlarga ega:

    title (nomi),
    duration (davomiyligi, minutda),
    rating (reyting).

    Quyidagi metodlarni qo‘shing:

    increase_duration(minutes) — filmning davomiyligini minutes minutga oshirsin.
    Agar davomiylik 150 minutdan oshsa, reytingni 0.5 ga kamaytiruvchi metod yozing.

4 masala  ⇒  
Telefon nomli class yarating.

Elementlari:

    Telefon nomi;
    Telefon RAM hajmi;
    Narxi;
    Ishlab chiqaruvchi kompaniya.

Shart:

    Kiritish va chiqarish methodlarini yozing.
    4 ta obyekt yarating va RAM hajmi 2 GB dan ko‘p va 8 GB dan kichik bo‘lgan telefonlar haqida ma’lumot chiqaring

5-masala  ⇒
Do'kon nomli class yarating.

Class elementlari quyidagicha bo'lsin:

    Do'kon nomi;
    Joylashuvi (manzili);
    Sotiladigan mahsulot turi;
    Ish vaqti.

 Sharti :       Classda kiritish va chiqarish methodlarini yozing. 5 ta obyekt yarating va mahsulot turi "Elektronika" bo'lgan do'konlar haqida ma'lumot chiqaring.
6 -  masala ⇒  
 Avtomobil nomli class yarating.

Class elementlari quyidagicha bo'lsin:

    Avtomobil markasi;
    Modeli;
    Ishlab chiqarilgan yili;
    Narxi.

Shart:

Class ichida kiritish va chiqarish methodlarini ishlating. Obyektlar ichidan ishlab chiqarilgan yili 2010-yildan katta bo'lgan avtomobillar haqida ma'lumot chiqaring.

—------------------------------------------------------------------------------------------------------------------------

O’rta

1- masala ⇒

School class yarating. U yerda maktabning nomi va talabalar ro'yxati bo'lsin. Talabalar ro'yxatiga yangi talabani qo'shish va ro'yxatdan o'chirish uchun metodlar yozing.

2-masala ⇒

Restaurant nomli classdan FastFood (tez ovqatlanish) va FineDining (yuqori darajadagi restoran) vorislarini hosil qiling. Har birining menyusi va narxlarini ifodalovchi metod bo'lsin.

3  -  masala  ⇒

  Student (talaba):

    Student classini yarating, atribut sifatida ism (name), yosh (age), va baholar (grades) ro‘yxatini qabul qilsin.
    get_average methodini yozing, bu method talabaning o‘rtacha bahosini qaytarsin.
    is_passing methodi esa o‘rtacha baho 60 dan yuqori bo‘lsa True, aks holda False qaytarsin.

.
4  -   masala  ⇒
 Talaba (Student) class yarating.

Elementlari:

    Talaba ismi;
    O‘qish kursi;
    O‘rtacha bahosi;
    Stipendiya miqdori.

Shart:

    5 ta obyekt yarating.
    O‘rtacha bahosi 80 dan yuqori va stipendiya miqdori 1 mln so‘mdan katta bo‘lgan talabalar haqida ma’lumot chiqaring.

5 - masala ⇒
Shopping Cart

    Tavsif:
    ShoppingCart nomli klass yarating. Bu klass foydalanuvchining xarid savatini boshqaradi.
    Metodlar:

    add_item(name, price) — yangi mahsulotni qo‘shadi.
    remove_item(name) — mahsulotni savatdan o‘chiradi.
    get_total() — savatdagi mahsulotlarning jami narxini hisoblaydi.

    Masalan:

    Mahsulotlar qo‘shilgach, foydalanuvchi get_total() metodini chaqiradi. Savatning umumiy narxi qaytarilishi kerak.

—------------------------------------------------------------------------------------------------------------------------

Qiyin

1 -  masala  ⇒

  Advanced Library Management:

    Book classiga quyidagilarni qo‘shing:

    borrower (qarz olgan odam),
    due_date (qaytarish muddati).

    Quyidagi metodlarni yozing:

    borrow(name, date) — kitobni qarzga olingan deb belgilasin.
    return_book() — qarzdorni tozalasin.
    Agar muddat o‘tgan bo‘lsa, "Jazo qo‘llaniladi" xabarini chiqarsin.

2 -  masala  ⇒
 Musiqa asbobi (Instrument) class yarating.

Elementlari:

    Asbob nomi;
    Narxi;
    Ishlab chiqaruvchi kompaniya;
    Turi (struna, klaviatura va boshqalar).

Shart:

    7 ta obyekt yarating.
    Narxi 2 mln so‘mdan yuqori va turi klaviatura bo‘lgan musiqa asboblarini chiqarib bering.

3-  masala  ⇒
  Xodimlarni boshqarish (Manager) class yarating.

Elementlari:

    Xodim ismi;
    Lavozimi;
    Ish vaqti (soat);
    Ish haqi.

Shart:

    7 ta obyekt yarating.
    Ish vaqti 40 soatdan yuqori va lavozimi "Rahbar" bo‘lgan xodimlarni ro‘yxatga oling.

4-  masala ⇒ 
Talabalar o'rtasida stipendiya tayinlash haqida masala yarating.

Class elementi quyidagilar bo'lsin:

    Talaba ismi;
    O'rtacha bahosi;
    Davlat granti yoki kontrakt asosida o'qishi;
    Stipendiya miqdori.

Class ichida kiritish va chiqarish methodlarini yozing. 5 ta obyekt yarating va faqat davlat grantida o'qiydigan va o'rtacha bahosi 85 dan yuqori bo'lgan talabalar stipendiya miqdorini chiqaring.

5  - masala  ⇒

Vaqt nomli klassda soat, minut va sekund berilgan.

Ya'na 3ta klass e'lon qiling va ular Vaqt klassiga bog'liq bo'lishi kerak:

Hour nomli klass soatni 5ga oshiradi,

Minut nomli klass minutni 5ga oshiradi va

Sekund nomli klass sekundni 5ga oshiradi.

O’zgargan vaqtni chiqaring.


