# -*- coding: utf-8 -*-
"""
Build Complete Official Quiz
Contains the EXACT 20-question teacher exam paper (SMART CHOICE 1 - UNITS 1-6 Practice Quiz)
as Questions 1 to 20, plus the Challenge Quiz and variation questions!
"""

import json

# EXACT 20 QUESTIONS FROM TEACHER'S WORD DOCUMENT (1-6 EXAM PREPARATION)
official_20_exam = [
    {
        "id": 1,
        "is_official_exam": True,
        "category": "🏆 HOCANIN 20 SORULUK RESMİ SINAVI",
        "tag": "Resmi Sınav • Soru 1 • To Be",
        "question": "Hello! My name ___ Daniel.",
        "options": [
            {"label": "A", "text": "are"},
            {"label": "B", "text": "is"},
            {"label": "C", "text": "am"},
            {"label": "D", "text": "be"},
            {"label": "E", "text": "were"}
        ],
        "answer": "B",
        "teacher_feedback": "✓ Correct! Well done.\n'My name' is third-person singular (it) -> is. (My name is Daniel).",
        "translation": "Merhaba! Benim adım Daniel.",
        "explanation": "'My name' (Benim adım) tekil bir kavramdır ('it' zamirine denk gelir). Tekil öznelerle Geniş Zamanda 'To Be' fiili 'is' olarak çekimlenir: 'My name is Daniel.'",
        "distractors": "• A (are): Çoğul özneler içindir.\n• C (am): Sadece 'I' (ben) öznesiyle kullanılır (I am Daniel denir ama My name am denmez!).\n• D (be): Fiilin çekimlenmemiş yalın halidir.\n• E (were): Geçmiş zaman çoğuldur.",
        "tip": "Hoca Tuzağı: 'My' kelimesini görüp 'am' işaretleme! Özne 'I' değil 'My name' (adım = tekil it) olduğu için IS gelir."
    },
    {
        "id": 2,
        "is_official_exam": True,
        "category": "🏆 HOCANIN 20 SORULUK RESMİ SINAVI",
        "tag": "Resmi Sınav • Soru 2 • To Be Origin",
        "question": "We ___ from Brazil.",
        "options": [
            {"label": "A", "text": "is"},
            {"label": "B", "text": "am"},
            {"label": "C", "text": "are"},
            {"label": "D", "text": "be"},
            {"label": "E", "text": "was"}
        ],
        "answer": "C",
        "teacher_feedback": "✓ Correct! Well done.\n'We' is plural and takes 'are': We are from Brazil.",
        "translation": "Biz Brezilya'danız (Brezilyalıyız).",
        "explanation": "'We' (biz) çoğul bir öznedir. Geniş Zamanda 'We' öznesi 'To Be' fiilinde daima 'are' alır: 'We are from Brazil.'",
        "distractors": "• A (is): Tekiller (he/she/it) içindir.\n• B (am): 'I' içindir.\n• D (be): Çekimlenmemiştir.\n• E (was): Geçmiş zaman tekildir.",
        "tip": "I am | He/She/It is | You/We/They ARE."
    },
    {
        "id": 3,
        "is_official_exam": True,
        "category": "🏆 HOCANIN 20 SORULUK RESMİ SINAVI",
        "tag": "Resmi Sınav • Soru 3 • Infinitive with To",
        "question": "It's nice to ___ you.",
        "options": [
            {"label": "A", "text": "meeting"},
            {"label": "B", "text": "meets"},
            {"label": "C", "text": "met"},
            {"label": "D", "text": "meet"},
            {"label": "E", "text": "meeted"}
        ],
        "answer": "D",
        "teacher_feedback": "✓ Correct! Well done.\nAfter the infinitive marker 'to', the verb must be in its base form: to meet. 'Nice to meet you.'",
        "translation": "Tanıştığımıza memnun oldum.",
        "explanation": "İngilizcede 'to' edatından sonra fiil hiçbir ek almadan YALIN (base form) halde gelir: 'to meet'. 'Nice to meet you' kalıbı standarttır.",
        "distractors": "• A (meeting): -ing takısı almış.\n• B (meets): -s takısı almış.\n• C (met): 2. halidir (geçmiş zaman).\n• E (meeted): İngilizcede böyle bir kelime yoktur.",
        "tip": "'It is nice to...' sonrasında fiil DAİMA YALIN kalır: to MEET."
    },
    {
        "id": 4,
        "is_official_exam": True,
        "category": "🏆 HOCANIN 20 SORULUK RESMİ SINAVI",
        "tag": "Resmi Sınav • Soru 4 • Greeting Response",
        "question": "A: How are you today?\nB: ___",
        "options": [
            {"label": "A", "text": "I'm 19."},
            {"label": "B", "text": "I'm from Spain."},
            {"label": "C", "text": "I'm fine, thanks."},
            {"label": "D", "text": "I'm a student."},
            {"label": "E", "text": "Nice to meet you."}
        ],
        "answer": "C",
        "teacher_feedback": "✓ Correct! Well done.\n'How are you today?' asks about your current feeling/well-being. Best answer: I'm fine, thanks.",
        "translation": "A: \"Bugün nasılsın?\" — B: \"İyiyim, teşekkürler.\"",
        "explanation": "'How are you today?' (Bugün nasılsın?) sorusuna durum bildiren en doğal yanıt 'I'm fine, thanks.' dır (Hoca Word dosyasında sarıyla işaretlemiştir!).",
        "distractors": "• A: 'How old are you?' cevabıdır.\n• B: 'Where are you from?' cevabıdır.\n• D: 'What do you do?' cevabıdır.\n• E: İlk kez tanışırken söylenir.",
        "tip": "How are you? $\rightarrow$ I'm fine, thanks."
    },
    {
        "id": 5,
        "is_official_exam": True,
        "category": "🏆 HOCANIN 20 SORULUK RESMİ SINAVI",
        "tag": "Resmi Sınav • Soru 5 • How Often",
        "question": "A: How often do you play tennis?\nB: ___",
        "options": [
            {"label": "A", "text": "At the weekend."},
            {"label": "B", "text": "In the gym."},
            {"label": "C", "text": "Very well."},
            {"label": "D", "text": "Yes, I do."},
            {"label": "E", "text": "Three times a week."}
        ],
        "answer": "E",
        "teacher_feedback": "✓ Correct! Well done.\n'How often...?' asks about frequency. The frequency expression is: Three times a week.",
        "translation": "A: \"Ne sıklıkla tenis oynarsın?\" — B: \"Haftada üç kez.\"",
        "explanation": "'How often...?' eylemin yapılma sıklığını sorar. 'Three times a week' (haftada 3 kez) sıklık belirten tek doğru seçenektir (Hoca Word'de sarıyla işaretlemiştir!).",
        "distractors": "• A: 'When do you play?' cevabıdır.\n• B: 'Where do you play?' cevabıdır.\n• C: 'How well do you play?' cevabıdır.\n• D: 'Do you play tennis?' cevabıdır.",
        "tip": "How often...? $\rightarrow$ Three times a week / twice a week / once a day."
    },
    {
        "id": 6,
        "is_official_exam": True,
        "category": "🏆 HOCANIN 20 SORULUK RESMİ SINAVI",
        "tag": "Resmi Sınav • Soru 6 • What do you do?",
        "question": "A: What do you do?\nB: ___",
        "options": [
            {"label": "A", "text": "I'm an engineer."},
            {"label": "B", "text": "I'm from Mexico."},
            {"label": "C", "text": "I'm 21 years old."},
            {"label": "D", "text": "I'm fine."},
            {"label": "E", "text": "I like music."}
        ],
        "answer": "A",
        "teacher_feedback": "✓ Correct! Well done.\n'What do you do?' is an idiom meaning 'What is your job?'. The answer gives your profession: I'm an engineer.",
        "translation": "A: \"Ne iş yapıyorsun?\" — B: \"Ben bir mühendisim.\"",
        "explanation": "'What do you do?' İngilizcede 'Mesleğin nedir?' anlamına gelir. Doğru cevap meslek bildiren 'I'm an engineer.' dır (Hoca sarıyla işaretlemiştir!).",
        "distractors": "• B: Memleket cevabıdır.\n• C: Yaş cevabıdır.\n• D: Hal hatır cevabıdır.\n• E: İlgi alanı cevabıdır.",
        "tip": "What do you do? = Mesleğin ne? $\rightarrow$ I'm an engineer."
    },
    {
        "id": 7,
        "is_official_exam": True,
        "category": "🏆 HOCANIN 20 SORULUK RESMİ SINAVI",
        "tag": "Resmi Sınav • Soru 7 • Crowded Line",
        "question": "The supermarket is very ___ today. There are many people waiting in line.",
        "options": [
            {"label": "A", "text": "quiet"},
            {"label": "B", "text": "crowded"},
            {"label": "C", "text": "empty"},
            {"label": "D", "text": "cheap"},
            {"label": "E", "text": "noisy"}
        ],
        "answer": "B",
        "teacher_feedback": "✓ Correct! Well done.\n'Many people waiting in line' indicates that the supermarket is crowded.",
        "translation": "Süpermarket bugün çok kalabalık. Kuyrukta bekleyen birçok insan var.",
        "explanation": "'many people waiting in line' (kuyrukta bekleyen çok insan var) ifadesi süpermarketin **kalabalık (crowded)** olduğunu açıkça gösterir (Hoca sarıyla işaretlemiştir!).",
        "distractors": "• A (quiet): Sessiz / sakin.\n• C (empty): Boş (kuyruk varken boş olamaz).\n• D (cheap): Ucuz.\n• E (noisy): Gürültülü.",
        "tip": "many people in line $\rightarrow$ CROWDED (kalabalık)."
    },
    {
        "id": 8,
        "is_official_exam": True,
        "category": "🏆 HOCANIN 20 SORULUK RESMİ SINAVI",
        "tag": "Resmi Sınav • Soru 8 • Right now taking",
        "question": "Please don't make noise. The students ___ an exam right now.",
        "options": [
            {"label": "A", "text": "take"},
            {"label": "B", "text": "takes"},
            {"label": "C", "text": "are taking"},
            {"label": "D", "text": "is taking"},
            {"label": "E", "text": "taking"}
        ],
        "answer": "C",
        "teacher_feedback": "✓ Correct! Well done.\n'Please don't make noise' and 'right now' indicate Present Continuous. 'The students' is plural -> are taking.",
        "translation": "Lütfen gürültü yapmayın. Öğrenciler şu anda sınava giriyorlar.",
        "explanation": "'right now' ve 'don't make noise' uyarıları eylemin şu an gerçekleştiğini gösterir. 'The students' çoğul (onlar) olduğu için **are taking** doğru cevaptır.",
        "distractors": "• A ve B: Geniş zamandır; konuşma anını anlatamaz.\n• D: 'students' çoğuldur, 'is' alamaz.\n• E: Yardımcı fiil 'are' eksiktir.",
        "tip": "right now + students (çoğul) $\rightarrow$ ARE TAKING."
    },
    {
        "id": 9,
        "is_official_exam": True,
        "category": "🏆 HOCANIN 20 SORULUK RESMİ SINAVI",
        "tag": "Resmi Sınav • Soru 9 • Usually vs Today",
        "question": "My father usually ___ tea, but today he ___ coffee.",
        "options": [
            {"label": "A", "text": "drinks / is drinking"},
            {"label": "B", "text": "is drinking / drinks"},
            {"label": "C", "text": "drink / is drinking"},
            {"label": "D", "text": "drinks / drinking"},
            {"label": "E", "text": "is drink / drinks"}
        ],
        "answer": "A",
        "teacher_feedback": "✓ Correct! Well done.\n'usually' = routine with singular subject (drinks). 'today' = temporary action happening now (is drinking).",
        "translation": "Babam genellikle çay içer, fakat bugün kahve içiyor.",
        "explanation": "'usually' alışkanlık bildirdiği için Geniş Zaman (My father drinks). 'today' bugüne özel eylem olduğu için Şimdiki Zaman (he is drinking). Sıralama: **drinks / is drinking**.",
        "distractors": "• B: Zamanlar terstir.\n• C: 'My father' tekildir, 'drink' alamaz (-s gerekir).\n• D: İkinci kısımda yardımcı fiil 'is' eksiktir.\n• E: 'is drink' hatalı yapıdır.",
        "tip": "usually $\rightarrow$ drinks | today $\rightarrow$ is drinking."
    },
    {
        "id": 10,
        "is_official_exam": True,
        "category": "🏆 HOCANIN 20 SORULUK RESMİ SINAVI",
        "tag": "Resmi Sınav • Soru 10 • Possessive Adjective",
        "question": "Julia is my cousin. ___ parents live in Ankara.",
        "options": [
            {"label": "A", "text": "His"},
            {"label": "B", "text": "She"},
            {"label": "C", "text": "Their"},
            {"label": "D", "text": "Her"},
            {"label": "E", "text": "Our"}
        ],
        "answer": "D",
        "teacher_feedback": "✓ Correct! Well done.\nJulia is female (she), so the possessive adjective is 'Her' (Her parents).",
        "translation": "Julia benim kuzenimdir. Onun anne babası Ankara'da yaşıyor.",
        "explanation": "Julia bir kadın ismidir (she). Kadınlar için iyelik sıfatı (onun) **Her** dir: 'Her parents' (onun anne babası).",
        "distractors": "• A (His): Erkekler (he) içindir.\n• B (She): Özne zamiridir ('She parents' denmez).\n• C (Their): Onların demektir.\n• E (Our): Bizim demektir.",
        "tip": "Julia (kadın) $\rightarrow$ HER parents. Erkek olsaydı $\rightarrow$ HIS parents."
    },
    {
        "id": 11,
        "is_official_exam": True,
        "category": "🏆 HOCANIN 20 SORULUK RESMİ SINAVI",
        "tag": "Resmi Sınav • Soru 11 • Articles (an actor)",
        "question": "My brother is ___ actor.",
        "options": [
            {"label": "A", "text": "a"},
            {"label": "B", "text": "an"},
            {"label": "C", "text": "the"},
            {"label": "D", "text": "some"},
            {"label": "E", "text": "many"}
        ],
        "answer": "B",
        "teacher_feedback": "✓ Correct! Well done.\n'Actor' begins with a vowel sound (/ˈæktər/), so we use 'an': an actor.",
        "translation": "Erkek kardeşim bir aktördür (oyuncudur).",
        "explanation": "'actor' kelimesi sesli harf ile başladığı için mesleğin önüne 'a' değil **an** gelir: 'an actor'.",
        "distractors": "• A: 'a actor' sesli harf kuralına aykırıdır.\n• C: 'the' belirli bir kişiyi anlatırken kullanılır, meslek tanıtırken 'a/an' esastır.\n• D ve E: Tekil isimlerle 'some' veya 'many' kullanılmaz.",
        "tip": "Sesliyle başlayan meslek: AN actor, AN architect, AN engineer."
    },
    {
        "id": 12,
        "is_official_exam": True,
        "category": "🏆 HOCANIN 20 SORULUK RESMİ SINAVI",
        "tag": "Resmi Sınav • Soru 12 • What time",
        "question": "A: What ___ is your English class?\nB: It's at 10:15.",
        "options": [
            {"label": "A", "text": "hour"},
            {"label": "B", "text": "clock"},
            {"label": "C", "text": "time"},
            {"label": "D", "text": "watch"},
            {"label": "E", "text": "day"}
        ],
        "answer": "C",
        "teacher_feedback": "✓ Correct! Well done.\nThe phrase 'What time...?' asks for the exact time of an event. 'What time is your English class?'",
        "translation": "A: \"İngilizce dersin saat kaçta?\" — B: \"10:15'te.\"",
        "explanation": "Saat kaçta olduğunu sorarken kalıbımız **What time...?** dır. 'What time is your class?' kalıplaşmış doğru sorudur.",
        "distractors": "• A (What hour): İngilizcede 'What hour' denmez.\n• B (What clock): Saat sormaz.\n• D (What watch): Kol saati demektir.\n• E (What day): 'Hangi gün?' demektir; cevapta 10:15 verildiği için saat sorulmuştur.",
        "tip": "Saat sorusu: WHAT TIME is...?"
    },
    {
        "id": 13,
        "is_official_exam": True,
        "category": "🏆 HOCANIN 20 SORULUK RESMİ SINAVI",
        "tag": "Resmi Sınav • Soru 13 • Airport was/were",
        "question": "We ___ at the airport at 5 a.m. yesterday. It ___ empty.",
        "options": [
            {"label": "A", "text": "were / was"},
            {"label": "B", "text": "was / were"},
            {"label": "C", "text": "were / were"},
            {"label": "D", "text": "are / was"},
            {"label": "E", "text": "was / was"}
        ],
        "answer": "A",
        "teacher_feedback": "✓ Correct! Well done.\n'We' is plural -> were. 'It' (the airport) is singular -> was. Both in past tense ('yesterday').",
        "translation": "Biz dün sabah saat 05:00'te havalimanındaydık. Havalimanı (orası) bomboştu.",
        "explanation": "'We' (çoğul) + yesterday -> **were**. 'It' (havalimanı / tekil) -> **was**. Sıralama: **were / was**.",
        "distractors": "• B: Şıklar terstir.\n• C: 'It' tekildir, were alamaz.\n• D: 'yesterday' ile 'are' kullanılmaz.\n• E: 'We was' kural dışıdır.",
        "tip": "We WERE / It WAS."
    },
    {
        "id": 14,
        "is_official_exam": True,
        "category": "🏆 HOCANIN 20 SORULUK RESMİ SINAVI",
        "tag": "Resmi Sınav • Soru 14 • Weather was / Friends were",
        "question": "Last weekend the weather ___ great, so my friends and I ___ at the park.",
        "options": [
            {"label": "A", "text": "were / was"},
            {"label": "B", "text": "was / was"},
            {"label": "C", "text": "was / were"},
            {"label": "D", "text": "were / were"},
            {"label": "E", "text": "is / were"}
        ],
        "answer": "C",
        "teacher_feedback": "✓ Correct! Well done.\n'The weather' is singular (it) -> was. 'My friends and I' = we (plural) -> were.",
        "translation": "Geçen hafta sonu hava harikaydı, bu yüzden arkadaşlarım ve ben parktaydık.",
        "explanation": "'the weather' (tekil/sayılamaz) -> **was**. 'my friends and I' (arkadaşlarım ve ben = we çoğul) -> **were**. Sıralama: **was / were**.",
        "distractors": "• A: Şıklar terstir.\n• B: 'my friends and I' çoğuldur, was alamaz.\n• D: 'weather were' yanlıştır.\n• E: 'last weekend' varken 'is' gelemez.",
        "tip": "The weather $\rightarrow$ WAS | My friends and I $\rightarrow$ WERE (was / were)."
    },
    {
        "id": 15,
        "is_official_exam": True,
        "category": "🏆 HOCANIN 20 SORULUK RESMİ SINAVI",
        "tag": "Resmi Sınav • Soru 15 • Which is NOT correct?",
        "question": "Which sentence is NOT correct?",
        "options": [
            {"label": "A", "text": "She isn't working today."},
            {"label": "B", "text": "They don't work on Sundays."},
            {"label": "C", "text": "I wasn't at work."},
            {"label": "D", "text": "We aren't at work."},
            {"label": "E", "text": "He isn't work today."}
        ],
        "answer": "E",
        "teacher_feedback": "✓ Correct! Well done.\nThe present continuous needs the -ing form: He isn't working today. \"Isn't work\" is wrong.",
        "translation": "Hangi cümle YANLIŞTIR? -> 'He isn't work today.'",
        "explanation": "'isn't' yardımcı fiilinden sonra gelen eylem fiili Şimdiki Zamanda mutlaka **-ing** takısı almalıdır: 'He isn't working today'. 'Isn't work' yapısı tamamen kural dışıdır.",
        "distractors": "• A, B, C ve D cümleleri gramer kurallarına tamamen uygundur.",
        "tip": "Hocanın Uyarısı: 'isn't' ile yalın fiil 'work' YAN YANA GELEMEZ! 'isn't work' YANLIŞTIR."
    },
    {
        "id": 16,
        "is_official_exam": True,
        "category": "🏆 HOCANIN 20 SORULUK RESMİ SINAVI",
        "tag": "Resmi Sınav • Soru 16 • Were you and Ben?",
        "question": "\"Were you and Ben in the same class last year?\" \"Yes, we ___.\"",
        "options": [
            {"label": "A", "text": "was"},
            {"label": "B", "text": "are"},
            {"label": "C", "text": "did"},
            {"label": "D", "text": "were"},
            {"label": "E", "text": "weren't"}
        ],
        "answer": "D",
        "teacher_feedback": "✓ Correct! Well done.\n'You and Ben' = we. In affirmative past short answer: 'Yes, we were.'",
        "translation": "\"Sen ve Ben geçen yıl aynı sınıfta mıydınız?\" \"Evet, öyleydik.\"",
        "explanation": "'you and Ben' cevapta 'we' olur. Geçmiş zamanda 'we' ile olumlu cevap: **Yes, we were.**",
        "distractors": "• A (was): 'we' ile was denmez.\n• B (are): Şimdiki zamandır.\n• C (did): To be sorusudur.\n• E (weren't): Yes ile olumsuzluk olmaz.",
        "tip": "HOCANIN KESİN SINAV SORUSU: you and Ben -> Yes, we WERE."
    },
    {
        "id": 17,
        "is_official_exam": True,
        "category": "🏆 HOCANIN 20 SORULUK RESMİ SINAVI",
        "tag": "Resmi Sınav • Soru 17 • Habit Does / doesn't",
        "question": "\"___ she usually walk to school?\" \"No, she ___. She takes the bus.\"",
        "options": [
            {"label": "A", "text": "Is / isn't"},
            {"label": "B", "text": "Do / doesn't"},
            {"label": "C", "text": "Does / doesn't"},
            {"label": "D", "text": "Does / isn't"},
            {"label": "E", "text": "Is / doesn't"}
        ],
        "answer": "C",
        "teacher_feedback": "✓ Correct! Well done.\n\"Usually\" shows a habit -> present simple. With \"she\": Does she...? No, she doesn't.",
        "translation": "\"O genellikle okula yürüyerek mi gider?\" \"Hayır, gitmez. Otobüse biner.\"",
        "explanation": "'usually' ve eylem fiili 'walk' vardır. 'she' öznesiyle soru: **Does she walk...?** / Cevap: **No, she doesn't.**",
        "distractors": "• A: 'walk' eylem fiilidir, 'Is she walk' denemez.\n• B: 'she' ile 'Do' kullanılmaz.\n• D: Does sorusuna isn't cevabı verilmez.\n• E: Hatalı soru yapısıdır.",
        "tip": "usually + walk $\rightarrow$ DOES she walk...? / No, she DOESN'T."
    },
    {
        "id": 18,
        "is_official_exam": True,
        "category": "🏆 HOCANIN 20 SORULUK RESMİ SINAVI",
        "tag": "Resmi Sınav • Soru 18 • There are / Noisy",
        "question": "There ___ a lot of cars in the street. It's very ___.",
        "options": [
            {"label": "A", "text": "is / noisy"},
            {"label": "B", "text": "are / quiet"},
            {"label": "C", "text": "is / quiet"},
            {"label": "D", "text": "are / empty"},
            {"label": "E", "text": "are / noisy"}
        ],
        "answer": "E",
        "teacher_feedback": "✓ Correct! Well done.\n'A lot of cars' is plural, requiring 'There are'. Many cars in the street make it very 'noisy'.",
        "translation": "Caddede bir sürü araba var. Burası çok gürültülü.",
        "explanation": "1) 'a lot of cars' çoğul bir nesnedir $\rightarrow$ çoğul olduğu için **There are** kullanılır.\n2) Caddede çok araba olması orayı **gürültülü (noisy)** yapar. Sıralama: **are / noisy**.",
        "distractors": "• A ve C: 'cars' çoğuldur, 'is' alamaz.\n• B: Çok araba varken sokak 'quiet' (sessiz) olamaz.\n• D: Çok araba varken sokak 'empty' (boş) olamaz.",
        "tip": "a lot of cars (çoğul) $\rightarrow$ ARE | arabalar çoksa $\rightarrow$ NOISY (gürültülü)."
    },
    {
        "id": 19,
        "is_official_exam": True,
        "category": "🏆 HOCANIN 20 SORULUK RESMİ SINAVI",
        "tag": "Resmi Sınav • Soru 19 • Share / have",
        "question": "My brother and I ___ a room, but our parents ___ their own room.",
        "options": [
            {"label": "A", "text": "shares / has"},
            {"label": "B", "text": "share / have"},
            {"label": "C", "text": "share / has"},
            {"label": "D", "text": "are sharing / have"},
            {"label": "E", "text": "shares / have"}
        ],
        "answer": "B",
        "teacher_feedback": "✓ Correct! Well done.\n'My brother and I' = we (plural) -> share. 'Our parents' = they (plural) -> have. Neither takes -s.",
        "translation": "Kardeşim ve ben bir odayı paylaşıyoruz, fakat anne babamızın kendi odaları var.",
        "explanation": "'My brother and I' (we) $\rightarrow$ **share**. 'our parents' (they) $\rightarrow$ **have**. İki fiil de yalın kalır: **share / have**.",
        "distractors": "• A, C, D ve E seçenekleri çoğul özne kuralına aykırıdır.",
        "tip": "İki özne de çoğul: SHARE / HAVE."
    },
    {
        "id": 20,
        "is_official_exam": True,
        "category": "🏆 HOCANIN 20 SORULUK RESMİ SINAVI",
        "tag": "Resmi Sınav • Soru 20 • Were you / wasn't ill",
        "question": "\"___ you at the party last night?\" \"No, I ___. I was ill.\"",
        "options": [
            {"label": "A", "text": "Was / wasn't"},
            {"label": "B", "text": "Were / weren't"},
            {"label": "C", "text": "Are / wasn't"},
            {"label": "D", "text": "Were / wasn't"},
            {"label": "E", "text": "Were / didn't"}
        ],
        "answer": "D",
        "teacher_feedback": "✓ Correct! Well done.\nQuestion with 'you': Were you...? Short answer with 'I': No, I wasn't.",
        "translation": "\"Dün gece partide miydin?\" \"Hayır, değildim. Hastaydım.\"",
        "explanation": "1) Karşıdaki kişiye 'you' öznesiyle sorarken: **Were you...?**\n2) Cevap veren kişi kendisinden bahsettiği için ('I'): **No, I wasn't.**\nSıralama: **Were / wasn't**.",
        "distractors": "• A: 'you' ile Was sorulamaz.\n• B: 'I' öznesi ile 'weren't' denemez ('I wasn't' olmalı).\n• C: 'last night' geçmiş zamandır, Are olamaz.\n• E: Soru to be iledir, didn't ile cevap verilmez.",
        "tip": "Soru 'Were you...?' $\rightarrow$ Cevap 'No, I WASN'T' (Özne I olduğu için wasn't gelir!)."
    }
]

# Load remaining questions from existing json
with open("all_questions_final.json", "r", encoding="utf-8") as f:
    existing = json.load(f)

# Collect all non-duplicate questions
existing_filtered = []
seen_questions = set(q["question"] for q in official_20_exam)

for q in existing:
    # If this question prompt is not one of the official 20, keep it!
    # Or if it's different in answer/text
    q_sig = (q["question"], q["answer"])
    official_sigs = set((x["question"], x["answer"]) for x in official_20_exam)
    if q_sig not in official_sigs:
        q["is_official_exam"] = False
        existing_filtered.append(q)

full_bank = official_20_exam + existing_filtered

# Re-index all sequentially
for i, q in enumerate(full_bank, 1):
    q["id"] = i

print(f"Total compiled questions in complete bank: {len(full_bank)}")
print("Official 20 questions count:", len(official_20_exam))

with open("all_questions_master.json", "w", encoding="utf-8") as f:
    json.dump(full_bank, f, ensure_ascii=False, indent=2)

print("Saved all_questions_master.json successfully!")

