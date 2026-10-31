# -*- coding: utf-8 -*-
"""
Smart Choice 1 A1 English Exam Preparation - Comprehensive Question Bank & Mobile App Generator
Generates a complete, standalone, responsive, educational HTML web app with 50 5-choice questions.
"""

import json

questions = [
    # ==========================================
    # UNIT 1: To Be, Greetings, Introductions (10 Questions)
    # ==========================================
    {
        "id": 1,
        "unit": "Ünite 1",
        "unit_title": "To Be & Tanışma",
        "question": 'A: "How are you?"\nB: "___________"',
        "options": [
            {"label": "A", "text": "I am from London."},
            {"label": "B", "text": "Fine, thanks. And you?"},
            {"label": "C", "text": "Nice to meet you, too."},
            {"label": "D", "text": "I'm a student."},
            {"label": "E", "text": "He is fine."}
        ],
        "answer": "B",
        "translation": 'A: "Nasılsın?" — B: "İyiyim, teşekkürler. Ya sen?"',
        "explanation": 'İngilizcede "How are you?" (Nasılsın?) sorusuna verilecek en doğal ve nezaket içeren karşılık "Fine, thanks. And you?" (İyiyim, teşekkürler. Ya sen?) ifadesidir.',
        "distractors": "• A şıkkı: 'Where are you from?' (Nerelisin?) sorusunun cevabıdır.\n• C şıkkı: İlk kez tanışırken söylenen 'Nice to meet you' ifadesine yanıttır.\n• D şıkkı: Meslek sorusuna ('What do you do?') yanıttır.\n• E şıkkı: 'He' (O) öznesi kullanılmıştır; soru ise doğrudan karşımızdaki 'sen'e sorulmuştur.",
        "tip": 'Soru "How are you?" veya "How is it going?" ise cevapta "Fine / Great / Not bad" ve nezaketen "And you?" ara.'
    },
    {
        "id": 2,
        "unit": "Ünite 1",
        "unit_title": "To Be & Tanışma",
        "question": 'Alex: "Maria, this is my friend Daniel."\nDaniel: "Nice to meet you, Maria."\nMaria: "___________"',
        "options": [
            {"label": "A", "text": "Nice to meet you, too."},
            {"label": "B", "text": "I don't like it."},
            {"label": "C", "text": "Yes, she is."},
            {"label": "D", "text": "Where are you from?"},
            {"label": "E", "text": "See you yesterday."}
        ],
        "answer": "A",
        "translation": 'Alex: "Maria, bu arkadaşım Daniel."\nDaniel: "Tanıştığıma memnun oldum Maria."\nMaria: "Ben de tanıştığıma memnun oldum."',
        "explanation": 'Biriyle ilk defa tanıştırıldığınızda söylenen "Nice to meet you" kalıbına verilecek tek standart nezaket cevabı, sonuna "too" (de/da) eklenerek söylenen "Nice to meet you, too" cümlesidir.',
        "distractors": "• B şıkkı: 'Bundan hoşlanmadım' diyerek kaba ve mantıksız bir ifade oluşturur.\n• C şıkkı: Evet/Hayır soru yanıtıdır.\n• D şıkkı: Memleket sorma sorusudur, nezaket cevabı değildir.\n• E şıkkı: 'See you yesterday' zaman açısından anlamsızdır (yesterday dün demektir).",
        "tip": 'Sınavda biri "Nice to meet you" diyorsa cevap mutlaka sonu "...too" ile bitendir.'
    },
    {
        "id": 3,
        "unit": "Ünite 1",
        "unit_title": "To Be & Tanışma",
        "question": 'Carrie and Mark ___________ managers at an international company.',
        "options": [
            {"label": "A", "text": "is"},
            {"label": "B", "text": "am"},
            {"label": "C", "text": "are"},
            {"label": "D", "text": "be"},
            {"label": "E", "text": "does"}
        ],
        "answer": "C",
        "translation": 'Carrie ve Mark uluslararası bir şirkette yöneticidirler.',
        "explanation": 'Öznemiz "Carrie and Mark" iki kişidir, yani 3. çoğul şahıstır (They / Onlar). Geniş Zamanda \'be\' fiili çekimi: I -> am, He/She/It -> is, You/We/They -> are. Bu yüzden doğru cevap "are" olur.',
        "distractors": "• A (is): Tekil şahıslar (he/she/it) için kullanılır.\n• B (am): Sadece 'I' (ben) öznesi ile kullanılır.\n• D (be): Fiilin çekimlenmemiş yalın halidir.\n• E (does): Eylem cümlelerinde soru/olumsuzluk yardımcı fiilidir, isim cümlesinde 'be' yerine geçemez.",
        "tip": 'İki isim "and" ile bağlanmışsa özne daima ÇOĞULDUR (They) ve ARE gerektirir.'
    },
    {
        "id": 4,
        "unit": "Ünite 1",
        "unit_title": "To Be & Tanışma",
        "question": 'A: "Where ___________ you from?"\nB: "I ___________ from Japan."',
        "options": [
            {"label": "A", "text": "are / am"},
            {"label": "B", "text": "is / am"},
            {"label": "C", "text": "are / is"},
            {"label": "D", "text": "do / am"},
            {"label": "E", "text": "are / are"}
        ],
        "answer": "A",
        "translation": 'A: "Nerelisin?" — B: "Japonya\'danım (Japonum)."',
        "explanation": 'Memleket/ülke sorarken kalıp: "Where are you from?" dur. Cevap verirken "I" öznesiyle "am" kullanılır: "I am from Japan."',
        "distractors": "• B şıkkında 'you' ile 'is' kullanılamaz.\n• C şıkkında 'I' ile 'is' kullanılamaz.\n• D şıkkında 'Where do you from?' yanlıştır; 'from' edattır, fiil değildir, 'be' fiili gerekir.\n• E şıkkında 'I are' yanlıştır.",
        "tip": 'Kalıbı unutma: "Where are you from?" -> "I am from + Ülke".'
    },
    {
        "id": 5,
        "unit": "Ünite 1",
        "unit_title": "To Be & Tanışma",
        "question": 'I ___________ a doctor. I am an architect.',
        "options": [
            {"label": "A", "text": "not am"},
            {"label": "B", "text": "am not"},
            {"label": "C", "text": "isn't"},
            {"label": "D", "text": "aren't"},
            {"label": "E", "text": "don't"}
        ],
        "answer": "B",
        "translation": 'Ben doktor değilim. Ben bir mimarım.',
        "explanation": 'I öznesinin \'to be\' ile olumsuzluk eki "am not" (veya I\'m not) şeklindedir. \'Not\' eki yardımcı fiilden sonra gelir.',
        "distractors": "• A (not am): Sözcük sırası terstir.\n• C (isn't): he/she/it içindir.\n• D (aren't): you/we/they içindir.\n• E (don't): Fiil cümlelerinde kullanılır; doktor olmak durum/isim bildirdiği için 'to be' şarttır.",
        "tip": 'I öznesi için "amn\'t" diye bir kısaltma YOKTUR! Doğrusu "I\'m not" veya "I am not"tır.'
    },
    {
        "id": 6,
        "unit": "Ünite 1",
        "unit_title": "To Be & Tanışma",
        "question": '___________ your parents at home right now?',
        "options": [
            {"label": "A", "text": "Is"},
            {"label": "B", "text": "Are"},
            {"label": "C", "text": "Do"},
            {"label": "D", "text": "Does"},
            {"label": "E", "text": "Was"}
        ],
        "answer": "B",
        "translation": 'Anne baban şu anda evdeler mi?',
        "explanation": '"Your parents" (ebeveynlerin) çoğul bir kelimedir (sonundaki -s takısına dikkat). Öznesi "they" olduğu için ve cümlede başka bir fiil bulunmadığından soru çoğul \'to be\' fiili olan "Are" ile kurulur.',
        "distractors": "• A (Is): Tekil özneler içindir.\n• C ve D (Do/Does): Cümlede ana bir eylem fiili varsa kullanılır (Örn: Do your parents live in Izmir?). Burada sadece 'at home' yer ifadesi vardır.\n• E (Was): Tekil ve geçmiş zaman halidir.",
        "tip": 'Parents (anne-baba), shoes (ayakkabılar), glasses (gözlük) gibi çoğul kelimeler daima ARE alır.'
    },
    {
        "id": 7,
        "unit": "Ünite 1",
        "unit_title": "To Be & Tanışma",
        "question": 'A: "Is he an engineer at this company?"\nB: "Yes, ___________."',
        "options": [
            {"label": "A", "text": "he does."},
            {"label": "B", "text": "he is."},
            {"label": "C", "text": "he's."},
            {"label": "D", "text": "is he."},
            {"label": "E", "text": "he has."}
        ],
        "answer": "B",
        "translation": 'A: "O bu şirkette mühendis mi?" — B: "Evet, öyle."',
        "explanation": '"Is he...?" sorusunun olumlu kısa yanıtı "Yes, he is." şeklinde verilir. Kısa olumlu cevaplarda KESİNLİKLE kısaltma yapılmaz ("Yes, he\'s" YANLIŞTIR).',
        "distractors": "• A (he does): 'Does he...?' sorusunun cevabıdır.\n• C (he's): İngilizce dilbilgisinde kısa olumlu cevaplarda apostrof ile kısaltma yapılamaz!\n• D (is he): Soru sıralamasıdır.\n• E (he has): Soru 'to be' ile sorulmuştur, have ile cevap verilemez.",
        "tip": 'Sınav Tuzağı: Kısa olumlu yanıtta ASLA kısaltma olmaz! Doğrusu: Yes, I am. / Yes, he is. / Yes, they are.'
    },
    {
        "id": 8,
        "unit": "Ünite 1",
        "unit_title": "To Be & Tanışma",
        "question": 'My sister is ___________ architect, and my brother is ___________ photographer.',
        "options": [
            {"label": "A", "text": "an / a"},
            {"label": "B", "text": "a / an"},
            {"label": "C", "text": "a / a"},
            {"label": "D", "text": "an / an"},
            {"label": "E", "text": "the / the"}
        ],
        "answer": "A",
        "translation": 'Kız kardeşim bir mimar, erkek kardeşim ise bir fotoğrafçıdır.',
        "explanation": 'Tekil meslek isimlerinin önüne sesli harf ile başlıyorsa "an" (an architect, an actor), sessiz harf ile başlıyorsa "a" (a photographer, a doctor) gelir.',
        "distractors": "• B şıkkında a architect ve an photographer denmiştir, harf kuralına aykırıdır.\n• C, D ve E seçenekleri sesli/sessiz uyumuna uymaz.",
        "tip": 'Sesli ile başlayan meslekler: an architect, an actor, an engineer, an artist. Sessizle başlayanlar: a doctor, a teacher, a manager.'
    },
    {
        "id": 9,
        "unit": "Ünite 1",
        "unit_title": "To Be & Tanışma",
        "question": 'A: "___________ is your phone number?"\nB: "It is 555-0192."',
        "options": [
            {"label": "A", "text": "Who"},
            {"label": "B", "text": "Where"},
            {"label": "C", "text": "What"},
            {"label": "D", "text": "How"},
            {"label": "E", "text": "Why"}
        ],
        "answer": "C",
        "translation": 'A: "Telefon numaran nedir?" — B: "555-0192\'dir."',
        "explanation": 'Telefon numarası, isim, soyisim, e-posta gibi kişisel bilgileri sorarken soru zamiri olarak "What" (Ne / Nedir) kullanılır: "What is your phone number?"',
        "distractors": "• A (Who): 'Kim?' demektir, insanları sorar.\n• B (Where): 'Nerede / Nereye?' demektir, yer sorar.\n• D (How): 'Nasıl?' demektir.\n• E (Why): 'Neden / Niçin?' demektir.",
        "tip": 'Telefon numarası ve isim sorularında standart kalıp: "What is your...?"'
    },
    {
        "id": 10,
        "unit": "Ünite 1",
        "unit_title": "To Be & Tanışma",
        "question": 'Aşağıdaki cümlelerin hangisi dilbilgisi kurallarına göre **tamamen doğrudur**?',
        "options": [
            {"label": "A", "text": "She are from Canada."},
            {"label": "B", "text": "They isn't at work today."},
            {"label": "C", "text": "How old are you?"},
            {"label": "D", "text": "Are he a student?"},
            {"label": "E", "text": "I is 20 years old."}
        ],
        "answer": "C",
        "translation": 'Kaç yaşındasın?',
        "explanation": '"How old are you?" cümlesi; soru kalıbı, çoğul yardımcı fiil (are) ve özne (you) uyumu açısından kusursuzdur.',
        "distractors": "• A şıkkında 'She is' olmalıdır.\n• B şıkkında 'They aren't' olmalıdır.\n• D şıkkında 'Is he' olmalıdır.\n• E şıkkında 'I am' olmalıdır.",
        "tip": 'Özne-Yüklem Tablosu: I AM | HE/SHE/IT IS | YOU/WE/THEY ARE.'
    },

    # ==========================================
    # UNIT 2: Simple Present, Daily Routines, Jobs (10 Questions)
    # ==========================================
    {
        "id": 11,
        "unit": "Ünite 2",
        "unit_title": "Present Simple & Meslekler",
        "question": 'Daniel ___________ in an office, but his wife ___________ from home.',
        "options": [
            {"label": "A", "text": "work / work"},
            {"label": "B", "text": "works / works"},
            {"label": "C", "text": "work / works"},
            {"label": "D", "text": "works / work"},
            {"label": "E", "text": "is working / work"}
        ],
        "answer": "B",
        "translation": 'Daniel bir ofiste çalışır, fakat eşi evden çalışır.',
        "explanation": 'Daniel (He) ve his wife (She) 3. tekil şahıstır. Geniş Zamanda (Simple Present) olumlu cümlelerde he/she/it özneleriyle fiile -s takısı eklenir: work -> works.',
        "distractors": "• A: İki fiilde de -s takısı unutulmuştur.\n• C ve D: Fiillerden biri yalın bırakılmıştır; her iki özne de tekildir (-s gerekir).\n• E: Rutin durumlar için Present Simple (works) tercih edilir.",
        "tip": 'Geniş Zaman Kuralı: He / She / It öznesi olumlu cümlede fiile mutlaka -s, -es veya -ies taktırır!'
    },
    {
        "id": 12,
        "unit": "Ünite 2",
        "unit_title": "Present Simple & Meslekler",
        "question": 'My father ___________ TV every evening, and my mother ___________ to university by subway.',
        "options": [
            {"label": "A", "text": "watch / go"},
            {"label": "B", "text": "watches / goes"},
            {"label": "C", "text": "watchs / gos"},
            {"label": "D", "text": "watchies / go"},
            {"label": "E", "text": "is watching / is going"}
        ],
        "answer": "B",
        "translation": 'Babam her akşam televizyon izler ve annem metroyla üniversiteye gider.',
        "explanation": 'Fiiller -ch, -sh, -ss, -x veya -o ile bitiyorsa 3. tekil şahısta sonlarına sadece -s değil, **-es** eklenir: watch -> watches, go -> goes.',
        "distractors": "• A: Fiiller yalın bırakılmıştır.\n• C: 'watchs' ve 'gos' yanlış yazılmıştır (-es gerekir).\n• D: 'watchies' tamamen hatalı bir kurgudur.\n• E: 'every evening' rutin bildirdiği için Present Simple gerekir.",
        "tip": 'Yazım Kuralı: -ch (watches), -sh (washes), -o (goes, does), -ss (passes), -x (fixes) fiilleri -ES alır.'
    },
    {
        "id": 13,
        "unit": "Ünite 2",
        "unit_title": "Present Simple & Meslekler",
        "question": 'She ___________ English on Mondays, but she ___________ on weekends.',
        "options": [
            {"label": "A", "text": "studys / don't study"},
            {"label": "B", "text": "studies / doesn't study"},
            {"label": "C", "text": "study / doesn't study"},
            {"label": "D", "text": "studies / don't study"},
            {"label": "E", "text": "is studying / isn't study"}
        ],
        "answer": "B",
        "translation": 'O pazartesi günleri İngilizce çalışır, fakat hafta sonları ders çalışmaz.',
        "explanation": '1) "study" fiili sessiz harf + y ile bittiği için 3. tekil şahısta \'y\' harfi düşer ve **-ies** gelir (studies). 2) 3. tekil şahsın olumsuzunda **doesn\'t + yalın fiil** kullanılır (doesn\'t study).',
        "distractors": "• A: 'studys' yanlış yazımdır (y düşmeli), ayrıca 'she' ile 'don't' kullanılmaz.\n• C: İlk fiilde -s/-ies takısı eksiktir.\n• D: 'she' öznesiyle 'don't' kullanılamaz (doesn't olmalı).\n• E: Yapısal olarak hatalıdır.",
        "tip": 'Sessiz + y ile bitenler: study -> studies, fly -> flies. Sesli + y ile bitenler: play -> plays.'
    },
    {
        "id": 14,
        "unit": "Ünite 2",
        "unit_title": "Present Simple & Meslekler",
        "question": 'They ___________ for Korean Air, and he ___________ in Recife.',
        "options": [
            {"label": "A", "text": "don't work / doesn't live"},
            {"label": "B", "text": "doesn't work / don't live"},
            {"label": "C", "text": "don't works / doesn't lives"},
            {"label": "D", "text": "aren't work / isn't live"},
            {"label": "E", "text": "not work / not live"}
        ],
        "answer": "A",
        "translation": 'Onlar Korean Air için çalışmıyorlar ve o Recife\'de yaşamıyor.',
        "explanation": 'Geniş Zaman olumsuz cümle kuralı:\n• I / You / We / They + **don\'t + fiilin yalın hali**\n• He / She / It + **doesn\'t + fiilin yalın hali**\nÖnemli: doesn\'t geldikten sonra fiile ASLA tekrar -s takısı eklenmez!',
        "distractors": "• B şıkkında özneler ve yardımcı fiiller ters eşleştirilmiştir.\n• C şıkkında don't ve doesn't sonrası fiillere -s eklenmiştir (büyük hata!).\n• D şıkkında to be (aren't/isn't) ile yalın fiil bir arada kullanılmıştır (gramer dışı).\n• E şıkkında yardımcı fiil yoktur.",
        "tip": 'Altın Kural: Don\'t veya Doesn\'t gördüğün anda fiil %100 YALIN (s takısız) kalır!'
    },
    {
        "id": 15,
        "unit": "Ünite 2",
        "unit_title": "Present Simple & Meslekler",
        "question": '___________ you work in an office, or ___________ your brother work in a hospital?',
        "options": [
            {"label": "A", "text": "Do / does"},
            {"label": "B", "text": "Does / do"},
            {"label": "C", "text": "Do / do"},
            {"label": "D", "text": "Are / is"},
            {"label": "E", "text": "Does / does"}
        ],
        "answer": "A",
        "translation": 'Sen bir ofiste mi çalışıyorsun, yoksa erkek kardeşin bir hastanede mi çalışıyor?',
        "explanation": 'Geniş Zamanda eylem bildiren fiillerle (work) soru yaparken:\n• "you" öznesi için **Do** kullanılır: Do you work...?\n• "your brother" (he) tekil öznesi için **Does** kullanılır: Does your brother work...?',
        "distractors": "• B şıkkında Do ve Does ters yazılmıştır.\n• C şıkkında brother (he) için 'do' kullanılmıştır.\n• D şıkkında Are ve Is kullanılmıştır (Are you work denmez, Are you working veya Do you work denir).\n• E şıkkında you ile 'does' kullanılmıştır.",
        "tip": 'Soru oluştururken: I/You/We/They -> DO | He/She/It -> DOES.'
    },
    {
        "id": 16,
        "unit": "Ünite 2",
        "unit_title": "Present Simple & Meslekler",
        "question": 'A: "Where ___________ she ___________?"\nB: "She works in a software company."',
        "options": [
            {"label": "A", "text": "do / work"},
            {"label": "B", "text": "does / work"},
            {"label": "C", "text": "does / works"},
            {"label": "D", "text": "is / work"},
            {"label": "E", "text": "does / working"}
        ],
        "answer": "B",
        "translation": 'A: "O nerede çalışıyor?" — B: "Bir yazılım şirketinde çalışıyor."',
        "explanation": 'Wh- Soru Sözcüğü Dizilimi:\nSoru Kelimesi + Do/Does + Özne + Fiilin YALIN hali?\n"She" tekil özne olduğu için "does" gelir, esas fiil "work" ise yalın kalır: "Where does she work?"',
        "distractors": "• A: 'she' öznesiyle 'do' kullanılamaz.\n• C: Soru cümlesinde 'does' varken fiile bir daha 's' takılmaz ('works' denmez).\n• D: 'is' ile yalın fiil 'work' yan yana gelemez.\n• E: Geniş zaman soru kalıbında -ing kullanılmaz.",
        "tip": 'Hocaların en çok soru hazırladığı yer: Soru ve olumsuzlarda DOES geldiğinde fiildeki -s UÇAR!'
    },
    {
        "id": 17,
        "unit": "Ünite 2",
        "unit_title": "Present Simple & Meslekler",
        "question": 'A: "What do you do?"\nB: "___________"',
        "options": [
            {"label": "A", "text": "I am doing homework right now."},
            {"label": "B", "text": "I'm an engineer."},
            {"label": "C", "text": "I'm fine, thank you."},
            {"label": "D", "text": "Yes, I do."},
            {"label": "E", "text": "I was at home yesterday."}
        ],
        "answer": "B",
        "translation": 'A: "Ne iş yapıyorsun? (Mesleğin ne?)" — B: "Ben bir mühendisim."',
        "explanation": '"What do you do?" sorusu İngilizcede kalıplaşmış bir ifadedir ve "Mesleğin ne? Ne işle meşgulsün?" anlamına gelir. Cevabı daima meslek veya öğrenci olma durumuyla verilir ("I\'m an engineer / student").',
        "distractors": "• A: 'Şu an ne yapıyorsun?' sorusunun ('What are you doing?') cevabıdır.\n• C: 'How are you?' sorusunun cevabıdır.\n• D: 'Do you...?' ile başlayan evet/hayır sorularının cevabıdır; Wh- sorusuna yes/no denmez.\n• E: Geçmiş zaman yer bildirir.",
        "tip": 'FARKA DİKKAT: "What do you do?" = Mesleğin ne? / "What are you doing?" = Şu an ne yapıyorsun?'
    },
    {
        "id": 18,
        "unit": "Ünite 2",
        "unit_title": "Present Simple & Meslekler",
        "question": 'A: "Does she teach at a university?"\nB: "No, ___________."',
        "options": [
            {"label": "A", "text": "she don't."},
            {"label": "B", "text": "she doesn't."},
            {"label": "C", "text": "she isn't."},
            {"label": "D", "text": "she doesn't teaches."},
            {"label": "E", "text": "she not."}
        ],
        "answer": "B",
        "translation": 'A: "O bir üniversitede ders veriyor mu?" — B: "Hayır, vermiyor."',
        "explanation": '"Does she...?" sorusunun olumsuz kısa cevabı "No, she doesn\'t." şeklindedir. Kısa cevap soru hangi yardımcı fiille sorulmuşsa (Does) onunla tamamlanır.',
        "distractors": "• A: 'she' öznesiyle 'don't' kullanılmaz.\n• C: Soru 'Is she...?' olsaydı 'she isn't' olurdu; soru Does ile sorulmuştur.\n• D: Kısa cevapta fiil tekrar edilmez, sadece yardımcı fiil konur.\n• E: Eksik ve bozuk yapıdır.",
        "tip": 'Soru neyle başladıysa kısa cevap onunla biter: Does she...? -> Yes, she does / No, she doesn\'t.'
    },
    {
        "id": 19,
        "unit": "Ünite 2",
        "unit_title": "Present Simple & Meslekler",
        "question": 'Mark ___________ two brothers, but he ___________ a car.',
        "options": [
            {"label": "A", "text": "haves / doesn't have"},
            {"label": "B", "text": "has / doesn't has"},
            {"label": "C", "text": "has / doesn't have"},
            {"label": "D", "text": "have / don't have"},
            {"label": "E", "text": "is having / hasn't"}
        ],
        "answer": "C",
        "translation": 'Mark\'ın iki erkek kardeşi var, fakat arabası yok.',
        "explanation": '"Have" (sahip olmak) fiili he/she/it için düzensizdir ve **has** olur ("haves" diye bir kelime yoktur). Olumsuz cümlede ise doesn\'t geldikten sonra fiil yalın haline döner: **doesn\'t have**.',
        "distractors": "• A: 'haves' diye bir İngilizce kelime yoktur.\n• B: doesn't sonrasında 'has' değil yalın hal olan 'have' gelmelidir.\n• D: Mark tekil şahıstır, olumlu cümlede have denemez.\n• E: Sahiplik anlamındaki have -ing almaz.",
        "tip": 'Önemli İstisna: He has (olumlu) AMA He doesn\'t have (olumsuz) / Does he have? (soru).'
    },
    {
        "id": 20,
        "unit": "Ünite 2",
        "unit_title": "Present Simple & Meslekler",
        "question": 'Aşağıdaki cümlelerin hangisinde bir **dilbilgisi hatası** vardır?',
        "options": [
            {"label": "A", "text": "Where do they live?"},
            {"label": "B", "text": "He doesn't likes coffee."},
            {"label": "C", "text": "She teaches English at high school."},
            {"label": "D", "text": "Do you have a pet?"},
            {"label": "E", "text": "We don't watch TV in the morning."}
        ],
        "answer": "B",
        "translation": 'O kahve sevmez. (Cümle hatalıdır!)',
        "explanation": 'B şıkkında kural hatası yapılmıştır: Cümlede "doesn\'t" yardımcı fiili varken ana fiil yalın kalmalıdır ("He doesn\'t like coffee" olmalıdır, likes YANLIŞTIR). Diğer bütün şıklar tamamen doğrudur.',
        "distractors": "• A şıkkı: Where + do + they + live? (Doğru)\n• C şıkkı: She + teaches (-ch sonuna -es gelmiş, Doğru)\n• D şıkkı: Do + you + have...? (Doğru)\n• E şıkkı: We + don't + watch... (Doğru)",
        "tip": 'Hata bulma sorularında gözün hemen "doesn\'t / does + fiil-s" aramasın; orası %90 tuzaktır!'
    },

    # ==========================================
    # UNIT 4: Frequency Adverbs & How Often (8 Questions)
    # ==========================================
    {
        "id": 21,
        "unit": "Ünite 4",
        "unit_title": "Frequency Adverbs & How Often",
        "question": 'Which frequency adverb represents **100% of the time (7 days a week)**?',
        "options": [
            {"label": "A", "text": "never"},
            {"label": "B", "text": "sometimes"},
            {"label": "C", "text": "usually"},
            {"label": "D", "text": "always"},
            {"label": "E", "text": "hardly ever"}
        ],
        "answer": "D",
        "translation": 'Hangi sıklık zarfı zamanın %100\'ünü (haftada 7 gün) temsil eder?',
        "explanation": 'Smart Choice Ünite 4 sıklık tablosuna göre:\n• **always** = %100 (Her zaman / haftanın 7 günü)\n• **usually** = %80 (Genellikle / haftanın 5-6 günü)\n• **sometimes** = %50 (Bazen / haftanın 2-3 günü)\n• **never** = %0 (Asla / hiç / 0 gün)',
        "distractors": "• A (never) %0'dır.\n• B (sometimes) %50'dir.\n• C (usually) %80'dir.\n• E (hardly ever) neredeyse hiçtir (%10 civarı).",
        "tip": 'Sıralama: always (%100) > usually (%80) > sometimes (%50) > never (%0).'
    },
    {
        "id": 22,
        "unit": "Ünite 4",
        "unit_title": "Frequency Adverbs & How Often",
        "question": 'I ___________ do yoga. (0 days a week — I really dislike it!)',
        "options": [
            {"label": "A", "text": "always"},
            {"label": "B", "text": "usually"},
            {"label": "C", "text": "sometimes"},
            {"label": "D", "text": "never"},
            {"label": "E", "text": "often"}
        ],
        "answer": "D",
        "translation": 'Ben asla yoga yapmam. (Haftada 0 gün — gerçekten hiç sevmem!)',
        "explanation": 'Parantez içinde verilen "0 days a week" (haftada sıfır gün) bilgisi eylemin hiçbir zaman yapılmadığını gösterir. %0 sıklık bildiren kelime **never** (asla/hiç) dır.',
        "distractors": "• A, B, C ve E seçenekleri eylemin belirli sıklıklarla yapıldığını belirtir (0 gün olamaz).",
        "tip": 'Soru kökünde \"0 days\" veya \"not ever\" görürsen cevabın tereddütsüz \"never\"dır.'
    },
    {
        "id": 23,
        "unit": "Ünite 4",
        "unit_title": "Frequency Adverbs & How Often",
        "question": 'Kelimelerin **doğru cümle dizilişi** hangisidir? (usually / get up / I / early)',
        "options": [
            {"label": "A", "text": "I get up usually early."},
            {"label": "B", "text": "I usually get up early."},
            {"label": "C", "text": "Usually I get up early always."},
            {"label": "D", "text": "Get up I usually early."},
            {"label": "E", "text": "I get usually up early."}
        ],
        "answer": "B",
        "translation": 'Ben genellikle erken kalkarım.',
        "explanation": 'Sıklık zarflarının (always, usually, sometimes, never) normal eylem fiilleriyle kullanım kuralı: Fiilden **ÖNCE** gelirler.\nFormül: **Özne + Sıklık Zarfı + Esas Fiil** -> "I usually get up early."',
        "distractors": "• A şıkkında sıklık zarfı fiilden sonraya konmuştur.\n• C şıkkında hem usually hem always bir arada kullanılmıştır.\n• D ve E şıklarında fiil ve özne dizilimi bozulmuştur.",
        "tip": 'Kural: Normal fiillerden ÖNCE (before main verbs), To Be fiilinden SONRA (after be).'
    },
    {
        "id": 24,
        "unit": "Ünite 4",
        "unit_title": "Frequency Adverbs & How Often",
        "question": 'Which sentence is grammatically **correct** regarding the position of the adverb?',
        "options": [
            {"label": "A", "text": "He never is late for class."},
            {"label": "B", "text": "He is late never for class."},
            {"label": "C", "text": "He is never late for class."},
            {"label": "D", "text": "Never he is late for class."},
            {"label": "E", "text": "He late is never for class."}
        ],
        "answer": "C",
        "translation": 'O derse asla geç kalmaz.',
        "explanation": 'Sıklık zarfları "To Be" (am, is, are, was, were) fiillerinden **SONRA** gelir.\nFormül: **Özne + am/is/are + Sıklık Zarfı** -> "He is never late."',
        "distractors": "• A: 'never' to be fiilinin önüne konmuştur (yanlış).\n• B: Sıfattan sonraya konmuştur (yanlış).\n• D: Cümle başına konmuştur (yanlış).\n• E: Cümle dizilimi tamamen bozuktur.",
        "tip": 'Akılda tutma formülü: "BE + Frequency Adverb" (am always, is usually, are never).'
    },
    {
        "id": 25,
        "unit": "Ünite 4",
        "unit_title": "Frequency Adverbs & How Often",
        "question": 'A: "___________ do you play tennis?"\nB: "Twice a week."',
        "options": [
            {"label": "A", "text": "How many"},
            {"label": "B", "text": "How much"},
            {"label": "C", "text": "How often"},
            {"label": "D", "text": "How long"},
            {"label": "E", "text": "How old"}
        ],
        "answer": "C",
        "translation": 'A: "Ne sıklıkla tenis oynarsın?" — B: "Haftada iki kez."',
        "explanation": 'Bir eylemin ne sıklıkla tekrarlandığını sormak için kullanılan soru kalıbı **How often...?** (Ne sıklıkla?) dır. Cevapta sıklık belirteçleri (once a week, twice a week, usually vb.) yer alır.',
        "distractors": "• A (How many): 'Kaç tane?' demektir, sayılabilen miktar sorar.\n• B (How much): 'Ne kadar?' demektir, fiyat/miktar sorar.\n• D (How long): 'Ne kadar süre?' demektir.\n• E (How old): 'Kaç yaşında?' demektir.",
        "tip": 'Cevapta "once / twice / three times a week / every day" varsa soru kesinlikle "How often"dır.'
    },
    {
        "id": 26,
        "unit": "Ünite 4",
        "unit_title": "Frequency Adverbs & How Often",
        "question": 'Anna goes swimming only on Wednesdays. So she swims ___________ a week.',
        "options": [
            {"label": "A", "text": "once"},
            {"label": "B", "text": "twice"},
            {"label": "C", "text": "two times"},
            {"label": "D", "text": "four times"},
            {"label": "E", "text": "every"}
        ],
        "answer": "A",
        "translation": 'Anna sadece çarşamba günleri yüzmeye gider. Yani haftada bir kez yüzer.',
        "explanation": 'İngilizcede tekrarlanma sıklıkları:\n• 1 kez = **once** (once a week)\n• 2 kez = **twice** (twice a week)\n• 3 veya daha fazla kez = **three times, four times** a week. Çarşamba tek bir gün olduğu için cevap "once" dır.',
        "distractors": "• B ve C iki kez demektir.\n• D dört kez demektir.\n• E 'every a week' şeklinde kullanılamaz ('every week' denir).",
        "tip": '1 kez = ONCE, 2 kez = TWICE. Üçten sonra rakam + times: three times, four times.'
    },
    {
        "id": 27,
        "unit": "Ünite 4",
        "unit_title": "Frequency Adverbs & How Often",
        "question": '"every day", "once a week" ve "three times a month" gibi zaman ifadeleri kural olarak cümlenin neresinde yer alır?',
        "options": [
            {"label": "A", "text": "Özne ile fiilin hemen arasında"},
            {"label": "B", "text": "Cümlenin en sonunda"},
            {"label": "C", "text": "Sadece yardımcı fiilden hemen önce"},
            {"label": "D", "text": "Fiilden hemen önce, özneden sonra"},
            {"label": "E", "text": "Soru kelimesinin hemen yanında"}
        ],
        "answer": "B",
        "translation": '"Her gün", "haftada bir kez", "ayda üç kez" gibi ifadeler cümlenin sonunda yer alır.',
        "explanation": 'Tek kelimelik sıklık zarfları (always, usually) fiilden önce gelirken; kelime öbeği şeklindeki zaman/sıklık belirteçleri (every day, once a week, twice a month) cümlenin **EN SONUNDA** yer alır (Örn: I go running every day / She plays tennis twice a week).',
        "distractors": "• A ve D: Tek kelimelik sıklık zarflarının yeridir.\n• C ve E: Gramer dışıdır.",
        "tip": 'Always / usually -> Fiilin ÖNÜNDE; Every day / once a week -> Cümlenin SONUNDA.'
    },
    {
        "id": 28,
        "unit": "Ünite 4",
        "unit_title": "Frequency Adverbs & How Often",
        "question": 'A: "Do you ever exercise after class?"\nB: "Yes, I ___________ play tennis with my friend."',
        "options": [
            {"label": "A", "text": "never"},
            {"label": "B", "text": "usually"},
            {"label": "C", "text": "not"},
            {"label": "D", "text": "don't"},
            {"label": "E", "text": "am"}
        ],
        "answer": "B",
        "translation": 'A: "Derslerden sonra hiç egzersiz yapar mısın?" — B: "Evet, genellikle arkadaşımla tenis oynarım."',
        "explanation": 'Cevap "Yes" ile başladığı için olumlu bir sıklık zarfı gelmelidir. "usually" (genellikle) anlam ve gramer olarak cümleyi doğru tamamlar.',
        "distractors": "• A (never): Cümle 'Yes' ile başlarken 'never' (asla) kullanılamaz; çelişki yaratır.\n• C ve D: Olumsuzluk ekleridir, Yes ile başlayan olumlu cümleye uymaz.\n• E (am): 'I am play tennis' hatalı bir yapıdır.",
        "tip": '\"Do you ever...?\" (Hiç ... yapar mısın?) sorusuna olumlu cevapta usually/always/sometimes, olumsuzda No, never denir.'
    },

    # ==========================================
    # UNIT 5 / MIXED: Present Simple vs Present Continuous (12 Questions)
    # ==========================================
    {
        "id": 29,
        "unit": "Ünite 5",
        "unit_title": "Present Simple vs Continuous",
        "question": 'Look! The children ___________ in the park right now.',
        "options": [
            {"label": "A", "text": "play"},
            {"label": "B", "text": "plays"},
            {"label": "C", "text": "are playing"},
            {"label": "D", "text": "is playing"},
            {"label": "E", "text": "played"}
        ],
        "answer": "C",
        "translation": 'Bak! Çocuklar şu anda parkta oynuyorlar.',
        "explanation": '"Look!" (Bak!) uyarısı ve "right now" (şu anda) zaman zarfı, eylemin konuşma anında yapıldığını gösterir. Bu yüzden Şimdiki Zaman (Present Continuous: am/is/are + V-ing) kullanılır. Öznemiz "the children" çoğul (onlar) olduğu için **are playing** doğru cevaptır.',
        "distractors": "• A ve B: Geniş Zaman biçimleridir; şu an süren eylemde -ing gerekir.\n• D (is playing): Tekil özneler içindir; 'children' çoğuldur (child tekil, children çoğul).\n• E (played): Geçmiş zamandır.",
        "tip": 'Anahtar Kelimeler: Look!, Listen!, Be quiet!, right now, at the moment görürsen doğrudan AM/IS/ARE + V-ing işaretle!'
    },
    {
        "id": 30,
        "unit": "Ünite 5",
        "unit_title": "Present Simple vs Continuous",
        "question": 'My sister ___________ the piano every day, but right now she ___________ a book.',
        "options": [
            {"label": "A", "text": "plays / reads"},
            {"label": "B", "text": "is playing / is reading"},
            {"label": "C", "text": "plays / is reading"},
            {"label": "D", "text": "is playing / reads"},
            {"label": "E", "text": "play / reading"}
        ],
        "answer": "C",
        "translation": 'Kız kardeşim her gün piyano çalar, fakat şu anda kitap okuyor.',
        "explanation": 'Cümlenin ilk kısmı "every day" (her gün) rutin bildirdiği için Present Simple (plays) gerektirir. İkinci kısmı ise "right now" (şu anda) dediği için Present Continuous (is reading) gerektirir.',
        "distractors": "• A: İkinci kısımda 'right now' varken reads kullanılmıştır.\n• B: İlk kısımda 'every day' varken is playing kullanılmıştır.\n• D: Zamanlar ters verilmiştir.\n• E: Dilbilgisi çekimleri eksiktir.",
        "tip": 'Zaman Zarfı Eşleşmesi: "every day / on Sundays" -> Present Simple (-s) | "right now / at the moment" -> Continuous (is/are -ing).'
    },
    {
        "id": 31,
        "unit": "Ünite 5",
        "unit_title": "Present Simple vs Continuous",
        "question": 'He ___________ TV at the moment. He is sleeping in his room.',
        "options": [
            {"label": "A", "text": "doesn't watch"},
            {"label": "B", "text": "isn't watching"},
            {"label": "C", "text": "don't watch"},
            {"label": "D", "text": "aren't watching"},
            {"label": "E", "text": "not watching"}
        ],
        "answer": "B",
        "translation": 'O şu anda televizyon izlemiyor. Odasında uyuyor.',
        "explanation": '"at the moment" (şu anda) ifadesi Present Continuous olumsuz yapısını gerektirir: Özne + am not / isn\'t / aren\'t + fiil-ing. "He" öznesi için doğru biçim **isn\'t watching** dir.',
        "distractors": "• A (doesn't watch): Rutin olumsuzluklarda kullanılır, at the moment ile kullanılmaz.\n• C (don't watch): Hem geniş zamandır hem 'he' ile don't kullanılmaz.\n• D (aren't watching): Çoğul özneler içindir.\n• E (not watching): Yardımcı fiil 'is' eksiktir.",
        "tip": '"at the moment" = şu anda = isn\'t / aren\'t + V-ing.'
    },
    {
        "id": 32,
        "unit": "Ünite 5",
        "unit_title": "Present Simple vs Continuous",
        "question": 'Be quiet! The baby ___________ in the bedroom.',
        "options": [
            {"label": "A", "text": "sleep"},
            {"label": "B", "text": "sleeps"},
            {"label": "C", "text": "is sleeping"},
            {"label": "D", "text": "are sleeping"},
            {"label": "E", "text": "does sleep"}
        ],
        "answer": "C",
        "translation": 'Sessiz ol! Bebek yatak odasında uyuyor.',
        "explanation": '"Be quiet!" (Sessiz ol!) uyarısı tam o anda gerçekleşen kritik bir durumu bildirir. "The baby" tekil bir özne (it/he/she) olduğu için **is sleeping** kullanılır.',
        "distractors": "• A ve B: Geniş zaman formlarıdır, konuşma anındaki eylemi anlatamazlar.\n• D (are sleeping): 'The baby' tekildir, 'are' çoğuldur.\n• E: Vurgulu olumlu geniş zaman yapısıdır, bağlama uymaz.",
        "tip": '"Listen!", "Be quiet!", "Look out!" gibi ünlemler konuşma anını işaret eder, doğrudan şimdiki zamana (is/are -ing) götürür.'
    },
    {
        "id": 33,
        "unit": "Ünite 5",
        "unit_title": "Present Simple vs Continuous",
        "question": 'A: "What ___________ you ___________ right now?"\nB: "I\'m doing my homework."',
        "options": [
            {"label": "A", "text": "do / do"},
            {"label": "B", "text": "are / doing"},
            {"label": "C", "text": "does / do"},
            {"label": "D", "text": "are / do"},
            {"label": "E", "text": "do / doing"}
        ],
        "answer": "B",
        "translation": 'A: "Şu anda ne yapıyorsun?" — B: "Ödevimi yapıyorum."',
        "explanation": '"right now" şu anda yapılan eylemi sorduğu için Present Continuous soru dizilimi kullanılır: Wh- word + am/is/are + özne + V-ing? -> "What **are** you **doing** right now?"',
        "distractors": "• A (What do you do?): Meslek sorusudur, 'right now' ile kullanılmaz.\n• C: 'you' ile 'does' kullanılmaz.\n• D: 'are' yardımcı fiilinden sonra fiil yalın kalamaz (-ing şarttır).\n• E: 'do' ile '-ing' birleşemez.",
        "tip": 'Şimdiki zaman sorusunda "are/is" başa, fiilin sonuna ise "-ing" gelir.'
    },
    {
        "id": 34,
        "unit": "Ünite 5",
        "unit_title": "Present Simple vs Continuous",
        "question": 'The local library ___________ on Sundays.',
        "options": [
            {"label": "A", "text": "isn't opening"},
            {"label": "B", "text": "doesn't open"},
            {"label": "C", "text": "don't open"},
            {"label": "D", "text": "aren't open"},
            {"label": "E", "text": "not open"}
        ],
        "answer": "B",
        "translation": 'Yerel kütüphane pazar günleri açılmaz.',
        "explanation": '"on Sundays" (pazar günleri) ifadesi genel bir çalışma saatini / kuralı belirtir. Genel kurallar Present Simple ile anlatılır. "The local library" tekil (it) olduğu için olumsuz hali **doesn\'t open** dır.',
        "distractors": "• A (isn't opening): Geçici bir şimdiki zaman anlatır; genel kurallarda Present Simple esastır.\n• C (don't open): Tekil özneyle don't kullanılmaz.\n• D (aren't open): open burada fiildir, aren't ile yalın fiil birleşmez.\n• E: Yardımcı fiil eksiktir.",
        "tip": 'Günlerin çoğul hali ("on Sundays / on Mondays") her pazar/pazartesi anlamına gelir, DAİMA Geniş Zaman (doesn\'t/don\'t) ister.'
    },
    {
        "id": 35,
        "unit": "Ünite 5",
        "unit_title": "Present Simple vs Continuous",
        "question": 'I ___________ video games right now. I am studying for my English exam!',
        "options": [
            {"label": "A", "text": "don't play"},
            {"label": "B", "text": "am not playing"},
            {"label": "C", "text": "not playing"},
            {"label": "D", "text": "isn't playing"},
            {"label": "E", "text": "doesn't play"}
        ],
        "answer": "B",
        "translation": 'Şu anda video oyunu oynamıyorum. İngilizce sınavıma çalışıyorum!',
        "explanation": '"right now" zaman zarfı ve cümlenin ikinci yarısındaki "I am studying" yapısı şimdiki zamanı gösterir. "I" öznesinin şimdiki zaman olumsuzu **am not playing** dir.',
        "distractors": "• A (don't play): Geniş zaman rutin bildirir.\n• C: 'am' yardımcı fiili eksiktir.\n• D (isn't): 'I' öznesiyle isn't denemez.\n• E (doesn't): 'I' öznesiyle doesn't denemez.",
        "tip": 'I öznesi Şimdiki Zamanda olumsuz yapılırken "I am not + V-ing" şeklinde kurulur.'
    },
    {
        "id": 36,
        "unit": "Ünite 5",
        "unit_title": "Present Simple vs Continuous",
        "question": 'A: "___________ you speak English?"\nB: "Yes, I study it every day."',
        "options": [
            {"label": "A", "text": "Are"},
            {"label": "B", "text": "Do"},
            {"label": "C", "text": "Is"},
            {"label": "D", "text": "Does"},
            {"label": "E", "text": "Were"}
        ],
        "answer": "B",
        "translation": 'A: "İngilizce konuşur musun (biliyor musun)?" — B: "Evet, her gün çalışıyorum."',
        "explanation": 'Bir dili konuşabilme genel bir yetenek/durumdur ve eylem fiili "speak" yalın haldedir. "you" öznesi ile genel zaman sorusu **Do you speak English?** kalıbıyla sorulur.',
        "distractors": "• A (Are): 'Are you speak' denemez; 'are' gelseydi fiil 'speaking' olmak zorundaydı.\n• C ve D (Is/Does): 'you' öznesiyle kullanılmazlar.\n• E (Were): Geçmiş zamandır.",
        "tip": 'Yalın eylem fiilleri (speak, live, work) ile soru sorarken öznemiz you/they ise başına "DO" gelir.'
    },
    {
        "id": 37,
        "unit": "Ünite 5",
        "unit_title": "Present Simple vs Continuous",
        "question": '"___________ they ___________ football in the garden right now?"',
        "options": [
            {"label": "A", "text": "Do / play"},
            {"label": "B", "text": "Are / playing"},
            {"label": "C", "text": "Does / play"},
            {"label": "D", "text": "Are / play"},
            {"label": "E", "text": "Is / playing"}
        ],
        "answer": "B",
        "translation": 'Onlar şu anda bahçede futbol mu oynuyorlar?',
        "explanation": '"right now" zaman belirteci Şimdiki Zamanı (Present Continuous) gerektirir. "they" öznesi için soru yapısı: **Are** they **playing**? şeklindedir.',
        "distractors": "• A: 'right now' varken geniş zaman (Do/play) kullanılmaz.\n• C: 'they' ile 'does' kullanılmaz.\n• D: 'Are' varsa fiil mutlaka -ing almalıdır ('play' yalın kalamaz).\n• E: 'they' öznesi ile 'is' kullanılamaz.",
        "tip": 'Şimdiki zaman Evet/Hayır soruları: Am I / Is he-she-it / Are you-we-they + Fiil-ING?'
    },
    {
        "id": 38,
        "unit": "Ünite 5",
        "unit_title": "Present Simple vs Continuous",
        "question": 'I ___________ tomatoes. I never eat them.',
        "options": [
            {"label": "A", "text": "am not liking"},
            {"label": "B", "text": "don't like"},
            {"label": "C", "text": "doesn't like"},
            {"label": "D", "text": "not like"},
            {"label": "E", "text": "am liking"}
        ],
        "answer": "B",
        "translation": 'Ben domates sevmem. Onları asla yemem.',
        "explanation": '"Like" (sevmek) fiili duygu/durum bildiren bir durum fiilidir (stative verb). İngilizcede durum fiilleri konuşma anında bile olsa kural olarak -ing takısı ALMAZ. Geniş zamanda "I" öznesiyle **don\'t like** kullanılır.',
        "distractors": "• A (am not liking): 'like' durum fiilidir, -ing alamaz (I am liking denmez).\n• C: 'I' öznesiyle 'doesn't' kullanılmaz.\n• D: Yardımcı fiil eksiktir.\n• E: Hem olumlu hem -ing li hatalı biçimdir.",
        "tip": 'Durum Fiilleri Kuralı: like, love, hate, want, know fiilleri şimdiki zamanda bile -ING almaz! "I don\'t like" denir.'
    },
    {
        "id": 39,
        "unit": "Ünite 5",
        "unit_title": "Present Simple vs Continuous",
        "question": 'What time ___________ the movie ___________ tonight?',
        "options": [
            {"label": "A", "text": "do / start"},
            {"label": "B", "text": "does / start"},
            {"label": "C", "text": "is / starting"},
            {"label": "D", "text": "does / starts"},
            {"label": "E", "text": "are / start"}
        ],
        "answer": "B",
        "translation": 'Film bu akşam saat kaçta başlıyor?',
        "explanation": 'Sinema saatleri, tren/uçak tarifeleri ve ders başlangıç saatleri gibi resmi programlar Geniş Zaman (Present Simple) ile sorulur. "the movie" tekil (it) olduğu için soru yardımcı fiili **does**, ana fiil ise yalın **start** olur: "What time does the movie start?"',
        "distractors": "• A: 'the movie' tekildir, 'do' alamaz.\n• C: Programlanmış resmi saatlerde 'does ... start' standard kalıptır.\n• D: Soru cümlesinde does varken ana fiile 's' takılmaz (starts denemez).\n• E: Film tekildir, 'are' alamaz.",
        "tip": 'Saat sorularında: "What time does the lesson / concert / movie start?"'
    },
    {
        "id": 40,
        "unit": "Ünite 5",
        "unit_title": "Present Simple vs Continuous",
        "question": 'Who ___________ she ___________ to on the phone right now?',
        "options": [
            {"label": "A", "text": "do / talk"},
            {"label": "B", "text": "does / talk"},
            {"label": "C", "text": "is / talking"},
            {"label": "D", "text": "are / talking"},
            {"label": "E", "text": "is / talk"}
        ],
        "answer": "C",
        "translation": 'O şu anda telefonda kiminle konuşuyor?',
        "explanation": '"right now" zaman belirteci ve "she" tekil öznesi için doğru soru dizilimi: Who + **is** + she + **talking** to?',
        "distractors": "• A ve B: 'right now' varken geniş zaman (do/does) kullanılmaz.\n• D (are): 'she' tekil olduğu için 'are' kullanılamaz.\n• E: 'is' varken fiil yalın bırakılamaz (-ing gereklidir).",
        "tip": 'Who / What / Where + IS + he/she + Fiil-ING (Şu an olan sorular).'
    },

    # ==========================================
    # UNIT 6: Past of Be (Was / Were) & Vocabulary (10 Questions)
    # ==========================================
    {
        "id": 41,
        "unit": "Ünite 6",
        "unit_title": "Was / Were & Geçmiş Zaman",
        "question": 'I ___________ at home yesterday because I was sick.',
        "options": [
            {"label": "A", "text": "were"},
            {"label": "B", "text": "was"},
            {"label": "C", "text": "am"},
            {"label": "D", "text": "did"},
            {"label": "E", "text": "been"}
        ],
        "answer": "B",
        "translation": 'Dün hastaydım, bu yüzden evdeydim.',
        "explanation": 'Geçmiş zamanda (yesterday) "To Be" fiili ikiye ayrılır:\n• **I / He / She / It -> WAS**\n• **You / We / They -> WERE**\nÖznemiz "I" olduğu için doğru yanıt **was** dır.',
        "distractors": "• A (were): Çoğul özneler (you/we/they) içindir.\n• C (am): Şimdiki/Geniş zamandır; 'yesterday' ile kullanılamaz.\n• D (did): Eylem cümlelerinde kullanılır; yer bildiren isim cümlelerinde 'was' kullanılır.\n• E (been): Fiilin 3. halidir, tek başına yüklem olamaz.",
        "tip": 'Formül: I / HE / SHE / IT -> WAS | YOU / WE / THEY -> WERE.'
    },
    {
        "id": 42,
        "unit": "Ünite 6",
        "unit_title": "Was / Were & Geçmiş Zaman",
        "question": 'Richard and Dan ___________ at my house last Saturday. We played video games.',
        "options": [
            {"label": "A", "text": "was"},
            {"label": "B", "text": "were"},
            {"label": "C", "text": "are"},
            {"label": "D", "text": "did"},
            {"label": "E", "text": "wasn't"}
        ],
        "answer": "B",
        "translation": 'Richard ve Dan geçen cumartesi benim evimdeydiler. Video oyunları oynadık.',
        "explanation": '"Richard and Dan" iki kişidir, yani özne çoğuldur (They). Geçmiş zaman belirteci "last Saturday" olduğundan çoğul geçmiş zaman hali olan **were** kullanılır.',
        "distractors": "• A (was): Tekil özneler içindir; özne iki kişi olduğu için çoğuldur.\n• C (are): Şimdiki zamandır; 'last Saturday' geçmiş zamandır.\n• D (did): Eylem fiiliyle soru/olumsuzluk yapar, 'at my house' yer tamlaması to be gerektirir.\n• E (wasn't): Hem tekildir hem anlam olumlu olmalıdır.",
        "tip": 'İki kişi varsa özne "THEY"dir ve geçmiş zamanda mutlaka WERE alır!'
    },
    {
        "id": 43,
        "unit": "Ünite 6",
        "unit_title": "Was / Were & Geçmiş Zaman",
        "question": 'Carrie ___________ in class yesterday. She was at the doctor.',
        "options": [
            {"label": "A", "text": "wasn't"},
            {"label": "B", "text": "weren't"},
            {"label": "C", "text": "isn't"},
            {"label": "D", "text": "didn't"},
            {"label": "E", "text": "not was"}
        ],
        "answer": "A",
        "translation": 'Carrie dün derste değildi. Doktordaydı.',
        "explanation": 'Carrie (She) tekildir. Doktorda olduğu için dünkü derste bulunmamıştır (olumsuz anlam). Geçmiş zaman tekil olumsuz biçimi **wasn\'t** (was not) dır.',
        "distractors": "• B (weren't): Çoğul özneler (you/we/they) içindir.\n• C (isn't): Şimdiki/Geniş zamandır, 'yesterday' ile uyumsuzdur.\n• D (didn't): Eylem fiili gerektirir (Örn: didn't go); burada yer tamlaması 'in class' vardır.\n• E (not was): Sözcük sırası yanlıştır.",
        "tip": 'Olumsuzlar: I/He/She/It -> wasn\'t | You/We/They -> weren\'t.'
    },
    {
        "id": 44,
        "unit": "Ünite 6",
        "unit_title": "Was / Were & Geçmiş Zaman",
        "question": 'A: "___________ you at the party last night?"\nB: "No, I ___________."',
        "options": [
            {"label": "A", "text": "Was / wasn't"},
            {"label": "B", "text": "Were / wasn't"},
            {"label": "C", "text": "Were / weren't"},
            {"label": "D", "text": "Did / didn't"},
            {"label": "E", "text": "Was / weren't"}
        ],
        "answer": "B",
        "translation": 'A: "Dün gece partide miydin?" — B: "Hayır, değildim."',
        "explanation": 'Karşıdaki kişiye ("you") sorarken **Were you...?** denir. Cevap veren kişi ise kendisinden ("I") bahsettiği için tekil olumsuz yanıt verir: **No, I wasn\'t.**',
        "distractors": "• A şıkkında 'you' ile 'Was' sorulamaz.\n• C şıkkında 'I' öznesi ile 'weren't' denemez ('I wasn't' olmalı).\n• D şıkkında parti yer tamlamasıdır, 'did' fiil gerektirir.\n• E şıkkında her iki taraf da yanlıştır.",
        "tip": 'Önemli Sınav Tuzağı: Soru "Were you...?" diye sorulur ama cevap "Yes, I was" veya "No, I wasn\'t" olur (özne you\'dan I\'a döner!).'
    },
    {
        "id": 45,
        "unit": "Ünite 6",
        "unit_title": "Was / Were & Geçmiş Zaman",
        "question": 'A: "Where ___________ you yesterday morning?"\nB: "I was at the gym with my brother."',
        "options": [
            {"label": "A", "text": "was"},
            {"label": "B", "text": "were"},
            {"label": "C", "text": "are"},
            {"label": "D", "text": "did"},
            {"label": "E", "text": "have"}
        ],
        "answer": "B",
        "translation": 'A: "Dün sabah neredeydin?" — B: "Erkek kardeşimle spor salonundaydım."',
        "explanation": '"yesterday morning" (dün sabah) geçmiş zaman ifadesidir. "you" öznesi için geçmiş zaman soru yapısı: Where + **were** + you...?',
        "distractors": "• A (was): 'you' öznesi ile 'was' kullanılamaz.\n• C (are): Şimdiki zamandır; geçmiş zamanla uyumsuzdur.\n• D (did): Cümlede esas eylem fiili yoktur.\n• E (have): Alakasız yardımcı fiildir.",
        "tip": 'Geçmiş Zaman Wh- Soruları: Where was he? / Where were you? / Where were they?'
    },
    {
        "id": 46,
        "unit": "Ünite 6",
        "unit_title": "Was / Were & Kelimeler",
        "question": 'I couldn\'t ride my bicycle this morning because my bike tire was ___________.',
        "options": [
            {"label": "A", "text": "long"},
            {"label": "B", "text": "sick"},
            {"label": "C", "text": "flat"},
            {"label": "D", "text": "late"},
            {"label": "E", "text": "crowded"}
        ],
        "answer": "C",
        "translation": 'Bu sabah bisikletime binemedim çünkü lastiğim patlaktı/inikti.',
        "explanation": 'Smart Choice Ünite 6 kelime listesinde araba veya bisiklet lastiğinin inik/patlak olması **flat tire** (patlak lastik) olarak öğretilmiştir.',
        "distractors": "• A (long): Uzun demektir (kuyruklar için kullanılır: long lines).\n• B (sick): Hasta demektir (insanlar için kullanılır: I am sick).\n• D (late): Geç demektir (otobüs veya insanlar için: bus is late).\n• E (crowded): Kalabalık demektir (otobüs/mekanlar için).",
        "tip": 'Kelimeleri Eşleştir: flat -> tire (lastik) | sick -> person (hasta insan) | late -> bus/train (geç otobüs).'
    },
    {
        "id": 47,
        "unit": "Ünite 6",
        "unit_title": "Was / Were & Kelimeler",
        "question": 'The bus was twenty minutes late because the morning traffic was ___________.',
        "options": [
            {"label": "A", "text": "flat"},
            {"label": "B", "text": "terrible"},
            {"label": "C", "text": "sick"},
            {"label": "D", "text": "tall"},
            {"label": "E", "text": "fun"}
        ],
        "answer": "B",
        "translation": 'Otobüs 20 dakika gecikti çünkü sabah trafiği berbattı.',
        "explanation": 'Smart Choice Ünite 6 ve ünite testinde trafik sıkışıklığı ve olumsuz yol şartları için öğretilen sıfat **terrible** (berbat / çok kötü) kelimesidir: "The traffic is terrible."',
        "distractors": "• A (flat): Lastik için kullanılır.\n• C (sick): Canlılar için hasta anlamına gelir.\n• D (tall): Uzun boylu demektir.\n• E (fun): Eğlenceli demektir; gecikmeye yol açan trafik eğlenceli olamaz.",
        "tip": 'Ünite 6 Kalıbı: "terrible traffic" (berbat trafik) veya "terrible weather" (berbat hava).'
    },
    {
        "id": 48,
        "unit": "Ünite 6",
        "unit_title": "Was / Were & Kelimeler",
        "question": 'There were hundreds of passengers at the train station, so the ticket lines were very ___________.',
        "options": [
            {"label": "A", "text": "sick"},
            {"label": "B", "text": "long"},
            {"label": "C", "text": "flat"},
            {"label": "D", "text": "broken"},
            {"label": "E", "text": "short"}
        ],
        "answer": "B",
        "translation": 'Tren istasyonunda yüzlerce yolcu vardı, bu yüzden bilet kuyrukları çok uzundu.',
        "explanation": 'Smart Choice Ünite 6 testinde geçen "The lines at the train station are long" cümlesine göre insan kuyrukları/sıraları için kullanılan sıfat **long** (uzun) dur.',
        "distractors": "• A (sick): Hasta demektir.\n• C (flat): Düz / inik lastik demektir.\n• D (broken): Bozuk/kırık demektir (eşyalar için).\n• E (short): Yüzlerce yolcu varken sıralar kısa olamaz.",
        "tip": 'Ünite 6 Eşleştirmesi: "long lines" = uzun kuyruklar / sıralar.'
    },
    {
        "id": 49,
        "unit": "Ünite 6",
        "unit_title": "Was / Were & Kelimeler",
        "question": 'Daniel couldn\'t call his parents yesterday because his mobile phone was ___________.',
        "options": [
            {"label": "A", "text": "crowded"},
            {"label": "B", "text": "flat"},
            {"label": "C", "text": "broken"},
            {"label": "D", "text": "late"},
            {"label": "E", "text": "long"}
        ],
        "answer": "C",
        "translation": 'Daniel dün anne babasını arayamadı çünkü cep telefonu bozuktu/kırıktı.',
        "explanation": 'Cihazların, telefonların veya aletlerin çalışmaması / arızalı olması durumu **broken** (bozuk/kırık) sıfatı ile anlatılır: "Daniel\'s phone is broken."',
        "distractors": "• A (crowded): Kalabalık demektir (otobüs, tren, sokak için).\n• B (flat): Lastik için kullanılır.\n• D (late): Geç demektir.\n• E (long): Uzun demektir.",
        "tip": 'Cihaz/Alet bozuksa -> BROKEN | Mekan kalabalıksa -> CROWDED.'
    },
    {
        "id": 50,
        "unit": "Ünite 6",
        "unit_title": "Was / Were & Kelimeler",
        "question": 'Aşağıdaki zaman zarflarından hangisi **Past Tense (Was / Were - Geçmiş Zaman)** ile **KULLANILAMAZ**?',
        "options": [
            {"label": "A", "text": "yesterday morning"},
            {"label": "B", "text": "last night"},
            {"label": "C", "text": "two days ago"},
            {"label": "D", "text": "right now"},
            {"label": "E", "text": "last week"}
        ],
        "answer": "D",
        "translation": 'Hangi zaman zarfı geçmiş zamanla kullanılamaz? -> "right now" (şu anda)',
        "explanation": '"right now" (şu anda) zaman zarfı Şimdiki Zaman (Present Continuous) belirtecidir ve konuşma anını anlatır. Geçmiş zamanla (was/were) asla kullanılamaz. Diğer 4 seçenek ise geçmiş zamanın en temel zaman belirteçleridir.',
        "distractors": "• A (yesterday morning): Dün sabah (Geçmiş)\n• B (last night): Dün gece (Geçmiş)\n• C (two days ago): İki gün önce (Geçmiş)\n• E (last week): Geçen hafta (Geçmiş)",
        "tip": 'Geçmiş Zaman Anahtarları: yesterday, last night/week/year, ... ago. "Right now / at the moment" görürsen şimdiki zamandır.'
    }
]

