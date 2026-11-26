"""Static site generator for London Momentum (GitHub Pages now, WordPress later).
python3 src/build.py  -> writes HTML into the repo root."""
import json, html, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from content import TOPICS, ARTICLES, SRC, CLASSES, TIMETABLE

R = Path(__file__).resolve().parent.parent
SITE = 'London Momentum'
IG = 'https://www.instagram.com/ldnmomentum/'
FB = 'https://www.facebook.com/LondonMomentum'
TOP = {t['slug']: t for t in TOPICS}
E = lambda s: html.escape(s, quote=True)
strip = lambda s: re.sub('<[^>]+>', '', s)

LOGO = '''<svg viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="20" r="19" fill="#0B2342"/><path d="M9 26c4-9 9-13 15-13" fill="none" stroke="#12A27B" stroke-width="4" stroke-linecap="round"/><path d="M13 30c4-6 8-9 14-9" fill="none" stroke="#FF5A4E" stroke-width="4" stroke-linecap="round"/><path d="M24 9l7 4-5 6" fill="none" stroke="#FFC845" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'''
ICO_IG = '<svg viewBox="0 0 24 24"><path d="M12 7a5 5 0 100 10 5 5 0 000-10zm0 8.2A3.2 3.2 0 1112 8.8a3.2 3.2 0 010 6.4zM17.3 5.5a1.2 1.2 0 100 2.4 1.2 1.2 0 000-2.4zM21.9 7.1c-.1-1.6-.4-3-1.6-4.2S17.6 1.3 16 1.2C14.3 1.1 9.7 1.1 8 1.2c-1.6.1-3 .4-4.2 1.6S2.2 5.4 2.1 7.1C2 8.8 2 13.2 2.1 14.9c.1 1.6.4 3 1.6 4.2s2.6 1.5 4.2 1.6c1.7.1 6.3.1 8 0 1.6-.1 3-.4 4.2-1.6s1.5-2.6 1.6-4.2c.1-1.7.1-6.1 0-7.8zM19.8 17a3.3 3.3 0 01-1.8 1.8c-1.3.5-4.3.4-5.7.4s-4.4.1-5.7-.4A3.3 3.3 0 014.8 17c-.5-1.3-.4-4.3-.4-5.7s-.1-4.4.4-5.7A3.3 3.3 0 016.6 3.8c1.3-.5 4.3-.4 5.7-.4s4.4-.1 5.7.4a3.3 3.3 0 011.8 1.8c.5 1.3.4 4.3.4 5.7s.1 4.4-.4 5.7z"/></svg>'
ICO_FB = '<svg viewBox="0 0 24 24"><path d="M14 8V6c0-.9.2-1.4 1.6-1.4H18V1h-3.3C11.2 1 10 2.7 10 5.6V8H7.5v3.5H10V23h4V11.5h3.3L18 8z"/></svg>'

NAV = [('Topics', 'topics/'), ('Tools', 'tools/'), ('Classes', 'classes/'), ('About', 'about/'), ('Contact', 'contact/')]

def emo(n, cls='e', size=None):
    s = f' width="{size}" height="{size}"' if size else ''
    return f'<img class="{cls}" src="{{root}}assets/emoji/{n}.svg" alt=""{s} loading="lazy">'

def fixlinks(h):
    def f(m):
        v = m.group(2)
        if v.startswith(('http', '#', 'mailto')) or not v: return m.group(0)
        mm = re.match(r'^((?:\.\./)*)([^?#]*?)(/?)([?#].*)?$', v)
        pre, body, sl, tail = mm.group(1), mm.group(2), mm.group(3), mm.group(4) or ''
        if sl and body and body != '.': return f'{m.group(1)}="{pre}{body}.html{tail}"'
        return m.group(0)
    return re.sub(r'(href)="([^"]*)"', f, h)

