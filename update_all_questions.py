# -*- coding: utf-8 -*-
import json

with open("all_60_questions.json", "r", encoding="utf-8") as f:
    existing_q = json.load(f)

# Load the exact teacher questions from the new screenshots
new_exact_teacher_questions = [
    {
        "is_exam_certain": True,
        "category": "⭐ KESİN SINAV SORULARI",
        "tag": "⭐ KESİN SINAV SORUSU • Past of Be",
        "question": "\"Were you and Ben in the same class last year?\" \"Yes, we ___.\"",
        "options": [
            {"label": "A", "text": "was"},
            {"label": "B", "text": "are"},
            {"label": "C", "text": "did"},
            {"label": "D", "text": "were"},
            {"label": "E", "text": "weren't"}
        ],
        "answer": "D",
        "teacher_feedback": "✓ Correct! Well done.\nThe subject in the answer is 'we' (you and Ben = we), which requires 'were' in the past affirmative short answer: 'Yes, we were.'",
        "translation": "\"Sen ve Ben geçen yıl aynı sınıfta mıydınız?\" \"Evet, öyleydik (aynı sınıftaydık).\"",
        "explanation": "1) Sorudaki özne 'you and Ben' (sen ve Ben) karşılık olarak 'we' (biz) şahsına dönüşür.\n2) Geçmiş zamanda 'we' çoğul öznesiyle 'To Be' fiilinin olumlu hali were dür.\n3) 'Yes' ile başlayan olumlu kısa cevapta: Yes, we were. kullanılır.",
        "distractors": "• A (was): 'was' sadece tekil şahıslarla (I, he, she, it) kullanılır; 'we' ile ASLA 'was' denmez.\n• B (are): Şimdiki zamandır; soru 'last year' (geçen yıl) diyerek geçmiş zamanı sormaktadır.\n• C (did): Soru 'To Be' fiiliyle sorulmuştur ('Were you...?'), 'did' eylem fiili sorularında gelir.\n• E (weren't): 'Yes' ile başlayan olumlu bir cevapta olumsuz ek olan 'weren't' kullanılamaz.",
        "tip": "HOCANIN KESİN SINAV SORUSU! 'you and Ben' -> 'we' demektir ve geçmiş zamanda daima WERE alır: 'Yes, we were.' (Asla 'was' veya 'are' işaretleme!)."
    },
    {
        "is_exam_certain": True,
        "category": "⭐ KESİN SINAV SORULARI",
        "tag": "⭐ HOCANIN CANLI DERSİ • Listen! & Can't",
        "question": "Listen! The neighbours ___ loud music, and I ___ sleep.",
        "options": [
            {"label": "A", "text": "play / can't"},
            {"label": "B", "text": "are playing / can't"},
            {"label": "C", "text": "are playing / don't can"},
            {"label": "D", "text": "are playing / not can"},
            {"label": "E", "text": "play / am not can"}
        ],
        "answer": "B",
        "teacher_feedback": "✓ Correct! Well done.\n\"Listen!\" means it's happening now -> are playing. After can we make the negative with can't, never don't or not.",
        "translation": "Dinle! Komşular yüksek sesle müzik çalıyorlar ve ben uyuyamıyorum.",
        "explanation": "1) 'Listen!' (Dinle!) uyarısı konuşma anını belirtir -> Present Continuous (The neighbours are playing).\n2) 'can' yardımcı fiilinin olumsuzu İngilizcede can't ile yapılır. İngilizcede ASLA 'don't can' veya 'not can' denmez!",
        "distractors": "• A: 'Listen!' varken geniş zaman (play) kullanılamaz.\n• C: 'don't can' kesinlikle dilbilgisi kural dışıdır.\n• D: 'not can' kesinlikle kural dışıdır (dersteki çeldirici tuzak!).\n• E: 'am not can' uydurma bir yapıdır.",
        "tip": "Hocanın Uyarısı: 'Listen!' -> ARE PLAYING; 'can' olumsuzu ise KESİNLİKLE 'can't' olur! 'don't can' veya 'not can' ASLA OLMAZ!"
    },
    {
        "is_exam_certain": True,
        "category": "⭐ KESİN SINAV SORULARI",
        "tag": "⭐ HOCANIN CANLI DERSİ • We were / It was",
        "question": "We ___ at the airport at 5 a.m. yesterday. It ___ empty.",
        "options": [
            {"label": "A", "text": "were / was"},
            {"label": "B", "text": "was / were"},
            {"label": "C", "text": "were / were"},
            {"label": "D", "text": "are / was"},
            {"label": "E", "text": "was / was"}
        ],
        "answer": "A",
        "teacher_feedback": "✓ Correct! Well done.\n'We' is plural and takes 'were'. 'It' (the airport) is singular and takes 'was'. Both actions are in the past ('yesterday').",
        "translation": "Biz dün sabah saat 05:00'te havalimanındaydık. Havalimanı (orası) bomboştu.",
        "explanation": "1) Birinci boşlukta 'We' (biz / çoğul) ve 'yesterday' olduğu için were gelir (We were).\n2) İkinci boşlukta 'It' (havalimanı / tekil) olduğu için was gelir (It was empty).",
        "distractors": "• B: was / were şıkları ters verilmiştir ('We was' denemez!).\n• C: 'It' tekil olduğu için 'were' alamaz.\n• D: 'yesterday' geçmiş zamandır, 'are' şimdiki zamandır.\n• E: 'We was' kural hatasıdır.",
        "tip": "Özne Eşleştirmesi: WE -> WERE | IT -> WAS. (Doğru sıralama: were / was)."
    },
    {
        "is_exam_certain": False,
        "category": "⭐ KESİN SINAV SORULARI",
        "tag": "Past of Be • We were",
        "question": "\"Were you and your sister at home yesterday morning?\" \"Yes, we ___.\"",
        "options": [
            {"label": "A", "text": "was"},
            {"label": "B", "text": "were"},
            {"label": "C", "text": "did"},
            {"label": "D", "text": "are"},
            {"label": "E", "text": "weren't"}
        ],
        "answer": "B",
        "teacher_feedback": "✓ Correct! Well done.\n'You and your sister' = we. In affirmative past short answer: 'Yes, we were.'",
        "translation": "\"Sen ve kız kardeşin dün sabah evde miydiniz?\" \"Evet, öyleydik (evdeydik).\"",
        "explanation": "Özne 'you and your sister' (sen ve kız kardeşin) yanıt verirken 'we' (biz) olur. Geçmiş zamanda 'we' ile olumlu cevapta Yes, we were. denir.",
        "distractors": "• A (was): 'we' ile was kullanılamaz.\n• C: Soru to be ile sorulmuştur, did denemez.\n• D: 'yesterday' varken şimdiki zaman 'are' gelemez.\n• E: 'Yes' cevabında olumsuzluk olamaz.",
        "tip": "Soru 'Were you and [Kişi]...?' ise cevap KESİNLİKLE 'Yes, we were' veya 'No, we weren't' olur!"
    },
    {
        "is_exam_certain": False,
        "category": "⭐ KESİN SINAV SORULARI",
        "tag": "Listen! & Can't Knocking",
        "question": "Listen! Someone ___ loudly on the front door, but I ___ open it right now.",
        "options": [
            {"label": "A", "text": "knocks / can't"},
            {"label": "B", "text": "is knocking / can't"},
            {"label": "C", "text": "is knocking / don't can"},
            {"label": "D", "text": "is knocking / not can"},
            {"label": "E", "text": "knock / am not can"}
        ],
        "answer": "B",
        "teacher_feedback": "✓ Correct! Well done.\n'Listen!' signals Present Continuous (is knocking). Negative of can is always 'can't'.",
        "translation": "Dinle! Biri ön kapıyı sertçe çalıyor, fakat şu anda açamıyorum.",
        "explanation": "'Listen!' şimdiki zamanı gerektirir (is knocking). 'can' yardımcı fiilinin olumsuzu ise daima can't dır.",
        "distractors": "• A: 'Listen!' varken knocks denemez.\n• C, D ve E: 'don't can' veya 'not can' kesinlikle İngilizcede yoktur.",
        "tip": "İkili Kalıp: is knocking / can't."
    },
    {
        "is_exam_certain": False,
        "category": "⭐ KESİN SINAV SORULARI",
        "tag": "They were / It was",
        "question": "The students ___ at the museum yesterday afternoon. It ___ very crowded.",
        "options": [
            {"label": "A", "text": "were / was"},
            {"label": "B", "text": "was / were"},
            {"label": "C", "text": "were / were"},
            {"label": "D", "text": "are / was"},
            {"label": "E", "text": "was / was"}
        ],
        "answer": "A",
        "teacher_feedback": "✓ Correct! Well done.\n'The students' is plural (they), taking 'were'. 'It' (the museum) is singular, taking 'was'.",
        "translation": "Öğrenciler dün öğleden sonra müzedeydiler. Müze çok kalabalıktı.",
        "explanation": "Öğrenciler çoğuldur (They) -> were. Müze tekildir (It) -> was. Cevap: were / was.",
        "distractors": "• B: Çoğul özneye 'was' konmuştur.\n• C: 'It' tekildir, were alamaz.\n• D: 'yesterday' geçmiş zamandır.\n• E: Öğrencilere 'was' denemez.",
        "tip": "The students -> WERE | It -> WAS."
    }
]

# Prepend the new ones at the very beginning
all_combined = new_exact_teacher_questions + existing_q

# Re-assign sequential IDs from 1 to N
for idx, q in enumerate(all_combined, 1):
    q["id"] = idx

print(f"Total compiled questions: {len(all_combined)}")

with open("all_questions_final.json", "w", encoding="utf-8") as f:
    json.dump(all_combined, f, ensure_ascii=False, indent=2)

print("Saved all_questions_final.json successfully!")
