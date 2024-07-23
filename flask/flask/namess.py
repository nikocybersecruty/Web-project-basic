import random
azerbaycan_adlari = [
    "Əli", "Məmməd", "Elçin", "Elvin", "Emin", "Nurlan", "Elmir", "Cavid", "Vüsal", "Tural",
    "Anar", "Əhməd", "Həsən", "Orxan", "Kamran", "Fərid", "İsmayıl", "Ramin", "Murad", "Hüseyn",
    "İbrahim", "Fikrət", "Natiq", "İlqar", "Rahib", "Elnur", "Rəşad", "Ramiz", "Asif", "Vüqar",
    "Elman", "Ruslan", "Şahin", "Kənan", "Eşqin", "Fuad", "İlham", "Mehdi", "Pərviz", "Elnar",
    "Eltun", "Samir", "Tamerlan", "Məqsəd", "Mətləb", "Etibar", "Qafar", "İntiqam", "Həbib", "Bahadur",
    "Cahangir", "Yusif", "Toğrul", "Kamal", "Tofiq", "Arif", "Faiq", "Bahram", "Nail", "Aydın",
    "Azər", "İlkin", "Şakir", "Zaur", "Ənvər", "Qurban", "Ceyhun", "Təbriz", "Rövşən", "Samir",
    "Elşad", "Mürsəl", "Teymur", "Yaşar", "Fəxrəddin", "Qədir", "Loğman", "Cəlil", "Vidadi", "Eldar",
    "Elxan", "Pənah", "Qalib", "Hidayət", "Rüstəm", "Bayram", "Musa", "Elçin", "Qurbanəli", "Ərşad",
    "Rüfət", "Ağasəlim", "Nurəddin", "Ədalət", "Həsənağa", "Ələkbər", "Babək", "Hümmət", "Hidayət", "Nazim",
    "Qabil", "Vahid", "Adil", "Ziya", "Nazim", "Aslan", "Vasif", "Salman", "Məftun", "Sabir",
    "İsa", "Əliyar", "Zöhrab", "Mədət", "Qəşəm", "Nazim", "Babək", "Əhməd", "Kamran", "Həsənbala",
    "Kamran", "İsrafil", "Məmmədağa", "Aslan", "Ələkbər", "Etibar", "Sərvər", "Surxay", "Allahverdi", "Mübariz",
    "Sahib", "Qasım", "Bayram", "Vidadi", "Nuru", "Qüdrət", "Elçin", "Əvəz", "Səbuhi", "Ələddin",
    "Bəhrəm", "Elşən", "Sahib", "Abbas", "Mirzə", "Vilayət", "Həsənağa", "Əyyub", "Həsən", "Məmməd",
    "Tərlan", "Etibar", "Adəm", "Zakir", "Əlibala", "Məmməd", "Alim", "Mübariz", "Çingiz", "Rövşən",
    "Çingiz", "Qafar", "Səfər", "Natiq", "Müslüm", "Fəxrəddin", "Elgün", "Oqtay", "Əbülfəz", "Zülfüqar",
    "Şakir", "Sabir", "Qorxmaz", "Ümid", "Ənvər", "Nizami", "Firudin", "Vilayət", "Vaqif", "Samir",
    "Azad", "Bəhruz", "Adil", "Yaqub", "Aydın", "Rasim", "Rasim", "Qəzənfər", "Kamil", "Allahyar",
    "Akif", "Musa", "Çingiz", "İmamverdi", "İsfəndiyar", "Pərviz", "Eldar", "Mübariz", "Vüsal", "Pənah",
    "Babək", "Vahid", "Mübariz", "Ağabala", "Vidadi", "Elçin", "Adil", "Nurəddin", "Məftun", "Vaqif",
    "Tofiq", "Rəşad", "Ağadadaş", "Vilayət", "Mirzə", "Nuru", "Mürvət", "Vüqar", "Mübariz", "Elman",
    "Rafiq", "Çingiz", "Rasim", "Məmmədağa", "Əhməd", "Yaşar", "Mirzə", "Ağadadaş", "Sabir", "Əziz",
    "Fikrət", "Pərviz", "Tərlan", "Kamil", "Çingiz", "Rəşad", "Yaqub", "Ceyhun", "Mürsəl", "Çingiz",
    "Adil", "Cəlil", "Mübariz", "Zakir", "Mirzə", "Mübariz", "Çingiz", "Allahverdi", "Elçin", "Tofiq"
]
azerbaycan_soyadlari = [
    "Əliyev", "Hüseynov", "Məmmədov", "Əliyeva", "Quliyev", "Qasımov", "İbrahimov", "Qurbanov", "Abdullayev", "Rzayev",
    "Nəsirov", "İsmayılov", "Həsənov", "Mirzəyev", "Səfərov", "Süleymanov", "Fərzəliyev", "Orucov", "Vəliyev", "Rəhimov",
    "Sadıqov", "Abbasov", "Məhərrəmov", "Qəhrəmanov", "Qarayev", "Aslanov", "Əsədov", "Məlikov", "Şirinov", "Əhmədov",
    "Fətullayev", "Şahbazov", "Kazımov", "Əzimov", "Məhəmmədov", "Əkbərov", "Quliyeva", "İbrahimova", "Hüseynova", "Səfərova",
    "Abdullayeva", "Qurbanova", "İsmayılova", "Məmmədova", "Əliyeva", "Qasımova", "Rzayeva", "Nəsirova", "Həsənova", "Mirzəyeva",
    "Sadıqova", "Abbasova", "Məhərrəmova", "Qəhrəmanova", "Qarayeva", "Aslanova", "Əsədova", "Məlikova", "Şirinova", "Əhmədova",
    "Fətullayeva", "Şahbazova", "Kazımova", "Əzimova", "Məhəmmədova", "Əkbərova", "Cəfərov", "Cavadov", "İbadov", "Muradov",
    "Babayev", "İsmayıl", "Rüstəmov", "Ağayev", "Musa", "Hacıyev", "Nəbiyev", "Yusifov", "Qədirli", "Ələkbərov",
    "Eyvazov", "Xəlilov", "Əliyev", "Fətəliyev", "Cavadlı", "Mərdanov", "Rəsulov", "Şərifov", "Bayramov", "Soltanov",
    "Tağıyev", "Abbasəliyev", "Əsədov", "Şəfiyev", "Əlibəyov", "Pənahov", "Əzizov", "Nəcəfov", "Zeynalov", "Quliyev",
    "Bəşirov", "Həsənzadə", "Əfəndiyev", "Qasımzadə", "Əfəndizadə", "Abdullayev", "Qasımov", "Hüseynov", "Qurbanov", "Nəsirov",
    "Rzayev", "Əhmədov", "Kazımov", "Qədirli", "Məmmədov", "Şirinov", "Məhərrəmov", "Sadıqov", "Əsədov", "Abbasov",
    "Fərzəliyev", "Süleymanov", "İbrahimov", "Fətullayev", "Əzimov", "Şahbazov", "Qəhrəmanov", "Orucov", "Rəhimov", "Vəliyev",
    "Mirzəyev", "Həsənov", "İsmayılov", "Əliyeva", "Quliyeva", "Qasımova", "Hüseynova", "Qurbanova", "Nəsirova", "Rzayeva",
    "Əhmədova", "Kazımova", "Qədirli", "Məmmədova", "Şirinova", "Məhərrəmova", "Sadıqova", "Əsədova", "Abbasova", "Fərzəliyeva",
    "Süleymanova", "İbrahimova", "Fətullayeva", "Əzimova", "Şahbazova", "Qəhrəmanova", "Orucova", "Rəhimova", "Vəliyeva", "Mirzəyeva",
    "Həsənova", "İsmayılova", "Mustafayev", "Səmədov", "Əbdürrəhmanov", "Ələkbərov", "Nəbiyev", "Əzimov", "Rəsulzadə", "Hacıyev",
    "Babayev", "Rüstəmov", "Ağayev", "Muradov", "İbadov", "Cavadov", "Cəfərov", "Ələkbərov", "Eyvazov", "Xəlilov",
    "Əliyev", "Fətəliyev", "Cavadlı", "Mərdanov", "Rəsulov", "Şərifov", "Bayramov", "Soltanov", "Tağıyev", "Abbasəliyev",
    "Əsədov", "Şəfiyev", "Əlibəyov", "Pənahov", "Əzizov", "Nəcəfov", "Zeynalov", "Quliyev", "Bəşirov", "Həsənzadə",
    "Əfəndiyev", "Qasımzadə", "Əfəndizadə", "Abdullayev", "Qasımov", "Hüseynov", "Qurbanov", "Nəsirov", "Rzayev", "Əhmədov",
    "Kazımov", "Qədirli", "Məmmədov", "Şirinov", "Məhərrəmov", "Sadıqov", "Əsədov", "Abbasov", "Fərzəliyev", "Süleymanov",
    "İbrahimov", "Fətullayev", "Əzimov", "Şahbazov", "Qəhrəmanov", "Orucov", "Rəhimov", "Vəliyev", "Mirzəyev", "Həsənov",
    "İsmayılov", "Əliyeva", "Quliyeva", "Qasımova", "Hüseynova", "Qurbanova", "Nəsirova", "Rzayeva", "Əhmədova", "Kazımova",
    "Qədirli", "Məmmədova", "Şirinova", "Məhərrəmova", "Sadıqova", "Əsədova", "Abbasova", "Fərzəliyeva", "Süleymanova", "İbrahimova",
    "Fətullayeva", "Əzimova", "Şahbazova", "Qəhrəmanova", "Orucova", "Rəhimova", "Vəliyeva", "Mirzəyeva", "Həsənova", "İsmayılova"
]

def get_name():
    random_name=random.choice(azerbaycan_adlari)
    return random_name
def get_surname():
    random_surname=random.choice(azerbaycan_soyadlari)
    while random_surname.endswith('a'):
        random_surname = random.choice(azerbaycan_soyadlari)
    return random_surname
