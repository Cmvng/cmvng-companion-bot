<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cmvng SignalVault — Forex & Crypto Signals</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Outfit:wght@300;400;500;600;700&family=Geist+Mono:wght@300;400;500&display=swap" rel="stylesheet">
<style>
:root {
  --bg: #09090B;
  --bg-card: #111113;
  --bg-elevated: #18181B;
  --border: rgba(255,255,255,0.08);
  --border-hover: rgba(255,255,255,0.15);
  --text: #FAFAFA;
  --text-secondary: #A1A1AA;
  --text-muted: #52525B;
  --green: #22C55E;
  --green-dim: rgba(34,197,94,0.1);
  --green-glow: rgba(34,197,94,0.15);
  --red: #EF4444;
  --red-dim: rgba(239,68,68,0.1);
  --gold: #EAB308;
  --gold-dim: rgba(234,179,8,0.1);
  --blue: #3B82F6;
  --blue-dim: rgba(59,130,246,0.1);
  --radius: 12px;
  --radius-sm: 8px;
  --radius-pill: 100px;
  --font: 'Outfit', sans-serif;
  --font-serif: 'Instrument Serif', Georgia, serif;
  --font-mono: 'Geist Mono', monospace;
  --transition: 0.3s cubic-bezier(0.22,1,0.36,1);
}
* { margin:0; padding:0; box-sizing:border-box; }
body { font-family:var(--font); background:var(--bg); color:var(--text); -webkit-font-smoothing:antialiased; overflow-x:hidden; }
a { color:var(--green); text-decoration:none; }

/* ── Nav ── */
.nav { max-width:1200px; margin:0 auto; padding:20px 32px; display:flex; justify-content:space-between; align-items:center; }
.nav-brand { display:flex; align-items:center; gap:10px; }
.nav-mark { width:28px; height:28px; background:var(--green); border-radius:7px; display:flex; align-items:center; justify-content:center; font-weight:700; font-size:11px; color:var(--bg); }
.nav-name { font-weight:600; font-size:15px; }
.nav-right { display:flex; align-items:center; gap:16px; }
.nav-testnet { font-size:11px; color:var(--gold); background:var(--gold-dim); padding:4px 10px; border-radius:var(--radius-pill); font-weight:500; }
.nav-cta { font-size:13px; font-weight:600; color:var(--bg); background:var(--green); padding:8px 20px; border-radius:var(--radius-pill); transition:opacity var(--transition); }
.nav-cta:hover { opacity:0.85; }

/* ── Hero ── */
.hero { max-width:1200px; margin:0 auto; padding:80px 32px 60px; text-align:center; position:relative; }
.hero::before { content:''; position:absolute; top:-100px; left:50%; transform:translateX(-50%); width:600px; height:600px; background:radial-gradient(circle, var(--green-glow) 0%, transparent 70%); pointer-events:none; z-index:0; }
.hero-content { position:relative; z-index:1; }
.hero-badge { display:inline-flex; align-items:center; gap:8px; padding:6px 16px; background:var(--bg-elevated); border:1px solid var(--border); border-radius:var(--radius-pill); font-size:12px; color:var(--text-secondary); margin-bottom:28px; }
.hero-badge-dot { width:6px; height:6px; background:var(--green); border-radius:50%; animation:pulse 2s infinite; }
@keyframes pulse { 0%,100%{opacity:1;transform:scale(1)} 50%{opacity:.5;transform:scale(.8)} }
.hero h1 { font-family:var(--font-serif); font-size:clamp(40px,6vw,72px); font-weight:400; line-height:1.05; letter-spacing:-0.03em; margin-bottom:20px; }
.hero h1 em { font-style:italic; color:var(--green); }
.hero-sub { font-size:17px; color:var(--text-secondary); max-width:520px; margin:0 auto 36px; line-height:1.6; }
.hero-ctas { display:flex; gap:12px; justify-content:center; flex-wrap:wrap; }
.btn-primary { padding:14px 32px; background:var(--green); color:var(--bg); font-family:var(--font); font-size:14px; font-weight:600; border:none; border-radius:var(--radius-sm); cursor:pointer; transition:all var(--transition); text-decoration:none; display:inline-block; }
.btn-primary:hover { opacity:.88; transform:translateY(-1px); }
.btn-secondary { padding:14px 32px; background:transparent; color:var(--text); font-family:var(--font); font-size:14px; font-weight:500; border:1px solid var(--border); border-radius:var(--radius-sm); cursor:pointer; transition:all var(--transition); text-decoration:none; display:inline-block; }
.btn-secondary:hover { border-color:var(--border-hover); background:var(--bg-elevated); }

/* ── Stats Bar ── */
.stats-bar { max-width:1200px; margin:0 auto 80px; padding:0 32px; }
.stats-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:1px; background:var(--border); border-radius:var(--radius); overflow:hidden; }
.stat-item { background:var(--bg-card); padding:24px; text-align:center; }
.stat-val { font-family:var(--font-mono); font-size:28px; font-weight:600; margin-bottom:4px; }
.stat-val.green { color:var(--green); }
.stat-label { font-size:11px; color:var(--text-muted); text-transform:uppercase; letter-spacing:.1em; font-weight:600; }

/* ── Section ── */
.section { max-width:1200px; margin:0 auto; padding:0 32px 80px; }
.section-label { font-size:11px; color:var(--green); text-transform:uppercase; letter-spacing:.15em; font-weight:600; margin-bottom:12px; }
.section-title { font-family:var(--font-serif); font-size:clamp(28px,3.5vw,40px); font-weight:400; margin-bottom:16px; letter-spacing:-0.02em; }
.section-sub { font-size:15px; color:var(--text-secondary); max-width:500px; line-height:1.6; margin-bottom:40px; }

