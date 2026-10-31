# -*- coding: utf-8 -*-
import json

with open("all_questions_master.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

questions_json = json.dumps(questions, ensure_ascii=False)

html_template = """<!DOCTYPE html>
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
            --primary-hover: #d9531e;
            --primary-light: #fff3ec;
            --bg: #f8fafc;
            --card-bg: #ffffff;
            --text-main: #1e293b;
            --text-muted: #64748b;
            --border: #e2e8f0;
            --badge-bg: #fca5a5;
            --badge-text: #ffffff;
            --success-border: #10b981;
            --success-bg: #ecfdf5;
            --success-text: #065f46;
            --wrong-border: #ef4444;
            --wrong-bg: #fef2f2;
            --wrong-text: #991b1b;
            --font-serif: 'DM Serif Display', Georgia, serif;
            --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            --radius: 16px;
            --shadow: 0 4px 18px rgba(0, 0, 0, 0.05);
        }

        [data-theme="dark"] {
            --bg: #0b0f19;
            --card-bg: #151d2e;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --border: #243048;
            --primary-light: #2c1a11;
            --success-bg: #064e3b33;
            --wrong-bg: #7f1d1d33;
            --shadow: 0 4px 18px rgba(0, 0, 0, 0.35);
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
            padding-bottom: 50px;
            transition: background-color 0.2s, color 0.2s;
        }

        /* Top Header */
        header {
            position: sticky;
            top: 0;
            z-index: 100;
            background: var(--card-bg);
            border-bottom: 1px solid var(--border);
            padding: 10px 16px;
            backdrop-filter: blur(8px);
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
            font-weight: 700;
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
            transition: all 0.15s ease;
        }

        .icon-btn:active {
            transform: scale(0.92);
        }

        /* Container */
        .container {
            max-width: 680px;
            margin: 0 auto;
            padding: 14px 16px;
        }

        /* Mode Switcher Tabs */
        .view-mode-bar {
            display: flex;
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 3px;
            margin-bottom: 12px;
        }

        .view-btn {
            flex: 1;
            padding: 8px 10px;
            font-size: 0.8rem;
            font-weight: 600;
            text-align: center;
            border: none;
            background: transparent;
            color: var(--text-muted);
            border-radius: 9px;
            cursor: pointer;
            transition: all 0.15s;
        }

        .view-btn.active {
            background: var(--primary);
            color: white;
            box-shadow: 0 2px 6px rgba(242, 101, 34, 0.3);
        }

        /* Category Filter (Horizontal Scroll) */
        .category-filter-wrap {
            overflow-x: auto;
            white-space: nowrap;
            padding-bottom: 6px;
            margin-bottom: 12px;
            -webkit-overflow-scrolling: touch;
            scrollbar-width: none;
        }
        .category-filter-wrap::-webkit-scrollbar { display: none; }

        .cat-chip {
            display: inline-block;
            background: var(--card-bg);
            border: 1px solid var(--border);
            color: var(--text-muted);
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 0.78rem;
            font-weight: 600;
            cursor: pointer;
            margin-right: 5px;
            transition: all 0.15s;
        }

        .cat-chip.active {
            background: var(--text-main);
            color: var(--card-bg);
            border-color: var(--text-main);
        }

        /* Status Bar (Teacher style) */
        .quiz-status-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 0.75rem;
            font-weight: 700;
            letter-spacing: 0.5px;
            text-transform: uppercase;
            color: var(--primary);
            margin-bottom: 6px;
        }

        .progress-track {
            width: 100%;
            height: 5px;
            background: var(--border);
            border-radius: 3px;
            overflow: hidden;
            margin-bottom: 16px;
        }

        .progress-fill {
            height: 100%;
            background: var(--primary);
            width: 0%;
            transition: width 0.3s ease;
        }

        /* Question Card */
        .quiz-card {
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 22px 18px;
            box-shadow: var(--shadow);
            margin-bottom: 16px;
            transition: transform 0.15s ease;
        }

        .q-meta {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
        }

        .q-cat-tag {
            font-size: 0.7rem;
            font-weight: 700;
            text-transform: uppercase;
            padding: 2px 8px;
            background: var(--primary-light);
            color: var(--primary);
            border-radius: 6px;
        }

        .q-num-text {
            font-size: 0.78rem;
            font-weight: 700;
            color: var(--text-muted);
        }

        .question-title {
            font-family: var(--font-serif);
            font-size: 1.25rem;
            line-height: 1.45;
            color: var(--text-main);
            margin-bottom: 20px;
            font-weight: 400;
            letter-spacing: -0.2px;
            white-space: pre-line;
        }

        /* Options */
        .options-group {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .option-button {
            background: var(--card-bg);
            border: 1.5px solid var(--border);
            border-radius: 12px;
            padding: 13px 14px;
            display: flex;
            align-items: center;
            gap: 12px;
            cursor: pointer;
            text-align: left;
            transition: all 0.15s ease;
            position: relative;
            min-height: 50px;
        }

        .option-button:hover:not(:disabled) {
            border-color: #cbd5e1;
            background: var(--primary-light);
        }

        .option-letter {
            width: 28px;
            height: 28px;
            border-radius: 50%;
            background: var(--badge-bg);
            color: #ffffff;
            font-weight: 700;
            font-size: 0.82rem;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            transition: all 0.15s;
        }

        .option-text {
            font-size: 0.95rem;
            color: var(--text-main);
            font-weight: 500;
            line-height: 1.35;
            flex: 1;
        }

        /* States */
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
            margin-top: 18px;
            background: var(--success-bg);
            border: 1px solid var(--success-border);
            border-radius: 12px;
            padding: 15px 16px;
            display: none;
            animation: fadeIn 0.25s ease;
        }

        .feedback-box.show {
            display: block;
        }

        .feedback-header {
            font-size: 0.95rem;
            font-weight: 700;
            color: var(--success-text);
            margin-bottom: 6px;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .feedback-teacher-text {
            font-size: 0.9rem;
            line-height: 1.45;
            color: var(--text-main);
            margin-bottom: 12px;
        }

        /* Detailed Study Elements */
        .feedback-details {
            border-top: 1px dashed rgba(16, 185, 129, 0.35);
            padding-top: 10px;
            margin-top: 8px;
            font-size: 0.84rem;
            line-height: 1.5;
        }

        .detail-row {
            margin-bottom: 8px;
        }

        .detail-label {
            font-weight: 700;
            color: var(--text-muted);
            text-transform: uppercase;
            font-size: 0.7rem;
            letter-spacing: 0.5px;
            margin-bottom: 2px;
        }

        .detail-content {
            white-space: pre-line;
            color: var(--text-main);
        }

        /* Next Question Button */
        .next-btn-container {
            margin-top: 16px;
            display: none;
        }
        .next-btn-container.show {
            display: block;
        }

        .next-btn {
            background: var(--primary);
            color: white;
            border: none;
            padding: 12px 20px;
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

        /* Nav controls */
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

        /* List View Container */
        #listViewContainer {
            display: none;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-4px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Jump Modal */
        .modal {
            display: none;
            position: fixed;
            top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(0,0,0,0.5);
            z-index: 200;
            align-items: center;
            justify-content: center;
            padding: 16px;
            backdrop-filter: blur(2px);
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
        .grid-num-btn.correct { background: var(--success-border); color: white; border-color: var(--success-border); }
        .grid-num-btn.wrong { background: var(--wrong-border); color: white; border-color: var(--wrong-border); }
    </style>
</head>
<body>

    <!-- Header -->
    <header>
        <div class="header-inner">
            <div class="app-title">
                <span>Smart Choice 1</span>
                <span class="tag">Resmi Sınav & Challenge Quiz (91 Soru)</span>
            </div>
            <div class="header-actions">
                <button class="icon-btn" onclick="openJumpModal()" title="Sorular">🔢</button>
                <button class="icon-btn" onclick="toggleTheme()" id="themeBtn" title="Tema">🌙</button>
                <button class="icon-btn" onclick="resetAll()" title="Sıfırla">🔄</button>
            </div>
        </div>
    </header>

    <div class="container">
        <!-- View Mode Switcher -->
        <div class="view-mode-bar">
            <button class="view-btn active" id="singleModeBtn" onclick="switchView('single')">🎯 Challenge Quiz Modu (Tek Tek)</button>
            <button class="view-btn" id="listModeBtn" onclick="switchView('list')">📋 Tüm Soruları Listele (Hızlı İncele)</button>
        </div>

        <!-- Category Filters -->
        <div class="category-filter-wrap">
            <button class="cat-chip active" onclick="setCategory('all')">🌟 Tümü (91)</button>
            <button class="cat-chip" style="background:#fef3c7; border-color:#d97706; color:#b45309; font-weight:700;" onclick="setCategory('🏆 HOCANIN RESMİ SINAV BELGESİ')">🏆 HOCANIN RESMİ WORD SINAV SORULARI</button>
            <button class="cat-chip" style="background:#fef3c7; border-color:#d97706; color:#b45309; font-weight:700;" onclick="setCategory('🏆 HOCANIN 20 SORULUK RESMİ SINAVI')">🏆 HOCANIN 20 SORULUK RESMİ SINAVI</button>
            <button class="cat-chip" style="border-color:#d97706; color:#d97706;" onclick="setCategory('⭐ KESİN SINAV SORULARI')">⭐ KESİN SINAV SORULARI</button>
            <button class="cat-chip" onclick="setCategory('Hocanın Canlı Ders Soruları')">📸 Canlı Ders Soruları</button>
            <button class="cat-chip" onclick="setCategory('İki Boşluklu Cümleler')">🔄 İki Boşluklu Cümleler (Anna ___ but she ___)</button>
            <button class="cat-chip" onclick="setCategory('Which question is correct?')">❓ "Which question is correct?"</button>
            <button class="cat-chip" onclick="setCategory('Which sentence is correct?')">📝 "Which sentence is correct?"</button>
            <button class="cat-chip" onclick="setCategory('Sıfat & Kelime Soruları')">💡 Sıfat & Kelime (The film was so ___ that...)</button>
            <button class="cat-chip" onclick="setCategory('Articles (a / an / the)')">🔤 Articles (a / an / the)</button>
            <button class="cat-chip" onclick="setCategory('Best Answer • Dialogue')">💬 "Best answer:" Diyalog Soruları</button>
            <button class="cat-chip" onclick="setCategory('wrong_only')">❌ Sadece Yanlışlarım</button>
        </div>

        <!-- ================= SINGLE QUESTION VIEW (TEACHER SCREEN) ================= -->
        <div id="singleViewContainer">
            <!-- Status Bar & Score -->
            <div class="quiz-status-bar">
                <span id="qCounter">QUESTION 1 / 91</span>
                <span id="scoreCounter">SCORE: 0</span>
            </div>
            <div class="progress-track">
                <div class="progress-fill" id="progressFill"></div>
            </div>

            <!-- Question Card -->
            <div class="quiz-card" id="quizCard">
                <div class="q-meta">
                    <span class="q-cat-tag" id="qTag">Challenge Quiz</span>
                    <span class="q-num-text" id="qIndexText">Soru 1 / 60</span>
                </div>
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

            <!-- Navigation Controls -->
            <div class="nav-controls">
                <button class="text-btn" onclick="prevQuestion()">← Önceki Soru</button>
                <button class="text-btn" onclick="nextQuestion()">Sonraki Soru →</button>
            </div>
        </div>

        <!-- ================= LIST VIEW (ALL QUESTIONS) ================= -->
        <div id="listViewContainer"></div>

    </div>

    <!-- Quick Jump Modal -->
    <div class="modal" id="jumpModal" onclick="closeJumpModal(event)">
        <div class="modal-body" onclick="event.stopPropagation()">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <h3 style="font-size:1rem;">Sorular Listesi (1 - 91)</h3>
                <button class="icon-btn" onclick="closeJumpModal()">✕</button>
            </div>
            <p style="font-size:0.8rem; color:var(--text-muted); margin-top:4px;">Yeşil: Doğru, Kırmızı: Yanlış</p>
            <div class="grid-nums" id="gridNums"></div>
        </div>
    </div>

    <script>
        const ALL_QUESTIONS = """ + questions_json + """;

        let filteredQuestions = [...ALL_QUESTIONS];
        let currentIndex = 0;
        let score = 0;
        let userAnswers = {}; // { qId: selectedOptionLabel }
        let currentCategory = 'all';
        let currentView = 'single'; // 'single' or 'list'

        // Load state
        try {
            const saved = localStorage.getItem('smart_choice_tuba_quiz_state');
            if (saved) {
                const p = JSON.parse(saved);
                userAnswers = p.answers || {};
                score = p.score || 0;
            }
        } catch(e) {}

        function initTheme() {
            const t = localStorage.getItem('smart_choice_theme') || 'light';
            document.documentElement.setAttribute('data-theme', t);
            document.getElementById('themeBtn').textContent = t === 'dark' ? '☀️' : '🌙';
        }

        function toggleTheme() {
            const cur = document.documentElement.getAttribute('data-theme') || 'light';
            const next = cur === 'dark' ? 'light' : 'dark';
            document.documentElement.setAttribute('data-theme', next);
            localStorage.setItem('smart_choice_theme', next);
            document.getElementById('themeBtn').textContent = next === 'dark' ? '☀️' : '🌙';
        }

        function switchView(mode) {
            currentView = mode;
            document.getElementById('singleModeBtn').classList.toggle('active', mode === 'single');
            document.getElementById('listModeBtn').classList.toggle('active', mode === 'list');
            document.getElementById('singleViewContainer').style.display = mode === 'single' ? 'block' : 'none';
            document.getElementById('listViewContainer').style.display = mode === 'list' ? 'block' : 'none';

            if (mode === 'single') {
                renderSingleQuestion();
            } else {
                renderListView();
            }
        }

        function setCategory(cat) {
            currentCategory = cat;
            document.querySelectorAll('.cat-chip').forEach(chip => {
                chip.classList.toggle('active', chip.getAttribute('onclick').includes("'" + cat + "'"));
            });

            if (cat === 'all') {
                filteredQuestions = [...ALL_QUESTIONS];
            } else if (cat === 'wrong_only') {
                filteredQuestions = ALL_QUESTIONS.filter(q => userAnswers[q.id] && userAnswers[q.id] !== q.answer);
            } else {
                filteredQuestions = ALL_QUESTIONS.filter(q => q.category === cat);
            }

            currentIndex = 0;
            if (currentView === 'single') {
                renderSingleQuestion();
            } else {
                renderListView();
            }
        }

        function renderSingleQuestion() {
            if (filteredQuestions.length === 0) {
                document.getElementById('questionText').textContent = "Bu kategoride soru bulunmuyor veya yanlış yaptığınız soru kalmadı! 🎉";
                document.getElementById('optionsGroup').innerHTML = '';
                document.getElementById('feedbackBox').classList.remove('show');
                document.getElementById('nextBtnContainer').classList.remove('show');
                document.getElementById('qCounter').textContent = "TAMAMLANDI";
                document.getElementById('progressFill').style.width = "100%";
                return;
            }

            if (currentIndex >= filteredQuestions.length) currentIndex = 0;
            const q = filteredQuestions[currentIndex];
            const total = filteredQuestions.length;

            document.getElementById('qCounter').textContent = `QUESTION ${currentIndex + 1} / ${total}`;
            document.getElementById('scoreCounter').textContent = `SCORE: ${score}`;
            document.getElementById('progressFill').style.width = `${((currentIndex + 1) / total) * 100}%`;
            document.getElementById('qTag').textContent = q.tag || q.category;
            document.getElementById('qIndexText').textContent = `Soru ${currentIndex + 1} / ${total} (No: ${q.id})`;
            document.getElementById('questionText').textContent = q.question;

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

                btn.onclick = () => selectSingleOption(opt.label);
                btn.innerHTML = `
                    <span class="option-letter">${opt.label}</span>
                    <span class="option-text">${opt.text}</span>
                `;
                group.appendChild(btn);
            });

            // Feedback
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
                    fHeader.textContent = '✗ Incorrect. Doğru kuralı inceleyin:';
                    fHeader.style.color = 'var(--wrong-text)';
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

        function selectSingleOption(label) {
            const q = filteredQuestions[currentIndex];
            if (userAnswers[q.id] !== undefined) return;

            userAnswers[q.id] = label;
            if (label === q.answer) {
                score++;
            }

            saveState();
            renderSingleQuestion();
        }

        function nextQuestion() {
            if (currentIndex < filteredQuestions.length - 1) {
                currentIndex++;
                renderSingleQuestion();
                window.scrollTo({ top: 0, behavior: 'smooth' });
            } else {
                alert(`Tebrikler! Testi tamamladınız.\nToplam Başarı: ${score} Doğru`);
            }
        }

        function prevQuestion() {
            if (currentIndex > 0) {
                currentIndex--;
                renderSingleQuestion();
                window.scrollTo({ top: 0, behavior: 'smooth' });
            }
        }

        function renderListView() {
            const container = document.getElementById('listViewContainer');
            container.innerHTML = '';

            if (filteredQuestions.length === 0) {
                container.innerHTML = `<div style="text-align:center; padding:30px; background:var(--card-bg); border-radius:var(--radius); border:1px solid var(--border)">Bu kategoride soru bulunmuyor! 🎉</div>`;
                return;
            }

            filteredQuestions.forEach((q, idx) => {
                const card = document.createElement('div');
                card.className = 'quiz-card';
                card.id = 'list-q-' + q.id;

                const answered = userAnswers[q.id] !== undefined;
                const userChoice = userAnswers[q.id];

                let optionsHtml = '';
                q.options.forEach(opt => {
                    let cls = 'option-button';
                    if (answered) {
                        if (opt.label === q.answer) cls += ' selected-correct';
                        else if (opt.label === userChoice) cls += ' selected-wrong';
                    }

                    optionsHtml += `
                        <button class="${cls}" ${answered ? 'disabled' : ''} onclick="chooseListOption(${q.id}, '${opt.label}')">
                            <span class="option-letter">${opt.label}</span>
                            <span class="option-text">${opt.text}</span>
                        </button>
                    `;
                });

                const feedbackHtml = answered ? `
                    <div class="feedback-box show" style="display:block;">
                        <div class="feedback-header" style="color:${userChoice === q.answer ? 'var(--success-text)' : 'var(--wrong-text)'}">
                            ${userChoice === q.answer ? '✓ Correct! Well done.' : '✗ Incorrect. Doğru Cevap: ' + q.answer}
                        </div>
                        <div class="feedback-teacher-text">${escapeHtml(q.teacher_feedback || q.explanation)}</div>
                        <div class="feedback-details">
                            <div class="detail-row">
                                <div class="detail-label">🇹🇷 Türkçe Çevirisi:</div>
                                <div class="detail-content">${escapeHtml(q.translation)}</div>
                            </div>
                            <div class="detail-row">
                                <div class="detail-label">💡 Neden Doğru? (Kural):</div>
                                <div class="detail-content">${escapeHtml(q.explanation)}</div>
                            </div>
                            <div class="detail-row">
                                <div class="detail-label">⚠️ Çeldiriciler:</div>
                                <div class="detail-content">${escapeHtml(q.distractors)}</div>
                            </div>
                            <div class="detail-row">
                                <div class="detail-label">📌 Sınav İpucu:</div>
                                <div class="detail-content">${escapeHtml(q.tip)}</div>
                            </div>
                        </div>
                    </div>
                ` : '';

                card.innerHTML = `
                    <div class="q-meta">
                        <span class="q-cat-tag">${q.tag || q.category}</span>
                        <span class="q-num-text">Soru ${idx + 1} / ${filteredQuestions.length}</span>
                    </div>
                    <div class="question-title">${escapeHtml(q.question)}</div>
                    <div class="options-group">${optionsHtml}</div>
                    ${feedbackHtml}
                `;
                container.appendChild(card);
            });
        }

        function chooseListOption(qId, label) {
            if (userAnswers[qId] !== undefined) return;
            userAnswers[qId] = label;

            const targetQ = ALL_QUESTIONS.find(x => x.id === qId);
            if (targetQ && targetQ.answer === label) score++;

            saveState();
            renderListView();
        }

        function saveState() {
            try {
                localStorage.setItem('smart_choice_tuba_quiz_state', JSON.stringify({
                    answers: userAnswers,
                    score: score
                }));
            } catch(e) {}
        }

        function resetAll() {
            if (confirm('Tüm çözümlerinizi sıfırlamak istiyor musunuz?')) {
                userAnswers = {};
                score = 0;
                currentIndex = 0;
                saveState();
                if (currentView === 'single') renderSingleQuestion();
                else renderListView();
            }
        }

        function openJumpModal() {
            const grid = document.getElementById('gridNums');
            grid.innerHTML = '';
            ALL_QUESTIONS.forEach((q, idx) => {
                const btn = document.createElement('button');
                btn.className = 'grid-num-btn';
                btn.textContent = idx + 1;

                if (userAnswers[q.id]) {
                    if (userAnswers[q.id] === q.answer) btn.classList.add('correct');
                    else btn.classList.add('wrong');
                }

                btn.onclick = () => {
                    closeJumpModal();
                    setCategory('all');
                    if (currentView === 'single') {
                        currentIndex = idx;
                        renderSingleQuestion();
                    } else {
                        const el = document.getElementById('list-q-' + q.id);
                        if (el) el.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    }
                };
                grid.appendChild(btn);
            });
            document.getElementById('jumpModal').classList.add('open');
        }

        function closeJumpModal() {
            document.getElementById('jumpModal').classList.remove('open');
        }

        function escapeHtml(text) {
            if (!text) return '';
            return text.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
        }

        // Init
        initTheme();
        renderSingleQuestion();
    </script>
</body>
</html>
"""

with open("sinav_calisma.html", "w", encoding="utf-8") as f:
    f.write(html_template)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("Saved sinav_calisma.html and index.html with all 60 questions successfully!")

