# -*- coding: utf-8 -*-
"""
Teacher-Style Challenge Quiz Generator
Matches the exact style, format, and questions from the teacher's 'Smart Choice 1 - Challenge Quiz'
"""

import json

questions = [
    # ==========================================
    # SECTION 1: HOCANIN EKRANDAKİ BİREBİR SORULARI (TEACHER SCREENSHOT QUESTIONS)
    # ==========================================
    {
        "id": 1,
        "unit": "Hocanın Challenge Soruları",
        "unit_title": "Challenge Quiz • Present Simple",
        "question": "Anna ___ coffee, but she ___ tea every morning.",
        "options": [
            {"label": "A", "text": "don't drink / drinks"},
            {"label": "B", "text": "doesn't drinks / drink"},
            {"label": "C", "text": "doesn't drink / drinks"},
            {"label": "D", "text": "isn't drinking / drinks"},
            {"label": "E", "text": "doesn't drink / is drinking"}
        ],
        "answer": "C",
        "teacher_feedback": "✓ Correct! Well done.\nPresent simple, third person singular: negative = doesn't + base verb (doesn't drink); positive = verb + s (drinks). \"Every morning\" shows a habit.",
        "translation": "Anna kahve içmez, fakat her sabah çay içer.",
        "explanation": "Anna 3. tekil şahıstır (She). Geniş Zamanda tekil şahıs olumsuz çekimi: doesn't + fiilin yalın hali (doesn't drink). Olumlu çekimi ise fiil + s takısıdır (drinks). 'every morning' bir rutin/alışkanlık belirtir.",
        "distractors": "• A: Anna için 'don't' kullanılamaz (doesn't olmalı).\n• B: 'doesn't' sonrasında fiile tekrar -s takılmaz (doesn't drinks YANLIŞTIR).\n• D: 'isn't drinking' geçici şimdiki zamandır, genel kahve sevmeme alışkanlığına uymaz.\n• E: 'every morning' rutin bildirir, is drinking (şimdiki zaman) olamaz.",
        "tip": "Hocanın en klasik sorusu: doesn't gördüğün an fiil YALIN (s takısız) kalır, virgülden sonraki olumlu kısımda ise fiil -s alır!"
    },
    {
        "id": 2,
        "unit": "Hocanın Challenge Soruları",
        "unit_title": "Challenge Quiz • Articles (a / an / the)",
        "question": "She is ___ honest person and ___ best student in our class.",
        "options": [
            {"label": "A", "text": "a / the"},
            {"label": "B", "text": "an / a"},
            {"label": "C", "text": "a / a"},
            {"label": "D", "text": "an / the"},
            {"label": "E", "text": "the / an"}
        ],
        "answer": "D",
        "teacher_feedback": "✓ Correct! Well done.\n'Honest' starts with a vowel sound (silent 'h'), so we use 'an'. For superlatives ('best'), we always use 'the'.",
        "translation": "O dürüst bir insandır ve sınıfımızdaki en iyi öğrencidir.",
        "explanation": "1) 'honest' kelimesindeki 'h' harfi okunmaz (silent h), kelime sesli harf sesiyle (/ˈɒnɪst/) başlar. Bu yüzden başına 'a' değil **an** gelir (an honest person).\n2) 'best' bir üstünlük (superlative) sıfatıdır; en iyiyi belirtirken daima **the** kullanılır (the best student).",
        "distractors": "• A: 'a honest' telaffuz kuralına aykırıdır, 'an' gereklidir.\n• B ve C: İkinci boşlukta 'best' önüne 'the' gelmelidir, 'a' gelemez.\n• E: Şıklar terstir.",
        "tip": "Hocanın favori tuzağı: 'honest' (dürüst) ve 'hour' (saat) kelimelerinde 'h' okunmaz, başına 'AN' gelir! Superlative (best, fastest, tallest) önüne ise 'THE' gelir."
    },
    {
        "id": 3,
        "unit": "Hocanın Challenge Soruları",
        "unit_title": "Challenge Quiz • Question Formation",
        "question": "Which question is correct?",
        "options": [
            {"label": "A", "text": "Where does she work?"},
            {"label": "B", "text": "Where she works?"},
            {"label": "C", "text": "Where does she works?"},
            {"label": "D", "text": "Where is she work?"},
            {"label": "E", "text": "Where do she work?"}
        ],
        "answer": "A",
        "teacher_feedback": "✓ Correct! Well done.\nWh- question word + does + subject (she) + base verb (work)? The main verb never takes -s when 'does' is used.",
        "translation": "O nerede çalışıyor / çalışır?",
        "explanation": "Wh- Soru Kuralı (Geniş Zaman):\nSoru Kelimesi (Where) + Yardımcı Fiil (does) + Özne (she) + Fiilin YALIN Hali (work)?\nCümlede 'does' varken ana fiil 'work' asla -s almaz.",
        "distractors": "• B: Yardımcı fiil 'does' unutulmuştur.\n• C: Soru cümlesinde 'does' varken fiile tekrar 's' eklenmiştir (works YANLIŞTIR).\n• D: 'is' yardımcı fiili ile yalın fiil 'work' birleşemez.\n• E: 'she' öznesiyle 'do' kullanılamaz.",
        "tip": "'Which question is correct?' sorularında gözün doğrudan: DOES + ÖZNE + YALIN FİİL kombinasyonunu arasın!"
    },
    {
        "id": 4,
        "unit": "Hocanın Challenge Soruları",
        "unit_title": "Challenge Quiz • Vocabulary in Context",
        "question": "The film was so ___ that I almost fell asleep.",
        "options": [
            {"label": "A", "text": "exciting"},
            {"label": "B", "text": "interesting"},
            {"label": "C", "text": "funny"},
            {"label": "D", "text": "crowded"},
            {"label": "E", "text": "boring"}
        ],
        "answer": "E",
        "teacher_feedback": "✓ Correct! Well done.\nIf you almost fall asleep, the film wasn't interesting. It was boring.",
        "translation": "Film o kadar sıkıcıydı ki neredeyse uyuyakalacaktım.",
        "explanation": "Cümlenin devamındaki 'almost fell asleep' (neredeyse uyuyakalıyordum) ipucu, filmin insanı uyutacak kadar **sıkıcı (boring)** olduğunu gösterir.",
        "distractors": "• A (exciting): Heyecan verici (uyutmaz).\n• B (interesting): İlginç (uyutmaz).\n• C (funny): Komik (uyutmaz).\n• D (crowded): Kalabalık (film için değil, mekanlar için kullanılır).",
        "tip": "Cümledeki ipucuna dikkat: 'fell asleep' (uyuyakaldı) $\rightarrow$ BORING (sıkıcı)."
    },
    {
        "id": 5,
        "unit": "Hocanın Challenge Soruları",
        "unit_title": "Challenge Quiz • Best Answer / Dialogue",
        "question": "\"What are you doing?\" Best answer:",
        "options": [
            {"label": "A", "text": "I cook dinner."},
            {"label": "B", "text": "Yes, I am."},
            {"label": "C", "text": "I'm cooking dinner."},
            {"label": "D", "text": "I'm a cook."},
            {"label": "E", "text": "I cooked well."}
        ],
        "answer": "C",
        "teacher_feedback": "✓ Correct! Well done.\nThe question asks about an action in progress right now (Present Continuous: What are you doing?). The answer must be in Present Continuous: I'm cooking dinner.",
        "translation": "\"Şu anda ne yapıyorsun?\" En uygun cevap: \"Akşam yemeği pişiriyorum.\"",
        "explanation": "Soru Present Continuous (Şimdiki Zaman) ile konuşma anında ne yapıldığını sormaktadır. Cevap da aynı zamanda olmalıdır: I'm + V-ing $\rightarrow$ **I'm cooking dinner.**",
        "distractors": "• A (I cook dinner): Geniş zamandır; 'şu an ne yapıyorsun?' sorusuna uymaz.\n• B (Yes, I am): Wh- sorusuna evet/hayır denmez.\n• D (I'm a cook): 'What do you do?' (Mesleğin ne?) sorusunun cevabıdır.\n• E: Geçmiş zamandır.",
        "tip": "Hocanın ayrımı: 'What are you doing?' $\rightarrow$ I'm cooking (Şu an yapıyorum) | 'What do you do?' $\rightarrow$ I'm a cook (Aşçıyım/Meslek)."
    },

    # ==========================================
    # SECTION 2: HOCANIN AYNI TARZINDAKİ YENİ CHALLENGE SORULARI (20 Soru)
    # ==========================================
    {
        "id": 6,
        "unit": "Hocanın Challenge Soruları",
        "unit_title": "Challenge Quiz • Articles & Pronunciation",
        "question": "He is ___ university student, and he studies for ___ hour every night.",
        "options": [
            {"label": "A", "text": "an / an"},
            {"label": "B", "text": "a / an"},
            {"label": "C", "text": "an / a"},
            {"label": "D", "text": "a / a"},
            {"label": "E", "text": "the / the"}
        ],
        "answer": "B",
        "teacher_feedback": "✓ Correct! Well done.\n'University' starts with a consonant 'y' sound (/juː/), so it takes 'a'. 'Hour' starts with a silent 'h' (vowel sound), so it takes 'an'.",
        "translation": "O bir üniversite öğrencisidir ve her gece bir saat ders çalışır.",
        "explanation": "1) 'university' kelimesi 'u' harfiyle başlasa da okunuşu sessiz /y/ sesiyle (/juːnɪˈvɜːrsəti/) başlar. Bu yüzden başına **a** gelir (a university).\n2) 'hour' kelimesindeki 'h' okunmaz, sesli /aʊər/ ile başlar. Bu yüzden başına **an** gelir (an hour).",
        "distractors": "• A, C, D ve E seçenekleri İngilizce telaffuz ve sesli/sessiz uyum kuralına aykırıdır.",
        "tip": "Sınav Klasikleri: A university (/y/ sesi) AMA An hour (okunmayan h sesi)."
    },
    {
        "id": 7,
        "unit": "Hocanın Challenge Soruları",
        "unit_title": "Challenge Quiz • Best Answer / Dialogue",
        "question": "\"What do you do?\" Best answer:",
        "options": [
            {"label": "A", "text": "I am studying English right now."},
            {"label": "B", "text": "I'm an architect."},
            {"label": "C", "text": "Yes, I do."},
            {"label": "D", "text": "I do my homework every day."},
            {"label": "E", "text": "I'm fine, thanks."}
        ],
        "answer": "B",
        "teacher_feedback": "✓ Correct! Well done.\n'What do you do?' is an idiom that means 'What is your job / occupation?'. The answer gives your profession: I'm an architect.",
        "translation": "\"Ne iş yapıyorsun / Mesleğin ne?\" En uygun cevap: \"Ben bir mimarım.\"",
        "explanation": "'What do you do?' İngilizcede kalıplaşmış olarak 'Mesleğin nedir?' anlamına gelir. Yanıt daima meslek veya öğrencilik bildirir: 'I'm an architect.'",
        "distractors": "• A: 'What are you doing right now?' sorusunun cevabıdır.\n• C: Wh- sorularına Yes/No denmez.\n• D: Kelime oyunu çeldiricisidir; meslek sorusuna ödev cevabı verilmez.\n• E: 'How are you?' sorusuna cevaptır.",
        "tip": "Hoca kesin sorar: 'What do you do?' = Mesleğin ne? -> I'm an architect / student / teacher."
    },
    {
        "id": 8,
        "unit": "Hocanın Challenge Soruları",
        "unit_title": "Challenge Quiz • Grammatical Correctness",
        "question": "Which sentence is grammatically correct?",
        "options": [
            {"label": "A", "text": "He doesn't likes coffee."},
            {"label": "B", "text": "He don't like coffee."},
            {"label": "C", "text": "He doesn't like coffee."},
            {"label": "D", "text": "He not like coffee."},
            {"label": "E", "text": "He isn't like coffee."}
        ],
        "answer": "C",
        "teacher_feedback": "✓ Correct! Well done.\nWith 'he', the negative auxiliary verb is 'doesn't', followed by the base form of the verb 'like' without -s.",
        "translation": "O kahve sevmez.",
        "explanation": "He/She/It için olumsuz yapı: doesn't + yalın fiil (like). 'doesn't like' kurala tam uygundur.",
        "distractors": "• A: 'doesn't' varken fiile -s takılmıştır (büyük hata).\n• B: 'he' ile 'don't' kullanılamaz.\n• D: Yardımcı fiil eksiktir.\n• E: 'like' durum fiilidir, isn't ile birleşmez.",
        "tip": "doesn't + YALIN FİİL. doesn't likes DİYEN YANAR!"
    },
    {
        "id": 9,
        "unit": "Hocanın Challenge Soruları",
        "unit_title": "Challenge Quiz • Vocabulary in Context",
        "question": "The party was so ___ that everyone was dancing and laughing all night.",
        "options": [
            {"label": "A", "text": "boring"},
            {"label": "B", "text": "terrible"},
            {"label": "C", "text": "fun"},
            {"label": "D", "text": "sick"},
            {"label": "E", "text": "flat"}
        ],
        "answer": "C",
        "teacher_feedback": "✓ Correct! Well done.\nEveryone was dancing and laughing, which means the party was fun (enjoyable).",
        "translation": "Parti o kadar eğlenceliydi ki herkes bütün gece dans edip güldü.",
        "explanation": "Herkesin gece boyunca dans edip eğlenmesi partinin **eğlenceli (fun)** olduğunu gösterir.",
        "distractors": "• A (boring): Sıkıcı.\n• B (terrible): Berbat.\n• D (sick): Hasta.\n• E (flat): Patlak/düz (lastik için).",
        "tip": "İpucu: 'dancing and laughing' $\rightarrow$ FUN (eğlenceli)."
    },
    {
        "id": 10,
        "unit": "Hocanın Challenge Soruları",
        "unit_title": "Challenge Quiz • Question Formation",
        "question": "Which question is correct?",
        "options": [
            {"label": "A", "text": "Why was he late for class yesterday?"},
            {"label": "B", "text": "Why he was late for class yesterday?"},
            {"label": "C", "text": "Why did he was late for class yesterday?"},
            {"label": "D", "text": "Why were he late for class yesterday?"},
            {"label": "E", "text": "Why was he be late for class yesterday?"}
        ],
        "answer": "A",
        "teacher_feedback": "✓ Correct! Well done.\nPast tense of 'be' question: Question word (Why) + was + subject (he) + adjective (late)?",
        "translation": "O dün derse neden geç kaldı?",
        "explanation": "Geçmiş zaman 'To Be' soru dizilimi:\nSoru Sözcüğü (Why) + was/were + Özne (he) + Sıfat (late)?\n'he' tekil olduğu için 'was' özneden önce gelir: 'Why was he late...?'",
        "distractors": "• B: Soru dizilimi değil, düz cümle dizilimidir ('he was' denmiş).\n• C: Hem 'did' hem 'was' bir arada asla kullanılamaz.\n• D: 'he' ile 'were' kullanılamaz.\n• E: Hem 'was' hem 'be' yan yana gelemez.",
        "tip": "To be sorularında yardımcı fiil (was/were) MUTLAKA özneden ÖNCE gelir: Why WAS he late?"
    },
    {
        "id": 11,
        "unit": "Hocanın Challenge Soruları",
        "unit_title": "Challenge Quiz • Present Simple vs Continuous",
        "question": "Tom ___ to the gym on weekdays, but today he ___ at home.",
        "options": [
            {"label": "A", "text": "go / relaxes"},
            {"label": "B", "text": "goes / is relaxing"},
            {"label": "C", "text": "is going / relaxes"},
            {"label": "D", "text": "goes / relaxes"},
            {"label": "E", "text": "is going / is relaxing"}
        ],
        "answer": "B",
        "teacher_feedback": "✓ Correct! Well done.\n'on weekdays' shows a regular routine (Present Simple: goes). 'today' shows a temporary action happening now (Present Continuous: is relaxing).",
        "translation": "Tom hafta içleri spor salonuna gider, fakat bugün evde dinleniyor.",
        "explanation": "İlk kısım 'on weekdays' rutin belirttiği için Present Simple (Tom goes). İkinci kısım 'today' bugüne özel geçici durumu anlattığı için Present Continuous (he is relaxing).",
        "distractors": "• A: Tom tekildir, 'go' alamaz (-es gerekir).\n• C: Zamanlar ters bağlanmıştır.\n• D: İkinci kısımda 'today' vurgusu varken şimdiki zaman tercih edilir.\n• E: 'on weekdays' rutin olduğu için şimdiki zaman olamaz.",
        "tip": "Rutin (on weekdays / every day) $\rightarrow$ GOES | Bugün / Şu an (today / right now) $\rightarrow$ IS RELAXING."
    },
    {
        "id": 12,
        "unit": "Hocanın Challenge Soruları",
        "unit_title": "Challenge Quiz • Unit 6 Vocabulary",
        "question": "I couldn't enter the supermarket at 10:30 p.m. because it was ___.",
        "options": [
            {"label": "A", "text": "broken"},
            {"label": "B", "text": "closed"},
            {"label": "C", "text": "flat"},
            {"label": "D", "text": "sick"},
            {"label": "E", "text": "long"}
        ],
        "answer": "B",
        "teacher_feedback": "✓ Correct! Well done.\nA store or supermarket is 'closed' at night when people cannot enter.",
        "translation": "Gece 22:30'da süpermarkete giremedim çünkü kapalıydı.",
        "explanation": "Mağaza veya dükkanların mesai bitimi durumu **closed** (kapalı) sıfatı ile anlatılır (Smart Choice Unit 6 Test sorusu).",
        "distractors": "• A (broken): Eşyalar/aletler bozuk olduğunda denir.\n• C (flat): Lastik için kullanılır.\n• D (sick): İnsanlar için kullanılır.\n• E (long): Kuyruklar/sıralar için kullanılır.",
        "tip": "Mağaza/Dükkan $\rightarrow$ CLOSED (kapalı) | Cihaz/Telefon $\rightarrow$ BROKEN (bozuk) | Lastik $\rightarrow$ FLAT (inik)."
    },
    {
        "id": 13,
        "unit": "Hocanın Challenge Soruları",
        "unit_title": "Challenge Quiz • Frequency Adverbs & How Often",
        "question": "Which question is correct?",
        "options": [
            {"label": "A", "text": "How often does your brother play tennis?"},
            {"label": "B", "text": "How often do your brother play tennis?"},
            {"label": "C", "text": "How often your brother plays tennis?"},
            {"label": "D", "text": "How often is your brother play tennis?"},
            {"label": "E", "text": "How often does your brother plays tennis?"}
        ],
        "answer": "A",
        "teacher_feedback": "✓ Correct! Well done.\n'Your brother' is singular (he), so we use 'does'. The main verb 'play' stays in base form without -s.",
        "translation": "Erkek kardeşin ne sıklıkla tenis oynar?",
        "explanation": "How often + does + your brother (he) + play (yalın)? Kurala tam uyan tek şık A'dır.",
        "distractors": "• B: 'your brother' (he) için 'do' kullanılamaz.\n• C: Soru yardımcı fiili unutulmuştur.\n• D: 'is' ile yalın 'play' birleşemez.\n• E: 'does' varken fiile -s eklenemez ('plays' YANLIŞTIR).",
        "tip": "How often DOES + tekil şahıs + YALIN FİİL."
    },
    {
        "id": 14,
        "unit": "Hocanın Challenge Soruları",
        "unit_title": "Challenge Quiz • Vocabulary in Context",
        "question": "We waited for forty minutes to buy train tickets because the line was very ___.",
        "options": [
            {"label": "A", "text": "sick"},
            {"label": "B", "text": "flat"},
            {"label": "C", "text": "broken"},
            {"label": "D", "text": "long"},
            {"label": "E", "text": "late"}
        ],
        "answer": "D",
        "teacher_feedback": "✓ Correct! Well done.\nWaiting for 40 minutes means there was a 'long line' (a long queue of people).",
        "translation": "Tren bileti almak için 40 dakika bekledik çünkü kuyruk çok uzundu.",
        "explanation": "40 dakika bekleme sebebi insan kuyruğunun (line) **uzun (long)** olmasıdır. 'long lines' Smart Choice Unit 6'nın kilit kelime öbeğidir.",
        "distractors": "• A: İnsanlar için hasta.\n• B: Lastik için inik.\n• C: Eşyalar için kırık/bozuk.\n• E: Otobüs için geç.",
        "tip": "line (sıra/kuyruk) $\rightarrow$ LONG (uzun)."
    },
    {
        "id": 15,
        "unit": "Hocanın Challenge Soruları",
        "unit_title": "Challenge Quiz • Short Answers Trap",
        "question": "A: \"Are you tired after work?\"\nB: \"Yes, ___________.\"",
        "options": [
            {"label": "A", "text": "I'm."},
            {"label": "B", "text": "I am."},
            {"label": "C", "text": "I do."},
            {"label": "D", "text": "am I."},
            {"label": "E", "text": "I was."}
        ],
        "answer": "B",
        "teacher_feedback": "✓ Correct! Well done.\nIn affirmative short answers, never use contractions! 'Yes, I am' is correct. ('Yes, I'm' is never used).",
        "translation": "A: \"İşten sonra yorgun musun?\" — B: \"Evet, yorgunum.\"",
        "explanation": "Kısa olumlu cevaplarda KESİNLİKLE apostrof ile kısaltma yapılamaz. 'Yes, I am' doğru kalıptır; 'Yes, I'm' İngilizcede kural dışıdır.",
        "distractors": "• A: 'Yes, I'm' asla denmez (hocanın en büyük sınav tuzağı).\n• C: Soru 'Do you...?' değil, 'Are you...?' dur.\n• D: Soru devrik dizilimidir.\n• E: Soru şimdiki zamandır, geçmiş zamanla cevap verilmez.",
        "tip": "ALTIN SINAV KURALI: Olumlu kısa cevapta kısaltma YASAKTIR! (Yes, I am. / Yes, he is. / Yes, they are.)"
    },
    {
        "id": 16,
        "unit": "Hocanın Challenge Soruları",
        "unit_title": "Challenge Quiz • Present Simple Contrast",
        "question": "She ___ meat because she is a vegetarian, but she ___ fish sometimes.",
        "options": [
            {"label": "A", "text": "doesn't eat / eats"},
            {"label": "B", "text": "don't eat / eats"},
            {"label": "C", "text": "doesn't eats / eat"},
            {"label": "D", "text": "isn't eating / eats"},
            {"label": "E", "text": "doesn't eat / is eating"}
        ],
        "answer": "A",
        "teacher_feedback": "✓ Correct! Well done.\nThird person singular (she): negative = doesn't + base verb (doesn't eat); positive = verb + s (eats).",
        "translation": "O vejetaryen olduğu için et yemez, fakat bazen balık yer.",
        "explanation": "She öznesiyle olumsuz: **doesn't eat**. Olumlu: **eats**. Anna sorusuyla birebir aynı mantıktadır.",
        "distractors": "• B: She ile don't kullanılmaz.\n• C: doesn't varken fiile -s eklenemez.\n• D: Genel kuraldır, şimdiki zaman olamaz.\n• E: 'sometimes' geniş zaman zarfıdır, is eating olamaz.",
        "tip": "Hocanın favori soru şablonu: [Özne] doesn't [yalın fiil], but [özne] [fiil-s]."
    },
    {
        "id": 17,
        "unit": "Hocanın Challenge Soruları",
        "unit_title": "Challenge Quiz • Past of Be (Was/Were)",
        "question": "Which question is correct?",
        "options": [
            {"label": "A", "text": "Was they at home last night?"},
            {"label": "B", "text": "Were they at home last night?"},
            {"label": "C", "text": "Did they at home last night?"},
            {"label": "D", "text": "Were they were at home last night?"},
            {"label": "E", "text": "Are they at home last night?"}
        ],
        "answer": "B",
        "teacher_feedback": "✓ Correct! Well done.\n'They' takes 'were' in the past tense. In question form: Were + they + place + time?",
        "translation": "Onlar dün gece evdeler miydi?",
        "explanation": "'They' çoğul öznesinin geçmiş zaman hali **were** dür. Soru yaparken 'Were' başa gelir: 'Were they at home last night?'",
        "distractors": "• A: 'They' ile 'was' kullanılamaz (was tekiller içindir).\n• C: 'Did' eylem fiili gerektirir (Did they stay at home? gibi); yer tamlamalarında to be (were) kullanılır.\n• D: İki kere were kullanılmıştır.\n• E: 'last night' geçmiş zamandır, 'are' şimdiki zamandır.",
        "tip": "Geçmiş zaman çoğul soru: WERE they...? / WERE you...? / WERE we...?"
    },
    {
        "id": 18,
        "unit": "Hocanın Challenge Soruları",
        "unit_title": "Challenge Quiz • Vocabulary in Context",
        "question": "The morning bus was so ___ that I couldn't find an empty seat to sit down.",
        "options": [
            {"label": "A", "text": "terrible"},
            {"label": "B", "text": "crowded"},
            {"label": "C", "text": "flat"},
            {"label": "D", "text": "long"},
            {"label": "E", "text": "sick"}
        ],
        "answer": "B",
        "teacher_feedback": "✓ Correct! Well done.\nIf you cannot find a seat because there are too many people, the bus is crowded.",
        "translation": "Sabah otobüsü o kadar kalabalıktı ki oturacak boş bir koltuk bulamadım.",
        "explanation": "Oturacak yer bulunamaması otobüsün tıklım tıklım / **kalabalık (crowded)** olduğunu belirtir.",
        "distractors": "• A (terrible): Berbat (otobüsün doluluğunu doğrudan nitelemez).\n• C (flat): Lastik için.\n• D (long): Kuyruk için.\n• E (sick): Hasta insan için.",
        "tip": "İpucu: 'no empty seat / too many people' $\rightarrow$ CROWDED (kalabalık)."
    },
    {
        "id": 19,
        "unit": "Hocanın Challenge Soruları",
        "unit_title": "Challenge Quiz • Articles (a / an)",
        "question": "My father is ___ engineer, and my mother works as ___ manager in a bank.",
        "options": [
            {"label": "A", "text": "a / an"},
            {"label": "B", "text": "an / a"},
            {"label": "C", "text": "a / a"},
            {"label": "D", "text": "an / an"},
            {"label": "E", "text": "the / the"}
        ],
        "answer": "B",
        "teacher_feedback": "✓ Correct! Well done.\n'Engineer' starts with a vowel sound (an engineer). 'Manager' starts with a consonant sound (a manager).",
        "translation": "Babam bir mühendis, annem ise bir bankada müdür olarak çalışıyor.",
        "explanation": "Sesli başlayan meslekler: **an engineer**. Sessiz başlayan meslekler: **a manager**.",
        "distractors": "• A: Şıklar terstir.\n• C, D ve E: Sesli/sessiz uyumuna uymaz.",
        "tip": "AN engineer, AN architect, AN artist AMA A manager, A teacher, A doctor."
    },
    {
        "id": 20,
        "unit": "Hocanın Challenge Soruları",
        "unit_title": "Challenge Quiz • Dialogue & Where were you",
        "question": "A: \"Where were you yesterday afternoon?\"\nB: \"___________\"",
        "options": [
            {"label": "A", "text": "I was at the library with Leo."},
            {"label": "B", "text": "I am at the library now."},
            {"label": "C", "text": "Yes, I was."},
            {"label": "D", "text": "I went at the library."},
            {"label": "E", "text": "I wasn't yesterday."}
        ],
        "answer": "A",
        "teacher_feedback": "✓ Correct! Well done.\nThe question asks for a place in the past (Where were you yesterday afternoon?). The correct answer is: I was at the library.",
        "translation": "A: \"Dün öğleden sonra neredeydin?\" — B: \"Leo ile birlikte kütüphanedeydim.\"",
        "explanation": "'Where were you...?' sorusuna geçmiş zaman yer bildirimiyle tam cevap verilir: **I was at the library.**",
        "distractors": "• B: 'now' ve 'am' şimdiki zamandır.\n• C: Wh- sorusuna Yes/No denmez.\n• D: 'went at' yanlıştır ('went to' denir).\n• E: Eksik ve anlamsızdır.",
        "tip": "Where were you...? $\rightarrow$ I was at [Mekan]."
    },
    {
        "id": 21,
        "unit": "Hocanın Challenge Soruları",
        "unit_title": "Challenge Quiz • Word Order (Adverbs)",
        "question": "Which sentence is grammatically correct?",
        "options": [
            {"label": "A", "text": "She usually goes to bed early."},
            {"label": "B", "text": "She goes usually to bed early."},
            {"label": "C", "text": "She is usually goes to bed early."},
            {"label": "D", "text": "Usually she go to bed early."},
            {"label": "E", "text": "She go usually to bed early."}
        ],
        "answer": "A",
        "teacher_feedback": "✓ Correct! Well done.\nFrequency adverbs go BEFORE the main verb: Subject + usually + goes.",
        "translation": "O genellikle erken yatar.",
        "explanation": "Sıklık zarfları esas fiilden **ÖNCE** gelir: She (özne) + **usually** (zarf) + **goes** (fiil) to bed early.",
        "distractors": "• B: Zarf fiilden sonraya konmuştur.\n• C: Hem 'is' hem 'goes' bir arada kullanılamaz.\n• D ve E: 'she' öznesiyle fiil 'go' kalamaz (-es almalıdır).",
        "tip": "Sıralama: Özne + ALWAYS / USUALLY + Fiil."
    },
    {
        "id": 22,
        "unit": "Hocanın Challenge Soruları",
        "unit_title": "Challenge Quiz • Look! Clue",
        "question": "Look at the sky! It ___ to rain, so take your umbrella.",
        "options": [
            {"label": "A", "text": "starts"},
            {"label": "B", "text": "is starting"},
            {"label": "C", "text": "start"},
            {"label": "D", "text": "started"},
            {"label": "E", "text": "starting"}
        ],
        "answer": "B",
        "teacher_feedback": "✓ Correct! Well done.\n'Look at the sky!' directs attention to something happening right now, which requires Present Continuous: is starting.",
        "translation": "Gökyüzüne bak! Yağmur yağmaya başlıyor, bu yüzden şemsiyeni al.",
        "explanation": "'Look at the sky!' konuşma anındaki eylemi işaret eder. Tekil özne 'It' için Present Continuous biçimi **is starting** dir.",
        "distractors": "• A: Geniş zamandır; konuşma anını anlatamaz.\n• C: 'It' ile 'start' kullanılamaz.\n• D: Geçmiş zamandır.\n• E: Yardımcı fiil 'is' eksiktir.",
        "tip": "Look! / Look at ...! $\rightarrow$ IS / ARE + V-ING."
    },
    {
        "id": 23,
        "unit": "Hocanın Challenge Soruları",
        "unit_title": "Challenge Quiz • Vocabulary in Context",
        "question": "I dropped my phone on the floor and now the screen is ___.",
        "options": [
            {"label": "A", "text": "crowded"},
            {"label": "B", "text": "flat"},
            {"label": "C", "text": "broken"},
            {"label": "D", "text": "late"},
            {"label": "E", "text": "sick"}
        ],
        "answer": "C",
        "teacher_feedback": "✓ Correct! Well done.\nDropping a phone causes the screen to be broken (cracked / damaged).",
        "translation": "Telefonumu yere düşürdüm ve şimdi ekranı kırık/bozuk.",
        "explanation": "Yere düşen telefonun ekranı kırılır veya bozulur (**broken**).",
        "distractors": "• A: Kalabalık.\n• B: İnik lastik.\n• D: Geç.\n• E: Hasta.",
        "tip": "phone / screen $\rightarrow$ BROKEN."
    },
    {
        "id": 24,
        "unit": "Hocanın Challenge Soruları",
        "unit_title": "Challenge Quiz • Do you ever...",
        "question": "A: \"Do you ever exercise after class?\"\nB: \"Yes, I ___________ go swimming with my friends.\"",
        "options": [
            {"label": "A", "text": "never"},
            {"label": "B", "text": "usually"},
            {"label": "C", "text": "don't"},
            {"label": "D", "text": "not"},
            {"label": "E", "text": "am"}
        ],
        "answer": "B",
        "teacher_feedback": "✓ Correct! Well done.\nThe answer starts with 'Yes', so a positive frequency adverb like 'usually' is required. ('Never' would contradict 'Yes').",
        "translation": "A: \"Derslerden sonra hiç egzersiz yapar mısın?\" — B: \"Evet, genellikle arkadaşlarımla yüzmeye giderim.\"",
        "explanation": "'Yes' ile başlayan olumlu yanıtta 'never' veya olumsuzluk kelimeleri yer alamaz. Uygun zarf **usually** (genellikle) dir.",
        "distractors": "• A (never): Asla demektir, 'Yes' ile çelişir.\n• C ve D: Olumsuzluk ekleridir.\n• E: 'I am go' dilbilgisi hatasıdır.",
        "tip": "Yes $\rightarrow$ usually / always / sometimes. No $\rightarrow$ never."
    },
    {
        "id": 25,
        "unit": "Hocanın Challenge Soruları",
        "unit_title": "Challenge Quiz • Frequency with To Be",
        "question": "Which sentence is grammatically correct?",
        "options": [
            {"label": "A", "text": "He is never late for our meetings."},
            {"label": "B", "text": "He never is late for our meetings."},
            {"label": "C", "text": "He is late never for our meetings."},
            {"label": "D", "text": "Never he is late for our meetings."},
            {"label": "E", "text": "He late is never for our meetings."}
        ],
        "answer": "A",
        "teacher_feedback": "✓ Correct! Well done.\nWith the verb 'be', the frequency adverb comes AFTER: Subject + is + never + adjective.",
        "translation": "O toplantılarımıza asla geç kalmaz.",
        "explanation": "Sıklık zarfları 'to be' (am/is/are) fiilinden **SONRA** gelir: He + **is** + **never** + late.",
        "distractors": "• B: 'never' be fiilinden önceye konmuştur (yanlış).\n• C: Sıfattan sonraya konmuştur.\n• D: Cümle başına konmuştur.\n• E: Devrik ve bozuktur.",
        "tip": "Kural: Normal fiilden ÖNCE (usually goes) | BE fiilinden SONRA (is never)."
    }
]