/* ── Signal Preview ── */
.signal-preview { display:grid; grid-template-columns:1fr 1fr; gap:16px; margin-bottom:40px; }
.signal-card { background:var(--bg-card); border:1px solid var(--border); border-radius:var(--radius); padding:20px; position:relative; overflow:hidden; }
.signal-card::before { content:''; position:absolute; left:0; top:0; bottom:0; width:3px; }
.signal-card.buy::before { background:var(--green); }
.signal-card.sell::before { background:var(--red); }
.signal-top { display:flex; justify-content:space-between; align-items:center; margin-bottom:14px; }
.signal-pair { font-size:16px; font-weight:700; }
.signal-dir { font-size:10px; font-weight:700; padding:3px 10px; border-radius:var(--radius-pill); }
.signal-dir.buy { background:var(--green-dim); color:var(--green); }
.signal-dir.sell { background:var(--red-dim); color:var(--red); }
.signal-levels { display:grid; grid-template-columns:1fr 1fr 1fr; gap:8px; margin-bottom:12px; }
.signal-level { text-align:center; }
.signal-level-val { font-family:var(--font-mono); font-size:13px; font-weight:500; }
.signal-level-label { font-size:9px; color:var(--text-muted); text-transform:uppercase; letter-spacing:.06em; margin-top:2px; }
.signal-meta { display:flex; gap:6px; }
.signal-tag { font-size:9px; font-weight:700; padding:2px 8px; border-radius:var(--radius-pill); }
.signal-tag.t1 { background:var(--green-dim); color:var(--green); }
.signal-tag.t2 { background:var(--blue-dim); color:var(--blue); }
.signal-tag.rr { background:var(--bg-elevated); color:var(--text-secondary); }

/* ── How It Works ── */
.steps-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:16px; }
.step-card { background:var(--bg-card); border:1px solid var(--border); border-radius:var(--radius); padding:28px 24px; transition:border-color var(--transition); }
.step-card:hover { border-color:var(--border-hover); }
.step-num { font-family:var(--font-mono); font-size:12px; color:var(--green); font-weight:600; margin-bottom:14px; }
.step-card h3 { font-size:15px; font-weight:600; margin-bottom:8px; }
.step-card p { font-size:13px; color:var(--text-secondary); line-height:1.55; }

/* ── Performance Chart ── */
.perf-card { background:var(--bg-card); border:1px solid var(--border); border-radius:var(--radius); padding:28px; margin-bottom:40px; }
.perf-header { display:flex; justify-content:space-between; align-items:center; margin-bottom:20px; }
.perf-title { font-size:15px; font-weight:600; }
.perf-live { display:flex; align-items:center; gap:6px; font-size:11px; color:var(--green); }
.perf-dot { width:6px; height:6px; background:var(--green); border-radius:50%; animation:pulse 2s infinite; }
.perf-stats { display:grid; grid-template-columns:repeat(4,1fr); gap:16px; margin-top:20px; padding-top:16px; border-top:1px solid var(--border); }
.perf-stat { text-align:center; }
.perf-stat-val { font-family:var(--font-mono); font-size:18px; font-weight:600; }
.perf-stat-label { font-size:10px; color:var(--text-muted); text-transform:uppercase; letter-spacing:.08em; margin-top:2px; }

/* ── Pairs ── */
.pairs-grid { display:flex; flex-wrap:wrap; gap:8px; margin-bottom:40px; }
.pair-chip { background:var(--bg-card); border:1px solid var(--border); border-radius:var(--radius-sm); padding:8px 14px; font-family:var(--font-mono); font-size:12px; font-weight:500; transition:border-color var(--transition); }
.pair-chip:hover { border-color:var(--border-hover); }
.pair-chip span { color:var(--text-muted); font-size:10px; margin-left:6px; }

/* ── Plans ── */
.plans { display:grid; grid-template-columns:repeat(4,1fr); gap:12px; margin-bottom:40px; }
.plan { background:var(--bg-card); border:1px solid var(--border); border-radius:var(--radius); padding:24px 20px; cursor:pointer; transition:all var(--transition); display:flex; flex-direction:column; position:relative; }
.plan:hover { border-color:var(--border-hover); }
.plan.selected { border-color:var(--green); box-shadow:0 0 24px var(--green-dim); }
.plan-check { position:absolute; top:16px; right:16px; width:18px; height:18px; border-radius:50%; border:1.5px solid var(--border); transition:all var(--transition); display:flex; align-items:center; justify-content:center; }
.plan.selected .plan-check { background:var(--green); border-color:var(--green); }
.plan.selected .plan-check::after { content:''; width:6px; height:6px; background:var(--bg); border-radius:50%; }
.popular-flag { position:absolute; top:-1px; left:50%; transform:translateX(-50%); padding:3px 12px; background:var(--green); color:var(--bg); font-size:10px; font-weight:700; letter-spacing:.06em; text-transform:uppercase; border-radius:0 0 6px 6px; }
.plan-tier { font-size:10px; font-weight:700; text-transform:uppercase; letter-spacing:.08em; color:var(--text-muted); margin-bottom:14px; }
.plan-price { margin-bottom:4px; }
.plan-price .val { font-size:32px; font-weight:700; letter-spacing:-0.03em; line-height:1; }
.plan-price .cur { font-size:13px; font-weight:400; color:var(--text-secondary); margin-left:2px; }
.plan-period { font-size:12px; color:var(--text-muted); margin-bottom:14px; }
.plan-divider { width:100%; height:1px; background:var(--border); margin-bottom:14px; }
.plan-desc { font-size:12.5px; color:var(--text-secondary); line-height:1.5; margin-bottom:14px; flex-grow:1; }
.plan-features { list-style:none; display:flex; flex-direction:column; gap:7px; margin-bottom:16px; }
.plan-features li { font-size:12px; color:var(--text-secondary); display:flex; align-items:flex-start; gap:8px; line-height:1.4; }
.feat-icon { flex-shrink:0; width:14px; height:14px; color:var(--text-muted); display:flex; align-items:center; justify-content:center; margin-top:1px; }
.plan.selected .feat-icon { color:var(--green); }
.feat-icon svg { width:10px; height:10px; }
.signal-type-tag { display:inline-block; padding:1px 5px; border-radius:3px; font-size:9px; font-weight:700; font-family:var(--font-mono); letter-spacing:.04em; }
.tag-t1 { background:var(--green-dim); color:var(--green); }
.tag-t2 { background:var(--blue-dim); color:var(--blue); }
.plan-cta { display:block; text-align:center; padding:10px; border-radius:var(--radius-sm); background:var(--bg-elevated); border:1px solid var(--border); color:var(--text); font-family:var(--font); font-size:12px; font-weight:600; text-decoration:none; transition:all var(--transition); }
.plan-cta:hover { border-color:var(--border-hover); background:var(--border); }
.plan.selected .plan-cta { background:var(--green); border-color:var(--green); color:var(--bg); }
.plan-cta-outline { background:transparent; }
body.payment-mode .plan-cta { display:none; }