def page(path, title, body, desc='', active='', extra_head=''):
    if path == '': path = 'index.html'
    elif path.endswith('/'): path = path[:-1] + '.html'
    depth = path.count('/')
    root = '../' * depth or './'
    nav = ''.join(f'<a href="{root}{u}"{" aria-current=page" if active == u else ""}>{n}</a>' for n, u in NAV)
    full = f'''<!doctype html>
<html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}{"" if title == SITE else " | " + SITE}</title>
<meta name="description" content="{E(desc or 'London Momentum – friendly, evidence-based tips, tools and online classes to help Londoners move more, eat well and feel better.')}">
<meta property="og:title" content="{E(title)}"><meta property="og:site_name" content="{SITE}"><meta property="og:locale" content="en_GB">
<meta name="theme-color" content="#0B2342"><link rel="icon" href="{root}assets/favicon.svg" type="image/svg+xml">
<link rel="preload" href="{root}assets/fonts/bricolage-grotesque-latin-800-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{root}assets/css/site.css">{extra_head}</head>
<body data-root="{root}">
<a class="skip" href="#main">Skip to main content</a>
<div class="preview">🚧 <b>Preview site</b> – content is live, online class booking is coming soon.</div>
<header class="hdr"><div class="wrap">
<a class="logo" href="{root}">{LOGO}<span>London Momentum<small>MOVE · EAT · THRIVE</small></span></a>
<button class="burger" aria-label="Menu" aria-expanded="false">☰</button>
<nav class="nav" aria-label="Main">{nav}</nav>
<a class="btn btn-p" href="{root}classes/">Book a class</a>
</div></header>
<main id="main">{body}</main>
<footer class="ftr"><div class="wrap"><div class="cols">
<div><a class="logo" href="{root}">{LOGO}<span>London Momentum<small>MOVE · EAT · THRIVE</small></span></a>
<p style="margin-top:14px;max-width:320px">Friendly, evidence-based health tips, tools and online classes for Londoners. Every fact we share comes with its source.</p>
<div class="soc"><a href="{IG}" aria-label="Instagram" rel="noopener" target="_blank">{ICO_IG}</a><a href="{FB}" aria-label="Facebook" rel="noopener" target="_blank">{ICO_FB}</a></div></div>
<div><h4>Topics</h4>{''.join(f'<a href="{root}topics/{t["slug"]}/">{t["name"]}</a>' for t in TOPICS)}</div>
<div><h4>Tools</h4><a href="{root}tools/#bmi">BMI calculator</a><a href="{root}tools/#waist">Waist-to-height ratio</a><a href="{root}tools/#activity">Activity tracker</a><a href="{root}tools/#alcohol">Alcohol units</a><a href="{root}tools/#water">Water tracker</a><a href="{root}tools/#five">5 A Day counter</a></div>
<div><h4>London Momentum</h4><a href="{root}about/">About us</a><a href="{root}classes/">Online classes</a><a href="{{root}}contact/">Contact</a><a href="{{root}}privacy/">Privacy policy</a><a href="{root}cookies/">Cookies</a><a href="{root}disclaimer/">Medical disclaimer</a><a href="{root}accessibility/">Accessibility</a></div>
</div>
<div class="disc"><span>The information on this site is for general education only and isn’t a substitute for advice from your GP or another health professional. In an emergency call 999; for urgent advice call NHS 111.</span><span>© 2026 London Momentum</span></div>
</div></footer>
<button class="fab" hidden aria-label="Open your weekly activity tracker"><span class="mini"><i></i></span><span></span></button>
<div class="cookie" role="dialog" aria-label="Cookies"><b>No tracking cookies here 🍪</b><p style="margin-top:6px">We don’t use advertising or analytics cookies. Your tool results stay in your own browser. <a href="{root}cookies/">Learn more</a></p><div class="b"><button class="btn btn-n" style="padding:10px 16px">OK, got it</button></div></div>
<script src="{root}assets/js/site.js" defer></script>
</body></html>'''
    full = full.replace('{{root}}', '{root}').replace('{root}', root)
    full = fixlinks(full)
    out = R / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(full, encoding='utf-8')

def img(p, alt, cls='', zoom=False, lazy=True):
    z = f' data-zoom="{{root}}assets/img/{p}.webp"' if zoom else ''
    return f'<img src="{{root}}assets/img/{p}.webp" alt="{E(alt)}"{z}{" loading=lazy" if lazy else ""}{f" class={cls}" if cls else ""} width="900" height="1125">'

def card(a):
    t = TOP[a['topic']]
    return f'''<a class="card" href="{{root}}articles/{a['slug']}/"><div class="im">{img(a['img'], a['title'])}</div><div class="bd"><div class="tg" style="color:{t['color']}">{t['name']}{' · Guide' if a['kind'] == 'guide' else ''}</div><h3>{E(a['title'])}</h3><p>{E(a['excerpt'])}</p></div></a>'''

def topic_card(t):
    n = sum(1 for a in ARTICLES if a['topic'] == t['slug'])
    return f'''<a class="topic" href="{{root}}topics/{t['slug']}/" style="--t:{t['tint']};--c:{t['color']}"><span class="n">{n} guides</span>{emo(t['emoji'])}<h3>{t['name']}</h3><p>{E(t['lead'][:110].rsplit(' ', 1)[0])}…</p></a>'''

QUIZ = [
 dict(s='Only exercise at the gym counts towards your 150 minutes a week.', f=False, e='Brisk walking, cycling, dancing and gardening all count.', l='myth-vs-fact-exercise'),
 dict(s='1 minute of vigorous activity counts as about 2 minutes of moderate activity.', f=True, e='That’s why 75 vigorous minutes give similar benefits to 150 moderate minutes.', l='how-much-should-you-move'),
 dict(s='Frozen and tinned fruit and vegetables count towards your 5 A Day.', f=True, e='Fresh, frozen, tinned and dried all count.', l='eat-the-rainbow-5-a-day'),
 dict(s='With most back pain, bed rest is the best way to recover.', f=False, e='Staying active usually helps you recover faster.', l='back-pain-keep-moving'),
 dict(s='Tea and coffee count towards your 6–8 drinks a day.', f=True, e='Water, lower-fat milk and sugar-free drinks including tea and coffee all count.', l='stay-hydrated'),
 dict(s='Short bursts of activity are too short to make a difference.', f=False, e='Activity of any length adds up and benefits your health.', l='150-minutes-is-21-a-day'),
 dict(s='The UK low-risk drinking guideline is no more than 14 units a week.', f=True, e='For both men and women, spread over 3 or more days.', l='four-habits-that-protect-your-health'),
 dict(s='If you’re over 65, it’s too late to start strength exercises.', f=False, e='It’s never too late – adults over 65 are advised to do strength and balance activities on 2 days a week.', l='whats-stopping-you'),
]