# Write JSON safely
questions_json = json.dumps(questions, ensure_ascii=False)

html_content = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Smart Choice 1 • Challenge Quiz & Sınav Hazırlık</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #f26522; /* Teacher's app coral/orange */
            --primary-dark: #d45113;
            --primary-light: #fff5ee;
            --bg: #f5f6f8;
            --card-bg: #ffffff;
            --text-main: #1f2937;
            --text-muted: #6b7280;
            --border: #e5e7eb;
            --badge-bg: #f87171;
            --badge-text: #ffffff;
            --success-border: #10b981;
            --success-bg: #ecfdf5;
            --success-text: #065f46;
            --wrong-border: #ef4444;
            --wrong-bg: #fef2f2;
            --font-serif: 'DM Serif Display', Georgia, serif;
            --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            --radius: 18px;
            --shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.06);
        }

        [data-theme="dark"] {
            --bg: #0f172a;
            --card-bg: #1e293b;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --border: #334155;
            --primary-light: #332014;
            --success-bg: #064e3b33;
            --wrong-bg: #7f1d1d33;
            --shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.4);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            -webkit-tap-highlight-color: transparent;
            font-family: var(--font-sans);
        }

        body {
            background-color: var(--bg);
            color: var(--text-main);
            min-height: 100vh;
            padding-bottom: 40px;
            transition: background-color 0.2s, color 0.2s;
        }

        /* Top Header */
        header {
            position: sticky;
            top: 0;
            z-index: 100;
            background: var(--card-bg);
            border-bottom: 1px solid var(--border);
            padding: 12px 16px;
        }

        .header-inner {
            max-width: 680px;
            margin: 0 auto;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .app-title {
            font-size: 0.95rem;
            font-weight: 600;
            color: var(--text-main);
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .app-title span.tag {
            background: var(--primary-light);
            color: var(--primary);
            font-size: 0.72rem;
            padding: 2px 8px;
            border-radius: 99px;
            font-weight: 700;
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
            font-size: 0.95rem;
        }

        /* Container */
        .container {
            max-width: 680px;
            margin: 0 auto;
            padding: 16px;
        }

        /* Progress Bar (Exact matching teacher screen) */
        .quiz-status-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 0.76rem;
            font-weight: 700;
            letter-spacing: 0.5px;
            text-transform: uppercase;
            color: var(--text-muted);
            margin-bottom: 8px;
        }

        .status-left {
            color: var(--primary);
        }

        .status-right {
            color: var(--primary);
        }

        .progress-track {
            width: 100%;
            height: 5px;
            background: var(--border);
            border-radius: 3px;
            overflow: hidden;
            margin-bottom: 18px;
        }

        .progress-fill {
            height: 100%;
            background: var(--primary);
            width: 0%;
            transition: width 0.3s ease;
        }

        /* Mode Switcher Tabs */
        .mode-tabs {
            display: flex;
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 3px;
            margin-bottom: 16px;
        }

        .mode-tab {
            flex: 1;
            padding: 8px 10px;
            font-size: 0.82rem;
            font-weight: 600;
            text-align: center;
            border: none;
            background: transparent;
            color: var(--text-muted);
            border-radius: 9px;
            cursor: pointer;
            transition: all 0.15s;
        }

        .mode-tab.active {
            background: var(--primary);
            color: white;
            box-shadow: 0 2px 6px rgba(242, 101, 34, 0.3);
        }

        /* Challenge Card (Exact Teacher Styling) */
        .quiz-card {
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 24px 20px;
            box-shadow: var(--shadow);
            margin-bottom: 18px;
        }

        .question-title {
            font-family: var(--font-serif);
            font-size: 1.35rem;
            line-height: 1.45;
            color: var(--text-main);
            margin-bottom: 22px;
            font-weight: 400;
            letter-spacing: -0.2px;
        }

        /* Options */
        .options-group {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .option-button {
            background: var(--card-bg);
            border: 1.5px solid var(--border);
            border-radius: 12px;
            padding: 14px 16px;
            display: flex;
            align-items: center;
            gap: 14px;
            cursor: pointer;
            text-align: left;
            transition: all 0.15s ease;
            position: relative;
        }

        .option-button:hover:not(:disabled) {
            border-color: #cbd5e1;
            background: #fafafa;
        }

        .option-letter {
            width: 30px;
            height: 30px;
            border-radius: 50%;
            background: #fca5a5; /* soft teacher coral */
            color: #ffffff;
            font-weight: 700;
            font-size: 0.85rem;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            transition: all 0.15s;
        }

        .option-text {
            font-size: 0.98rem;
            color: var(--text-main);
            font-weight: 500;
            line-height: 1.35;
        }

        /* Selected States */
        .option-button.selected-correct {
            border-color: var(--success-border) !important;
            background: var(--success-bg) !important;
        }
        .option-button.selected-correct .option-letter {
            background: var(--success-border) !important;
        }

        .option-button.selected-wrong {
            border-color: var(--wrong-border) !important;
            background: var(--wrong-bg) !important;
        }
        .option-button.selected-wrong .option-letter {
            background: var(--wrong-border) !important;
        }

        /* Teacher's Green Feedback Box */
        .feedback-box {
            margin-top: 20px;
            background: var(--success-bg);
            border: 1px solid var(--success-border);
            border-radius: 12px;
            padding: 16px 18px;
            display: none;
            animation: fadeIn 0.2s ease;
        }

        .feedback-box.show {
            display: block;
        }

        .feedback-header {
            font-size: 0.98rem;
            font-weight: 700;
            color: var(--success-text);
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .feedback-teacher-text {
            font-size: 0.92rem;
            line-height: 1.5;
            color: var(--text-main);
            margin-bottom: 12px;
        }

        /* Extra Educational Section inside feedback */
        .feedback-details {
            border-top: 1px dashed rgba(16, 185, 129, 0.3);
            padding-top: 10px;
            margin-top: 10px;
            font-size: 0.85rem;
            line-height: 1.5;
        }

        .detail-row {
            margin-bottom: 8px;
        }
        .detail-label {
            font-weight: 700;
            color: var(--text-muted);
            text-transform: uppercase;
            font-size: 0.72rem;
            letter-spacing: 0.5px;
            margin-bottom: 2px;
        }
        .detail-content {
            white-space: pre-line;
            color: var(--text-main);
        }

        /* Next Question Button (Teacher Style) */
        .next-btn-container {
            margin-top: 18px;
            display: none;
        }
        .next-btn-container.show {
            display: block;
        }

        .next-btn {
            background: var(--primary);
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 10px;
            font-weight: 600;
            font-size: 0.95rem;
            cursor: pointer;
            box-shadow: 0 2px 8px rgba(242, 101, 34, 0.35);
            transition: all 0.15s;
            width: 100%;
        }

        .next-btn:active {
            transform: scale(0.98);
        }

        /* Navigation controls */
        .nav-controls {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 14px;
        }

        .text-btn {
            background: none;
            border: none;
            color: var(--text-muted);
            font-size: 0.85rem;
            font-weight: 600;
            cursor: pointer;
            padding: 8px 12px;
            border-radius: 8px;
        }

        .text-btn:hover {
            color: var(--primary);
            background: var(--primary-light);
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-4px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Modal */
        .modal {
            display: none;
            position: fixed;
            top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(0,0,0,0.5);
            z-index: 200;
            align-items: center;
            justify-content: center;
            padding: 16px;
        }
        .modal.open { display: flex; }
        .modal-body {
            background: var(--card-bg);
            border-radius: var(--radius);
            max-width: 480px;
            width: 100%;
            max-height: 80vh;
            overflow-y: auto;
            padding: 20px;
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
        .grid-num-btn.correct { background: var(--success-border); color: white; }
        .grid-num-btn.wrong { background: var(--wrong-border); color: white; }
    </style>
</head>
<body>

    <!-- Header -->
    <header>
        <div class="header-inner">
            <div class="app-title">
                <span>Smart Choice 1</span>
                <span class="tag">Challenge Quiz</span>
            </div>
            <div class="header-actions">
                <button class="icon-btn" onclick="openJumpModal()" title="Sorular">🔢</button>
                <button class="icon-btn" onclick="toggleTheme()" id="themeBtn" title="Tema">🌙</button>
                <button class="icon-btn" onclick="resetAll()" title="Sıfırla">🔄</button>
            </div>
        </div>
    </header>

    <div class="container">
        <!-- Progress Bar & Score (Exact teacher replica) -->
        <div class="quiz-status-bar">
            <span class="status-left" id="qCounter">QUESTION 1 / 25</span>
            <span class="status-right" id="scoreCounter">SCORE: 0</span>
        </div>
        <div class="progress-track">
            <div class="progress-fill" id="progressFill"></div>
        </div>

        <!-- Question Card -->
        <div class="quiz-card" id="quizCard">
            <div class="question-title" id="questionText">Loading question...</div>
            <div class="options-group" id="optionsGroup"></div>

            <!-- Teacher Feedback Box -->
            <div class="feedback-box" id="feedbackBox">
                <div class="feedback-header" id="feedbackHeader">✓ Correct! Well done.</div>
                <div class="feedback-teacher-text" id="teacherText"></div>
                <div class="feedback-details">
                    <div class="detail-row">
                        <div class="detail-label">🇹🇷 Türkçe Çevirisi:</div>
                        <div class="detail-content" id="detailTrans"></div>
                    </div>
                    <div class="detail-row">
                        <div class="detail-label">💡 Neden Doğru? (Kural):</div>
                        <div class="detail-content" id="detailExp"></div>
                    </div>
                    <div class="detail-row">
                        <div class="detail-label">⚠️ Çeldiriciler (Diğer Şıklar):</div>
                        <div class="detail-content" id="detailDistr"></div>
                    </div>
                    <div class="detail-row">
                        <div class="detail-label">📌 Sınav Taktik / İpucu:</div>
                        <div class="detail-content" id="detailTip"></div>
                    </div>
                </div>
            </div>

            <!-- Next Question Button -->
            <div class="next-btn-container" id="nextBtnContainer">
                <button class="next-btn" onclick="nextQuestion()">Next question →</button>
            </div>
        </div>

        <!-- Navigation Buttons -->
        <div class="nav-controls">
            <button class="text-btn" onclick="prevQuestion()">← Önceki Soru</button>
            <button class="text-btn" onclick="nextQuestion()">Sonraki Soru →</button>
        </div>
    </div>

    <!-- Modal for Question Jump -->
    <div class="modal" id="jumpModal" onclick="closeJumpModal(event)">
        <div class="modal-body" onclick="event.stopPropagation()">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <h3 style="font-size:1rem;">Sorular Listesi</h3>
                <button class="icon-btn" onclick="closeJumpModal()">✕</button>
            </div>
            <div class="grid-nums" id="gridNums"></div>
        </div>
    </div>

    <script>
        const QUESTIONS = """ + questions_json + """;

        let currentIndex = 0;
        let score = 0;
        let userAnswers = {}; // { qId: selectedLabel }

        // Load saved state
        try {
            const saved = localStorage.getItem('teacher_quiz_state');
            if (saved) {
                const parsed = JSON.parse(saved);
                userAnswers = parsed.answers || {};
                score = parsed.score || 0;
            }
        } catch(e) {}

        function initTheme() {
            const theme = localStorage.getItem('teacher_quiz_theme') || 'light';
            document.documentElement.setAttribute('data-theme', theme);
            document.getElementById('themeBtn').textContent = theme === 'dark' ? '☀️' : '🌙';
        }

        function toggleTheme() {
            const cur = document.documentElement.getAttribute('data-theme') || 'light';
            const next = cur === 'dark' ? 'light' : 'dark';
            document.documentElement.setAttribute('data-theme', next);
            localStorage.setItem('teacher_quiz_theme', next);
            document.getElementById('themeBtn').textContent = next === 'dark' ? '☀️' : '🌙';
        }

        function renderQuestion() {
            const q = QUESTIONS[currentIndex];
            const total = QUESTIONS.length;

            // Status bar
            document.getElementById('qCounter').textContent = `QUESTION ${currentIndex + 1} / ${total}`;
            document.getElementById('scoreCounter').textContent = `SCORE: ${score}`;
            document.getElementById('progressFill').style.width = `${((currentIndex + 1) / total) * 100}%`;

            // Question text
            document.getElementById('questionText').textContent = q.question;

            // Options
            const group = document.getElementById('optionsGroup');
            group.innerHTML = '';

            const answered = userAnswers[q.id] !== undefined;
            const userChoice = userAnswers[q.id];

            q.options.forEach(opt => {
                const btn = document.createElement('button');
                btn.className = 'option-button';

                if (answered) {
                    btn.disabled = true;
                    if (opt.label === q.answer) {
                        btn.classList.add('selected-correct');
                    } else if (opt.label === userChoice) {
                        btn.classList.add('selected-wrong');
                    }
                }

                btn.onclick = () => selectOption(opt.label);

                btn.innerHTML = `
                    <span class="option-letter">${opt.label}</span>
                    <span class="option-text">${opt.text}</span>
                `;
                group.appendChild(btn);
            });

            // Feedback box
            const fBox = document.getElementById('feedbackBox');
            const nextContainer = document.getElementById('nextBtnContainer');

            if (answered) {
                const isCorrect = userChoice === q.answer;
                const fHeader = document.getElementById('feedbackHeader');
                
                if (isCorrect) {
                    fHeader.textContent = '✓ Correct! Well done.';
                    fHeader.style.color = 'var(--success-text)';
                    fBox.style.background = 'var(--success-bg)';
                    fBox.style.borderColor = 'var(--success-border)';
                } else {
                    fHeader.textContent = '✗ Incorrect. Check the explanation:';
                    fHeader.style.color = '#b91c1c';
                    fBox.style.background = 'var(--wrong-bg)';
                    fBox.style.borderColor = 'var(--wrong-border)';
                }

                document.getElementById('teacherText').textContent = q.teacher_feedback || q.explanation;
                document.getElementById('detailTrans').textContent = q.translation;
                document.getElementById('detailExp').textContent = q.explanation;
                document.getElementById('detailDistr').textContent = q.distractors;
                document.getElementById('detailTip').textContent = q.tip;

                fBox.classList.add('show');
                nextContainer.classList.add('show');
            } else {
                fBox.classList.remove('show');
                nextContainer.classList.remove('show');
            }
        }

        function selectOption(label) {
            const q = QUESTIONS[currentIndex];
            if (userAnswers[q.id] !== undefined) return;

            userAnswers[q.id] = label;
            if (label === q.answer) {
                score++;
            }

            saveState();
            renderQuestion();
        }

        function nextQuestion() {
            if (currentIndex < QUESTIONS.length - 1) {
                currentIndex++;
                renderQuestion();
                window.scrollTo({ top: 0, behavior: 'smooth' });
            } else {
                alert(`Tebrikler! Sınavı tamamladın.\nToplam Puanın: ${score} / ${QUESTIONS.length}`);
            }
        }

        function prevQuestion() {
            if (currentIndex > 0) {
                currentIndex--;
                renderQuestion();
                window.scrollTo({ top: 0, behavior: 'smooth' });
            }
        }

        function saveState() {
            try {
                localStorage.setItem('teacher_quiz_state', JSON.stringify({
                    answers: userAnswers,
                    score: score
                }));
            } catch(e) {}
        }

        function resetAll() {
            if (confirm('Tüm çözümlerini sıfırlayıp 1. sorudan başlamak istiyor musun?')) {
                userAnswers = {};
                score = 0;
                currentIndex = 0;
                saveState();
                renderQuestion();
            }
        }

        function openJumpModal() {
            const grid = document.getElementById('gridNums');
            grid.innerHTML = '';
            QUESTIONS.forEach((q, idx) => {
                const btn = document.createElement('button');
                btn.className = 'grid-num-btn';
                btn.textContent = idx + 1;

                if (userAnswers[q.id]) {
                    if (userAnswers[q.id] === q.answer) {
                        btn.classList.add('correct');
                    } else {
                        btn.classList.add('wrong');
                    }
                }

                btn.onclick = () => {
                    currentIndex = idx;
                    closeJumpModal();
                    renderQuestion();
                };
                grid.appendChild(btn);
            });
            document.getElementById('jumpModal').classList.add('open');
        }

        function closeJumpModal() {
            document.getElementById('jumpModal').classList.remove('open');
        }

        // Initialize
        initTheme();
        renderQuestion();
    </script>
</body>
</html>
"""

# Save updated files
with open("sinav_calisma.html", "w", encoding="utf-8") as f:
    f.write(html_content)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Teacher style quiz generated successfully with {len(questions)} questions!")

