# -*- coding: utf-8 -*-
"""
Add questions from Slides 13, 16, 18 of SmartChoice1_Challenge_Quiz.pptx:
1. Q12: I have ___ umbrella, but it isn't ___ new one. -> an / a
2. Q16: How ___ do you visit your grandparents? Every weekend. -> often
3. Q20: Yesterday it ___ cold and windy, so we ___ at the beach. -> was / weren't
4. Slide 14: My brother ___ football on Saturdays, but this Saturday he ___ for an exam. -> plays / is studying
"""
import json

with open("all_questions_master.json", "r", encoding="utf-8") as f:
    master = json.load(f)

new_questions = [
    {
        "is_official_exam": True,
        "is_exam_certain": True,
        "category": "🏆 HOCANIN SLAYT CHALLENGE SORULARI",
        "tag": "⭐ SLAYT • Q12 • Articles: an umbrella / a new one",
        "question": "I have ___ umbrella, but it isn't ___ new one.",
        "options": [
            {"label": "A", "text": "a / an"},
            {"label": "B", "text": "an / the"},
            {"label": "C", "text": "an / a"},
            {"label": "D", "text": "the / an"},
            {"label": "E", "text": "a / a"}
        ],
        "answer": "C",
        "teacher_feedback": "✓ Correct! Well done.\n'Umbrella' begins with a vowel sound (/ʌ/) so it takes 'an'. 'New one' begins with a consonant sound (/n/) so it takes 'a'.",
        "translation": "Benim bir şemsiyem var, fakat o yeni bir şemsiye/tane değil.",
        "explanation": "Articles (a / an) Altın Kuralı:\n1) 'umbrella' kelimesi sesli sesle (/ʌ/ - ambrela) başladığı için başına **an** gelir: **an umbrella**.\n2) İkinci boşlukta 'new one' sıfat tamlaması sessiz sesle (/n/ - niv) başladığı için başına **a** gelir: **a new one**.\nDoğru eşleştirme: **an / a**.",
        "distractors": "• A: 'umbrella' için 'a' kullanılamaz; 'new' için 'an' kullanılamaz (tam tersidir).\n• B: 'the new one' belirli bir şemsiyeden bahsetmez, sıradan yeni bir tanedir.\n• D: 'the' gereksizdir, 'umbrella' bilinmeyen nesnedir.\n• E: 'umbrella' önüne 'a' gelemez.",
        "tip": "Kelimenin baş harfinin okunuşuna bak: /a, e, ı, i, o, ö, u, ü/ sesiyle başlıyorsa -> AN (an umbrella, an apple). Sessiz sesle başlıyorsa -> A (a new one, a car)."
    },
    {
        "is_official_exam": True,
        "is_exam_certain": True,
        "category": "🏆 HOCANIN SLAYT CHALLENGE SORULARI",
        "tag": "⭐ SLAYT • Q16 • Soru Kalıbı: How often?",
        "question": "How ___ do you visit your grandparents? Every weekend.",
        "options": [
            {"label": "A", "text": "long"},
            {"label": "B", "text": "often"},
            {"label": "C", "text": "much"},
            {"label": "D", "text": "old"},
            {"label": "E", "text": "many"}
        ],
        "answer": "B",
        "teacher_feedback": "✓ Correct! Well done.\nWe use 'How often' to ask about frequency. The answer 'Every weekend' shows how frequently the action happens.",
        "translation": "\"Büyükanne ve büyükbabanı ne sıklıkla ziyaret edersin?\" \"Her hafta sonu.\"",
        "explanation": "Soru Kalıbı Analizi:\nCevapta **'Every weekend'** (Her hafta sonu) bir **sıklık / rutin** belirtmektedir. Bir eylemin hangi sıklıkla yapıldığını soran tek İngilizce soru kalıbı **'How often...?'** (Ne sıklıkla?) dır.",
        "distractors": "• A: 'How long' = Ne kadar süre / Ne kadar uzunlukta?\n• C: 'How much' = Ne kadar? (fiyat / sayılamayan miktar)\n• D: 'How old' = Kaç yaşında?\n• E: 'How many' = Kaç tane? (sayılabilen çoğul nesneler)",
        "tip": "Cevapta 'always, usually, sometimes, every day, twice a week, every weekend' varsa soru DAİMA 'HOW OFTEN' ile sorulmuştur!"
    },
    {
        "is_official_exam": True,
        "is_exam_certain": True,
        "category": "🏆 HOCANIN SLAYT CHALLENGE SORULARI",
        "tag": "⭐ SLAYT • Q20 • Past of Be: was / weren't",
        "question": "Yesterday it ___ cold and windy, so we ___ at the beach.",
        "options": [
            {"label": "A", "text": "wasn't / were"},
            {"label": "B", "text": "weren't / weren't"},
            {"label": "C", "text": "wasn't / was"},
            {"label": "D", "text": "was / was"},
            {"label": "E", "text": "was / weren't"}
        ],
        "answer": "E",
        "teacher_feedback": "✓ Correct! Well done.\n'It' takes 'was' (it was cold and windy). 'So' (therefore) provides logical consequence: because it was cold and windy, 'we weren't at the beach'. Plural 'we' takes 'weren't'.",
        "translation": "Dün hava soğuk ve rüzgarlıydı, bu yüzden biz sahilde/plajda değildik.",
        "explanation": "Mantık ve Zaman Analizi:\n1) 'Yesterday' geçmiş zamandır. 'it' tekil öznesi için To Be geçmiş hali **was** dır: **it was cold and windy**.\n2) 'so' (bu yüzden) bir sebep-sonuç bağlacıdır. Hava soğuk ve rüzgarlı olduğu için mantıken plajda **değildik**: **we weren't at the beach**.\n3) 'we' öznesi çoğuldur, 'wasn't' değil **weren't** alır.\nDoğru sıralama: **was / weren't**.",
        "distractors": "• A: 'wasn't / were' mantıksızdır (Hava soğuk değildi bu yüzden plajdaydık olurdu ama rüzgarlıydı diyor).\n• B: 'it' tekildir, 'weren't' alamaz.\n• C: 'we' çoğuldur, tekil 'was' alamaz.\n• D: 'we was' dilbilgisi hatasıdır (we were olmalıdır) ve hava soğukken plajda olmak mantıksızdır.",
        "tip": "1) it $\rightarrow$ WAS | 2) we $\rightarrow$ WERE / WEREN'T | 3) 'so' bağlacının mantık akışına dikkat et!"
    },
    {
        "is_official_exam": True,
        "is_exam_certain": True,
        "category": "🏆 HOCANIN SLAYT CHALLENGE SORULARI",
        "tag": "⭐ SLAYT • Q14 • Habit vs This Saturday",
        "question": "My brother ___ football on Saturdays, but this Saturday he ___ for an exam.",
        "options": [
            {"label": "A", "text": "plays / is studying"},
            {"label": "B", "text": "is playing / studies"},
            {"label": "C", "text": "play / is studying"},
            {"label": "D", "text": "plays / study"},
            {"label": "E", "text": "is playing / study"}
        ],
        "answer": "A",
        "teacher_feedback": "✓ Correct! Well done.\n'on Saturdays' indicates regular habit (Present Simple: plays). 'this Saturday' indicates a temporary action happening now/this weekend (Present Continuous: is studying).",
        "translation": "Erkek kardeşim cumartesi günleri futbol oynar, fakat bu cumartesi sınav için ders çalışıyor.",
        "explanation": "Zaman Karşılaştırması:\n1) 'on Saturdays' çoğuldur, her cumartesi yapılan rutini bildirir. 'My brother' (he) için geniş zaman: **plays**.\n2) 'this Saturday' (bu cumartesi) geçici özel bir durumu anlatır: **is studying**.\nDoğru sıralama: **plays / is studying**.",
        "distractors": "• B: Zamanlar terstir.\n• C: 'My brother' tekildir, 'play' olamaz (plays olmalı).\n• D: 'this Saturday' geniş zaman alamaz.\n• E: 'is playing' rutin için kullanılamaz.",
        "tip": "on Saturdays (genel rutin) $\rightarrow$ PLAYS | this Saturday (bu cumartesiye özel) $\rightarrow$ IS STUDYING."
    }
]

updated_master = new_questions + master

# Re-assign sequential IDs
for idx, q in enumerate(updated_master, 1):
    q["id"] = idx

print(f"Total questions count: {len(updated_master)}")

with open("all_questions_master.json", "w", encoding="utf-8") as f:
    json.dump(updated_master, f, ensure_ascii=False, indent=2)

print("Saved all_questions_master.json successfully!")

