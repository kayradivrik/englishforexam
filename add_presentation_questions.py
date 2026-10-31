# -*- coding: utf-8 -*-
"""
Add New Questions from SmartChoice1_Challenge_Quiz.pptx:
1. Question 2: Which sentence is correct? -> She is never late for work.
2. Question 4: "___ your sister like spicy food?" "No, she ___." -> Does / doesn't
3. Question 5: There ___ any milk in the fridge, but there ___ some eggs. -> isn't / are
4. Question 6: My birthday is ___ March, ___ the 14th. -> in / on
5. Question 7: Please don't call me now. I ___ dinner for my family. -> am making
6. Slide 4: Look! The children ___ in the garden. They usually ___ tennis. -> are playing / play
"""

import json

with open("all_questions_master.json", "r", encoding="utf-8") as f:
    master_questions = json.load(f)

new_ppt_questions = [
    {
        "is_official_exam": True,
        "is_exam_certain": True,
        "category": "🏆 HOCANIN SLAYT CHALLENGE SORULARI",
        "tag": "⭐ SLAYT • Q6 • Prepositions IN / ON",
        "question": "My birthday is ___ March, ___ the 14th.",
        "options": [
            {"label": "A", "text": "in / on"},
            {"label": "B", "text": "on / in"},
            {"label": "C", "text": "at / on"},
            {"label": "D", "text": "in / at"},
            {"label": "E", "text": "on / on"}
        ],
        "answer": "A",
        "teacher_feedback": "✓ Correct! Well done.\nWe use 'in' for months alone (in March) and 'on' for specific dates and days (on the 14th).",
        "translation": "Benim doğum günüm mart ayında, ayın 14'ündedir.",
        "explanation": "Zaman Edatları Altın Kuralı:\n1) Aylar tek başına söylenirken başına **IN** gelir: 'in March' (Martta).\n2) Ayın günü / belirli bir tarih söylenirken başına **ON** gelir: 'on the 14th' (14'ünde).\nBu yüzden doğru eşleştirme: **in / on**.",
        "distractors": "• B: Şıklar terstir ('on March, in the 14th' kural dışıdır).\n• C: 'at' saatler içindir (at 10:15); ay için kullanılamaz.\n• D: Tarihler için 'at' değil 'on' kullanılır.\n• E: Aylar için 'on' değil 'in' kullanılır.",
        "tip": "HOCANIN EN ÇOK SEVDİĞİ EDAT KURALI: Sadece ay varsa -> IN (in March). Ayın günü / tarih varsa -> ON (on the 14th). Saat varsa -> AT (at 10:15)."
    },
    {
        "is_official_exam": True,
        "is_exam_certain": True,
        "category": "🏆 HOCANIN SLAYT CHALLENGE SORULARI",
        "tag": "⭐ SLAYT • Q5 • There isn't / There are",
        "question": "There ___ any milk in the fridge, but there ___ some eggs.",
        "options": [
            {"label": "A", "text": "aren't / is"},
            {"label": "B", "text": "isn't / is"},
            {"label": "C", "text": "aren't / are"},
            {"label": "D", "text": "isn't / are"},
            {"label": "E", "text": "isn't / be"}
        ],
        "answer": "D",
        "teacher_feedback": "✓ Correct! Well done.\n'Milk' is uncountable (singular) and takes 'isn't' with 'any'. 'Eggs' is plural and takes 'are' with 'some'.",
        "translation": "Buzdolabında hiç süt yok, fakat biraz yumurta var.",
        "explanation": "1) 'milk' (süt) sayılamaz tekil bir isimdir; olumsuzda 'any' ile kullanılırken tekil 'To Be' gerektirir: **There isn't any milk**.\n2) 'eggs' (yumurtalar) sayılabilen çoğul bir isimdir; olumlu 'some' ile çoğul 'To Be' gerektirir: **there are some eggs**.\nDoğru sıralama: **isn't / are**.",
        "distractors": "• A: 'milk' sayılamaz, çoğul 'aren't' alamaz.\n• B: 'eggs' çoğuldur, tekil 'is' alamaz.\n• C: 'milk' için 'aren't' denemez.\n• E: 'be' çekimlenmemiştir.",
        "tip": "Süt, su, çay (sayılamaz) $\rightarrow$ IS / ISN'T | Yumurtalar, elmalar (çoğul -s) $\rightarrow$ ARE / AREN'T."
    },
    {
        "is_official_exam": True,
        "is_exam_certain": True,
        "category": "🏆 HOCANIN SLAYT CHALLENGE SORULARI",
        "tag": "⭐ SLAYT • Q4 • Does your sister like?",
        "question": "\"___ your sister like spicy food?\" \"No, she ___.\"",
        "options": [
            {"label": "A", "text": "Do / don't"},
            {"label": "B", "text": "Does / doesn't"},
            {"label": "C", "text": "Is / isn't"},
            {"label": "D", "text": "Does / isn't"},
            {"label": "E", "text": "Did / didn't"}
        ],
        "answer": "B",
        "teacher_feedback": "✓ Correct! Well done.\n'Your sister' is singular (she). With main verb 'like', we use 'Does' in question and 'doesn't' in short answer.",
        "translation": "\"Kız kardeşin baharatlı yemek sever mi?\" \"Hayır, sevmez.\"",
        "explanation": "1) 'your sister' tekil 3. şahıstır (she).\n2) Cümlede 'like' (sevmek) eylem fiili vardır. Geniş zamanda tekil öznelerle soru **Does** ile sorulur.\n3) Olumsuz kısa cevap **No, she doesn't** şeklinde verilir.\nDoğru sıralama: **Does / doesn't**.",
        "distractors": "• A: 'your sister' (she) için 'Do' kullanılamaz.\n• C: 'like' eylem fiilidir, 'Is she like' denemez.\n• D: Does ile sorulan soruya 'isn't' ile cevap verilmez.\n• E: Genel beğeniler geniş zamanla sorulur.",
        "tip": "Tekil şahıs (sister/brother) + LIKE $\rightarrow$ DOES ... like? / No, she DOESN'T."
    },
    {
        "is_official_exam": True,
        "is_exam_certain": True,
        "category": "🏆 HOCANIN SLAYT CHALLENGE SORULARI",
        "tag": "⭐ SLAYT • Q7 • Don't call now am making",
        "question": "Please don't call me now. I ___ dinner for my family.",
        "options": [
            {"label": "A", "text": "make"},
            {"label": "B", "text": "makes"},
            {"label": "C", "text": "am making"},
            {"label": "D", "text": "making"},
            {"label": "E", "text": "am make"}
        ],
        "answer": "C",
        "teacher_feedback": "✓ Correct! Well done.\n'Please don't call me now' signals an action in progress right now (Present Continuous: am making).",
        "translation": "Lütfen beni şimdi arama. Ailem için akşam yemeği hazırlıyorum/yapıyorum.",
        "explanation": "'now' (şimdi) ve 'don't call me' uyarısı konuşma anını anlatır. 'I' öznesi için Present Continuous biçimi **am making** dir.",
        "distractors": "• A ve B: Geniş zamandır; konuşma anını anlatamaz.\n• D: 'am' yardımcı fiili eksiktir.\n• E: 'am make' dilbilgisi hatasıdır.",
        "tip": "now / right now $\rightarrow$ AM / IS / ARE + V-ING (I am making)."
    },
    {
        "is_official_exam": True,
        "is_exam_certain": True,
        "category": "🏆 HOCANIN SLAYT CHALLENGE SORULARI",
        "tag": "⭐ SLAYT • Q2 • She is never late",
        "question": "Which sentence is correct?",
        "options": [
            {"label": "A", "text": "She is never late for work."},
            {"label": "B", "text": "She never is late for work."},
            {"label": "C", "text": "She is late never for work."},
            {"label": "D", "text": "Never she is late for work."},
            {"label": "E", "text": "She does never late for work."}
        ],
        "answer": "A",
        "teacher_feedback": "✓ Correct! Well done.\nFrequency adverbs go AFTER the verb 'be': Subject + is + never + adjective.",
        "translation": "O işe asla geç kalmaz.",
        "explanation": "Sıklık zarfları 'to be' (am/is/are) fiilinden **SONRA** gelir: She + **is** + **never** + late for work.",
        "distractors": "• B: 'never' be fiilinden önceye konmuştur (yanlış).\n• C: Sıfattan sonraya konmuştur.\n• D: Cümle başına konmuştur.\n• E: 'late' sıfattır, 'does' ile birleşmez.",
        "tip": "To Be fiilinden SONRA: is NEVER / are ALWAYS / am USUALLY."
    },
    {
        "is_official_exam": True,
        "is_exam_certain": True,
        "category": "🏆 HOCANIN SLAYT CHALLENGE SORULARI",
        "tag": "⭐ SLAYT • Q3 • Look! vs Usually",
        "question": "Look! The children ___ in the garden. They usually ___ tennis on Saturdays.",
        "options": [
            {"label": "A", "text": "are playing / play"},
            {"label": "B", "text": "play / are playing"},
            {"label": "C", "text": "are playing / plays"},
            {"label": "D", "text": "plays / are playing"},
            {"label": "E", "text": "is playing / play"}
        ],
        "answer": "A",
        "teacher_feedback": "✓ Correct! Well done.\n'Look!' = right now (are playing). 'usually' with plural subject 'they' = routine base verb (play).",
        "translation": "Bak! Çocuklar bahçede oynuyorlar. Genellikle cumartesi günleri tenis oynarlar.",
        "explanation": "1) 'Look!' konuşma anını anlatır $\rightarrow$ **are playing**.\n2) 'usually' rutin alışkanlığı anlatır ve 'they' çoğul öznesinde fiil yalın kalır $\rightarrow$ **play**.\nSıralama: **are playing / play**.",
        "distractors": "• B: Zamanlar terstir.\n• C: 'they' çoğuldur, 'plays' alamaz.\n• D: 'children' çoğuldur, 'plays' alamaz.\n• E: 'children' çoğuldur, 'is playing' alamaz.",
        "tip": "Look! $\rightarrow$ are playing | usually + they $\rightarrow$ play."
    }
]

# Merge into master: Insert right at the top of the Slide Challenge category
updated_master = new_ppt_questions + master_questions

# Re-assign sequential IDs
for idx, q in enumerate(updated_master, 1):
    q["id"] = idx

print(f"Total master questions count: {len(updated_master)}")

with open("all_questions_master.json", "w", encoding="utf-8") as f:
    json.dump(updated_master, f, ensure_ascii=False, indent=2)

print("Saved all_questions_master.json successfully!")

