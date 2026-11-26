/* London Momentum – site interactions (no tracking, data stays in this browser) */
(() => {
const $ = (s, r = document) => r.querySelector(s), $$ = (s, r = document) => [...r.querySelectorAll(s)];
const ROOT = document.body.dataset.root || './';
const KEY = 'lm.v1';
const load = () => { try { return JSON.parse(localStorage.getItem(KEY)) || {} } catch (e) { return {} } };
const save = d => { try { localStorage.setItem(KEY, JSON.stringify(d)) } catch (e) {} };
let S = load(); S.log = S.log || {}; S.book = S.book || [];
const london = (d = new Date()) => new Intl.DateTimeFormat('en-CA', { timeZone: 'Europe/London', year: 'numeric', month: '2-digit', day: '2-digit' }).format(d);
const hourLondon = () => +new Intl.DateTimeFormat('en-GB', { timeZone: 'Europe/London', hour: 'numeric', hour12: false }).format(new Date());
const today = london();
const weekDays = () => { // Monday-start week in London
  const out = [], now = new Date(today + 'T12:00:00'); const wd = (now.getDay() + 6) % 7;
  for (let i = 0; i < 7; i++) { const d = new Date(now); d.setDate(now.getDate() - wd + i); out.push(d.toISOString().slice(0, 10)); }
  return out;
};
const weekTotal = () => weekDays().reduce((a, d) => a + (S.log[d] || 0), 0);
const greet = () => { const h = hourLondon(); return h < 12 ? 'Good morning' : h < 18 ? 'Good afternoon' : 'Good evening'; };
const toast = m => { let t = $('.toast'); if (!t) { t = document.createElement('div'); t.className = 'toast'; t.setAttribute('role', 'status'); document.body.append(t); } t.textContent = m; t.classList.add('on'); clearTimeout(t._h); t._h = setTimeout(() => t.classList.remove('on'), 2600); };
window.LM = { toast };

/* nav */
const bg = $('.burger'); if (bg) bg.onclick = () => { $('.nav').classList.toggle('open'); bg.setAttribute('aria-expanded', $('.nav').classList.contains('open')); };

/* ring + week helpers */
function ringSVG(v, max = 150, size = 150) {
  const r = size / 2 - 12, c = 2 * Math.PI * r, p = Math.min(v / max, 1);
  return `<svg width="${size}" height="${size}"><circle cx="${size/2}" cy="${size/2}" r="${r}" fill="none" stroke="#E3E7EE" stroke-width="14"/><circle cx="${size/2}" cy="${size/2}" r="${r}" fill="none" stroke="${p >= 1 ? '#12A27B' : '#FF5A4E'}" stroke-width="14" stroke-linecap="round" stroke-dasharray="${c}" stroke-dashoffset="${c * (1 - p)}" style="transition:stroke-dashoffset .8s"/></svg>`;
}
function weekBars() {
  const L = ['M', 'T', 'W', 'T', 'F', 'S', 'S'];
  return `<div class="week">${weekDays().map((d, i) => `<div class="${d === today ? 'today' : ''}"><i><b style="height:${Math.min((S.log[d] || 0) / 45 * 100, 100)}%"></b></i>${L[i]}</div>`).join('')}</div>`;
}
function updateFab() {
  const f = $('.fab'); if (!f) return; const t = weekTotal();
  f.querySelector('.mini').style.setProperty('--p', Math.min(t / 150 * 100, 100) + '%');
  f.querySelector('span').textContent = `${t} / 150 min this week`;
  f.hidden = !S.done;
}

/* ---------------- welcome check-in ---------------- */
const GOALS = {
  move: { t: 'Move more', topic: 'physical-activity', a: 'how-much-should-you-move', tool: 'activity', cls: 'walk' },
  eat: { t: 'Eat better', topic: 'healthy-eating', a: 'is-your-plate-balanced', tool: 'five', cls: 'cardio' },
  calm: { t: 'Feel calmer', topic: 'move-for-your-health', a: 'move-for-your-mind', tool: 'water', cls: 'mobility' },
  weight: { t: 'Healthy weight', topic: 'healthy-eating', a: 'swap-this-for-that', tool: 'bmi', cls: 'cardio' },
  strong: { t: 'Get stronger', topic: 'physical-activity', a: 'mix-all-3-types-of-activity', tool: 'activity', cls: 'strength' },
  start: { t: 'Just get started', topic: 'beat-the-barriers', a: 'whats-stopping-you', tool: 'activity', cls: 'walk' },
};
const ci = $('#checkin');
if (ci) {
  let st = 0, ans = { min: S.log[today] || 0, what: '', mood: 0, goal: S.goal || '' };
  const steps = $$('.step', ci), dots = $$('.dots i', ci);
  const show = n => { st = n; steps.forEach((s, i) => s.classList.toggle('on', i === n)); dots.forEach((d, i) => d.classList.toggle('on', i === n)); $('.ci-foot', ci).hidden = n === 4; };
  $('#ci-hello').textContent = (S.done ? 'Welcome back! ' : greet() + '! ') + '👋';
  const rng = $('#ci-range'), bv = $('#ci-val');
  const setMin = v => { ans.min = +v; rng.value = v; bv.innerHTML = `${v}<small> min</small>`; };
  setMin(ans.min);
  rng.oninput = e => setMin(e.target.value);
  $$('[data-min]', ci).forEach(b => b.onclick = () => setMin(b.dataset.min));
  $$('[data-what]', ci).forEach(b => b.onclick = () => { $$('[data-what]', ci).forEach(x => x.classList.remove('sel')); b.classList.add('sel'); ans.what = b.dataset.what; setTimeout(() => show(2), 250); });
  $$('.mood button', ci).forEach(b => b.onclick = () => { $$('.mood button', ci).forEach(x => x.classList.remove('sel')); b.classList.add('sel'); ans.mood = +b.dataset.v; setTimeout(() => show(3), 250); });
  $$('[data-goal]', ci).forEach(b => b.onclick = () => { $$('[data-goal]', ci).forEach(x => x.classList.remove('sel')); b.classList.add('sel'); ans.goal = b.dataset.goal; setTimeout(finish, 250); });
  $('#ci-next').onclick = () => st < 3 ? show(st + 1) : finish();
  $('#ci-back').onclick = () => st > 0 && show(st - 1);
  function finish() {
    S.log[today] = ans.min; S.goal = ans.goal || 'start'; S.mood = ans.mood; S.what = ans.what; S.done = today; save(S); render(); show(4); updateFab();
  }
  function render() {
    const t = weekTotal(), g = GOALS[S.goal || 'start'], left = Math.max(150 - t, 0), m = S.log[today] || 0;
    let msg;
    if (m === 0) msg = `No activity yet today – that’s fine. Even a 10-minute brisk walk counts towards your week.`;
    else if (t >= 150) msg = `Brilliant – you’ve hit the UK guideline of 150 active minutes this week. 🎉 Remember strength activities on 2 days too.`;
    else msg = `Nice work – ${m} minutes today. ${left} more minutes this week gets you to the UK guideline of 150.`;
    let extra = '';
    if (S.mood && S.mood <= 2) extra = `<p style="margin-top:10px">Feeling low? Moving can help your mood, but you don’t have to cope alone – <a href="${ROOT}articles/move-for-your-mind.html">read our mind guide</a> or talk to your GP.</p>`;
    $('#ci-result').innerHTML = `<div class="result"><div class="ring">${ringSVG(t)}<div class="rv"><div>${t}<small>of 150 min<br>this week</small></div></div></div><div><h3 style="font-size:22px">${m >= 30 ? 'Great going!' : m > 0 ? 'Every minute counts' : 'Let’s get moving'}</h3><p style="color:var(--mut);font-size:15px;margin-top:6px">${msg}</p></div></div>${weekBars()}
      <div class="reco">For your goal <b>“${g.t}”</b>: <a href="${ROOT}articles/${g.a}.html">read this first</a> · <a href="${ROOT}tools.html#${g.tool}">try a tool</a> · <a href="${ROOT}classes.html?c=${g.cls}">see a class</a>${extra}</div>
      <div style="display:flex;gap:14px;margin-top:16px"><button class="link" id="ci-again">Update today</button><a class="link" href="${ROOT}tools.html#activity">Log another day</a></div>`;
    $('#ci-again').onclick = () => show(0);
  }
  if (S.done === today) { render(); show(4); } else show(0);
}

/* ---------------- myth or fact quiz ---------------- */
const qz = $('#quiz');
if (qz) {
  const Q = JSON.parse($('#quiz-data').textContent); let i = 0, sc = 0, done = false;
  const draw = () => { const q = Q[i]; $('.stmt', qz).textContent = q.s; $('.fb', qz).className = 'fb'; $('.score', qz).textContent = `Question ${i + 1} of ${Q.length} · Score ${sc}`; done = false; $('#qz-next').hidden = true; };
  $$('[data-a]', qz).forEach(b => b.onclick = () => {
    if (done) return; done = true; const q = Q[i], ok = (b.dataset.a === 'fact') === q.f; if (ok) sc++;
    const fb = $('.fb', qz); fb.className = 'fb ' + (ok ? 'ok' : 'no'); fb.innerHTML = `<b>${ok ? 'Correct!' : 'Not quite.'}</b> It’s a <b>${q.f ? 'fact' : 'myth'}</b>. ${q.e} <a href="${ROOT}articles/${q.l}.html">Read more</a>`;
    $('.score', qz).textContent = `Question ${i + 1} of ${Q.length} · Score ${sc}`; $('#qz-next').hidden = false; $('#qz-next').textContent = i < Q.length - 1 ? 'Next question →' : 'Play again ↺';
  });
  $('#qz-next').onclick = () => { if (i < Q.length - 1) i++; else { i = 0; sc = 0; } draw(); };
  draw();
}

/* ---------------- tools ---------------- */
const tabs = $$('.tab');
if (tabs.length) {
  const open = id => { if (!$('#t-' + id)) id = tabs[0].dataset.t; tabs.forEach(t => t.classList.toggle('on', t.dataset.t === id)); $$('.tool').forEach(t => t.classList.toggle('on', t.id === 't-' + id)); };
  tabs.forEach(t => t.onclick = () => { open(t.dataset.t); history.replaceState(null, '', '#' + t.dataset.t); });
  open(location.hash.slice(1) || 'bmi'); addEventListener('hashchange', () => open(location.hash.slice(1)));
  $$('.seg').forEach(sg => $$('button', sg).forEach(b => b.onclick = () => { $$('button', sg).forEach(x => x.classList.remove('on')); b.classList.add('on'); sg.dispatchEvent(new Event('change')); }));

  // BMI
  const bmiU = $('#bmi-units'), bm = () => $('button.on', bmiU).dataset.u;
  const syncU = () => { $$('.u-m').forEach(e => e.hidden = bm() !== 'm'); $$('.u-i').forEach(e => e.hidden = bm() !== 'i'); calcBMI(); };
  bmiU.addEventListener('change', syncU);
  function calcBMI() {
    let h, w; if (bm() === 'm') { h = +$('#b-cm').value / 100; w = +$('#b-kg').value; } else { h = ((+$('#b-ft').value || 0) * 12 + (+$('#b-in').value || 0)) * .0254; w = ((+$('#b-st').value || 0) * 14 + (+$('#b-lb').value || 0)) * .45359237; }
    const out = $('#bmi-out'); if (!(h > 1 && w > 20)) { out.innerHTML = '<p>Enter your height and weight to see your BMI.</p>'; return; }
    const b = w / (h * h), eth = $('#b-eth').checked, ow = eth ? 23 : 25, ob = eth ? 27.5 : 30;
    let c, col; if (b < 18.5) { c = 'Underweight'; col = '#7FB6F0'; } else if (b < ow) { c = 'Healthy weight'; col = '#2FBF8E'; } else if (b < ob) { c = 'Overweight'; col = '#FFC845'; } else { c = 'Obesity'; col = '#FF8A5B'; }
    const pos = Math.max(0, Math.min(100, (b - 14) / (42 - 14) * 100));
    const hlo = 18.5 * h * h, hhi = (ow - .1) * h * h;
    out.innerHTML = `<div class="eyebrow">Your BMI</div><div class="big">${b.toFixed(1)}</div><span class="lbl" style="background:${col}">${c}</span>
      <div class="scale"><i style="left:${pos}%"></i></div><div class="scale-l"><span>18.5</span><span>${ow}</span><span>${ob}</span><span>40</span></div>
      <p style="margin-top:18px">For your height, a healthy-weight BMI range is roughly <b>${hlo.toFixed(1)}–${hhi.toFixed(1)} kg</b>${bm() === 'i' ? ` (${(hlo / 6.35029).toFixed(1)}–${(hhi / 6.35029).toFixed(1)} st)` : ''}.</p>
      <p class="method">BMI doesn’t measure body fat directly and can be less accurate for very muscular people, during pregnancy and in people over 65. It’s for adults (18+). Check your <a href="#" data-goto="waist">waist-to-height ratio</a> too, and speak to your GP about any concerns.</p>`;
    $$('[data-goto]', out).forEach(a => a.onclick = e => { e.preventDefault(); open(a.dataset.goto); });
  }
  $$('#t-bmi input').forEach(i => i.oninput = calcBMI); $('#b-eth').onchange = calcBMI; syncU();

  // Waist to height
  function calcW() {
    const w = +$('#w-waist').value, h = +$('#w-height').value, out = $('#waist-out');
    if (!(w > 0 && h > 0)) { out.innerHTML = '<p>Measure your waist and height in the same units (both cm or both inches).</p>'; return; }
    const r = w / h; let c, col, t;
    if (r < .5) { c = 'No increased health risk'; col = '#2FBF8E'; t = 'Your waist is less than half your height – keep it up.'; }
    else if (r < .6) { c = 'Increased health risk'; col = '#FFC845'; t = 'Small changes to food and activity can help bring this down.'; }
    else { c = 'High health risk'; col = '#FF8A5B'; t = 'It’s worth talking to your GP or practice nurse about your health.'; }
    out.innerHTML = `<div class="eyebrow">Your waist-to-height ratio</div><div class="big">${r.toFixed(2)}</div><span class="lbl" style="background:${col}">${c}</span><p style="margin-top:16px">${t}</p><p class="method">NICE: 0.4–0.49 no increased risk · 0.5–0.59 increased risk · 0.6 or more high risk. Recommended for adults with a BMI under 35.</p>`;
  }
  $$('#t-waist input').forEach(i => i.oninput = calcW); calcW();

  // Activity tracker
  const days = weekDays(), act = $('#act-days'), names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];
  S.vig = S.vig || {};
  act.innerHTML = days.map((d, i) => `<div class="row2" style="grid-template-columns:70px 1fr 1fr;align-items:center;margin:8px 0"><b${d === today ? ' style="color:var(--coral)"' : ''}>${names[i]}</b><input type="number" min="0" max="600" inputmode="numeric" data-d="${d}" data-k="log" placeholder="moderate min" value="${S.log[d] || ''}" aria-label="${names[i]} moderate minutes"><input type="number" min="0" max="600" inputmode="numeric" data-d="${d}" data-k="vig" placeholder="vigorous min" value="${S.vig[d] || ''}" aria-label="${names[i]} vigorous minutes"></div>`).join('');
  function calcA() {
    let mod = 0, vig = 0; days.forEach(d => { mod += S.log[d] || 0; vig += S.vig[d] || 0; });
    const eq = mod + vig * 2, p = Math.min(eq / 150 * 100, 100);
    $('#act-out').innerHTML = `<div class="eyebrow">This week</div><div class="result" style="margin-top:10px"><div class="ring">${ringSVG(eq)}<div class="rv"><div>${eq}<small>of 150<br>moderate-equivalent</small></div></div></div><div><p>${eq >= 150 ? '🎉 You’ve reached the UK guideline this week.' : `<b>${150 - eq} minutes</b> to go – that’s about ${Math.ceil((150 - eq) / Math.max(1, 7 - ((new Date(today).getDay() + 6) % 7)))} a day for the rest of the week.`}</p><p class="method">1 minute of vigorous activity counts as about 2 minutes of moderate activity. Plus: strength activities on at least 2 days a week.</p></div></div>${weekBars()}`;
    updateFab();
  }
  $$('input', act).forEach(i => i.oninput = () => { const v = Math.max(0, +i.value || 0); S[i.dataset.k][i.dataset.d] = v; if (i.dataset.k === 'log' && v) S.done = S.done || today; save(S); calcA(); });
  calcA();

  // Alcohol
  const DR = JSON.parse($('#drinks-data').textContent); S.dr = S.dr || {};
  $('#drinks').innerHTML = DR.map((d, i) => `<div class="dr"><span>${d.n}<em>${d.ml}ml · ${d.abv}% ABV · ${(d.ml * d.abv / 1000).toFixed(1)} units</em></span><div class="qty"><button data-i="${i}" data-s="-1" aria-label="Remove one">−</button><b id="dq${i}">${S.dr[i] || 0}</b><button data-i="${i}" data-s="1" aria-label="Add one">+</button></div></div>`).join('');
  function calcAl() {
    let u = DR.reduce((a, d, i) => a + (S.dr[i] || 0) * d.ml * d.abv / 1000, 0);
    const cml = +$('#al-ml').value, cab = +$('#al-abv').value, cq = +$('#al-q').value; if (cml && cab && cq) u += cml * cab / 1000 * cq;
    const over = u > 14;
    $('#al-out').innerHTML = `<div class="eyebrow">Your week</div><div class="big">${u.toFixed(1)}<small style="font-size:22px;color:var(--mut)"> units</small></div><div class="bar"><b style="width:${Math.min(u / 14 * 100, 100)}%;background:${over ? '#E5484D' : 'var(--green)'}"></b></div><p>${over ? `That’s <b>${(u - 14).toFixed(1)} units over</b> the UK low-risk guideline of 14 units a week.` : `Within the UK low-risk guideline of no more than 14 units a week.`}</p><p class="method">Units = strength (ABV %) × volume (ml) ÷ 1,000. If you drink as much as 14 units a week, spread it over 3 or more days and have several drink-free days. Worried about your drinking? Talk to your GP.</p>`;
  }
  $('#drinks').onclick = e => { const b = e.target.closest('button'); if (!b) return; const i = b.dataset.i; S.dr[i] = Math.max(0, (S.dr[i] || 0) + +b.dataset.s); $('#dq' + i).textContent = S.dr[i]; save(S); calcAl(); };
  $$('#t-alcohol .custom input').forEach(i => i.oninput = calcAl); calcAl();

  // Water + 5 a day (reset daily)
  if (S.wday !== today) { S.wday = today; S.water = 0; S.five = 0; save(S); }
  const gl = $('#glasses');
  const drawW = () => { gl.innerHTML = Array.from({ length: 8 }, (_, i) => `<button class="glass ${i < S.water ? 'f' : ''}" data-i="${i}" aria-label="Glass ${i + 1}"><b></b></button>`).join(''); $('#w-out').innerHTML = `<b style="font:800 40px Brico">${S.water} / 6–8</b><p>${S.water >= 6 ? 'Well hydrated – nice one! 💧' : 'Tap a glass each time you have a drink.'}</p>`; };
  gl.onclick = e => { const b = e.target.closest('.glass'); if (!b) return; const i = +b.dataset.i; S.water = S.water === i + 1 ? i : i + 1; save(S); drawW(); };
  drawW();
  const fv = $('#five');
  const drawF = () => { fv.innerHTML = Array.from({ length: 7 }, (_, i) => `<button class="mood-b" data-i="${i}" style="font-size:34px;width:62px;height:62px;border-radius:50%;border:2px solid ${i < S.five ? 'var(--green)' : 'var(--line)'};background:${i < S.five ? '#E3F5EE' : '#fff'};cursor:pointer">${['🍎', '🥦', '🥕', '🍌', '🍅', '🫐', '🥬'][i]}</button>`).join(''); $('#f-out').innerHTML = `<b style="font:800 40px Brico">${S.five} portion${S.five === 1 ? '' : 's'}</b><p>${S.five >= 5 ? 'You’ve hit your 5 A Day! 🌈' : `${5 - S.five} more to reach your 5 A Day.`}</p>`; };
  fv.onclick = e => { const b = e.target.closest('button'); if (!b) return; const i = +b.dataset.i; S.five = S.five === i + 1 ? i : i + 1; save(S); drawF(); };
  drawF();
}

/* ---------------- booking ---------------- */
const tt = $('#timetable');
if (tt) {
  const C = JSON.parse($('#classes-data').textContent), T = JSON.parse($('#tt-data').textContent);
  const byId = Object.fromEntries(C.map(c => [c.id, c]));
  const filt = new URLSearchParams(location.search).get('c');
  let sel = null; const nowH = hourLondon();
  const base = new Date(today + 'T12:00:00');
  const fmt = d => d.toLocaleDateString('en-GB', { weekday: 'short', day: 'numeric', month: 'short' });
  let html = '';
  for (let k = 0; k < 7; k++) {
    const d = new Date(base); d.setDate(base.getDate() + k); const wd = (d.getDay() + 6) % 7, iso = d.toISOString().slice(0, 10);
    html += `<div class="day"><h4>${k === 0 ? 'Today' : fmt(d)}</h4>${(T[wd] || []).filter(s => !filt || s[1] === filt || filt === 'one2one').map(([tm, id]) => { const past = k === 0 && +tm.slice(0, 2) <= nowH; const c = byId[id]; return `<button class="slot" ${past ? 'disabled' : ''} data-d="${iso}" data-t="${tm}" data-c="${id}"><b>${tm}</b>${c.name}<br><span style="color:var(--mut)">${c.mins} min · ${c.level}</span></button>`; }).join('') || '<p style="font-size:13px;color:var(--mut)">No sessions</p>'}</div>`;
  }
  tt.innerHTML = html;
  if (filt) { const n = $('#filter-note'); n.hidden = false; n.innerHTML = `Showing <b>${byId[filt]?.name || ''}</b> sessions · <a href="classes.html">show all classes</a>`; }
  const W = $('#wizard'), go = n => { $$('.wstep', W).forEach((s, i) => s.hidden = i !== n); $$('.steps span', W).forEach((s, i) => s.classList.toggle('on', i <= n)); };
  tt.onclick = e => { const b = e.target.closest('.slot'); if (!b || b.disabled) return; $$('.slot').forEach(x => x.classList.remove('sel')); b.classList.add('sel'); sel = { ...b.dataset }; const c = byId[sel.c]; const d = new Date(sel.d + 'T12:00:00');
    $('#w-sel').innerHTML = `<b style="font:800 22px Brico;color:var(--navy)">${c.name}</b><br>${d.toLocaleDateString('en-GB', { weekday: 'long', day: 'numeric', month: 'long' })} at ${sel.t} (UK time) · ${c.mins} min · online`; go(1); if (innerWidth < 960) W.scrollIntoView({ behavior: 'smooth' }); };
  $('#w-form').onsubmit = e => {
    e.preventDefault(); const f = e.target; if (!f.checkValidity()) { f.reportValidity(); return; }
    const parq = $$('[name=parq]:checked', f).length;
    const c = byId[sel.c]; const rec = { ...sel, name: f.name.value, email: f.email.value, at: Date.now() };
    S.book.push(rec); save(S);
    $('#w-done').innerHTML = `<div style="font-size:46px">🎉</div><h3 style="font-size:26px;margin:8px 0">Request saved, ${f.name.value.split(' ')[0]}!</h3><p>${c.name} · ${new Date(sel.d + 'T12:00:00').toLocaleDateString('en-GB', { weekday: 'long', day: 'numeric', month: 'long' })} at ${sel.t}</p>
      ${parq ? '<p class="notice" style="background:#FDE8E6;border-color:#F3B4AE">You answered “yes” to at least one health question. Please check with your GP before taking part, and tell your coach when you join.</p>' : ''}
      <p class="notice"><b>Preview:</b> online booking isn’t live yet, so this request is only saved in your browser and no payment is taken. Follow us on Instagram to hear when classes open.</p>
      <div style="display:flex;gap:10px;margin-top:16px;flex-wrap:wrap"><a class="btn btn-o" href="#" id="w-ics">Add to calendar</a><button class="btn btn-n" id="w-new">Book another</button></div>`;
    go(2);
    $('#w-new').onclick = () => { go(0); $$('.slot').forEach(x => x.classList.remove('sel')); };
    $('#w-ics').onclick = ev => { ev.preventDefault(); const [y, m, d] = sel.d.split('-'), [h, mi] = sel.t.split(':'); const st = `${y}${m}${d}T${h}${mi}00`; const end = new Date(+y, m - 1, +d, +h, +mi + c.mins); const pad = x => String(x).padStart(2, '0'); const en = `${end.getFullYear()}${pad(end.getMonth() + 1)}${pad(end.getDate())}T${pad(end.getHours())}${pad(end.getMinutes())}00`;
      const ics = `BEGIN:VCALENDAR\r\nVERSION:2.0\r\nPRODID:-//London Momentum//EN\r\nBEGIN:VEVENT\r\nUID:${rec.at}@londonmomentum\r\nDTSTAMP:${new Date().toISOString().replace(/[-:]/g, '').slice(0, 15)}Z\r\nDTSTART;TZID=Europe/London:${st}\r\nDTEND;TZID=Europe/London:${en}\r\nSUMMARY:${c.name} (London Momentum)\r\nEND:VEVENT\r\nEND:VCALENDAR`;
      const a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([ics], { type: 'text/calendar' })); a.download = 'london-momentum-class.ics'; a.click(); };
  };
  $('#w-back').onclick = () => go(0);
  go(0);
}