/* ── Payment Card ── */
.payment-card { background:var(--bg-card); border:1px solid var(--border); border-radius:var(--radius); padding:28px; max-width:480px; margin:0 auto; }
.pay-header { display:flex; justify-content:space-between; align-items:center; margin-bottom:20px; padding-bottom:14px; border-bottom:1px solid var(--border); }
.pay-header-left h3 { font-size:14px; font-weight:600; margin-bottom:2px; }
.pay-header-left span { font-size:11px; color:var(--text-muted); }
.pay-total .amount { font-size:22px; font-weight:700; letter-spacing:-0.02em; }
.pay-total .denom { font-size:11px; color:var(--text-muted); text-align:right; }
.steps-row { display:flex; align-items:center; gap:0; margin-bottom:24px; }
.s-step { display:flex; align-items:center; gap:6px; }
.s-num { width:26px; height:26px; border-radius:50%; border:1.5px solid var(--border); display:flex; align-items:center; justify-content:center; font-size:11px; font-weight:600; color:var(--text-muted); transition:all var(--transition); }
.s-step.active .s-num { background:var(--green); border-color:var(--green); color:var(--bg); }
.s-step.done .s-num { background:var(--green-dim); border-color:var(--green); color:var(--green); }
.s-label { font-size:11px; color:var(--text-muted); font-weight:500; }
.s-step.active .s-label { color:var(--text); }
.s-step.done .s-label { color:var(--green); }
.s-line { flex:1; height:1px; background:var(--border); margin:0 8px; }
.state { display:none; }
.state.visible { display:block; }
.network-pill { display:inline-flex; align-items:center; gap:6px; padding:4px 10px; background:var(--bg-elevated); border-radius:var(--radius-pill); font-family:var(--font-mono); font-size:10px; color:var(--text-muted); margin-bottom:16px; }
.network-pill .net-dot { width:5px; height:5px; background:var(--green); border-radius:50%; }
.btn-pay { width:100%; padding:13px; border:none; border-radius:var(--radius-sm); background:var(--green); color:var(--bg); font-family:var(--font); font-size:14px; font-weight:600; cursor:pointer; transition:all var(--transition); margin-bottom:10px; }
.btn-pay:hover { opacity:.88; }
.btn-outline { width:100%; padding:10px; border:1px solid var(--border); border-radius:var(--radius-sm); background:transparent; color:var(--text-secondary); font-family:var(--font); font-size:12px; cursor:pointer; transition:all var(--transition); }
.btn-outline:hover { background:var(--bg-elevated); }
.pay-hint { text-align:center; font-size:11px; color:var(--text-muted); line-height:1.6; margin-top:8px; }
.pay-hint a { color:var(--green); }
.wallet-info { display:flex; align-items:center; justify-content:space-between; padding:10px 14px; background:var(--bg-elevated); border-radius:var(--radius-sm); margin-bottom:16px; }
.wallet-left { display:flex; align-items:center; gap:8px; }
.wallet-dot { width:7px; height:7px; background:var(--green); border-radius:50%; }
.wallet-addr { font-family:var(--font-mono); font-size:12px; color:var(--text-secondary); }
.wallet-bal { font-size:12px; font-weight:600; }
.processing-view { display:flex; flex-direction:column; align-items:center; gap:12px; padding:24px 0; }
.loader { width:32px; height:32px; border:2.5px solid var(--border); border-top-color:var(--green); border-radius:50%; animation:spin .7s linear infinite; }
@keyframes spin { to{transform:rotate(360deg)} }
.processing-view p { font-size:14px; color:var(--text-secondary); }
.processing-view small { font-size:11px; color:var(--text-muted); }
.success-view { display:flex; flex-direction:column; align-items:center; gap:10px; padding:16px 0; text-align:center; }
.success-check { width:48px; height:48px; background:var(--green-dim); border-radius:50%; display:flex; align-items:center; justify-content:center; animation:pop .4s cubic-bezier(.34,1.56,.64,1); }
.success-check svg { width:20px; height:20px; color:var(--green); }
@keyframes pop { 0%{transform:scale(0)} 100%{transform:scale(1)} }
.success-view h3 { font-family:var(--font-serif); font-size:22px; }
.success-view p { font-size:13px; color:var(--text-secondary); max-width:300px; line-height:1.6; }
.tx-link { display:inline-flex; align-items:center; gap:4px; font-family:var(--font-mono); font-size:11px; color:var(--text-muted); padding:4px 10px; background:var(--bg-elevated); border-radius:var(--radius-pill); }
.tx-link:hover { color:var(--green); }
.free-msg { text-align:center; padding:28px; background:var(--bg-card); border:1px solid var(--border); border-radius:var(--radius); max-width:480px; margin:0 auto; }
.free-msg h3 { font-family:var(--font-serif); font-size:20px; margin-bottom:6px; }
.free-msg p { font-size:13px; color:var(--text-secondary); margin-bottom:14px; }

/* ── Wallet Modal ── */
.wallet-overlay { display:none; position:fixed; inset:0; background:rgba(0,0,0,0.6); backdrop-filter:blur(4px); z-index:1000; align-items:center; justify-content:center; }
.wallet-overlay.open { display:flex; }
.wallet-modal { background:var(--bg-card); border:1px solid var(--border); border-radius:16px; padding:24px; width:90%; max-width:360px; }
.wallet-modal-title { font-size:15px; font-weight:600; margin-bottom:4px; }
.wallet-modal-sub { font-size:11px; color:var(--text-muted); margin-bottom:16px; }
.wallet-list { display:flex; flex-direction:column; gap:6px; }
.wallet-option { display:flex; align-items:center; gap:12px; padding:12px 14px; border:1px solid var(--border); border-radius:var(--radius-sm); cursor:pointer; transition:all var(--transition); }
.wallet-option:hover { border-color:var(--border-hover); background:var(--bg-elevated); }
.wallet-option img, .wallet-option svg { width:32px; height:32px; border-radius:7px; }
.wallet-option-info { flex:1; }
.wallet-option-name { font-size:13px; font-weight:600; }
.wallet-option-desc { font-size:10px; color:var(--text-muted); }
.wallet-option-arrow { color:var(--text-muted); font-size:13px; }
.wallet-option.detected::after { content:'Detected'; font-size:9px; font-weight:600; color:var(--green); background:var(--green-dim); padding:2px 7px; border-radius:20px; }
.wallet-modal-close { width:100%; margin-top:12px; padding:8px; border:none; background:transparent; color:var(--text-muted); font-family:var(--font); font-size:12px; cursor:pointer; }
.wallet-modal-close:hover { color:var(--text); }
.wallet-modal-footer { text-align:center; margin-top:10px; font-size:10px; color:var(--text-muted); }
.wallet-modal-footer a { color:var(--green); }

