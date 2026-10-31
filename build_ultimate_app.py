# -*- coding: utf-8 -*-
"""
Build Ultimate App with Grammar Learning Mode
Includes:
- Mode 1: 🎯 Challenge Quiz Modu (Tek Tek Soru)
- Mode 2: 📋 Tüm Soruları Listele (Hızlı İncele)
- Mode 3: 📖 Gramer Öğretici Modu (Sınav Konularını Adım Adım Öğren)
"""

import json

with open("all_questions_master.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

questions_json = json.dumps(questions, ensure_ascii=False)

html_template = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Smart Choice 1 • Challenge Quiz & Gramer Öğretici</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #2563eb;
            --primary-hover: #1d4ed8;
            --primary-light: #f1f5f9;
            --bg: #f8fafc;
            --card-bg: #ffffff;
            --text-main: #0f172a;
            --text-muted: #64748b;
            --border: #e2e8f0;
            --badge-bg: #f1f5f9;
            --badge-text: #475569;
            --badge-border: #e2e8f0;
            --success-border: #10b981;
            --success-bg: #f0fdf4;
            --success-text: #166534;
            --wrong-border: #ef4444;
            --wrong-bg: #fef2f2;
            --wrong-text: #991b1b;
            --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Inter", sans-serif;
            --radius: 12px;
            --shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
        }

        [data-theme="dark"] {
            --bg: #090d16;
            --card-bg: #131b2e;
            --text-main: #f8fafc;
            --text-muted: #94a3b8;
            --border: #222f46;
            --badge-bg: #1c263c;
            --badge-text: #cbd5e1;
            --badge-border: #2e3e5c;
            --primary: #3b82f6;
            --primary-hover: #60a5fa;
            --primary-light: #172554;
            --success-border: #059669;
            --success-bg: #064e3b22;
            --success-text: #34d399;
            --wrong-border: #dc2626;
            --wrong-bg: #7f1d1d22;
            --wrong-text: #f87171;
            --shadow: 0 2px 8px rgba(0, 0, 0, 0.25);
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
            gap: 8px;
        }

        .app-title span.tag {
            background: var(--bg);
            border: 1px solid var(--border);
            color: var(--text-muted);
            font-size: 0.72rem;
            padding: 2px 8px;
            border-radius: 99px;
            font-weight: 600;
        }

        .header-actions {
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .icon-btn {
            background: var(--bg);
            border: 1px solid var(--border);
            color: var(--text-main);
            width: 34px;
            height: 34px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            font-size: 0.9rem;
            transition: all 0.15s ease;
        }

        .icon-btn:active {
            transform: scale(0.94);
        }

        /* Container */
        .container {
            max-width: 680px;
            margin: 0 auto;
            padding: 14px 16px;
        }

        /* View Mode Switcher (Clean Segmented Control) */
        .view-mode-bar {
            display: flex;
            background: var(--border);
            border-radius: 10px;
            padding: 3px;
            margin-bottom: 12px;
            gap: 2px;
        }

        [data-theme="dark"] .view-mode-bar {
            background: #1c263c;
        }

        .view-btn {
            flex: 1;
            padding: 8px 6px;
            font-size: 0.8rem;
            font-weight: 600;
            text-align: center;
            border: none;
            background: transparent;
            color: var(--text-muted);
            border-radius: 8px;
            cursor: pointer;
            transition: all 0.15s;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 4px;
        }

        .view-btn.active {
            background: var(--card-bg);
            color: var(--text-main);
            box-shadow: 0 1px 2px rgba(0, 0, 0, 0.08);
        }

        .view-btn.grammar-btn {
            color: var(--text-muted);
        }
        .view-btn.grammar-btn.active {
            background: var(--card-bg);
            color: var(--text-main);
            box-shadow: 0 1px 2px rgba(0, 0, 0, 0.08);
        }

        /* Category Filter (Horizontal Scroll, Clean Pill Style) */
        .category-filter-wrap {
            overflow-x: auto;
            white-space: nowrap;
            padding-bottom: 6px;
            margin-bottom: 14px;
            -webkit-overflow-scrolling: touch;
            scrollbar-width: none;
        }
        .category-filter-wrap::-webkit-scrollbar { display: none; }

        .cat-chip {
            display: inline-block;
            background: var(--card-bg);
            border: 1px solid var(--border);
            color: var(--text-muted);
            padding: 6px 14px;
            border-radius: 99px;
            font-size: 0.78rem;
            font-weight: 500;
            cursor: pointer;
            margin-right: 6px;
            transition: all 0.15s;
        }

        .cat-chip.active {
            background: var(--text-main);
            color: var(--card-bg);
            border-color: var(--text-main);
            font-weight: 600;
        }

        /* Status Bar */
        .quiz-status-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 0.75rem;
            font-weight: 600;
            color: var(--text-muted);
            margin-bottom: 8px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .progress-track {
            width: 100%;
            height: 4px;
            background: var(--border);
            border-radius: 99px;
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
        }

        .q-meta {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 14px;
        }

        .q-cat-tag {
            font-size: 0.72rem;
            font-weight: 600;
            padding: 3px 8px;
            background: var(--bg);
            border: 1px solid var(--border);
            color: var(--text-muted);
            border-radius: 6px;
        }

        .q-num-text {
            font-size: 0.78rem;
            font-weight: 600;
            color: var(--text-muted);
        }

        .question-title {
            font-size: 1.15rem;
            line-height: 1.5;
            color: var(--text-main);
            margin-bottom: 20px;
            font-weight: 600;
            white-space: pre-line;
        }

        /* Options */
        .options-group {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }

        .option-button {
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 10px;
            padding: 12px 14px;
            display: flex;
            align-items: center;
            gap: 12px;
            cursor: pointer;
            text-align: left;
            transition: all 0.15s ease;
            position: relative;
            min-height: 48px;
        }

        .option-button:hover:not(:disabled) {
            border-color: #94a3b8;
            background: var(--bg);
        }

        .option-letter {
            width: 26px;
            height: 26px;
            border-radius: 50%;
            background: var(--bg);
            color: var(--text-muted);
            border: 1px solid var(--border);
            font-weight: 600;
            font-size: 0.78rem;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            transition: all 0.15s;
        }

        .option-text {
            font-size: 0.92rem;
            color: var(--text-main);
            font-weight: 500;
            line-height: 1.4;
            flex: 1;
        }

        /* States */
        .option-button.selected-correct {
            border-color: var(--success-border) !important;
            background: var(--success-bg) !important;
        }
        .option-button.selected-correct .option-letter {
            background: var(--success-border) !important;
            color: #ffffff !important;
            border-color: var(--success-border) !important;
        }
        .option-button.selected-correct .option-text {
            color: var(--success-text) !important;
            font-weight: 600;
        }

        .option-button.selected-wrong {
            border-color: var(--wrong-border) !important;
            background: var(--wrong-bg) !important;
        }
        .option-button.selected-wrong .option-letter {
            background: var(--wrong-border) !important;
            color: #ffffff !important;
            border-color: var(--wrong-border) !important;
        }
        .option-button.selected-wrong .option-text {
            color: var(--wrong-text) !important;
        }

        /* Feedback Box */
        .feedback-box {
            margin-top: 16px;
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-left: 3px solid var(--success-border);
            border-radius: 10px;
            padding: 14px 16px;
            display: none;
            animation: fadeIn 0.2s ease;
        }

        .feedback-box.show {
            display: block;
        }

        .feedback-header {
            font-size: 0.88rem;
            font-weight: 700;
            color: var(--success-text);
            margin-bottom: 6px;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .feedback-teacher-text {
            font-size: 0.88rem;
            line-height: 1.45;
            color: var(--text-main);
            margin-bottom: 12px;
        }

        /* Detailed Study Elements */
        .feedback-details {
            border-top: 1px solid var(--border);
            padding-top: 10px;
            margin-top: 8px;
            font-size: 0.82rem;
            line-height: 1.5;
        }

        .detail-row {
            margin-bottom: 8px;
        }

        .detail-label {
            font-weight: 600;
            color: var(--text-muted);
            text-transform: uppercase;
            font-size: 0.68rem;
            letter-spacing: 0.5px;
            margin-bottom: 2px;
        }

        .detail-content {
            white-space: pre-line;
            color: var(--text-main);
        }

        /* Next Question Button */
        .next-btn-container {
            margin-top: 14px;
            display: none;
        }
        .next-btn-container.show {
            display: block;
        }

        .next-btn {
            background: var(--text-main);
            color: var(--card-bg);
            border: none;
            padding: 11px 18px;
            border-radius: 8px;
            font-weight: 600;
            font-size: 0.9rem;
            cursor: pointer;
            transition: opacity 0.15s;
            width: 100%;
        }

        .next-btn:active {
            opacity: 0.85;
            transform: scale(0.99);
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
            border: 1px solid var(--border);
            color: var(--text-muted);
            font-size: 0.8rem;
            font-weight: 500;
            cursor: pointer;
            padding: 6px 12px;
            border-radius: 6px;
        }

        .text-btn:hover {
            color: var(--text-main);
            border-color: #94a3b8;
        }

        /* ================= GRAMMAR LEARNING MODE STYLES ================= */
        #grammarViewContainer {
            display: none;
        }

        .grammar-hero {
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 16px 18px;
            margin-bottom: 14px;
        }

        .grammar-hero h2 {
            font-size: 1.05rem;
            font-weight: 700;
            color: var(--text-main);
            margin-bottom: 4px;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .grammar-hero p {
            font-size: 0.82rem;
            color: var(--text-muted);
            line-height: 1.45;
        }

        .g-card {
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 18px;
            margin-bottom: 14px;
            box-shadow: var(--shadow);
        }

        .g-card-header {
            display: flex;
            align-items: center;
            gap: 10px;
            margin-bottom: 12px;
            padding-bottom: 10px;
            border-bottom: 1px solid var(--border);
        }

        .g-num-badge {
            background: var(--bg);
            border: 1px solid var(--border);
            color: var(--text-main);
            font-size: 0.78rem;
            font-weight: 700;
            width: 24px;
            height: 24px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }

        .g-card-title {
            font-size: 0.98rem;
            font-weight: 700;
            color: var(--text-main);
        }

        .rule-box {
            background: var(--bg);
            border: 1px solid var(--border);
            padding: 12px 14px;
            border-radius: 8px;
            margin-bottom: 12px;
        }

        .rule-formula {
            font-family: var(--font-sans);
            font-weight: 700;
            font-size: 0.84rem;
            color: var(--text-main);
            margin-bottom: 6px;
            padding-bottom: 6px;
            border-bottom: 1px dashed var(--border);
        }

        .rule-text {
            font-size: 0.84rem;
            line-height: 1.5;
            color: var(--text-main);
        }

        .trap-box {
            background: var(--wrong-bg);
            border: 1px solid var(--wrong-border);
            border-radius: 8px;
            padding: 12px 14px;
            margin-bottom: 12px;
        }

        .trap-title {
            font-size: 0.75rem;
            font-weight: 700;
            color: var(--wrong-text);
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 4px;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .trap-content {
            font-size: 0.82rem;
            line-height: 1.5;
            color: var(--text-main);
        }

        .example-box {
            background: var(--success-bg);
            border: 1px solid var(--success-border);
            border-radius: 8px;
            padding: 12px 14px;
            margin-bottom: 12px;
        }

        .example-title {
            font-size: 0.75rem;
            font-weight: 700;
            color: var(--success-text);
            text-transform: uppercase;
            margin-bottom: 4px;
        }

        .example-content {
            font-size: 0.82rem;
            line-height: 1.5;
            color: var(--text-main);
        }

        .practice-link-btn {
            background: var(--bg);
            color: var(--text-main);
            border: 1px solid var(--border);
            padding: 8px 14px;
            border-radius: 8px;
            font-size: 0.8rem;
            font-weight: 600;
            cursor: pointer;
            width: 100%;
            text-align: center;
            transition: all 0.15s;
        }

        .practice-link-btn:hover {
            background: var(--text-main);
            color: var(--card-bg);
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
            background: rgba(0,0,0,0.4);
            z-index: 200;
            align-items: center;
            justify-content: center;
            padding: 16px;
        }
        .modal.open { display: flex; }
        .modal-body {
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            max-width: 480px;
            width: 100%;
            max-height: 80vh;
            overflow-y: auto;
            padding: 18px;
        }
        .grid-nums {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 6px;
            margin-top: 12px;
        }
        .grid-num-btn {
            background: var(--bg);
            border: 1px solid var(--border);
            padding: 8px 0;
            border-radius: 6px;
            font-weight: 600;
            font-size: 0.85rem;
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
                <span class="tag">Resmi Sınav & Gramer Öğretici (103 Soru)</span>
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
            <button class="view-btn active" id="singleModeBtn" onclick="switchView('single')">Sınav Modu</button>
            <button class="view-btn" id="listModeBtn" onclick="switchView('list')">Tüm Sorular</button>
            <button class="view-btn grammar-btn" id="grammarModeBtn" onclick="switchView('grammar')">Gramer Öğretici</button>
        </div>

        <!-- Category Filters (Hidden in Grammar Mode) -->
        <div class="category-filter-wrap" id="categoryFilterWrap">
            <button class="cat-chip active" onclick="setCategory('all')">Tümü (103)</button>
            <button class="cat-chip" onclick="setCategory('🏆 HOCANIN SLAYT CHALLENGE SORULARI')">Slayt Challenge (12)</button>
            <button class="cat-chip" onclick="setCategory('🏆 HOCANIN RESMİ SINAV BELGESİ')">Word Sınavı (20)</button>
            <button class="cat-chip" onclick="setCategory('🏆 HOCANIN 20 SORULUK RESMİ SINAVI')">Canlı Quiz (20)</button>
            <button class="cat-chip" onclick="setCategory('⭐ KESİN SINAV SORULARI')">Kesin Çıkacaklar</button>
            <button class="cat-chip" onclick="setCategory('Hocanın Canlı Ders Soruları')">Canlı Ders Soruları</button>
            <button class="cat-chip" onclick="setCategory('wrong_only')">Yanlışlarım</button>
        </div>

        <!-- ================= MODE 1: SINGLE QUESTION VIEW (TEACHER SCREEN) ================= -->
        <div id="singleViewContainer">
            <!-- Status Bar & Score -->
            <div class="quiz-status-bar">
                <span id="qCounter">QUESTION 1 / 103</span>
                <span id="scoreCounter">SCORE: 0</span>
            </div>
            <div class="progress-track">
                <div class="progress-fill" id="progressFill"></div>
            </div>

            <!-- Question Card -->
            <div class="quiz-card" id="quizCard">
                <div class="q-meta">
                    <span class="q-cat-tag" id="qTag">Challenge Quiz</span>
                    <span class="q-num-text" id="qIndexText">Soru 1 / 103</span>
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

        <!-- ================= MODE 2: LIST VIEW (ALL QUESTIONS) ================= -->
        <div id="listViewContainer"></div>

        <!-- ================= MODE 3: GRAMMAR LEARNING MODE ================= -->
        <div id="grammarViewContainer">
            <div class="grammar-hero">
                <h2>📖 Sınav Kazandıran Gramer Rehberi</h2>
                <p>Aşağıdaki 9 kritik gramer kartını dikkatlice oku. Bu kuralları anladığında sınavdaki 103 sorunun tamamını hiç zorlanmadan doğru çözeceksin!</p>
            </div>

            <!-- Kart 1: To Be & Kısa Cevap Tuzağı -->
            <div class="g-card">
                <div class="g-card-header">
                    <div class="g-num-badge">1</div>
                    <div class="g-card-title">To Be (am / is / are) & Kısa Cevap Tuzağı</div>
                </div>
                <div class="rule-box">
                    <div class="rule-formula">I -> AM | He / She / It -> IS | You / We / They -> ARE</div>
                    <div class="rule-text">
                        • <b>"My name"</b> tekildir ('it' yerine geçer) -> <b>My name IS Daniel</b> (Asla 'am' denmez!).<br>
                        • <b>"We"</b> çoğuldur -> <b>We ARE from Brazil.</b><br>
                        • <b>"It is nice to..."</b> sonrasında fiil YALIN kalır -> <b>It's nice to MEET you.</b>
                    </div>
                </div>
                <div class="trap-box">
                    <div class="trap-title">⚠️ Hocanın En Büyük Sınav Tuzağı:</div>
                    <div class="trap-content">
                        Olumlu kısa cevapta ASLA kesme işaretiyle kısaltma YAPILMAZ!<br>
                        ❌ <b>"Yes, I'm."</b> veya <b>"Yes, he's."</b> (YANLIŞTIR!)<br>
                        ✅ <b>"Yes, I AM."</b> ve <b>"Yes, he IS."</b> (DOĞRUDUR!)
                    </div>
                </div>
                <div class="example-box">
                    <div class="example-title">🎯 Sınav Sorusu Örneği (Soru 1 & 4):</div>
                    <div class="example-content">
                        • <i>"Hello! My name ___ Daniel."</i> -> Doğru Cevap: <b>is</b><br>
                        • <i>"Are you a student?"</i> -> Doğru Cevap: <b>Yes, I am.</b>
                    </div>
                </div>
                <button class="practice-link-btn" onclick="jumpToCategoryAndQuestion('🏆 HOCANIN 20 SORULUK RESMİ SINAVI', 1)">👉 Bu Konunun Sorularını Çöz (Soru 1-4)</button>
            </div>

            <!-- Kart 2: Articles (a / an / the) & Telaffuz Tuzakları -->
            <div class="g-card">
                <div class="g-card-header">
                    <div class="g-num-badge">2</div>
                    <div class="g-card-title">Articles (a / an / the) & Telaffuz Tuzakları</div>
                </div>
                <div class="rule-box">
                    <div class="rule-formula">Sessiz Ses Öncesi: A | Sesli Ses Öncesi: AN | Üstünlük / Tek Olanlar: THE</div>
                    <div class="rule-text">
                        • Normal sesli harfler: <b>an actor</b>, <b>an engineer</b>, <b>an architect</b>.<br>
                        • Normal sessiz harfler: <b>a teacher</b>, <b>a doctor</b>, <b>a manager</b>.
                    </div>
                </div>
                <div class="trap-box">
                    <div class="trap-title">⚠️ Hocanın Sorduğu 2 Dev Telaffuz Tuzağı:</div>
                    <div class="trap-content">
                        1) <b>Okunmayan 'H' (Silent H):</b> 'honest' ve 'hour' kelimelerinde baştaki 'h' okunmaz! Sesli sesle başlar -> <b>AN honest person</b>, <b>AN hour</b>.<br>
                        2) <b>'Y' Sesiyle Başlayan 'U':</b> 'university' ve 'useful' kelimeleri /y/ sessiz sesiyle okunur -> <b>A university student</b>, <b>A useful book</b>.<br>
                        3) <b>Superlative (En Üstünlük):</b> 'best', 'highest', 'most exciting' önüne daima <b>THE</b> gelir -> <b>the best student</b>.
                    </div>
                </div>
                <div class="example-box">
                    <div class="example-title">🎯 Sınav Sorusu Örneği:</div>
                    <div class="example-content">
                        <i>"She is ___ honest person and ___ best student in our class."</i> -> Doğru Cevap: <b>an / the</b>
                    </div>
                </div>
                <button class="practice-link-btn" onclick="jumpToCategoryAndQuestion('all', 11)">👉 Bu Konunun Sorularını Çöz (Soru 11 & Canlı Ders Soruları)</button>
            </div>

            <!-- Kart 3: Present Simple (Geniş Zaman) & doesn't Tuzağı -->
            <div class="g-card">
                <div class="g-card-header">
                    <div class="g-num-badge">3</div>
                    <div class="g-card-title">Present Simple (Geniş Zaman) & doesn't Tuzağı</div>
                </div>
                <div class="rule-box">
                    <div class="rule-formula">He / She / It: Fiil-(s/es) | I / You / We / They: YALIN Fiil</div>
                    <div class="rule-text">
                        • -es Kuralı: -ch, -sh, -ss, -x, -o ile bitenler -> <b>watches</b>, <b>goes</b>, <b>does</b>.<br>
                        • -ies Kuralı: Sessiz + y -> <b>studies</b> (study). Sesli + y -> <b>plays</b> (play).<br>
                        • Çoğul Özneler: <i>My brother and I</i> (we) ve <i>our parents</i> (they) fiili YALIN bırakır -> <b>share / have</b>.
                    </div>
                </div>
                <div class="trap-box">
                    <div class="trap-title">⚠️ Altın Sınav Kuralı (Hocanın En Çok Sorduğu!):</div>
                    <div class="trap-content">
                        Cümlede <b>doesn't</b> veya <b>does</b> varsa, ana fiildeki <b>-S TAKISI UÇAR!</b> Fiil %100 YALIN kalır!<br>
                        ❌ <b>"He doesn't likes coffee."</b> (YANLIŞ!)<br>
                        ✅ <b>"He doesn't LIKE coffee."</b> (DOĞRU!)<br>
                        ❌ <b>"Where does she works?"</b> (YANLIŞ!)<br>
                        ✅ <b>"Where does she WORK?"</b> (DOĞRU!)
                    </div>
                </div>
                <div class="example-box">
                    <div class="example-title">🎯 Sınav Sorusu Örneği:</div>
                    <div class="example-content">
                        • <i>"Anna ___ coffee, but she ___ tea every morning."</i> -> Doğru Cevap: <b>doesn't drink / drinks</b><br>
                        • <i>"My brother and I ___ a room, but our parents ___ their own room."</i> -> Doğru Cevap: <b>share / have</b>
                    </div>
                </div>
                <button class="practice-link-btn" onclick="jumpToCategoryAndQuestion('🏆 HOCANIN 20 SORULUK RESMİ SINAVI', 19)">👉 Bu Konunun Sorularını Çöz</button>
            </div>

            <!-- Kart 4: Sıklık Zarfları (always, usually, never) & Cümledeki Yeri -->
            <div class="g-card">
                <div class="g-card-header">
                    <div class="g-num-badge">4</div>
                    <div class="g-card-title">Sıklık Zarfları & Cümledeki Yeri</div>
                </div>
                <div class="rule-box">
                    <div class="rule-formula">Normal Fiilden ÖNCE | BE (am/is/are/was) Fiilinden SONRA</div>
                    <div class="rule-text">
                        • Sıklık ölçeği: <b>always</b> (%100 - 7 gün) > <b>usually</b> (%80 - 5 gün) > <b>sometimes</b> (%50) > <b>never</b> (%0 - 0 gün).<br>
                        • 1) Normal eylem fiilinden <b>ÖNCE</b>: <i>"She <b>usually</b> goes to bed early."</i><br>
                        • 2) To Be fiilinden <b>SONRA</b>: <i>"He is <b>never</b> late."</i>
                    </div>
                </div>
                <div class="trap-box">
                    <div class="trap-title">⚠️ Cümlenin Sonuna Gelen Zaman İfadeleri:</div>
                    <div class="trap-content">
                        • <b>"every day"</b>, <b>"once a week"</b> (haftada 1), <b>"twice a week"</b> (haftada 2), <b>"three times a week"</b> daima <b>cümlenin EN SONUNDA</b> yer alır!<br>
                        • <i>"How often do you play tennis?"</i> sorusunun cevabı: <b>"Three times a week."</b> dır.
                    </div>
                </div>
                <button class="practice-link-btn" onclick="jumpToCategoryAndQuestion('🏆 HOCANIN 20 SORULUK RESMİ SINAVI', 5)">👉 Bu Konunun Sorularını Çöz (Soru 5 & 17)</button>
            </div>

            <!-- Kart 5: Present Continuous (Şimdiki Zaman), Listen! & Can't -->
            <div class="g-card">
                <div class="g-card-header">
                    <div class="g-num-badge">5</div>
                    <div class="g-card-title">Present Continuous (Şimdiki Zaman) & Can't Kuralı</div>
                </div>
                <div class="rule-box">
                    <div class="rule-formula">am / is / are + Fiil-ING | Anahtarlar: right now, at the moment, Listen!, Look!, Be quiet!</div>
                    <div class="rule-text">
                        • <i>"Please don't make noise. The students <b>are taking</b> an exam right now."</i><br>
                        • <i>"Look! The baby <b>is sleeping</b>."</i>
                    </div>
                </div>
                <div class="trap-box">
                    <div class="trap-title">⚠️ Hocanın Vurguladığı 2 Kritik Hata:</div>
                    <div class="trap-content">
                        1) <b>"isn't" ile yalın fiil YAN YANA GELEMEZ:</b><br>
                        ❌ <i>"He isn't work today."</i> (Hatalı cümle!) -> ✅ <i>"He isn't working today."</i><br>
                        2) <b>'Can' Yardımcı Fiilinin Olumsuzu Sadece CAN'T dır:</b><br>
                        ❌ <i>"don't can"</i> veya <i>"not can"</i> diye bir şey YOKTUR! -> ✅ <b>"can't sleep"</b>.
                    </div>
                </div>
                <div class="example-box">
                    <div class="example-title">🎯 Sınav Sorusu Örneği:</div>
                    <div class="example-content">
                        <i>"Listen! The neighbours ___ loud music, and I ___ sleep."</i> -> Doğru Cevap: <b>are playing / can't</b>
                    </div>
                </div>
                <button class="practice-link-btn" onclick="jumpToCategoryAndQuestion('🏆 HOCANIN 20 SORULUK RESMİ SINAVI', 8)">👉 Bu Konunun Sorularını Çöz (Soru 8 & 15)</button>
            </div>

            <!-- Kart 6: Past of To Be (Was / Were) & "you and Ben" Tuzağı -->
            <div class="g-card">
                <div class="g-card-header">
                    <div class="g-num-badge">6</div>
                    <div class="g-card-title">Was / Were (Geçmiş Zaman) & "you and Ben" Tuzağı</div>
                </div>
                <div class="rule-box">
                    <div class="rule-formula">I / He / She / It -> WAS (wasn't) | You / We / They -> WERE (weren't)</div>
                    <div class="rule-text">
                        • Zaman belirteçleri: <b>yesterday</b>, <b>last night</b>, <b>last week</b>, <b>two days ago</b>.<br>
                        • <i>"I <b>was</b> at the library yesterday."</i><br>
                        • <i>"They <b>were</b> at the café last Sunday."</i><br>
                        • <i>"The weather <b>was</b> great, so my friends and I <b>were</b> at the park."</i>
                    </div>
                </div>
                <div class="trap-box">
                    <div class="trap-title">⚠️ HOCANIN KESİN SINAV SORUSU TUZAKLARI:</div>
                    <div class="trap-content">
                        1) <b>"you and Ben" Sorusu:</b> Karşı taraf "you and Ben" (sen ve Ben) derse cevapta özne <b>"we" (biz)</b> olur ve <b>WERE</b> alır:<br>
                        <i>"Were you and Ben in the same class last year?"</i> -> <b>"Yes, we WERE."</b><br>
                        2) <b>"your friends" Tuzağı:</b> 'your' tekil sanılır ama 'friends' (arkadaşlar) çoğuldur -> <b>"Where WERE your friends?"</b> (was YANLIŞTIR).
                    </div>
                </div>
                <button class="practice-link-btn" onclick="jumpToCategoryAndQuestion('🏆 HOCANIN RESMİ SINAV BELGESİ', 1)">👉 Bu Konunun Sorularını Çöz (Soru 16-20)</button>
            </div>

            <!-- Kart 7: Sınavın Kilit Sıfatları & Problem Eşleştirmeleri -->
            <div class="g-card">
                <div class="g-card-header">
                    <div class="g-num-badge">7</div>
                    <div class="g-card-title">Sınavın Kilit Sıfatları & Problem Eşleştirmeleri</div>
                </div>
                <div class="rule-box">
                    <div class="rule-formula">Cümledeki ipucunu yakala -> Doğru sıfatı anında işaretle!</div>
                    <div class="rule-text">
                        • <b>fell asleep</b> (uyuyakaldım) -> <b>boring</b> (sıkıcı film/kitap).<br>
                        • <b>dancing / screaming with joy</b> -> <b>exciting / fun</b> (heyecanlı/eğlenceli).<br>
                        • <b>many people waiting in line / no empty seat</b> -> <b>crowded</b> (kalabalık).<br>
                        • <b>bike / car tire</b> -> <b>flat</b> (flat tire = patlak/inik lastik).<br>
                        • <b>bus was 40 minutes late</b> -> <b>terrible</b> traffic (berbat trafik).<br>
                        • <b>waiting for 30 minutes</b> -> <b>long</b> lines (uzun kuyruklar).<br>
                        • <b>phone / laptop dropped / not working</b> -> <b>broken</b> (bozuk/kırık).<br>
                        • <b>supermarket / pharmacy at 11:30 p.m.</b> -> <b>closed</b> (kapalı).<br>
                        • <b>a lot of cars in the street</b> -> <b>noisy</b> (gürültülü).<br>
                        • <b>fever / in bed</b> -> <b>sick / ill</b> (hasta).
                    </div>
                </div>
                <button class="practice-link-btn" onclick="jumpToCategoryAndQuestion('🏆 HOCANIN 20 SORULUK RESMİ SINAVI', 7)">👉 Bu Konunun Sorularını Çöz (Soru 7 & 18)</button>
            </div>

            <!-- Kart 8: Kalıplaşmış Soru-Cevaplar & Diyaloglar -->
            <div class="g-card">
                <div class="g-card-header">
                    <div class="g-num-badge">8</div>
                    <div class="g-card-title">Kalıplaşmış Soru-Cevaplar & Diyaloglar</div>
                </div>
                <div class="rule-box">
                    <div class="rule-formula">Hangi Soruya Hangi Cevap Verilir?</div>
                    <div class="rule-text">
                        • <b>"What do you do?"</b> = Ne iş yapıyorsun? / Mesleğin ne? -> <b>"I'm an engineer / a student."</b><br>
                        • <b>"What are you doing?"</b> = Şu anda ne yapıyorsun? -> <b>"I'm cooking dinner / studying."</b><br>
                        • <b>"What time is your English class?"</b> -> <b>"It's at 10:15."</b> (What time = saat kaçta).<br>
                        • <b>"How are you today?"</b> -> <b>"I'm fine, thanks."</b><br>
                        • <b>"How's it going?"</b> -> <b>"Not bad, thanks. And you?"</b><br>
                        • <b>"Nice to meet you."</b> -> <b>"Nice to meet you, too."</b>
                    </div>
                </div>
                <button class="practice-link-btn" onclick="jumpToCategoryAndQuestion('🏆 HOCANIN 20 SORULUK RESMİ SINAVI', 4)">👉 Bu Konunun Sorularını Çöz (Soru 4, 6, 12)</button>
            </div>

            <!-- Kart 9: Zaman Edatları (IN / ON / AT) & There is / There are -->
            <div class="g-card">
                <div class="g-card-header">
                    <div class="g-num-badge">9</div>
                    <div class="g-card-title">Zaman Edatları (IN / ON / AT) & There is / There are</div>
                </div>
                <div class="rule-box">
                    <div class="rule-formula">Sadece Ay: IN | Belirli Gün veya Tarih: ON | Saat: AT</div>
                    <div class="rule-text">
                        • <b>Sadece Ay Belirtilirse:</b> <i>"My birthday is <b>in</b> March."</i> (Mart ayında).<br>
                        • <b>Ayın Günü / Tarih Belirtilirse:</b> <i>"My birthday is <b>on</b> the 14th / <b>on</b> March 14th."</i><br>
                        • <b>Saat Belirtilirse:</b> <i>"The class is <b>at</b> 10:15."</i><br>
                        • <b>Hocanın Slayt Sorusu (İkisi Birlikte):</b> <i>"My birthday is <b>in</b> March, <b>on</b> the 14th."</i> (Doğru Eşleştirme: <b>in / on</b>).
                    </div>
                </div>
                <div class="trap-box">
                    <div class="trap-title">⚠️ There is / There are & Sayılabilirlik (Milk vs Eggs):</div>
                    <div class="trap-content">
                        • <b>Sayılamayan İsimler (milk, water, coffee):</b> Tekildir! Olumsuzda 'any' ile: <b>There ISN'T any milk</b>.<br>
                        • <b>Sayılabilen Çoğul İsimler (eggs, cars):</b> Çoğuldur! Olumluda 'some' ile: <b>There ARE some eggs</b>.<br>
                        • <i>"There <b>isn't</b> any milk in the fridge, but there <b>are</b> some eggs."</i> (Doğru: <b>isn't / are</b>).<br>
                        • <b>Sıklık Zarfı Yeri (Hocanın Sorusu):</b> <i>"She <b>is never</b> late for work."</i> ('be' fiilinden SONRA!).
                    </div>
                </div>
                <div class="example-box">
                    <div class="example-title">🎯 Sınav Sorusu Örnekleri:</div>
                    <div class="example-content">
                        • <i>"My birthday is ___ March, ___ the 14th."</i> -> <b>in / on</b><br>
                        • <i>"There ___ any milk in the fridge, but there ___ some eggs."</i> -> <b>isn't / are</b><br>
                        • <i>"Look! The children ___ in the garden. They usually ___ tennis on Saturdays."</i> -> <b>are playing / play</b>
                    </div>
                </div>
                <button class="practice-link-btn" onclick="jumpToCategoryAndQuestion('🏆 HOCANIN SLAYT CHALLENGE SORULARI', 1)">👉 Slayt Challenge Sorularını Çöz (Soru 1-12)</button>
            </div>
        </div>

    </div>

    <!-- Quick Jump Modal -->
    <div class="modal" id="jumpModal" onclick="closeJumpModal(event)">
        <div class="modal-body" onclick="event.stopPropagation()">
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <h3 style="font-size:1rem;">Sorular Listesi (1 - 103)</h3>
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
        let currentView = 'single'; // 'single', 'list', or 'grammar'

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
            document.getElementById('grammarModeBtn').classList.toggle('active', mode === 'grammar');

            document.getElementById('singleViewContainer').style.display = mode === 'single' ? 'block' : 'none';
            document.getElementById('listViewContainer').style.display = mode === 'list' ? 'block' : 'none';
            document.getElementById('grammarViewContainer').style.display = mode === 'grammar' ? 'block' : 'none';

            // Filter bar is visible only in quiz and list mode
            document.getElementById('categoryFilterWrap').style.display = mode === 'grammar' ? 'none' : 'block';

            if (mode === 'single') {
                renderSingleQuestion();
            } else if (mode === 'list') {
                renderListView();
            } else {
                window.scrollTo({ top: 0, behavior: 'smooth' });
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

        function jumpToCategoryAndQuestion(cat, qNum) {
            switchView('single');
            setCategory(cat);
            if (qNum && qNum <= filteredQuestions.length) {
                currentIndex = qNum - 1;
            } else {
                currentIndex = 0;
            }
            renderSingleQuestion();
            window.scrollTo({ top: 0, behavior: 'smooth' });
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
                else if (currentView === 'list') renderListView();
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
                    switchView('single');
                    currentIndex = idx;
                    renderSingleQuestion();
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

print("Saved sinav_calisma.html and index.html with Grammar Learning Mode successfully!")

