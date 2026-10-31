# -*- coding: utf-8 -*-
"""
Add Slide 11 & Slide 9 questions from teacher's live presentation SmartChoice1_Challenge_Quiz.pptx
"""
import json

with open("all_questions_master.json", "r", encoding="utf-8") as f:
    master = json.load(f)

new_questions = [
    {
        "is_official_exam": True,
        "is_exam_certain": True,
        "category": "🏆 HOCANIN SLAYT CHALLENGE SORULARI",
        "tag": "⭐ SLAYT • Q11 • Which sentence is NOT correct?",
        "question": "Which sentence is NOT correct?",
        "options": [
            {"label": "A", "text": "She don't have a car."},
            {"label": "B", "text": "He doesn't like tea."},
            {"label": "C", "text": "They aren't studying now."},
            {"label": "D", "text": "I wasn't at school."},
            {"label": "E", "text": "We weren't happy."}
        ],
        "answer": "A",
        "teacher_feedback": "✓ Correct! Well done.\nPresent simple, third person singular negative requires 'doesn't + base verb' (She doesn't have a car). 'Don't' cannot be used with 'she'.",
        "translation": "Hangi cümle doğru DEĞİLDİR (yanlıştır)?",
        "explanation": "Dilbilgisi Kuralı:\n• Geniş zamanda (Present Simple) 3. tekil şahıslar (He / She / It) olumsuz cümle yaparken **doesn't** alır: **She doesn't have a car**.\n• 'don't' sadece I / You / We / They özneleriyle kullanılır. Bu yüzden **'She don't have a car'** dilbilgisi açısından KESİNLİKLE HATALIDIR (NOT correct).",
        "distractors": "• B: 'He doesn't like tea.' -> %100 Doğrudur (He + doesn't + yalın fiil).\n• C: 'They aren't studying now.' -> %100 Doğrudur (Şimdiki zaman olumsuz).\n• D: 'I wasn't at school.' -> %100 Doğrudur (I + was not).\n• E: 'We weren't happy.' -> %100 Doğrudur (We + were not).",
        "tip": "HOCANIN EN ÇOK SEVDİĞİ SINAV TUZAĞI: He/She/It asla 'don't' alamaz! Daima DOESN'T alır!"
    },
    {
        "is_official_exam": True,
        "is_exam_certain": True,
        "category": "🏆 HOCANIN SLAYT CHALLENGE SORULARI",
        "tag": "⭐ SLAYT • Q9 • Where were your parents?",
        "question": "Where ___ your parents at 9 p.m. last night? They ___ at home.",
        "options": [
            {"label": "A", "text": "was / were"},
            {"label": "B", "text": "were / was"},
            {"label": "C", "text": "were / were"},
            {"label": "D", "text": "are / were"},
            {"label": "E", "text": "was / was"}
        ],
        "answer": "C",
        "teacher_feedback": "✓ Correct! Well done.\n'Your parents' is plural (they), so it takes 'were' in the question. In the answer, 'They' also takes 'were'.",
        "translation": "Dün gece saat 21:00'de anne baban neredeydi? Onlar evdeydi.",
        "explanation": "Past of To Be (Was / Were) Kuralı:\n1) 'your parents' (anne ve baban) çoğuldur ('they' yerine geçer). Bu yüzden geçmiş zaman sorusunda **were** alır: **Where were your parents...?**\n2) İkinci cümlede özne açıkça 'They' (onlar) olduğu için yine **were** gelir: **They were at home.**\nDoğru eşleştirme: **were / were**.",
        "distractors": "• A: 'your parents' tekil sanılıp 'was' konursa elenirsiniz (parents çoğuldur!).\n• B: 'They was' diye bir kural İngilizcede yoktur.\n• D: 'last night' geçmiş zamandır, 'are' şimdiki zamandır kullanılamaz.\n• E: Çoğul öznelerle 'was' kullanılamaz.",
        "tip": "'your' kelimesine aldanma, yanındaki isme bak! 'parentS', 'friendS' çoğuldur -> WERE alır!"
    }
]

# Insert right after Slide Challenge questions (or at top of that category)
updated_master = new_questions + master

# Re-assign sequential IDs
for idx, q in enumerate(updated_master, 1):
    q["id"] = idx

print(f"Total questions count: {len(updated_master)}")

with open("all_questions_master.json", "w", encoding="utf-8") as f:
    json.dump(updated_master, f, ensure_ascii=False, indent=2)

print("Saved all_questions_master.json successfully!")