# ------------------------------------------------------------------ HOME
def home():
    guides = [a for a in ARTICLES if a['kind'] == 'guide']
    tips = [a for a in ARTICLES if a['kind'] == 'tip']
    pick = [tips[i] for i in (1, 7, 13, 19, 24, 26, 28, 4)]
    igimgs = ['beat-the-barriers/slide-01', 'move-for-your-health/heart-8-million', 'healthy-eating/five-a-day', 'physical-activity/150-minutes', 'healthy-lifestyle/support-team', 'beat-the-barriers/your-why',
              'healthy-eating/swaps', 'move-for-your-health/back-pain', 'physical-activity/types', 'healthy-lifestyle/who-definition', 'beat-the-barriers/small-wins', 'healthy-eating/hydration']
    acts = [('walk', 'person_walking', 'Walk'), ('run', 'person_running', 'Run'), ('cycle', 'person_biking', 'Cycle'), ('gym', 'person_lifting_weights', 'Gym'), ('yoga', 'person_in_lotus_position', 'Yoga'), ('swim', 'person_swimming', 'Swim'), ('dance', 'man_dancing', 'Dance'), ('none', 'couch_and_lamp', 'Nothing yet')]
    goals = [('move', 'Move more'), ('eat', 'Eat better'), ('calm', 'Feel calmer'), ('weight', 'Healthy weight'), ('strong', 'Get stronger'), ('start', 'Just get started')]
    body = f'''
<section class="hero"><div class="wrap">
<div>
<div class="eyebrow">Health &amp; fitness for Londoners</div>
<h1>Move more.<br>Feel better.<br><span>Every day.</span></h1>
<p class="lead">Friendly, evidence-based tips, free health tools and online classes – built around real London life. Every fact comes with its source.</p>
<div class="ctas"><a class="btn btn-p" href="classes/">Book an online class →</a><a class="btn btn-o" href="tools/">Try our health tools</a></div>
<div class="stats"><div><b>{len(ARTICLES)}</b>guides &amp; tips</div><div><b>6</b>free health tools</div><div><b>{len(CLASSES)}</b>online classes</div><div><b>100%</b>sourced facts</div></div>
</div>
<div class="checkin" id="checkin" aria-live="polite">
 <div class="step"><div class="eyebrow" id="ci-hello">Hello! 👋</div><h3>How long have you been active today?</h3><p class="q">Walking to the Tube counts too.</p>
  <div class="bigval" id="ci-val">0<small> min</small></div><input class="range" id="ci-range" type="range" min="0" max="120" step="5" value="0" aria-label="Active minutes today">
  <div class="chips">{''.join(f'<button class="chip" data-min="{m}">{m} min</button>' for m in (0, 10, 20, 30, 45, 60))}</div></div>
 <div class="step"><div class="eyebrow">Question 2 of 4</div><h3>What did you do?</h3><p class="q">Pick the main one.</p>
  <div class="chips">{''.join(f'<button class="chip" data-what="{k}">{emo(e, "", 22)}{n}</button>' for k, e, n in acts)}</div></div>
 <div class="step"><div class="eyebrow">Question 3 of 4</div><h3>How are you feeling today?</h3><p class="q">Be honest – there’s no wrong answer.</p>
  <div class="mood">{''.join(f'<button data-v="{i + 1}" aria-label="{l}">{f}</button>' for i, (f, l) in enumerate([('😞', 'Low'), ('😕', 'Meh'), ('🙂', 'OK'), ('😊', 'Good'), ('🤩', 'Great')]))}</div></div>
 <div class="step"><div class="eyebrow">Last one</div><h3>What would you like help with?</h3><p class="q">We’ll point you to the right place.</p>
  <div class="chips">{''.join(f'<button class="chip" data-goal="{k}">{n}</button>' for k, n in goals)}</div></div>
 <div class="step" id="ci-result"></div>
 <div class="ci-foot"><button class="link" id="ci-back">← Back</button><div class="dots"><i></i><i></i><i></i><i></i></div><button class="btn btn-n" id="ci-next" style="padding:10px 18px">Next →</button></div>
 <p style="font-size:12px;color:var(--mut);margin-top:14px">🔒 Your answers stay on this device.</p>
</div>
</div></section>

<section style="padding-top:40px"><div class="wrap">
<div class="sec-h"><div><div class="eyebrow">Explore</div><h2>Pick a topic</h2><p>Bite-sized guides based on NHS and UK government advice – the same content you know from our Instagram.</p></div><a class="btn btn-o" href="topics/">All topics</a></div>
<div class="grid g5">{''.join(topic_card(t) for t in TOPICS)}</div>
</div></section>

<section style="background:var(--sky)"><div class="wrap">
<div class="quiz" id="quiz"><div><div class="eyebrow">60-second challenge</div><h2>Myth or fact?</h2><p style="color:var(--mut);margin-top:10px">Think you know your health facts? Test yourself – every answer links to the evidence.</p><p class="score" style="margin-top:18px"></p></div>
<div><p class="stmt"></p><div class="ans"><button class="btn btn-g" data-a="fact">✓ Fact</button><button class="btn btn-p" data-a="myth">✗ Myth</button></div><div class="fb"></div><button class="link" id="qz-next" hidden style="margin-top:12px"></button></div></div>
<script type="application/json" id="quiz-data">{json.dumps(QUIZ)}</script>
</div></section>

<section><div class="wrap">
<div class="sec-h"><div><div class="eyebrow">Start here</div><h2>Our essential guides</h2></div></div>
<div class="grid g5">{''.join(card(a) for a in guides)}</div>
</div></section>

<section class="band"><div class="wrap">
<div class="sec-h"><div><div class="eyebrow">Free health tools</div><h2>Know your numbers</h2><p style="color:#b9c7d8">Quick, private calculators based on NHS, NICE and UK Chief Medical Officers’ guidance.</p></div><a class="btn btn-p" href="tools/">Open the tools</a></div>
<div class="grid g3">
{''.join(f'<a class="tool-teaser" href="tools/#{k}">{emo(e)}<h3>{n}</h3><p>{d}</p></a>' for k, e, n, d in [('bmi', 'bar_chart', 'BMI calculator', 'Metric or stones &amp; pounds, with NICE ethnicity-adjusted ranges.'), ('waist', 'person_standing', 'Waist-to-height ratio', 'Keep your waist to less than half your height.'), ('activity', 'stopwatch', 'Weekly activity tracker', 'Log your minutes and watch your ring fill to 150.'), ('alcohol', 'clipboard', 'Alcohol unit counter', 'Pints, glasses and shots – how many units is your week?'), ('water', 'droplet', 'Water tracker', 'Tap a glass each time you drink. Aim for 6–8.'), ('five', 'broccoli', '5 A Day counter', 'Count your fruit and veg portions today.')])}
</div></div></section>

<section><div class="wrap">
<div class="sec-h"><div><div class="eyebrow">Online classes</div><h2>Train with us, from anywhere in London</h2><p>Short, friendly online sessions at times that fit around work, school runs and the commute.</p></div><a class="btn btn-p" href="classes/">See the timetable</a></div>
<div class="grid g3">{''.join(f'<div class="cls">{emo(c["emoji"])}<h3 style="margin-top:12px">{c["name"]}</h3><div class="meta"><span class="pill">{c["mins"]} min</span><span class="pill">{c["level"]}</span><span class="pill">Online</span></div><p style="color:var(--mut);font-size:15px">{c["desc"]}</p><a href="classes/?c={c["id"]}" style="display:inline-block;margin-top:12px;font-weight:700">See times →</a></div>' for c in CLASSES[:3])}</div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<div class="sec-h"><div><div class="eyebrow">Latest tips</div><h2>Fresh from the feed</h2></div><a class="btn btn-o" href="topics/">Browse everything</a></div>
<div class="grid g4">{''.join(card(a) for a in pick)}</div>
</div></section>

<section style="padding-top:0"><div class="wrap">
<div class="sec-h"><div><div class="eyebrow">@ldnmomentum</div><h2>Follow us on Instagram</h2><p>New tips every day, plus behind-the-scenes from our classes.</p></div><a class="btn btn-n" href="{IG}" target="_blank" rel="noopener">Follow @ldnmomentum</a></div>
<div class="ig">{''.join(f'<a href="{IG}" target="_blank" rel="noopener" aria-label="View on Instagram">{img(p, "Instagram post")}</a>' for p in igimgs)}</div>
</div></section>

<section style="padding-top:0"><div class="wrap"><div class="nl">
<div><h2>One small win, every week 💌</h2><p style="margin-top:10px;opacity:.9">A short email with one tip, one tool and one class to try. No spam, unsubscribe any time.</p></div>
<form data-preview="Thanks! Our newsletter launches soon – we’ll keep you posted."><input type="email" required placeholder="Your email address" aria-label="Email address"><button class="btn btn-n">Sign me up</button><p style="font-size:12.5px;opacity:.85;width:100%">By signing up you agree to our <a href="privacy/" style="color:#fff">privacy policy</a>.</p></form>
</div></div></section>'''
    page('', SITE, body)

