# -*- coding: utf-8 -*-
"""
Add 10 Vocabulary and Reading questions from Oxford Learner's Bookshelf (Smart Choice 1, Page 39)
"""
import json

with open("all_questions_master.json", "r", encoding="utf-8") as f:
    master = json.load(f)

new_questions = [
    {
        "is_official_exam": True,
        "is_exam_certain": True,
        "category": "📘 OXFORD KİTAP SORULARI (PAGE 39)",
        "tag": "📘 Oxford Sayfa 39 • Dan works in a hospital",
        "question": "Dan works in a hospital. He's ___.",
        "options": [
            {"label": "A", "text": "a doctor"},
            {"label": "B", "text": "a chef"},
            {"label": "C", "text": "an architect"},
            {"label": "D", "text": "a police officer"},
            {"label": "E", "text": "a pilot"}
        ],
        "answer": "A",
        "teacher_feedback": "✓ Correct! Well done.\nA person who works in a hospital is 'a doctor'.",
        "translation": "Dan bir hastanede çalışıyor. O bir doktordur.",
        "explanation": "Meslekler & Çalışma Yerleri Eşleştirmesi:\n• 'hospital' (hastane) $\rightarrow$ **a doctor** (doktor) veya a nurse (hemşire).\n• 'chef' restoranda, 'architect' ofiste, 'police officer' polis merkezinde/sokakta, 'pilot' uçakta çalışır.",
        "distractors": "• B: 'chef' aşçıdır, hastanede değil restoranda çalışır.\n• C: 'architect' mimardır.\n• D: 'police officer' polis memurudur.\n• E: 'pilot' uçak kullanır.",
        "tip": "Hastanede çalışan $\rightarrow$ DOCTOR | Restoranda çalışan $\rightarrow$ CHEF | Okulda okuyan $\rightarrow$ STUDENT."
    },
    {
        "is_official_exam": True,
        "is_exam_certain": True,
        "category": "📘 OXFORD KİTAP SORULARI (PAGE 39)",
        "tag": "📘 Oxford Sayfa 39 • She studies at University",
        "question": "Mia is ___. She studies at New York University.",
        "options": [
            {"label": "A", "text": "a teacher"},
            {"label": "B", "text": "a pilot"},
            {"label": "C", "text": "a student"},
            {"label": "D", "text": "an actor"},
            {"label": "E", "text": "an engineer"}
        ],
        "answer": "C",
        "teacher_feedback": "✓ Correct! Well done.\nSomeone who studies at a university is 'a student'.",
        "translation": "Mia bir öğrencidir. New York Üniversitesinde okuyor/öğrenim görüyor.",
        "explanation": "Cümledeki İpucu:\n• 'She studies at New York University' (Üniversitede okuyor / ders çalışıyor) ifadesi Mia'nın bir **öğrenci (student)** olduğunu gösterir.",
        "distractors": "• A: 'teacher' öğretmenlik yapar (teaches).\n• B: 'pilot' uçak uçurur.\n• D: 'actor' tiyatro/film oyuncusudur.\n• E: 'engineer' mühendistir.",
        "tip": "'studies at school/university' $\rightarrow$ STUDENT | 'teaches at school' $\rightarrow$ TEACHER."
    },
    {
        "is_official_exam": True,
        "is_exam_certain": True,
        "category": "📘 OXFORD KİTAP SORULARI (PAGE 39)",
        "tag": "📘 Oxford Sayfa 39 • What's your favorite food?",
        "question": "What's your ___ food?",
        "options": [
            {"label": "A", "text": "like"},
            {"label": "B", "text": "love"},
            {"label": "C", "text": "favorite"},
            {"label": "D", "text": "hate"},
            {"label": "E", "text": "drink"}
        ],
        "answer": "C",
        "teacher_feedback": "✓ Correct! Well done.\n'Favorite' is the adjective used in the standard question: 'What's your favorite food?'.",
        "translation": "En sevdiğin yemek nedir?",
        "explanation": "Kalıp İfade:\nİngilizcede birinin 'en sevdiği' şeyi sormak için **'favorite'** sıfatı kullanılır: **What's your favorite food / color / movie?**\n'like' ve 'love' fiildir, 'your like food' diye bir tamlama yapılamaz.",
        "distractors": "• A: 'like' fiildir; 'What is your like' denemez.\n• B: 'love' fiildir.\n• D: 'hate' nefret etmektir.\n• E: 'drink' içecektir; 'drink food' denemez.",
        "tip": "İsmin önünde 'en sevilen' demek için daima FAVORITE kullanılır (favorite food / favorite movie)."
    },
    {
        "is_official_exam": True,
        "is_exam_certain": True,
        "category": "📘 OXFORD KİTAP SORULARI (PAGE 39)",
        "tag": "📘 Oxford Sayfa 39 • Are you a police officer?",
        "question": "Are you a ___ officer?",
        "options": [
            {"label": "A", "text": "movie"},
            {"label": "B", "text": "taxi"},
            {"label": "C", "text": "police"},
            {"label": "D", "text": "soccer"},
            {"label": "E", "text": "bank"}
        ],
        "answer": "C",
        "teacher_feedback": "✓ Correct! Well done.\nThe compound noun for the profession is 'police officer'.",
        "translation": "Sen bir polis memuru musun?",
        "explanation": "Bileşik İsim (Meslek Adı):\nİngilizcede polis memuru tamlaması **'police officer'** dır. 'movie officer' veya 'taxi officer' gibi kavramlar yoktur.",
        "distractors": "• A: 'movie' filmdir.\n• B: 'taxi' taksidir (taxi driver denir).\n• D: 'soccer' futboldur (soccer player denir).\n• E: 'bank' bankadır (bank clerk denir).",
        "tip": "OFFICER kelimesiyle birleşen meslek: POLICE OFFICER (polis memuru)."
    },
    {
        "is_official_exam": True,
        "is_exam_certain": True,
        "category": "📘 OXFORD KİTAP SORULARI (PAGE 39)",
        "tag": "📘 Oxford Sayfa 39 • Jin Park is from Seoul",
        "question": "Jin Park is ___ Seoul, South Korea, but he lives in Los Angeles.",
        "options": [
            {"label": "A", "text": "at"},
            {"label": "B", "text": "to"},
            {"label": "C", "text": "from"},
            {"label": "D", "text": "with"},
            {"label": "E", "text": "on"}
        ],
        "answer": "C",
        "teacher_feedback": "✓ Correct! Well done.\nWe use 'to be from' to state someone's origin/hometown: 'is from Seoul'.",
        "translation": "Jin Park Güney Kore'nin Seul şehrindendir (Seullüdür), fakat Los Angeles'ta yaşamaktadır.",
        "explanation": "Memleket / Köken Belirtme Kuralı:\nBir kişinin nereli olduğunu söylerken **'be from'** kalıbı kullanılır: **He is from Seoul** (O Seullüdür).",
        "distractors": "• A: 'at' belirli nokta konumlar içindir.\n• B: 'to' yönelme bildirir (go to).\n• D: 'with' ile demektir.\n• E: 'on' üstünde demektir.",
        "tip": "Nerelisin? sorusu 'Where are you FROM?' -> Cevabı 'I am FROM Turkey / Seoul'."
    },
    {
        "is_official_exam": True,
        "is_exam_certain": True,
        "category": "📘 OXFORD KİTAP SORULARI (PAGE 39)",
        "tag": "📘 Oxford Sayfa 39 • lives in Los Angeles",
        "question": "Jin Park is from Seoul, South Korea, but he lives ___ Los Angeles.",
        "options": [
            {"label": "A", "text": "at"},
            {"label": "B", "text": "with"},
            {"label": "C", "text": "from"},
            {"label": "D", "text": "in"},
            {"label": "E", "text": "on"}
        ],
        "answer": "D",
        "teacher_feedback": "✓ Correct! Well done.\nWe use the preposition 'in' with cities and countries: 'lives in Los Angeles'.",
        "translation": "Jin Park Güney Kore'nin Seul şehrindendir, fakat Los Angeles'ta yaşamaktadır.",
        "explanation": "Şehir / Ülke Edatı Kuralı:\nŞehirlerde ve ülkelerde yaşamak ifadesi için **'live in'** kullanılır: **lives in Los Angeles** / lives in Istanbul.",
        "distractors": "• A: Şehirler için 'at' değil 'in' kullanılır.\n• B: 'with' ile demektir (şehirle yaşanmaz).\n• C: 'from' oradan olduğunu belirtir, yaşanılan yer için 'in' gerekir.\n• E: 'on' caddeler/sokaklar içindir.",
        "tip": "Şehir ve ülke isimlerinin önüne DAİMA 'IN' gelir (in Los Angeles, in Turkey)."
    },
    {
        "is_official_exam": True,
        "is_exam_certain": True,
        "category": "📘 OXFORD KİTAP SORULARI (PAGE 39)",
        "tag": "📘 Oxford Sayfa 39 • works in a Korean restaurant",
        "question": "He's a chef. He works in a Korean ___ with his friend Alex.",
        "options": [
            {"label": "A", "text": "hospital"},
            {"label": "B", "text": "restaurant"},
            {"label": "C", "text": "office"},
            {"label": "D", "text": "airport"},
            {"label": "E", "text": "bank"}
        ],
        "answer": "B",
        "teacher_feedback": "✓ Correct! Well done.\nA chef works in a restaurant: 'works in a Korean restaurant'.",
        "translation": "O bir aşçıdır. Arkadaşı Alex ile birlikte bir Kore restoranında çalışmaktadır.",
        "explanation": "Meslek & İş Yeri Uyumu:\nCümlede Jin'in **'chef'** (aşçı) olduğu belirtilmiştir. Bir aşçı **'restaurant'** (restoran) içinde yemek pişirir.",
        "distractors": "• A: 'hospital' doktor/hemşire içindir.\n• C: 'office' ofis çalışanları/müdürler içindir.\n• D: 'airport' pilotlar/hostesler içindir.\n• E: 'bank' bankacılar içindir.",
        "tip": "CHEF (aşçı) $\rightarrow$ RESTAURANT (restoran)."
    },
    {
        "is_official_exam": True,
        "is_exam_certain": True,
        "category": "📘 OXFORD KİTAP SORULARI (PAGE 39)",
        "tag": "📘 Oxford Sayfa 39 • cooks Korean food",
        "question": "Jin cooks Korean ___ at work, but at home, he cooks many kinds of food.",
        "options": [
            {"label": "A", "text": "food"},
            {"label": "B", "text": "car"},
            {"label": "C", "text": "game"},
            {"label": "D", "text": "clothes"},
            {"label": "E", "text": "song"}
        ],
        "answer": "A",
        "teacher_feedback": "✓ Correct! Well done.\nThe verb 'cook' takes food objects: 'cooks Korean food'.",
        "translation": "Jin iş yerinde Kore yemekleri pişirir, fakat evde birçok çeşit yemek pişirir.",
        "explanation": "Fiil-Nesne Uyumu:\n'cook' (pişirmek) fiili sadece yiyeceklerle kullanılır: **cooks Korean food** (Kore yemekleri pişirir).",
        "distractors": "• B: 'car' arabadır (pişirilmez!).\n• C: 'game' oyundur.\n• D: 'clothes' kıyafettir.\n• E: 'song' şarkıdır.",
        "tip": "COOK (yemek pişirmek) $\rightarrow$ FOOD (yemek/yiyecek)."
    },
    {
        "is_official_exam": True,
        "is_exam_certain": True,
        "category": "📘 OXFORD KİTAP SORULARI (PAGE 39)",
        "tag": "📘 Oxford Sayfa 39 • Subject pronoun: he",
        "question": "Jin cooks Korean food at work, but at home, ___ cooks many kinds of food.",
        "options": [
            {"label": "A", "text": "he"},
            {"label": "B", "text": "she"},
            {"label": "C", "text": "they"},
            {"label": "D", "text": "we"},
            {"label": "E", "text": "you"}
        ],
        "answer": "A",
        "teacher_feedback": "✓ Correct! Well done.\nJin Park is a male subject (he), so the subject pronoun is 'he'.",
        "translation": "Jin iş yerinde Kore yemekleri pişirir, fakat evde o (kendisi) birçok çeşit yemek pişirir.",
        "explanation": "Özne Zamiri (Subject Pronoun):\nParagraf Jin Park'tan ('He is a chef', 'He works...') erkek özne olarak bahsetmektedir. Bu yüzden ikinci cümlede de özne **'he'** olmalıdır.",
        "distractors": "• B: 'she' kadınlar içindir; Jin Park erkektir.\n• C: 'they' çoğuldur, 'cooks' -s takısı almıştır (tekildir).\n• D: 'we' biz demektir.\n• E: 'you' sen/siz demektir.",
        "tip": "Jin Park (He) $\rightarrow$ he cooks."
    },
    {
        "is_official_exam": True,
        "is_exam_certain": True,
        "category": "📘 OXFORD KİTAP SORULARI (PAGE 39)",
        "tag": "📘 Oxford Sayfa 39 • He eats it three times a week",
        "question": "He loves salmon. He ___ it three times a week.",
        "options": [
            {"label": "A", "text": "eats"},
            {"label": "B", "text": "eat"},
            {"label": "C", "text": "is eating"},
            {"label": "D", "text": "eating"},
            {"label": "E", "text": "don't eat"}
        ],
        "answer": "A",
        "teacher_feedback": "✓ Correct! Well done.\n'three times a week' indicates regular frequency with third person singular 'He': Present Simple takes -s (eats).",
        "translation": "O somon balığını çok sever. Onu haftada üç kez yer.",
        "explanation": "Geniş Zaman & Sıklık Kuralı:\n1) 'three times a week' (haftada 3 kez) bir sıklık ve rutin anlatır $\rightarrow$ Geniş Zaman (Present Simple).\n2) 'He' öznesi 3. tekil şahıs olduğu için fiile **-s** takısı gelir: **He eats it**.",
        "distractors": "• B: 'eat' -s takısı almamıştır (He eat denmez).\n• C: 'is eating' şu anda yemektedir anlamına gelir, 'haftada 3 kez' rutiniyle uyumsuzdur.\n• D: Yardımcı fiilsiz 'eating' yüklem olamaz.\n• E: 'He' için 'don't eat' denmez (doesn't eat denir).",
        "tip": "He / She / It + Rutin (three times a week) $\rightarrow$ Fiile -s gelir: EATS!"
    }
]

# Prepend new questions to master
updated_master = new_questions + master

# Re-assign sequential IDs
for idx, q in enumerate(updated_master, 1):
    q["id"] = idx

print(f"Total questions count: {len(updated_master)}")

with open("all_questions_master.json", "w", encoding="utf-8") as f:
    json.dump(updated_master, f, ensure_ascii=False, indent=2)

print("Saved all_questions_master.json successfully!")
