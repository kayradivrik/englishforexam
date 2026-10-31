# -*- coding: utf-8 -*-
import json

with open("all_questions_master.json", "r", encoding="utf-8") as f:
    master_questions = json.load(f)

# The 5 exact new questions from the Word document screenshot
new_doc_questions = [
    {
        "is_official_exam": True,
        "is_exam_certain": True,
        "category": "🏆 HOCANIN RESMİ SINAV BELGESİ",
        "tag": "⭐ RESMİ WORD BELGESİ • Soru 16 • I was",
        "question": "I ___ at the library yesterday afternoon.",
        "options": [
            {"label": "A", "text": "were"},
            {"label": "B", "text": "was"},
            {"label": "C", "text": "am"},
            {"label": "D", "text": "are"},
            {"label": "E", "text": "be"}
        ],
        "answer": "B",
        "teacher_feedback": "✓ Correct! Well done.\nSubject 'I' in the past tense ('yesterday afternoon') takes 'was': I was at the library.",
        "translation": "Dün öğleden sonra kütüphanedeydim.",
        "explanation": "'I' öznesi geçmiş zamanda ('yesterday afternoon') 'To Be' fiilinde daima **was** alır: 'I was at the library yesterday afternoon.'",
        "distractors": "• A (were): Çoğul özneler (you/we/they) içindir; 'I were' denemez.\n• C ve D (am / are): Şimdiki zamandır; 'yesterday' ile kullanılamaz.\n• E (be): Çekimlenmemiştir.",
        "tip": "I + yesterday $\rightarrow$ WAS."
    },
    {
        "is_official_exam": True,
        "is_exam_certain": True,
        "category": "🏆 HOCANIN RESMİ SINAV BELGESİ",
        "tag": "⭐ RESMİ WORD BELGESİ • Soru 17 • Your friends were",
        "question": "Where ___ your friends last Saturday?",
        "options": [
            {"label": "A", "text": "was"},
            {"label": "B", "text": "is"},
            {"label": "C", "text": "are"},
            {"label": "D", "text": "were"},
            {"label": "E", "text": "be"}
        ],
        "answer": "D",
        "teacher_feedback": "✓ Correct! Well done.\n'Your friends' is plural (they), requiring 'were' in the past tense: Where were your friends...?",
        "translation": "Geçen cumartesi arkadaşların neredeydiler?",
        "explanation": "Öznemiz 'your friends' (arkadaşların) çoğuldur (-s takısına dikkat, zamiri 'they'). 'last Saturday' geçmiş zaman olduğuna göre çoğul geçmiş zaman yardımcı fiili **were** kullanılır: 'Where were your friends last Saturday?'",
        "distractors": "• A (was): 'was' tekil özneler içindir; 'friends' çoğul olduğu için was YANLIŞTIR.\n• B ve C (is / are): 'last Saturday' geçmiş zamandır, şimdiki zaman olamaz.\n• E (be): Çekimlenmemiş fiildir.",
        "tip": "HOCANIN BÜYÜK TUZAĞI: 'your' kelimesine aldanma! Özne 'friends' (çoğul - onlar) olduğu için WAS değil WERE gelir!"
    },
    {
        "is_official_exam": True,
        "is_exam_certain": True,
        "category": "🏆 HOCANIN RESMİ SINAV BELGESİ",
        "tag": "⭐ RESMİ WORD BELGESİ • Soru 18 • She wasn't",
        "question": "Choose the correct sentence.",
        "options": [
            {"label": "A", "text": "She weren't tired."},
            {"label": "B", "text": "She not was tired."},
            {"label": "C", "text": "She no was tired."},
            {"label": "D", "text": "She wasn't tired."},
            {"label": "E", "text": "She isn't tired yesterday."}
        ],
        "answer": "D",
        "teacher_feedback": "✓ Correct! Well done.\nThird person singular past negative of 'be' is 'wasn't': She wasn't tired.",
        "translation": "Doğru cümleyi seçiniz. $\rightarrow$ \"O yorgun değildi.\"",
        "explanation": "'She' 3. tekil şahıstır. Geçmiş zaman olumsuz 'To Be' biçimi **wasn't** (was not) dır: 'She wasn't tired.'",
        "distractors": "• A: 'She' tekildir, 'weren't' çoğuldur.\n• B ve C: 'not was' veya 'no was' İngilizcede tamamen kural dışıdır.\n• E: 'yesterday' varken şimdiki zaman 'isn't' kullanılamaz.",
        "tip": "She $\rightarrow$ WASN'T tired."
    },
    {
        "is_official_exam": True,
        "is_exam_certain": True,
        "category": "🏆 HOCANIN RESMİ SINAV BELGESİ",
        "tag": "⭐ RESMİ WORD BELGESİ • Soru 19 • Was Alex",
        "question": "___ Alex at work yesterday? Yes, he was.",
        "options": [
            {"label": "A", "text": "Were"},
            {"label": "B", "text": "Are"},
            {"label": "C", "text": "Was"},
            {"label": "D", "text": "Is"},
            {"label": "E", "text": "Be"}
        ],
        "answer": "C",
        "teacher_feedback": "✓ Correct! Well done.\nAlex is singular (he) and time is past ('yesterday'). Confirmed by the answer 'Yes, he was': Was Alex at work...?",
        "translation": "Alex dün işte miydi? Evet, öyleydi (işteydi).",
        "explanation": "'Alex' tekil şahıstır (he). 'yesterday' geçmiş zamandır. Ayrıca cümlenin devamındaki cevap 'Yes, he was' diyerek sorunun **Was** ile başladığını teyit eder: 'Was Alex at work yesterday?'",
        "distractors": "• A (Were): Alex tekildir, Were alamaz.\n• B ve D (Are / Is): 'yesterday' geçmiş zamandır.\n• E (Be): Soru yardımcı fiil olarak 'Be' ile başlamaz.",
        "tip": "Cevapta 'Yes, he WAS' varsa soru da kesinlikle WAS ile başlar: WAS Alex...?"
    },
    {
        "id": 20,
        "is_official_exam": True,
        "is_exam_certain": True,
        "category": "🏆 HOCANIN RESMİ SINAV BELGESİ",
        "tag": "⭐ RESMİ WORD BELGESİ • Soru 20 • They were at the café",
        "question": "They ___ at the café last Sunday.",
        "options": [
            {"label": "A", "text": "was"},
            {"label": "B", "text": "are"},
            {"label": "C", "text": "am"},
            {"label": "D", "text": "were"},
            {"label": "E", "text": "is"}
        ],
        "answer": "D",
        "teacher_feedback": "✓ Correct! Well done.\n'They' is plural and 'last Sunday' is in the past -> were. They were at the café last Sunday.",
        "translation": "Onlar geçen pazar kafedeydiler.",
        "explanation": "'They' çoğuldur. 'last Sunday' geçmiş zaman olduğuna göre çoğul geçmiş zaman hali **were** dür: 'They were at the café last Sunday.'",
        "distractors": "• A (was): Tekiller içindir; 'They was' büyük hatadır.\n• B ve E (are / is): Şimdiki zamandır; 'last Sunday' ile kullanılamaz.\n• C (am): Sadece 'I' içindir.",
        "tip": "They + last Sunday $\rightarrow$ WERE."
    }
]

# Insert right after official 20 (or at the top of official category)
# Let's ensure these 5 questions are part of the top official section!
all_updated = new_doc_questions + master_questions

# Re-assign clean IDs
for idx, q in enumerate(all_updated, 1):
    q["id"] = idx

print(f"Total updated questions: {len(all_updated)}")

with open("all_questions_master.json", "w", encoding="utf-8") as f:
    json.dump(all_updated, f, ensure_ascii=False, indent=2)

print("Saved all_questions_master.json successfully!")