# ------------------------------------------------------------------ TOPICS
def topics():
    body = f'''<div class="phead"><div class="wrap"><div class="crumbs"><a href="{{root}}">Home</a> / Topics</div><h1>Topics</h1><p>Every topic matches a series on our Instagram – expanded here with more detail and full sources.</p></div></div>
<section style="padding-top:50px"><div class="wrap"><div class="grid g3">{''.join(topic_card(t) for t in TOPICS)}</div></div></section>'''
    page('topics/', 'Topics', body, active='topics/')
    for t in TOPICS:
        arts = [a for a in ARTICLES if a['topic'] == t['slug']]
        g = next(a for a in arts if a['kind'] == 'guide')
        others = ''.join(topic_card(x) for x in TOPICS if x is not t)
        body = f'''<div class="phead" style="--t:{t['tint']}"><div class="wrap" style="display:flex;gap:30px;align-items:center;justify-content:space-between;flex-wrap:wrap"><div><div class="crumbs"><a href="{{root}}">Home</a> / <a href="{{root}}topics/">Topics</a> / {t['name']}</div><h1 style="color:{t['color']}">{t['name']}</h1><p>{t['lead']}</p></div>{emo(t['emoji'], 'e', 140)}</div></div>
<section style="padding-top:50px"><div class="wrap">
<a class="card" href="{{root}}articles/{g['slug']}/" style="flex-direction:row;flex-wrap:wrap;margin-bottom:40px"><div class="im" style="flex:0 0 320px;max-width:100%">{img(g['img'], g['title'])}</div><div class="bd" style="flex:1;min-width:260px;padding:34px"><div class="tg" style="color:{t['color']}">Start with the guide · {g['mins']} min read</div><h2 style="margin:12px 0">{E(g['title'])}</h2><p style="font-size:17px">{E(g['excerpt'])}</p><span class="btn btn-n" style="margin-top:20px">Read the guide →</span></div></a>
<h2 style="margin-bottom:24px">Quick tips</h2><div class="grid g3">{''.join(card(a) for a in arts if a['kind'] == 'tip')}</div>
</div></section>
<section style="padding-top:0"><div class="wrap"><h2 style="margin-bottom:24px">More topics</h2><div class="grid g4">{others}</div></div></section>'''
        page(f"topics/{t['slug']}/", t['name'], body, desc=t['lead'], active='topics/')

