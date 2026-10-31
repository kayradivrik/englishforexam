# -*- coding: utf-8 -*-
import json

with open("all_questions_final.json", "r", encoding="utf-8") as f:
    existing = json.load(f)

# The new exact questions from the user's latest screenshots
new_batch = [
    {
        "is_exam_certain": True,
        "category": "⭐ KESİN SINAV SORULARI",
        "tag": "⭐ CANLI DERS • Weather was / Friends were",
        "question": "Last weekend the weather ___ great, so my friends and I ___ at the park.",
        "options": [
            {"label": "A", "text": "were / was"},
            {"label": "B", "text": "was / was"},
            {"label": "C", "text": "was / were"},
            {"label": "D", "text": "were / were"},
            {"label": "E", "text": "is / were"}
        ],
        "answer": "C",
        "teacher_feedback": "✓ Correct! Well done.\n'The weather' is uncountable/singular (it) -> was. 'My friends and I' = we (plural) -> were. Both happened in the past (last weekend).",
        "translation": "Geçen hafta sonu hava harikaydı, bu yüzden arkadaşlarım ve ben parktaydık.",
        "explanation": "1) 'the weather' (hava durumu) tekil ve sayılamaz bir öznedir (it) -> geçmiş zaman hali **was** dır.\n2) 'my friends and I' (arkadaşlarım ve ben) 'we' (biz / çoğul) anlamına gelir -> geçmiş zaman hali **were** dür.\nDoğru sıralama: **was / were**.",
        "distractors": "• A: Şıklar terstir ('weather were' denemez!).\n• B: 'my friends and I' çoğuldur, 'was' alamaz.\n• D: 'weather were' yanlıştır.\n• E: 'last weekend' geçmiş zamandır, 'is' şimdiki zamandır.",
        "tip": "Hocanın Tuzağı: The weather -> WAS | My friends and I -> WERE (was / were)."
    },
    {
        "is_exam_certain": True,
        "category": "⭐ KESİN SINAV SORULARI",
        "tag": "⭐ CANLI DERS • Which is NOT correct?",
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
        "distractors": "• A: She isn't working today (Doğru şimdiki zaman olumsuzu).\n• B: They don't work on Sundays (Doğru geniş zaman olumsuzu).\n• C: I wasn't at work (Doğru geçmiş zaman to be).\n• D: We aren't at work (Doğru şimdiki zaman to be).",
        "tip": "Hocanın Canlı Ders Açıklaması: 'isn't' ile yalın fiil 'work' YAN YANA GELEMEZ! Doğrusu 'isn't working' olmalıdır."
    },
    {
        "is_exam_certain": True,
        "category": "⭐ KESİN SINAV SORULARI",
        "tag": "⭐ CANLI DERS • Habit Does / doesn't",
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
        "explanation": "1) 'usually' rutin/alışkanlık gösterir ve eylem fiili 'walk' vardır -> Geniş Zaman.\n2) 'she' öznesiyle soru: **Does she usually walk...?**\n3) Olumsuz kısa cevap: **No, she doesn't.**",
        "distractors": "• A: 'walk' eylem fiilidir, 'Is she walk' denemez.\n• B: 'she' öznesiyle 'Do' kullanılamaz.\n• D: Does ile sorulan soruya isn't ile cevap verilmez.\n• E: 'Is she walk' yanlıştır.",
        "tip": "usually + eylem fiili (walk) $\rightarrow$ DOES she walk...? / No, she DOESN'T."
    },
    {
        "is_exam_certain": True,
        "category": "⭐ KESİN SINAV SORULARI",
        "tag": "⭐ CANLI DERS • Plural Subject Share/Have",
        "question": "My brother and I ___ a room, but our parents ___ their own room.",
        "options": [
            {"label": "A", "text": "shares / has"},
            {"label": "B", "text": "share / have"},
            {"label": "C", "text": "share / has"},
            {"label": "D", "text": "are sharing / have"},
            {"label": "E", "text": "shares / have"}
        ],
        "answer": "B",
        "teacher_feedback": "✓ Correct! Well done.\n'My brother and I' = we (plural) -> share (base verb). 'Our parents' = they (plural) -> have (base verb). Neither takes -s.",
        "translation": "Erkek kardeşimle ben bir odayı paylaşıyoruz, fakat anne babamızın kendi odaları var.",
        "explanation": "1) 'My brother and I' (kardeşim ve ben) = 'we' (biz / çoğul) -> fiil yalın kalır: **share**.\n2) 'our parents' (anne babamız) = 'they' (onlar / çoğul) -> fiil yalın kalır: **have** (has tekiller içindir).\nİki fiil de çoğul özneye bağlı olduğu için -s takısı ALMAZ: **share / have**.",
        "distractors": "• A: İki fiile de tekil takısı (-s ve has) takılmıştır.\n• C: 'parents' çoğuldur, 'has' alamaz.\n• D: Rutin durumlar Simple Present gerektirir.\n• E: 'My brother and I' çoğuldur, 'shares' alamaz.",
        "tip": "Öznede 'and I' veya 'parents' varsa özne ÇOĞULDUR $\rightarrow$ fiil yalın kalır (SHARE / HAVE)."
    },
    # Extra high-yield twins
    {
        "is_exam_certain": False,
        "category": "⭐ KESİN SINAV SORULARI",
        "tag": "Traffic was / We were",
        "question": "Yesterday the morning traffic ___ terrible, so my colleagues and I ___ late for work.",
        "options": [
            {"label": "A", "text": "was / were"},
            {"label": "B", "text": "were / was"},
            {"label": "C", "text": "was / was"},
            {"label": "D", "text": "were / were"},
            {"label": "E", "text": "is / were"}
        ],
        "answer": "A",
        "teacher_feedback": "✓ Correct! Well done.\n'The traffic' is uncountable (it) -> was. 'My colleagues and I' = we (plural) -> were.",
        "translation": "Dün sabah trafiği berbattı, bu yüzden meslektaşlarım ve ben işe geç kaldık.",
        "explanation": "'traffic' tekil/sayılamaz -> was. 'my colleagues and I' (we) -> were: **was / were**.",
        "distractors": "• B, C, D ve E seçenekleri tekil/çoğul kuralına aykırıdır.",
        "tip": "The traffic $\rightarrow$ WAS | We $\rightarrow$ WERE."
    },
    {
        "is_exam_certain": False,
        "category": "⭐ KESİN SINAV SORULARI",
        "tag": "Which sentence is NOT correct?",
        "question": "Which sentence is NOT correct?",
        "options": [
            {"label": "A", "text": "He doesn't likes hot coffee."},
            {"label": "B", "text": "She teaches English at university."},
            {"label": "C", "text": "They were at home last night."},
            {"label": "D", "text": "We are studying for the exam right now."},
            {"label": "E", "text": "I don't live in Madrid."}
        ],
        "answer": "A",
        "teacher_feedback": "✓ Correct! Well done.\nIn negative present simple, we use doesn't + base verb: He doesn't like. \"Doesn't likes\" is wrong.",
        "translation": "Hangi cümle YANLIŞTIR? -> 'He doesn't likes hot coffee.'",
        "explanation": "'doesn't' sonrasında gelen fiil kesinlikle yalın olmalıdır ('doesn't like'). 'doesn't likes' dilbilgisi hatasıdır.",
        "distractors": "• B, C, D ve E cümleleri tamamen doğrudur.",
        "tip": "Hocanın favori tuzağı: 'doesn't' varsa fiilde -s takısı OLMAZ!"
    }
]

# Merge: Put these new questions right at the front
combined = new_batch + existing

# Re-assign sequential IDs
for idx, q in enumerate(combined, 1):
    q["id"] = idx

print(f"Total updated questions count: {len(combined)}")

with open("all_questions_final.json", "w", encoding="utf-8") as f:
    json.dump(combined, f, ensure_ascii=False, indent=2)

print("Updated all_questions_final.json successfully!")