/* ── Footer ── */
.footer { max-width:1200px; margin:0 auto; padding:40px 32px; border-top:1px solid var(--border); display:flex; justify-content:space-between; align-items:center; }
.footer-left { font-size:12px; color:var(--text-muted); }
.footer-right { font-size:11px; color:var(--text-muted); display:flex; align-items:center; gap:6px; }

/* ── Responsive ── */
@media(max-width:900px) { .plans,.signal-preview { grid-template-columns:repeat(2,1fr); } .steps-grid { grid-template-columns:1fr; } .stats-grid { grid-template-columns:repeat(2,1fr); } }
@media(max-width:580px) { .plans,.signal-preview { grid-template-columns:1fr; } .hero { padding:60px 20px 40px; } .section { padding:0 20px 60px; } .nav { padding:16px 20px; } .perf-stats { grid-template-columns:repeat(2,1fr); } }
@keyframes fadeIn { from{opacity:0;transform:translateY(12px)} to{opacity:1;transform:translateY(0)} }
.fade-in { animation:fadeIn .6s ease both; }
.fade-in-1 { animation-delay:.1s; }
.fade-in-2 { animation-delay:.2s; }
.fade-in-3 { animation-delay:.3s; }
.fade-in-4 { animation-delay:.4s; }
</style>
</head>
<body>

<!-- Nav -->
<nav class="nav">
  <div class="nav-brand">
    <div class="nav-mark">CV</div>
    <span class="nav-name">Cmvng SignalVault</span>
  </div>
  <div class="nav-right">
    <span class="nav-testnet">Arc Testnet · Beta</span>
    <a href="#plans" class="nav-cta">Get Started</a>
  </div>
</nav>

<!-- Hero -->
<section class="hero">
  <div class="hero-content fade-in">
    <div class="hero-badge">
      <span class="hero-badge-dot"></span>
      Live signals · Forex & Crypto
    </div>
    <h1>Precision entries.<br><em>Consistent edge.</em></h1>
    <p class="hero-sub">Limit-order signals with exact entries, exits, SL and TP across 25+ forex & crypto pairs. Delivered instantly to Telegram. Powered by Arc.</p>
    <div class="hero-ctas">
      <a href="#plans" class="btn-primary">View Plans</a>
      <a href="#how" class="btn-secondary">How It Works</a>
    </div>
  </div>
</section>

<!-- Stats Bar -->
<div class="stats-bar fade-in fade-in-1">
  <div class="stats-grid">
    <div class="stat-item"><div class="stat-val">25+</div><div class="stat-label">Active Pairs</div></div>
    <div class="stat-item"><div class="stat-val green">T1 + T2</div><div class="stat-label">Signal Tiers</div></div>
    <div class="stat-item"><div class="stat-val">&lt;1s</div><div class="stat-label">Arc Settlement</div></div>
    <div class="stat-item"><div class="stat-val green">24/7</div><div class="stat-label">Auto Monitoring</div></div>
  </div>
</div>

<!-- Signal Preview -->
<section class="section fade-in fade-in-2">
  <div class="section-label">Live Preview</div>
  <div class="section-title">What signals look like</div>
  <div class="section-sub">Every signal includes precise limit-order levels. You set it and the bot monitors TP/SL for you.</div>
  <div class="signal-preview">
    <div class="signal-card buy">
      <div class="signal-top">
        <span class="signal-pair">XAUUSD</span>
        <span class="signal-dir buy">BUY</span>
      </div>
      <div class="signal-levels">
        <div class="signal-level"><div class="signal-level-val">2,341.50</div><div class="signal-level-label">Entry</div></div>
        <div class="signal-level"><div class="signal-level-val" style="color:var(--red)">2,328.00</div><div class="signal-level-label">Stop Loss</div></div>
        <div class="signal-level"><div class="signal-level-val" style="color:var(--green)">2,370.50</div><div class="signal-level-label">Take Profit</div></div>
      </div>
      <div class="signal-meta">
        <span class="signal-tag t1">T1</span>
        <span class="signal-tag rr">RR 1:2.1</span>
        <span class="signal-tag rr">30M</span>
      </div>
    </div>
    <div class="signal-card sell">
      <div class="signal-top">
        <span class="signal-pair">BTCUSD</span>
        <span class="signal-dir sell">SELL</span>
      </div>
      <div class="signal-levels">
        <div class="signal-level"><div class="signal-level-val">104,250</div><div class="signal-level-label">Entry</div></div>
        <div class="signal-level"><div class="signal-level-val" style="color:var(--red)">105,800</div><div class="signal-level-label">Stop Loss</div></div>
        <div class="signal-level"><div class="signal-level-val" style="color:var(--green)">100,950</div><div class="signal-level-label">Take Profit</div></div>
      </div>
      <div class="signal-meta">
        <span class="signal-tag t1">T1</span>
        <span class="signal-tag rr">RR 1:2.1</span>
        <span class="signal-tag rr">15M</span>
      </div>
    </div>
  </div>
</section>

<!-- How It Works -->
<section class="section fade-in fade-in-3" id="how">
  <div class="section-label">How It Works</div>
  <div class="section-title">From signal to profit in 3 steps</div>
  <div class="section-sub">Fully automated. You just set the trade.</div>
  <div class="steps-grid">
    <div class="step-card">
      <div class="step-num">01</div>
      <h3>Signal fires</h3>
      <p>Custom strategy runs across 25+ pairs on 15M, 30M and 1H timeframes. When conditions align, a signal fires instantly to Telegram.</p>
    </div>
    <div class="step-card">
      <div class="step-num">02</div>
      <h3>You set the order</h3>
      <p>Each signal has exact entry, stop loss and take profit levels. Set a limit order on your broker — that's it.</p>
    </div>
    <div class="step-card">
      <div class="step-num">03</div>
      <h3>Bot monitors 24/7</h3>
      <p>Price checked every 15 minutes. TP hit, SL hit or expired — the bot tells you the result. Fully hands-free.</p>
    </div>
  </div>