# ------------------------------------------------------------------ ARTICLES
def articles():
    for a in ARTICLES:
        t = TOP[a['topic']]
        more = [x for x in ARTICLES if x['topic'] == a['topic'] and x is not a][:5]
        srcs = ''.join(f'<li><a href="{SRC[k][1]}" target="_blank" rel="noopener">{SRC[k][0]}</a></li>' for k in a['sources'])
        gal = ''
        if a.get('gallery'):
            gal = '<p style="font:700 14px DM;margin-top:18px">The full Instagram carousel</p><div class="gal">' + ''.join(img(p, f'Slide {i + 1}', zoom=True) for i, p in enumerate(a['gallery'])) + '</div>'
        body = f'''<div class="phead" style="--t:{t['tint']}"><div class="wrap"><div class="crumbs"><a href="{{root}}">Home</a> / <a href="{{root}}topics/{t['slug']}/">{t['name']}</a></div><h1 style="max-width:900px;font-size:clamp(34px,4.6vw,56px)">{E(a['title'])}</h1><p>{E(a['excerpt'])}</p>
<div class="meta-row"><span class="pill" style="background:#fff;color:{t['color']}">{t['name']}</span><span>⏱ {a['mins']} min read</span><span>✔ Fact-checked against UK sources</span><button class="link" data-share>Share ↗</button></div></div></div>
<div class="wrap article"><article class="prose">{a['body']}
{f'<div class="srcs"><h3>Sources</h3><ul>{srcs}</ul></div>' if srcs else ''}
<div class="helpful"><b>Was this helpful?</b><button class="btn btn-o" data-v="y" style="padding:9px 16px">👍 Yes</button><button class="btn btn-o" data-v="n" style="padding:9px 16px">👎 Not really</button></div>
<p style="font-size:13.5px;color:var(--mut);margin-top:20px">General information only – always follow advice from your GP or healthcare team.</p>
</article>
<aside class="side">{img(a['img'], a['title'], zoom=True, lazy=False)}{gal}
<div class="panel" style="margin-top:22px"><h3 style="font-size:18px;margin-bottom:10px">More in {t['name']}</h3>{''.join(f'<a href="{{root}}articles/{m["slug"]}/" style="display:block;padding:8px 0;border-bottom:1px solid var(--line);font-weight:600;text-decoration:none;color:var(--ink)">{E(m["title"])} →</a>' for m in more)}
<a class="btn btn-n" href="{IG}" target="_blank" rel="noopener" style="margin-top:16px;width:100%;justify-content:center">See it on Instagram</a></div></aside></div>'''
        page(f"articles/{a['slug']}/", a['title'], body, desc=a['excerpt'], active='topics/')

# ------------------------------------------------------------------ TOOLS
DRINKS = [
 dict(n='Pint of lower-strength beer/lager/cider', ml=568, abv=3.6), dict(n='Pint of higher-strength beer/lager/cider', ml=568, abv=5.2),
 dict(n='Can of beer/lager/cider', ml=440, abv=5.5), dict(n='Bottle of beer/lager/cider', ml=330, abv=5),
 dict(n='Small glass of wine', ml=125, abv=12), dict(n='Standard glass of wine', ml=175, abv=12), dict(n='Large glass of wine', ml=250, abv=12),
 dict(n='Bottle of wine', ml=750, abv=13.5), dict(n='Single shot of spirits', ml=25, abv=40), dict(n='Alcopop', ml=275, abv=5.5)]