/* ---------------- helpful + lightbox + forms ---------------- */
$$('.helpful button').forEach(b => b.onclick = () => { const h = b.closest('.helpful'); h.innerHTML = b.dataset.v === 'y' ? '<b>Thanks! 💚</b> Glad it helped – share it with someone who needs it.' : '<b>Thanks for telling us.</b> We’ll use your feedback to improve this page.'; });
const lb = document.createElement('div'); lb.className = 'lightbox'; lb.innerHTML = '<img alt="">'; lb.onclick = () => lb.classList.remove('on'); document.body.append(lb);
$$('[data-zoom]').forEach(i => i.onclick = () => { $('img', lb).src = i.dataset.zoom; $('img', lb).alt = i.alt; lb.classList.add('on'); });
$$('form[data-preview]').forEach(f => f.onsubmit = e => { e.preventDefault(); if (!f.checkValidity()) { f.reportValidity(); return; } f.reset(); toast(f.dataset.preview); });
const sh = $('[data-share]'); if (sh) sh.onclick = async () => { try { if (navigator.share) await navigator.share({ title: document.title, url: location.href }); else { await navigator.clipboard.writeText(location.href); toast('Link copied'); } } catch (e) {} };

/* cookie notice (we set no cookies; only local storage for your own tools) */
const ck = $('.cookie'); if (ck && !S.ck) { ck.classList.add('on'); $$('button', ck).forEach(b => b.onclick = () => { S.ck = 1; save(S); ck.classList.remove('on'); }); }
const fab = $('.fab'); if (fab) { fab.onclick = () => location.href = ROOT + 'tools.html#activity'; updateFab(); }
const rs = $('#reset-data'); if (rs) rs.onclick = () => { localStorage.removeItem(KEY); toast('Your saved data has been cleared'); setTimeout(() => location.reload(), 900); };
})();