</section>

<!-- Performance -->
<section class="section fade-in fade-in-4">
  <div class="section-label">Performance</div>
  <div class="section-title">Transparent results</div>
  <div class="section-sub">Every signal is tracked and verified automatically.</div>
  <div class="perf-card">
    <div class="perf-header">
      <span class="perf-title">Signal Performance</span>
      <span class="perf-live"><span class="perf-dot"></span> Live tracking</span>
    </div>
    <svg width="100%" height="120" viewBox="0 0 800 120" fill="none" preserveAspectRatio="none">
      <defs><linearGradient id="g1" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#22C55E" stop-opacity="0.2"/><stop offset="100%" stop-color="#22C55E" stop-opacity="0"/></linearGradient></defs>
      <path d="M0,100 C40,95 80,85 120,75 C160,65 200,80 240,68 C280,56 320,45 360,50 C400,55 440,38 480,32 C520,26 560,40 600,30 C640,18 680,25 720,20 C760,14 790,16 800,14" stroke="#22C55E" stroke-width="2" fill="none"/>
      <path d="M0,100 C40,95 80,85 120,75 C160,65 200,80 240,68 C280,56 320,45 360,50 C400,55 440,38 480,32 C520,26 560,40 600,30 C640,18 680,25 720,20 C760,14 790,16 800,14 L800,120 L0,120 Z" fill="url(#g1)"/>
    </svg>
    <div class="perf-stats">
      <div class="perf-stat"><div class="perf-stat-val" style="color:var(--green)">T1</div><div class="perf-stat-label">Best Signal Tier</div></div>
      <div class="perf-stat"><div class="perf-stat-val">1:2.15</div><div class="perf-stat-label">Avg Risk:Reward</div></div>
      <div class="perf-stat"><div class="perf-stat-val">25+</div><div class="perf-stat-label">Active Pairs</div></div>
      <div class="perf-stat"><div class="perf-stat-val" style="color:var(--green)">15m</div><div class="perf-stat-label">Check Interval</div></div>
    </div>
  </div>
</section>

<!-- Pairs -->
<section class="section">
  <div class="section-label">Markets</div>
  <div class="section-title">Pairs we trade</div>
  <div class="section-sub">Forex majors, crosses, metals, and top crypto — all monitored 24/7.</div>
  <div class="pairs-grid">
    <div class="pair-chip">XAUUSD <span>T1</span></div>
    <div class="pair-chip">EURJPY <span>T1</span></div>
    <div class="pair-chip">USDJPY <span>T1</span></div>
    <div class="pair-chip">EURUSD <span>T1</span></div>
    <div class="pair-chip">GBPJPY <span>T1</span></div>
    <div class="pair-chip">GBPNZD <span>T1</span></div>
    <div class="pair-chip">NZDCAD <span>T1</span></div>
    <div class="pair-chip">XAGUSD <span>T2</span></div>
    <div class="pair-chip">EURCHF <span>T2</span></div>
    <div class="pair-chip">GBPUSD <span>T2</span></div>
    <div class="pair-chip">BTCUSD <span>Crypto</span></div>
    <div class="pair-chip">ETHUSD <span>Crypto</span></div>
    <div class="pair-chip">SOLUSD <span>Crypto</span></div>
    <div class="pair-chip">ADAUSD <span>Crypto</span></div>
    <div class="pair-chip">BNBUSD <span>Crypto</span></div>
  </div>
</section>