def tools():
    T = [('bmi', 'bar_chart', 'BMI'), ('waist', 'person_standing', 'Waist-to-height'), ('activity', 'stopwatch', 'Activity tracker'), ('alcohol', 'clipboard', 'Alcohol units'), ('water', 'droplet', 'Water'), ('five', 'broccoli', '5 A Day')]
    src = lambda *k: '<p class="method">Source: ' + ' · '.join(f'<a href="{SRC[x][1]}" target="_blank" rel="noopener">{SRC[x][0]}</a>' for x in k) + '</p>'
    body = f'''<div class="phead"><div class="wrap"><div class="crumbs"><a href="{{root}}">Home</a> / Tools</div><h1>Free health tools</h1><p>Private, quick and based on UK guidance. Nothing you enter leaves your device.</p></div></div>
<section style="padding-top:40px"><div class="wrap">
<div class="tabs" role="tablist">{''.join(f'<button class="tab" data-t="{k}">{emo(e, "", 22)}{n}</button>' for k, e, n in T)}</div>

<div class="tool" id="t-bmi"><div class="panel form"><h2>BMI calculator</h2><p style="color:var(--mut)">Body mass index for adults aged 18 and over.</p>
<div class="seg" id="bmi-units"><button class="on" data-u="m">cm / kg</button><button data-u="i">ft / st</button></div>
<div class="u-m row2"><div><label for="b-cm">Height (cm)</label><input id="b-cm" type="number" inputmode="decimal" placeholder="e.g. 170"></div><div><label for="b-kg">Weight (kg)</label><input id="b-kg" type="number" inputmode="decimal" placeholder="e.g. 70"></div></div>
<div class="u-i"><label>Height</label><div class="row2"><input id="b-ft" type="number" placeholder="feet" aria-label="feet"><input id="b-in" type="number" placeholder="inches" aria-label="inches"></div><label>Weight</label><div class="row2"><input id="b-st" type="number" placeholder="stone" aria-label="stone"><input id="b-lb" type="number" placeholder="pounds" aria-label="pounds"></div></div>
<label class="check" style="font-weight:500;margin-top:18px"><input type="checkbox" id="b-eth"><span>I’m from a South Asian, Chinese, other Asian, Middle Eastern, Black African or African-Caribbean family background. <em style="color:var(--mut)">(NICE advises lower BMI thresholds for these groups because health risks rise at a lower BMI.)</em></span></label>
{src('nice', 'nhs-bmi')}</div><div class="out" id="bmi-out" aria-live="polite"></div></div>

<div class="tool" id="t-waist"><div class="panel form"><h2>Waist-to-height ratio</h2><p style="color:var(--mut)">NICE advises keeping your waist to less than half your height.</p>
<div class="row2"><div><label for="w-waist">Waist</label><input id="w-waist" type="number" inputmode="decimal" placeholder="e.g. 80"></div><div><label for="w-height">Height</label><input id="w-height" type="number" inputmode="decimal" placeholder="e.g. 170"></div></div>
<p class="method"><b>How to measure:</b> find the bottom of your ribs and the top of your hips. Wrap a tape measure around your waist midway between these points (just above the belly button) and breathe out naturally before measuring. Use the same units (cm or inches) for both.</p>
{src('nice')}</div><div class="out" id="waist-out" aria-live="polite"></div></div>

<div class="tool" id="t-activity"><div class="panel form"><h2>Weekly activity tracker</h2><p style="color:var(--mut)">Add your minutes for each day this week (Monday to Sunday). Moderate = you can talk but not sing. Vigorous = you can’t say more than a few words.</p>
<div id="act-days" style="margin-top:12px"></div>{src('cmo', 'nhs-activity')}</div><div class="out" id="act-out" aria-live="polite"></div></div>

<div class="tool" id="t-alcohol"><div class="panel form"><h2>Alcohol unit counter</h2><p style="color:var(--mut)">Add what you drink in a typical week.</p>
<div class="drinks" id="drinks"></div>
<div class="custom"><label>Something else?</label><div class="row2" style="grid-template-columns:1fr 1fr 1fr"><input id="al-ml" type="number" placeholder="ml" aria-label="Volume in ml"><input id="al-abv" type="number" step="0.1" placeholder="ABV %" aria-label="ABV percent"><input id="al-q" type="number" placeholder="how many" aria-label="How many"></div></div>
{src('nhs-alcohol')}</div><div class="out" id="al-out" aria-live="polite"></div>
<script type="application/json" id="drinks-data">{json.dumps(DRINKS)}</script></div>

<div class="tool" id="t-water"><div class="panel"><h2>Water tracker</h2><p style="color:var(--mut)">Aim for 6 to 8 cups or glasses of fluid a day – more when it’s hot or you’re active. Water, lower-fat milk and sugar-free drinks including tea and coffee all count.</p><div class="glasses" id="glasses"></div>{src('water')}</div><div class="out" id="w-out" aria-live="polite"></div></div>

<div class="tool" id="t-five"><div class="panel"><h2>5 A Day counter</h2><p style="color:var(--mut)">One adult portion is 80g of fruit or veg – roughly a handful. Fresh, frozen, tinned and dried all count; fruit juice counts once a day at most.</p><div style="display:flex;gap:10px;flex-wrap:wrap;margin:16px 0" id="five"></div>{src('five-a-day')}</div><div class="out" id="f-out" aria-live="polite"></div></div>

<p style="font-size:14px;color:var(--mut);margin-top:30px">These tools give general information, not a diagnosis. If you’re worried about your health, speak to your GP. Water and 5 A Day reset each day. <button class="link" id="reset-data">Clear all my saved data</button></p>
</div></section>'''
    page('tools/', 'Free health tools', body, desc='BMI, waist-to-height ratio, weekly activity, alcohol units, water and 5 A Day – free tools based on NHS and NICE guidance.', active='tools/')

# ------------------------------------------------------------------ CLASSES
PARQ = ['Has a doctor ever said you have a heart condition or high blood pressure?', 'Do you get chest pain at rest, during daily activities or when you’re active?',
        'Have you lost your balance because of dizziness, or lost consciousness, in the last 12 months?', 'Are you pregnant, or have you had a baby in the last 6 months?',
        'Do you have a bone, joint or muscle problem, or a long-term condition, that could get worse with activity?']