print(f"Total questions compiled: {len(questions)}")

# Write json for safe embedding
questions_json = json.dumps(questions, ensure_ascii=False)

html_template = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>İngilizce Sınavına Hazırlık Testi (A1) • Smart Choice</title>
    <style>
        :root {
            --primary: #2563eb;
            --primary-hover: #1d4ed8;
            --primary-light: #eff6ff;
            --bg: #f8fafc;
            --card-bg: #ffffff;
            --text-main: #0f172a;
            --text-muted: #64748b;
            --border: #e2e8f0;
            --success: #16a34a;
            --success-light: #f0fdf4;
            --danger: #dc2626;
            --danger-light: #fef2f2;
            --warning: #d97706;
            --warning-light: #fffbeb;
            --info: #0284c7;
            --info-light: #f0f9ff;
            --shadow: 0 4px 6px -1px rgb(0 0 0 / 0.07), 0 2px 4px -2px rgb(0 0 0 / 0.05);
            --radius: 14px;
        }

        [data-theme="dark"] {
            --primary: #3b82f6;
            --primary-hover: #60a5fa;
            --primary-light: #1e293b;
            --bg: #0b0f19;
            --card-bg: #151d2e;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --border: #243048;
            --success: #22c55e;
            --success-light: #064e3b33;
            --danger: #ef4444;
            --danger-light: #7f1d1d33;
            --warning: #f59e0b;
            --warning-light: #78350f33;
            --info: #38bdf8;
            --info-light: #0c4a6e33;
            --shadow: 0 4px 10px rgb(0 0 0 / 0.3);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            -webkit-tap-highlight-color: transparent;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        }

        body {
            background-color: var(--bg);
            color: var(--text-main);
            min-height: 100vh;
            padding-bottom: 70px;
            transition: background-color 0.2s ease, color 0.2s ease;
        }

        /* Top Header */
        header {
            position: sticky;
            top: 0;
            z-index: 100;
            background-color: var(--card-bg);
            border-bottom: 1px solid var(--border);
            padding: 12px 16px;
            backdrop-filter: blur(8px);
            box-shadow: 0 2px 4px rgba(0,0,0,0.03);
        }

        .header-content {
            max-width: 760px;
            margin: 0 auto;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .brand-title {
            font-size: 1.05rem;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 8px;
            color: var(--text-main);
        }

        .badge-total {
            font-size: 0.75rem;
            padding: 2px 8px;
            background: var(--primary-light);
            color: var(--primary);
            border-radius: 999px;
            font-weight: 600;
        }

        .header-actions {
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .icon-btn {
            background: var(--bg);
            border: 1px solid var(--border);
            color: var(--text-main);
            width: 36px;
            height: 36px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            font-size: 1rem;
            transition: all 0.15s ease;
        }

        .icon-btn:active {
            transform: scale(0.92);
        }

        /* Main Container */
        .container {
            max-width: 760px;
            margin: 0 auto;
            padding: 14px 16px;
        }

        /* Score Tracker & Sticky Bar */
        .stats-card {
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 14px 16px;
            margin-bottom: 14px;
            box-shadow: var(--shadow);
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 10px;
        }

        .stat-item {
            text-align: center;
            flex: 1;
        }

        .stat-val {
            font-size: 1.25rem;
            font-weight: 700;
        }

        .stat-label {
            font-size: 0.72rem;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-top: 2px;
        }

        .stat-val.correct { color: var(--success); }
        .stat-val.wrong { color: var(--danger); }
        .stat-val.rate { color: var(--primary); }

        .progress-bar-container {
            width: 100%;
            height: 6px;
            background: var(--border);
            border-radius: 3px;
            overflow: hidden;
            margin-bottom: 14px;
        }

        .progress-bar-fill {
            height: 100%;
            background: linear-gradient(90deg, var(--primary), var(--success));
            width: 0%;
            transition: width 0.3s ease;
        }

        /* Filter Tabs (Horizontal Scrollable for Mobile) */
        .tabs-wrapper {
            margin-bottom: 14px;
            overflow-x: auto;
            white-space: nowrap;
            padding-bottom: 4px;
            -webkit-overflow-scrolling: touch;
            scrollbar-width: none;
        }
        .tabs-wrapper::-webkit-scrollbar { display: none; }

        .tab-btn {
            display: inline-block;
            background: var(--card-bg);
            border: 1px solid var(--border);
            color: var(--text-muted);
            padding: 8px 14px;
            border-radius: 20px;
            font-size: 0.82rem;
            font-weight: 600;
            cursor: pointer;
            margin-right: 6px;
            transition: all 0.15s ease;
        }

        .tab-btn.active {
            background: var(--primary);
            color: #ffffff;
            border-color: var(--primary);
            box-shadow: 0 2px 8px rgba(37,99,235,0.3);
        }

        /* Mode Banner */
        .mode-banner {
            background: var(--primary-light);
            border: 1px solid var(--primary);
            color: var(--primary);
            padding: 10px 14px;
            border-radius: var(--radius);
            font-size: 0.84rem;
            margin-bottom: 14px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        /* Question Card */
        .q-card {
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 18px 16px;
            margin-bottom: 16px;
            box-shadow: var(--shadow);
            transition: transform 0.15s ease, border-color 0.15s ease;
        }

        .q-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 12px;
        }

        .q-unit-tag {
            font-size: 0.72rem;
            font-weight: 700;
            padding: 3px 9px;
            border-radius: 6px;
            background: var(--primary-light);
            color: var(--primary);
            text-transform: uppercase;
        }

        .q-num {
            font-size: 0.82rem;
            font-weight: 700;
            color: var(--text-muted);
        }

        .q-text {
            font-size: 1.05rem;
            font-weight: 600;
            line-height: 1.5;
            color: var(--text-main);
            margin-bottom: 16px;
            white-space: pre-line;
        }

        /* Options Grid (A, B, C, D, E) */
        .options-list {
            display: flex;
            flex-direction: column;
            gap: 9px;
        }

        .opt-btn {
            background: var(--card-bg);
            border: 1.5px solid var(--border);
            color: var(--text-main);
            padding: 13px 14px;
            border-radius: 10px;
            text-align: left;
            font-size: 0.95rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 12px;
            min-height: 50px;
            transition: all 0.15s ease;
            position: relative;
        }

        .opt-btn:active {
            transform: scale(0.99);
        }

        .opt-btn:hover:not(:disabled) {
            border-color: var(--primary);
            background: var(--primary-light);
        }

        .opt-badge {
            width: 28px;
            height: 28px;
            border-radius: 50%;
            background: var(--bg);
            border: 1px solid var(--border);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.85rem;
            font-weight: 700;
            flex-shrink: 0;
            transition: all 0.15s ease;
        }

        .opt-text {
            flex: 1;
            line-height: 1.35;
        }

        /* State Styles for Options */
        .opt-btn.correct {
            border-color: var(--success) !important;
            background: var(--success-light) !important;
            color: var(--text-main) !important;
            font-weight: 600;
        }
        .opt-btn.correct .opt-badge {
            background: var(--success);
            color: #ffffff;
            border-color: var(--success);
        }

        .opt-btn.wrong {
            border-color: var(--danger) !important;
            background: var(--danger-light) !important;
            color: var(--text-main) !important;
        }
        .opt-btn.wrong .opt-badge {
            background: var(--danger);
            color: #ffffff;
            border-color: var(--danger);
        }

        .opt-btn:disabled {
            cursor: default;
        }

        /* Instructive Explanation Box */
        .explanation-box {
            margin-top: 16px;
            border-top: 1px dashed var(--border);
            padding-top: 14px;
            display: none;
            animation: fadeIn 0.25s ease forwards;
        }

        .exp-section {
            background: var(--bg);
            border-left: 3.5px solid var(--primary);
            border-radius: 8px;
            padding: 12px 14px;
            margin-bottom: 10px;
        }

        .exp-section.trans {
            border-left-color: var(--info);
            background: var(--info-light);
        }

        .exp-section.tip {
            border-left-color: var(--warning);
            background: var(--warning-light);
        }

        .exp-section.distr {
            border-left-color: var(--danger);
        }

        .exp-title {
            font-size: 0.78rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 5px;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .exp-section.trans .exp-title { color: var(--info); }
        .exp-section.rule .exp-title { color: var(--primary); }
        .exp-section.tip .exp-title { color: var(--warning); }
        .exp-section.distr .exp-title { color: var(--danger); }

        .exp-content {
            font-size: 0.88rem;
            line-height: 1.5;
            color: var(--text-main);
            white-space: pre-line;
        }

        /* Bottom Fixed Action Bar */
        .bottom-bar {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: var(--card-bg);
            border-top: 1px solid var(--border);
            padding: 10px 16px;
            display: flex;
            align-items: center;
            justify-content: space-around;
            max-width: 760px;
            margin: 0 auto;
            z-index: 99;
            box-shadow: 0 -2px 10px rgba(0,0,0,0.05);
        }

        .nav-btn {
            background: var(--primary);
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 10px;
            font-weight: 600;
            font-size: 0.9rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .nav-btn.secondary {
            background: var(--bg);
            color: var(--text-main);
            border: 1px solid var(--border);
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-4px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Modal for Quick Question Jump */
        .modal {
            display: none;
            position: fixed;
            top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(0,0,0,0.5);
            z-index: 200;
            align-items: center;
            justify-content: center;
            padding: 16px;
            backdrop-filter: blur(3px);
        }
        .modal.open { display: flex; }
        .modal-body {
            background: var(--card-bg);
            border-radius: var(--radius);
            max-width: 500px;
            width: 100%;
            max-height: 80vh;
            overflow-y: auto;
            padding: 20px;
            box-shadow: var(--shadow);
        }
        .modal-title {
            font-size: 1.1rem;
            font-weight: 700;
            margin-bottom: 12px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .grid-nums {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 8px;
            margin-top: 14px;
        }
        .grid-num-btn {
            background: var(--bg);
            border: 1px solid var(--border);
            padding: 10px 0;
            border-radius: 8px;
            font-weight: 700;
            cursor: pointer;
            color: var(--text-main);
            text-align: center;
        }
        .grid-num-btn.answered-correct {
            background: var(--success);
            color: white;
            border-color: var(--success);
        }
        .grid-num-btn.answered-wrong {
            background: var(--danger);
            color: white;
            border-color: var(--danger);
        }
    </style>
</head>
<body>

    <!-- Header -->
    <header>
        <div class="header-content">
            <div class="brand-title">
                <span>🇬🇧 İngilizce Sınav Testi</span>
                <span class="badge-total" id="filterCount">50 Soru</span>
            </div>
            <div class="header-actions">
                <button class="icon-btn" onclick="openJumpModal()" title="Soru Seç">🔢</button>
                <button class="icon-btn" onclick="toggleTheme()" id="themeBtn" title="Gece/Gündüz Modu">🌙</button>
                <button class="icon-btn" onclick="resetProgress()" title="İlerlemeyi Sıfırla">🔄</button>
            </div>
        </div>
    </header>

    <div class="container">
        <!-- Progress Bar -->
        <div class="progress-bar-container">
            <div class="progress-bar-fill" id="progressFill"></div>
        </div>

        <!-- Stats Card -->
        <div class="stats-card">
            <div class="stat-item">
                <div class="stat-val correct" id="correctCount">0</div>
                <div class="stat-label">Doğru</div>
            </div>
            <div class="stat-item">
                <div class="stat-val wrong" id="wrongCount">0</div>
                <div class="stat-label">Yanlış</div>
            </div>
            <div class="stat-item">
                <div class="stat-val rate" id="successRate">%0</div>
                <div class="stat-label">Başarı</div>
            </div>
            <div class="stat-item">
                <div class="stat-val" id="answeredRatio">0/50</div>
                <div class="stat-label">Çözülen</div>
            </div>
        </div>

        <!-- Filter Tabs -->
        <div class="tabs-wrapper">
            <button class="tab-btn active" onclick="setFilter('all')">🌟 Tümü (50)</button>
            <button class="tab-btn" onclick="setFilter('Ünite 1')">📘 Ünite 1: To Be & Tanışma</button>
            <button class="tab-btn" onclick="setFilter('Ünite 2')">📗 Ünite 2: Present Simple</button>
            <button class="tab-btn" onclick="setFilter('Ünite 4')">📙 Ünite 4: Sıklık Zarfları</button>
            <button class="tab-btn" onclick="setFilter('Ünite 5')">📕 Ünite 5: Simple vs Continuous</button>
            <button class="tab-btn" onclick="setFilter('Ünite 6')">📓 Ünite 6: Was / Were & Kelimeler</button>
            <button class="tab-btn" onclick="setFilter('wrong_only')">❌ Sadece Yanlışlarım</button>
        </div>

        <!-- Questions Feed -->
        <div id="questionsContainer"></div>
    </div>

    <!-- Quick Jump Modal -->
    <div class="modal" id="jumpModal" onclick="closeJumpModal(event)">
        <div class="modal-body" onclick="event.stopPropagation()">
            <div class="modal-title">
                <span>Sorulara Hızlı Git</span>
                <button class="icon-btn" onclick="closeJumpModal()">✕</button>
            </div>
            <p style="font-size:0.82rem; color:var(--text-muted)">Yeşil: Doğru, Kırmızı: Yanlış, Gri: Henüz Çözülmedi.</p>
            <div class="grid-nums" id="gridNumsContainer"></div>
        </div>
    </div>

    <script>
        const QUESTIONS_DATA = """ + questions_json + """;

        // State
        let currentFilter = 'all';
        let userAnswers = {}; // { qId: selectedOptionLabel }
        
        // Load saved answers
        try {
            const saved = localStorage.getItem('smart_choice_quiz_answers');
            if (saved) userAnswers = JSON.parse(saved);
        } catch(e) {}

        // Theme management
        function initTheme() {
            const savedTheme = localStorage.getItem('smart_choice_theme') || 'light';
            document.documentElement.setAttribute('data-theme', savedTheme);
            document.getElementById('themeBtn').textContent = savedTheme === 'dark' ? '☀️' : '🌙';
        }

        function toggleTheme() {
            const cur = document.documentElement.getAttribute('data-theme') || 'light';
            const next = cur === 'dark' ? 'light' : 'dark';
            document.documentElement.setAttribute('data-theme', next);
            localStorage.setItem('smart_choice_theme', next);
            document.getElementById('themeBtn').textContent = next === 'dark' ? '☀️' : '🌙';
        }

        // Filter Questions
        function setFilter(filter) {
            currentFilter = filter;
            document.querySelectorAll('.tab-btn').forEach(btn => {
                btn.classList.toggle('active', btn.getAttribute('onclick').includes("'" + filter + "'"));
            });
            renderQuestions();
        }

        function renderQuestions() {
            const container = document.getElementById('questionsContainer');
            container.innerHTML = '';

            let filtered = QUESTIONS_DATA;
            if (currentFilter === 'wrong_only') {
                filtered = QUESTIONS_DATA.filter(q => userAnswers[q.id] && userAnswers[q.id] !== q.answer);
            } else if (currentFilter !== 'all') {
                filtered = QUESTIONS_DATA.filter(q => q.unit === currentFilter);
            }

            document.getElementById('filterCount').textContent = filtered.length + ' Soru';

            if (filtered.length === 0) {
                container.innerHTML = `
                    <div style="text-align:center; padding:40px 20px; background:var(--card-bg); border-radius:var(--radius); border:1px solid var(--border)">
                        <div style="font-size:2.5rem; margin-bottom:10px;">🎉</div>
                        <h3>Harika! Bu kategoride soru yok.</h3>
                        <p style="color:var(--text-muted); font-size:0.9rem; margin-top:6px;">Yanlış yaptığın soru bulunmuyor veya filtre boş.</p>
                    </div>
                `;
                updateStats();
                return;
            }

            filtered.forEach(q => {
                const answered = userAnswers[q.id] !== undefined;
                const userChoice = userAnswers[q.id];
                const isCorrect = userChoice === q.answer;

                const card = document.createElement('div');
                card.className = 'q-card';
                card.id = 'q-' + q.id;

                let optionsHtml = '';
                q.options.forEach(opt => {
                    let btnClass = 'opt-btn';
                    if (answered) {
                        if (opt.label === q.answer) {
                            btnClass += ' correct';
                        } else if (opt.label === userChoice) {
                            btnClass += ' wrong';
                        }
                    }

                    optionsHtml += `
                        <button class="${btnClass}" ${answered ? 'disabled' : ''} onclick="chooseOption(${q.id}, '${opt.label}')">
                            <span class="opt-badge">${opt.label}</span>
                            <span class="opt-text">${opt.text}</span>
                        </button>
                    `;
                });

                const explanationStyle = answered ? 'style="display:block;"' : '';

                card.innerHTML = `
                    <div class="q-header">
                        <span class="q-unit-tag">${q.unit_title}</span>
                        <span class="q-num">Soru ${q.id} / 50</span>
                    </div>
                    <div class="q-text">${escapeHtml(q.question)}</div>
                    <div class="options-list">
                        ${optionsHtml}
                    </div>
                    <div class="explanation-box" id="exp-${q.id}" ${explanationStyle}>
                        <div class="exp-section trans">
                            <div class="exp-title">🇹🇷 Türkçe Çevirisi & Anlamı</div>
                            <div class="exp-content">${escapeHtml(q.translation)}</div>
                        </div>
                        <div class="exp-section rule">
                            <div class="exp-title">💡 Doğru Cevap: ${q.answer} • Neden Doğru? (Kural)</div>
                            <div class="exp-content">${escapeHtml(q.explanation)}</div>
                        </div>
                        <div class="exp-section distr">
                            <div class="exp-title">⚠️ Çeldiriciler (Diğer Şıklar Neden Yanlış?)</div>
                            <div class="exp-content">${escapeHtml(q.distractors)}</div>
                        </div>
                        <div class="exp-section tip">
                            <div class="exp-title">📌 Sınav Tüyosu / Hoca Tuzağı</div>
                            <div class="exp-content">${escapeHtml(q.tip)}</div>
                        </div>
                    </div>
                `;

                container.appendChild(card);
            });

            updateStats();
        }

        function chooseOption(qId, selectedOption) {
            if (userAnswers[qId] !== undefined) return;
            userAnswers[qId] = selectedOption;
            try {
                localStorage.setItem('smart_choice_quiz_answers', JSON.stringify(userAnswers));
            } catch(e) {}

            renderQuestions();

            // Smooth scroll slightly if needed
            const card = document.getElementById('q-' + qId);
            if (card) {
                const exp = document.getElementById('exp-' + qId);
                if (exp) exp.style.display = 'block';
            }
        }

        function updateStats() {
            let correct = 0;
            let wrong = 0;
            const total = QUESTIONS_DATA.length;

            QUESTIONS_DATA.forEach(q => {
                if (userAnswers[q.id]) {
                    if (userAnswers[q.id] === q.answer) correct++;
                    else wrong++;
                }
            });

            const answered = correct + wrong;
            const rate = answered > 0 ? Math.round((correct / answered) * 100) : 0;
            const overallProgress = Math.round((answered / total) * 100);

            document.getElementById('correctCount').textContent = correct;
            document.getElementById('wrongCount').textContent = wrong;
            document.getElementById('successRate').textContent = '%' + rate;
            document.getElementById('answeredRatio').textContent = answered + '/' + total;
            document.getElementById('progressFill').style.width = overallProgress + '%';
        }

        function resetProgress() {
            if (confirm('Tüm çözümlerini sıfırlayıp baştan başlamak istiyor musun?')) {
                userAnswers = {};
                try {
                    localStorage.removeItem('smart_choice_quiz_answers');
                } catch(e) {}
                renderQuestions();
            }
        }

        function openJumpModal() {
            const modal = document.getElementById('jumpModal');
            const grid = document.getElementById('gridNumsContainer');
            grid.innerHTML = '';

            QUESTIONS_DATA.forEach(q => {
                const btn = document.createElement('button');
                btn.className = 'grid-num-btn';
                btn.textContent = q.id;

                if (userAnswers[q.id]) {
                    if (userAnswers[q.id] === q.answer) {
                        btn.classList.add('answered-correct');
                    } else {
                        btn.classList.add('answered-wrong');
                    }
                }

                btn.onclick = () => {
                    closeJumpModal();
                    setFilter('all');
                    setTimeout(() => {
                        const target = document.getElementById('q-' + q.id);
                        if (target) {
                            target.scrollIntoView({ behavior: 'smooth', block: 'center' });
                            target.style.outline = '2px solid var(--primary)';
                            setTimeout(() => { target.style.outline = 'none'; }, 1500);
                        }
                    }, 100);
                };
                grid.appendChild(btn);
            });

            modal.classList.add('open');
        }

        function closeJumpModal(e) {
            document.getElementById('jumpModal').classList.remove('open');
        }

        function escapeHtml(text) {
            return text
                .replace(/&/g, "&amp;")
                .replace(/</g, "&lt;")
                .replace(/>/g, "&gt;");
        }

        // Init
        initTheme();
        renderQuestions();
    </script>
</body>
</html>
"""

with open("sinav_calisma.html", "w", encoding="utf-8") as f:
    f.write(html_template)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("Saved sinav_calisma.html and index.html successfully!")