<!-- Plans -->
<section class="section" id="plans">
  <div class="section-label">Pricing</div>
  <div class="section-title">Pick your edge</div>
  <div class="section-sub">Pay with USDC on Arc Testnet. Cancel anytime.</div>

  <div class="plans" id="plansGrid">
    <div class="plan" data-tier="free" data-price="0" onclick="selectPlan(this)">
      <div class="plan-check"></div>
      <div class="plan-tier">Free</div>
      <div class="plan-price"><span class="val">$0</span></div>
      <div class="plan-period">Forever</div>
      <div class="plan-divider"></div>
      <p class="plan-desc">Real signals on real profitable pairs — see for yourself.</p>
      <ul class="plan-features">
        <li><span class="feat-icon"><svg viewBox="0 0 12 12"><path d="M2 6l3 3 5-5" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round"/></svg></span> 1 profitable forex pair</li>
        <li><span class="feat-icon"><svg viewBox="0 0 12 12"><path d="M2 6l3 3 5-5" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round"/></svg></span> 1 profitable crypto pair</li>
        <li><span class="feat-icon"><svg viewBox="0 0 12 12"><path d="M2 6l3 3 5-5" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round"/></svg></span> <span class="signal-type-tag tag-t1">T1</span> + <span class="signal-type-tag tag-t2">T2</span> signals</li>
        <li><span class="feat-icon"><svg viewBox="0 0 12 12"><path d="M2 6l3 3 5-5" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round"/></svg></span> 2 signals per day</li>
      </ul>
      <a href="https://t.me/cmvng_signalvault_bot?start=free" class="plan-cta plan-cta-outline">Get Started Free</a>
    </div>

    <div class="plan selected" data-tier="pro" data-price="15" onclick="selectPlan(this)">
      <div class="plan-check"></div>
      <div class="popular-flag">Popular</div>
      <div class="plan-tier">Pro</div>
      <div class="plan-price"><span class="val">15</span><span class="cur">USDC</span></div>
      <div class="plan-period">per month</div>
      <div class="plan-divider"></div>
      <p class="plan-desc">Real-time signals on all profitable pairs.</p>
      <ul class="plan-features">
        <li><span class="feat-icon"><svg viewBox="0 0 12 12"><path d="M2 6l3 3 5-5" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round"/></svg></span> <span class="signal-type-tag tag-t1">T1</span> + <span class="signal-type-tag tag-t2">T2</span> real-time</li>
        <li><span class="feat-icon"><svg viewBox="0 0 12 12"><path d="M2 6l3 3 5-5" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round"/></svg></span> Profitable pairs unlocked</li>
        <li><span class="feat-icon"><svg viewBox="0 0 12 12"><path d="M2 6l3 3 5-5" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round"/></svg></span> Unlimited signals</li>
        <li><span class="feat-icon"><svg viewBox="0 0 12 12"><path d="M2 6l3 3 5-5" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round"/></svg></span> Win-rate stats</li>
      </ul>
      <a href="https://t.me/cmvng_signalvault_bot?start=pro" class="plan-cta">Get Pro</a>
    </div>

    <div class="plan" data-tier="elite" data-price="50" onclick="selectPlan(this)">
      <div class="plan-check"></div>
      <div class="plan-tier">Elite</div>
      <div class="plan-price"><span class="val">50</span><span class="cur">USDC</span></div>
      <div class="plan-period">per month</div>
      <div class="plan-divider"></div>
      <p class="plan-desc">T1 priority delivery on every pair we track.</p>
      <ul class="plan-features">
        <li><span class="feat-icon"><svg viewBox="0 0 12 12"><path d="M2 6l3 3 5-5" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round"/></svg></span> Everything in Pro</li>
        <li><span class="feat-icon"><svg viewBox="0 0 12 12"><path d="M2 6l3 3 5-5" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round"/></svg></span> <span class="signal-type-tag tag-t1">T1</span> priority delivery</li>
        <li><span class="feat-icon"><svg viewBox="0 0 12 12"><path d="M2 6l3 3 5-5" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round"/></svg></span> All pairs unlocked</li>
        <li><span class="feat-icon"><svg viewBox="0 0 12 12"><path d="M2 6l3 3 5-5" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round"/></svg></span> VIP group</li>
      </ul>
      <a href="https://t.me/cmvng_signalvault_bot?start=elite" class="plan-cta">Get Elite</a>
    </div>

    <div class="plan" data-tier="institutional" data-price="150" onclick="selectPlan(this)">
      <div class="plan-check"></div>
      <div class="plan-tier">Institutional</div>
      <div class="plan-price"><span class="val">150</span><span class="cur">USDC</span></div>
      <div class="plan-period">per month</div>
      <div class="plan-divider"></div>
      <p class="plan-desc">API access and custom pairs for serious capital.</p>
      <ul class="plan-features">
        <li><span class="feat-icon"><svg viewBox="0 0 12 12"><path d="M2 6l3 3 5-5" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round"/></svg></span> Everything in Elite</li>
        <li><span class="feat-icon"><svg viewBox="0 0 12 12"><path d="M2 6l3 3 5-5" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round"/></svg></span> Signal API (webhook)</li>
        <li><span class="feat-icon"><svg viewBox="0 0 12 12"><path d="M2 6l3 3 5-5" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round"/></svg></span> Custom pair requests</li>
        <li><span class="feat-icon"><svg viewBox="0 0 12 12"><path d="M2 6l3 3 5-5" stroke="currentColor" stroke-width="1.5" fill="none" stroke-linecap="round"/></svg></span> 1-on-1 support</li>
      </ul>
      <a href="https://t.me/cmvng_signalvault_bot?start=institutional" class="plan-cta">Get Institutional</a>
    </div>
  </div>

  <!-- Payment Area (only visible when ?tgid= is in URL) -->
  <div id="paymentArea" style="display:none;">
    <div class="free-msg" id="freeMsg" style="display:none;">
      <h3>You're on Free</h3>
      <p>Head back to Telegram and start receiving signals.</p>
      <button class="btn-outline" onclick="window.open('https://t.me/cmvng_signalvault_bot','_blank')">Open Telegram →</button>
    </div>

    <div class="payment-card" id="payCard">
      <div class="pay-header">
        <div class="pay-header-left"><h3 id="payTierLabel">Pro Plan</h3><span>30 days · renew anytime</span></div>
        <div class="pay-total"><div class="amount" id="payAmountDisplay">15 <span style="font-size:14px;font-weight:400;color:var(--text-secondary);">USDC</span></div><div class="denom">on Arc Testnet</div></div>
      </div>
      <div class="steps-row">
        <div class="s-step active" id="s1"><span class="s-num">1</span><span class="s-label">Connect</span></div>
        <div class="s-line"></div>
        <div class="s-step" id="s2"><span class="s-num">2</span><span class="s-label">Pay</span></div>
        <div class="s-line"></div>
        <div class="s-step" id="s3"><span class="s-num">3</span><span class="s-label">Active</span></div>
      </div>

      <div class="state visible" id="stateConnect">
        <div class="network-pill"><span class="net-dot"></span>Arc Testnet · 5042002</div>
        <button class="btn-pay" onclick="connectWallet()">Connect Wallet</button>
        <p class="pay-hint">Supports MetaMask, Zerion, Coinbase, Rabby & more.<br>Arc Testnet added automatically.<br>Need testnet USDC? <a href="https://faucet.circle.com" target="_blank">Get it free →</a></p>
      </div>

      <div class="state" id="statePay">
        <div class="wallet-info"><div class="wallet-left"><span class="wallet-dot"></span><span class="wallet-addr" id="addrDisplay">0x...</span></div><span class="wallet-bal" id="balDisplay">— USDC</span></div>
        <button class="btn-pay" onclick="processPayment()">Pay <span id="payBtnAmount">15</span> USDC</button>
        <p class="pay-hint">Settles in &lt;1 second on Arc.</p>
      </div>

      <div class="state" id="stateAddNetwork">
        <div class="wallet-info"><div class="wallet-left"><span class="wallet-dot"></span><span class="wallet-addr" id="addrDisplayNetwork">0x...</span></div><span class="wallet-bal" style="color:var(--gold)">Wrong network</span></div>
        <p style="font-size:12px;color:var(--text-secondary);text-align:center;margin-bottom:14px;">Your wallet needs <b>Arc Testnet</b> to pay with USDC.</p>
        <button class="btn-pay" onclick="addArcNetwork()">Add Arc Testnet to Wallet</button>
        <button class="btn-outline" onclick="checkNetworkStatus()" style="margin-top:6px;font-size:11px;">I've already added it — continue</button>
      </div>

      <div class="state" id="stateProcessing"><div class="processing-view"><div class="loader"></div><p>Confirming on Arc...</p><small>Sub-second finality</small></div></div>

      <div class="state" id="stateSuccess"><div class="success-view">
        <div class="success-check"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M5 12l5 5L19 7"/></svg></div>
        <h3>You're in</h3>
        <p><strong id="successTierName">Pro</strong> is live. Head back to Telegram — signals are flowing.</p>
        <a class="tx-link" href="https://testnet.arcscan.app" target="_blank">View on ArcScan ↗</a>
        <button class="btn-outline" style="margin-top:8px;" onclick="window.open('https://t.me/cmvng_signalvault_bot','_blank')">Back to Telegram →</button>
      </div></div>
    </div>
  </div>