def classes():
    body = f'''<div class="phead" style="--t:#FFF1EF"><div class="wrap"><div class="crumbs"><a href="{{root}}">Home</a> / Classes</div><h1>Online classes</h1><p>Live, friendly sessions you can join from your living room, your local park or a quiet corner at work. All times are UK time.</p></div></div>
<section style="padding-top:44px"><div class="wrap">
<div class="grid g3" style="margin-bottom:56px">{''.join(f'<div class="cls">{emo(c["emoji"])}<h3 style="margin-top:12px">{c["name"]}</h3><div class="meta"><span class="pill">{c["mins"]} min</span><span class="pill">{c["level"]}</span></div><p style="color:var(--mut);font-size:15px">{c["desc"]}</p><a href="?c={c["id"]}#book" style="display:inline-block;margin-top:10px;font-weight:700">Show times →</a></div>' for c in CLASSES)}</div>
<div class="layout-2" id="book"><div><div class="sec-h" style="margin-bottom:18px"><div><div class="eyebrow">Next 7 days</div><h2>Pick a session</h2></div></div><p class="notice" id="filter-note" hidden style="margin:0 0 16px"></p><div class="tt" id="timetable"></div>
<p style="font-size:14px;color:var(--mut);margin-top:10px">1:1 coaching can be arranged at any listed time.</p></div>
<div class="wizard" id="wizard" aria-live="polite"><div class="steps"><span></span><span></span><span></span></div>
<div class="wstep"><h3 style="font-size:24px">Book your session</h3><p style="color:var(--mut);margin-top:6px">Choose a time from the timetable to get started.</p><div style="font-size:64px;text-align:center;margin:18px 0">📅</div><p class="notice"><b>New to exercise or living with a health condition?</b> That’s exactly who these classes are for – we’ll ask a few quick health questions so your coach can keep you safe.</p></div>
<div class="wstep" hidden><div id="w-sel" style="background:var(--sky);border-radius:14px;padding:14px 16px"></div>
<form id="w-form" novalidate><label for="f-name">Full name</label><input id="f-name" name="name" required autocomplete="name">
<label for="f-email">Email</label><input id="f-email" name="email" type="email" required autocomplete="email">
<label for="f-lvl">How active are you right now?</label><select id="f-lvl" name="lvl"><option>Just getting started</option><option>Active now and then</option><option>Active most weeks</option></select>
<label style="margin-top:18px">Quick health check – tick any that apply</label>{''.join(f'<label class="check" style="font-weight:500;margin:6px 0"><input type="checkbox" name="parq" value="{i}"><span>{q}</span></label>' for i, q in enumerate(PARQ))}
<label class="check" style="font-weight:500;margin-top:14px"><input type="checkbox" required><span>I agree to the <a href="{{root}}privacy/" target="_blank">privacy policy</a> and understand I should stop and seek help if I feel unwell during a session.</span></label>
<div style="display:flex;gap:10px;margin-top:16px"><button type="button" class="btn btn-o" id="w-back">← Back</button><button class="btn btn-p" style="flex:1;justify-content:center">Request booking</button></div></form></div>
<div class="wstep" hidden id="w-done"></div></div></div>
<script type="application/json" id="classes-data">{json.dumps(CLASSES)}</script><script type="application/json" id="tt-data">{json.dumps({str(k): v for k, v in TIMETABLE.items()})}</script>
</div></section>
<section style="padding-top:20px"><div class="wrap"><h2 style="margin-bottom:20px">Good to know</h2><div class="grid g3">
<div class="panel"><h3>💻 What you need</h3><p style="margin-top:8px;color:var(--mut)">A phone, tablet or laptop, a bit of floor space and a bottle of water. No equipment needed for most classes.</p></div>
<div class="panel"><h3>🩺 Your safety first</h3><p style="margin-top:8px;color:var(--mut)">If you have a health condition, check with your GP before starting. Stop if you feel chest pain, dizziness or unusual breathlessness.</p></div>
<div class="panel"><h3>🇬🇧 UK time</h3><p style="margin-top:8px;color:var(--mut)">All sessions run on UK time (GMT, or BST in summer), so they fit around London working days.</p></div>
</div></div></section>'''
    page('classes/', 'Online classes', body, desc='Book friendly online fitness classes – walking, strength, mobility, low-impact cardio, pilates and 1:1 coaching.', active='classes/')

# ------------------------------------------------------------------ STATIC PAGES
def simple(path, title, inner, active=''):
    page(path, title, f'<div class="phead"><div class="wrap"><div class="crumbs"><a href="{{root}}">Home</a> / {title}</div><h1>{title}</h1></div></div><div class="wrap legal">{inner}</div>', active=active)