</section>

<!-- Footer -->
<footer class="footer">
  <div class="footer-left">Cmvng SignalVault · Built on Arc</div>
  <div class="footer-right">Powered by Arc · &lt;1s settlement</div>
</footer>

<!-- Wallet Modal -->
<div class="wallet-overlay" id="walletModal">
  <div class="wallet-modal">
    <div class="wallet-modal-title">Connect Wallet</div>
    <div class="wallet-modal-sub">Pay with USDC on Arc Testnet</div>
    <div class="wallet-list" id="walletList"></div>
    <button class="wallet-modal-close" onclick="closeWalletModal()">Cancel</button>
    <div class="wallet-modal-footer">No wallet? <a href="https://metamask.io" target="_blank">Get MetaMask</a></div>
  </div>
</div>

<script>
  // ── Config ──
  const ARC_TESTNET_CHAIN_ID = '0x4CEF52';
  const ARC_TESTNET_CONFIG = { chainId:ARC_TESTNET_CHAIN_ID, chainName:'Arc Testnet', rpcUrls:['https://rpc.quicknode.testnet.arc.network'], nativeCurrency:{name:'USDC',symbol:'USDC',decimals:18}, blockExplorerUrls:['https://testnet.arcscan.app'] };
  const MERCHANT_WALLET = '0x751174BF2269e13663C5a37fd9dD7714079ED0e3';
  const API_URL = 'https://cmvng-payment-api-production.up.railway.app';
  const COMPANION_BOT_URL = 'https://web-production-a372f5.up.railway.app';
  let connectedAddress = '';
  let selectedTier = 'pro';
  let selectedPrice = 15;

  // ── Plan Selection ──
  window.selectPlan = function(el) {
    document.querySelectorAll('.plan').forEach(p => p.classList.remove('selected'));
    el.classList.add('selected');
    selectedTier = el.dataset.tier;
    selectedPrice = parseInt(el.dataset.price);
    const names = {free:'Free',pro:'Pro',elite:'Elite',institutional:'Institutional'};
    if (selectedTier === 'free') { document.getElementById('payCard').style.display='none'; document.getElementById('freeMsg').style.display='block'; }
    else { document.getElementById('payCard').style.display='block'; document.getElementById('freeMsg').style.display='none'; document.getElementById('payTierLabel').textContent=names[selectedTier]+' Plan'; document.getElementById('payAmountDisplay').innerHTML=selectedPrice+' <span style="font-size:14px;font-weight:400;color:var(--text-secondary);">USDC</span>'; document.getElementById('payBtnAmount').textContent=selectedPrice; showState('stateConnect'); resetSteps(); }
  };

  function showState(id){document.querySelectorAll('.state').forEach(s=>s.classList.remove('visible'));document.getElementById(id).classList.add('visible');}
  function resetSteps(){['s1','s2','s3'].forEach(s=>{document.getElementById(s).classList.remove('active','done')});document.getElementById('s1').classList.add('active');}
  function stepTo(n){['s1','s2','s3'].forEach((s,i)=>{const el=document.getElementById(s);el.classList.remove('active','done');if(i+1<n)el.classList.add('done');if(i+1===n)el.classList.add('active')});}

  // ── Wallet Definitions ──
  const WALLETS=[{name:'MetaMask',icon:'https://upload.wikimedia.org/wikipedia/commons/3/36/MetaMask_Fox.svg',check:p=>p&&p.isMetaMask},{name:'Rabby',icon:'https://rabby.io/assets/images/logo.svg',check:p=>p&&p.isRabby},{name:'Coinbase Wallet',icon:'https://altcoinsbox.com/wp-content/uploads/2022/12/coinbase-logo-300x300.webp',check:p=>p&&(p.isCoinbaseWallet||p.isCoinbaseBrowser)},{name:'Zerion',icon:'https://app.zerion.io/favicon-256.png',check:p=>p&&p.isZerion},{name:'Brave Wallet',icon:'https://brave.com/static-assets/images/brave-logo-sans-text.svg',check:p=>p&&p.isBraveWallet},{name:'Trust Wallet',icon:'https://trustwallet.com/assets/images/media/assets/TWT.svg',check:p=>p&&p.isTrust}];

  function openWalletModal(){const modal=document.getElementById('walletModal'),list=document.getElementById('walletList');list.innerHTML='';const all=[];if(window.ethereum){if(window.ethereum.providers&&window.ethereum.providers.length>0)window.ethereum.providers.forEach(p=>all.push(p));else all.push(window.ethereum);}if(!all.length){list.innerHTML='<div style="text-align:center;padding:20px;color:var(--text-muted)"><p style="font-size:14px;margin-bottom:8px;color:var(--text)">No wallet detected</p><p style="font-size:12px">Install <a href="https://metamask.io" target="_blank">MetaMask</a> or <a href="https://rabby.io" target="_blank">Rabby</a></p></div>';modal.classList.add('open');return;}const matched=[],used=new Set();WALLETS.forEach(w=>{for(let i=0;i<all.length;i++){if(!used.has(i)&&w.check(all[i])){matched.push({wallet:w,provider:all[i]});used.add(i);break;}}});all.forEach((p,i)=>{if(!used.has(i))matched.push({wallet:{name:'Browser Wallet',icon:''},provider:p});});matched.forEach(m=>{const btn=document.createElement('div');btn.className='wallet-option detected';const ic=m.wallet.icon?'<img src="'+m.wallet.icon+'" onerror="this.style.display=\'none\'">':'<div style="width:32px;height:32px;background:var(--bg-elevated);border-radius:7px;display:flex;align-items:center;justify-content:center">🔗</div>';btn.innerHTML=ic+'<div class="wallet-option-info"><div class="wallet-option-name">'+m.wallet.name+'</div><div class="wallet-option-desc">Ready to connect</div></div><span class="wallet-option-arrow">›</span>';btn.onclick=function(){closeWalletModal();connectWithProvider(m.provider,m.wallet.name);};list.appendChild(btn);});modal.classList.add('open');}
  function closeWalletModal(){document.getElementById('walletModal').classList.remove('open');}
  document.addEventListener('click',e=>{if(e.target.id==='walletModal')closeWalletModal();});
  function connectWallet(){openWalletModal();}

  async function connectWithProvider(provider,walletName){try{const accounts=await provider.request({method:'eth_requestAccounts'});connectedAddress=accounts[0];window._arcProvider=provider;const short=connectedAddress.slice(0,6)+'...'+connectedAddress.slice(-4);let currentChain='';try{currentChain=await provider.request({method:'eth_chainId'});}catch(e){}let onArc=(currentChain===ARC_TESTNET_CHAIN_ID);if(!onArc){try{await provider.request({method:'wallet_switchEthereumChain',params:[{chainId:ARC_TESTNET_CHAIN_ID}]});onArc=true;}catch(se){if(se.code===4902||se.message&&(se.message.includes('Unrecognized')||se.message.includes('not added'))){try{await provider.request({method:'wallet_addEthereumChain',params:[ARC_TESTNET_CONFIG]});try{const nc=await provider.request({method:'eth_chainId'});onArc=(nc===ARC_TESTNET_CHAIN_ID);}catch(e){}if(!onArc){try{await provider.request({method:'wallet_switchEthereumChain',params:[{chainId:ARC_TESTNET_CHAIN_ID}]});onArc=true;}catch(e){}}}catch(ae){}}}}if(onArc){document.getElementById('addrDisplay').textContent=short;try{const bal=await provider.request({method:'eth_getBalance',params:[connectedAddress,'latest']});document.getElementById('balDisplay').textContent=(parseInt(bal,16)/1e6).toFixed(2)+' USDC';}catch(e){document.getElementById('balDisplay').textContent='— USDC';}stepTo(2);showState('statePay');}else{document.getElementById('addrDisplayNetwork').textContent=short;stepTo(2);showState('stateAddNetwork');}}catch(err){if(err.code===4001)alert('Connection cancelled.');else alert('Failed to connect '+walletName+'. Make sure it is unlocked.');}}

  async function addArcNetwork(){const p=window._arcProvider||window.ethereum;try{await p.request({method:'wallet_addEthereumChain',params:[{chainId:'0x4CEF52',chainName:'Arc Testnet',rpcUrls:['https://rpc.quicknode.testnet.arc.network'],nativeCurrency:{name:'USDC',symbol:'USDC',decimals:18},blockExplorerUrls:['https://testnet.arcscan.app']}]});try{await p.request({method:'wallet_switchEthereumChain',params:[{chainId:'0x4CEF52'}]});}catch(e){}await checkNetworkStatus();}catch(err){if(err.code===4001)alert('Please approve adding the network in your wallet.');else alert('Auto-add failed.\n\nAdd manually:\nNetwork: Arc Testnet\nRPC: https://rpc.testnet.arc.network\nChain ID: 5042002\nSymbol: USDC\n\nThen click "I\'ve already added it"');}}

  async function checkNetworkStatus(){const p=window._arcProvider||window.ethereum;try{const c=await p.request({method:'eth_chainId'});if(c===ARC_TESTNET_CHAIN_ID){const short=connectedAddress.slice(0,6)+'...'+connectedAddress.slice(-4);document.getElementById('addrDisplay').textContent=short;try{const bal=await p.request({method:'eth_getBalance',params:[connectedAddress,'latest']});document.getElementById('balDisplay').textContent=(parseInt(bal,16)/1e6).toFixed(2)+' USDC';}catch(e){document.getElementById('balDisplay').textContent='— USDC';}showState('statePay');}else{alert('Still not on Arc Testnet. Switch in your wallet and try again.');}}catch(e){alert('Could not check. Try again.');}}

  async function processPayment(){showState('stateProcessing');stepTo(3);const params=new URLSearchParams(window.location.search);const tgid=params.get('tgid')||'';const tierMap={pro:1,elite:2,institutional:3};const tierNum=tierMap[selectedTier]||1;try{const provider=window._arcProvider||window.ethereum;var hex='0x'+(BigInt(selectedPrice)*1000000000000000000n).toString(16);const txHash=await provider.request({method:'eth_sendTransaction',params:[{from:connectedAddress,to:MERCHANT_WALLET,value:hex}]});const res=await fetch(API_URL+'/activate',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({user_id:tgid,tier:tierNum,wallet_address:connectedAddress,amount_usdc:selectedPrice,tx_hash:txHash})});const data=await res.json();if(data.ok){const names={pro:'Pro',elite:'Elite',institutional:'Institutional'};document.getElementById('successTierName').textContent=names[selectedTier];const txLink=document.querySelector('.tx-link');if(txLink)txLink.href='https://testnet.arcscan.app/tx/'+txHash;if(tgid){try{await fetch(COMPANION_BOT_URL+'/notify',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({user_id:tgid,tier_name:names[selectedTier],amount:selectedPrice,tx_hash:txHash})});}catch(e){}}showState('stateSuccess');document.getElementById('s3').classList.add('done');}else{throw new Error(data.reason||'Failed');}}catch(err){showState('statePay');stepTo(2);if(err.code===4001)alert('Transaction cancelled.');else if(err.message&&err.message.includes('insufficient'))alert('Not enough USDC!\nGet free testnet USDC at faucet.circle.com');else alert('Payment failed: '+(err.message||JSON.stringify(err)));}}

  // ── Init ──
  (function(){const p=new URLSearchParams(window.location.search);const tgid=p.get('tgid');const tier=p.get('tier');if(tgid){document.body.classList.add('payment-mode');document.getElementById('paymentArea').style.display='block';if(tier){const el=document.querySelector('[data-tier="'+tier+'"]');if(el)selectPlan(el);}}else{document.getElementById('paymentArea').style.display='none';}})();
</script>
</body>
</html>