def pages():
    simple('about/', 'About us', f'''<p style="font-size:20px">London Momentum is a London-based health and fitness community. We turn trusted UK health guidance into friendly, practical tips you can actually use – on Instagram, on this site and in our online classes.</p>
<h2>What we believe</h2><ul><li><b>Small steps win.</b> You don’t need a gym membership or a total life overhaul to feel better.</li><li><b>Facts, not fads.</b> Everything we share is based on sources like the NHS, NICE, the UK Chief Medical Officers, WHO and leading UK health charities – and we link to them.</li><li><b>Everyone’s welcome.</b> Whatever your age, size, background or starting point.</li></ul>
<h2>What we’re not</h2><p>We’re not a medical service and we don’t give personal medical advice. For that, please speak to your GP, pharmacist or call NHS 111.</p>
<h2>Join the community</h2><p>Follow <a href="{IG}">@ldnmomentum on Instagram</a> and <a href="{FB}">London Momentum on Facebook</a> for daily tips.</p>''', 'about/')
    simple('contact/', 'Contact', f'''<p style="font-size:19px">Questions about classes, ideas for a topic or a partnership in London? We’d love to hear from you.</p>
<div class="grid g2" style="margin-top:28px"><form class="panel form" data-preview="Thanks! Our contact form goes live soon – for now, please message us on Instagram."><label for="c-n">Name</label><input id="c-n" required><label for="c-e">Email</label><input id="c-e" type="email" required><label for="c-t">Topic</label><select id="c-t"><option>Online classes</option><option>Content idea</option><option>Partnership</option><option>Something else</option></select><label for="c-m">Message</label><textarea id="c-m" rows="5" required></textarea><button class="btn btn-p" style="margin-top:16px">Send message</button></form>
<div class="panel"><h3>The quickest way</h3><p style="margin:8px 0 16px;color:var(--mut)">Send us a direct message on Instagram – we usually reply within a day.</p><a class="btn btn-n" href="{IG}" target="_blank" rel="noopener">Message @ldnmomentum</a><h3 style="margin-top:28px">Need medical help?</h3><p style="margin-top:8px;color:var(--mut)">We can’t give medical advice. Call NHS 111 for urgent advice or 999 in an emergency.</p></div></div>''', 'contact/')
    simple('privacy/', 'Privacy policy', '''<p><em>Last updated: November 2026. This is a preview version and will be reviewed before online booking and newsletter sign-up go live.</em></p>
<h2>Who we are</h2><p>London Momentum is a health and fitness community based in London, UK. We follow the UK General Data Protection Regulation (UK GDPR) and the Data Protection Act 2018.</p>
<h2>Data stored on your device</h2><p>Our tools, the daily check-in and preview booking requests save your answers in your own browser’s local storage so they’re there next time you visit. This information is not sent to us. You can clear it at any time from the <a href="{{root}}tools/">tools page</a> or your browser settings.</p>
<h2>When booking and the newsletter go live</h2><p>We’ll collect only what we need (such as your name, email and the health information you choose to give for class safety), explain why, keep it secure and never sell it. Health information is special category data and will only be used with your explicit consent.</p>
<h2>Your rights</h2><p>You have the right to access, correct or delete your data, and to complain to the Information Commissioner’s Office (ico.org.uk).</p>''')
    simple('cookies/', 'Cookies', '''<p>This site does not use advertising, analytics or tracking cookies.</p><h2>Local storage</h2><p>We use your browser’s local storage to remember your tool results, check-in answers and whether you’ve seen the cookie notice. It stays on your device and isn’t shared with anyone.</p><h2>Third parties</h2><p>Links to Instagram, Facebook and other websites take you to sites with their own cookie policies.</p><p>If we add analytics in future, we’ll ask for your consent first.</p>''')
    simple('disclaimer/', 'Medical disclaimer', '''<p>The content on London Momentum is for general information and education only. It is not medical advice and is not a substitute for advice from your GP or another qualified health professional.</p><ul><li>Always speak to a health professional before starting a new exercise programme if you have a health condition, are pregnant or have any concerns.</li><li>Stop exercising and seek help if you feel chest pain, dizziness, faintness or unusual breathlessness.</li><li>In an emergency call <b>999</b>. For urgent advice call <b>NHS 111</b> or visit 111.nhs.uk.</li><li>If you’re struggling with your mental health, you can call Samaritans free on <b>116 123</b>, any time.</li></ul><p>Our calculators give estimates based on published UK guidance and can’t take your full health picture into account.</p>''')
    simple('accessibility/', 'Accessibility', '''<p>We want everyone to be able to use this website. We aim to meet the Web Content Accessibility Guidelines (WCAG) 2.2 at level AA.</p><ul><li>You can navigate the site with a keyboard, and there’s a “skip to main content” link.</li><li>Text can be zoomed up to 200% without breaking the layout.</li><li>Our Instagram designs are posted alongside full text versions on each article page.</li></ul><p>Found a problem? Please <a href="{{root}}contact/">let us know</a>.</p>''')
    page('404.html', 'Page not found', '<div class="wrap legal" style="text-align:center"><div style="font-size:80px">🧭</div><h1>Lost your way?</h1><p style="margin:16px 0 24px">This page has taken a wrong turn at Bank. Let’s get you back on track.</p><a class="btn btn-p" href="/londonmomentum/index.html">Back to the homepage</a></div>')

def export():
    data = dict(site=SITE, categories=[dict(slug=t['slug'], name=t['name'], description=t['lead']) for t in TOPICS],
                posts=[dict(slug=a['slug'], title=a['title'], category=a['topic'], excerpt=a['excerpt'], featured_image=f"assets/img/{a['img']}.webp",
                            content=a['body'].replace('{root}', '/'), sources=[dict(title=SRC[k][0], url=SRC[k][1]) for k in a['sources']], type=a['kind']) for a in ARTICLES],
                classes=CLASSES, timetable=TIMETABLE)
    (R / 'content').mkdir(exist_ok=True)
    (R / 'content' / 'wordpress-export.json').write_text(json.dumps(data, indent=1, ensure_ascii=False), encoding='utf-8')

(R / 'assets' / 'favicon.svg').write_text(LOGO.replace('aria-hidden="true"', 'xmlns="http://www.w3.org/2000/svg"'))
home(); topics(); articles(); tools(); classes(); pages(); export()
print('built', len(ARTICLES), 'articles')
