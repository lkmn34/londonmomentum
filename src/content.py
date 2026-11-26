"""All site content. Each topic = WordPress category, each article = WordPress post."""

SRC = {
    'who': ('World Health Organization – Constitution', 'https://www.who.int/about/governance/constitution'),
    'nhs-live-well': ('NHS – Live Well', 'https://www.nhs.uk/live-well/'),
    'better-health': ('NHS Better Health', 'https://www.nhs.uk/better-health/'),
    'hse': ('NHS England – Health Survey for England', 'https://digital.nhs.uk/data-and-information/publications/statistical/health-survey-for-england'),
    'sport-england': ('Sport England – Active Lives Adult Survey 2024–25', 'https://www.sportengland.org/research-and-data/data/active-lives'),
    'london-sport': ('London Sport – Active Lives data for London', 'https://data.londonsport.org/'),
    'cmo': ('UK Chief Medical Officers’ physical activity guidelines', 'https://www.gov.uk/government/publications/physical-activity-guidelines-uk-chief-medical-officers-report'),
    'nhs-activity': ('NHS – Physical activity guidelines for adults aged 19 to 64', 'https://www.nhs.uk/live-well/exercise/physical-activity-guidelines-for-adults-aged-19-to-64/'),
    'nhs-alcohol': ('NHS – Calculating alcohol units', 'https://www.nhs.uk/live-well/alcohol-advice/calculating-alcohol-units/'),
    'nhs-sleep': ('NHS – How to get to sleep', 'https://www.nhs.uk/live-well/sleep-and-tiredness/how-to-get-to-sleep/'),
    'eatwell': ('NHS – The Eatwell Guide', 'https://www.nhs.uk/live-well/eat-well/food-guidelines-and-food-labels/the-eatwell-guide/'),
    'five-a-day': ('NHS – 5 A Day', 'https://www.nhs.uk/live-well/eat-well/5-a-day/why-5-a-day/'),
    'fibre': ('NHS – How to get more fibre into your diet', 'https://www.nhs.uk/live-well/eat-well/digestive-health/how-to-get-more-fibre-into-your-diet/'),
    'water': ('NHS – Water, drinks and your health', 'https://www.nhs.uk/live-well/eat-well/food-guidelines-and-food-labels/water-drinks-nutrition/'),
    'bda': ('British Dietetic Association', 'https://www.bda.uk.com/'),
    'bnf': ('British Nutrition Foundation', 'https://www.nutrition.org.uk/'),
    'bhf': ('British Heart Foundation – UK factsheet', 'https://www.bhf.org.uk/what-we-do/our-research/heart-statistics'),
    'ros': ('Royal Osteoporosis Society', 'https://theros.org.uk/'),
    'mind': ('Mind – Mental health facts and statistics', 'https://www.mind.org.uk/information-support/types-of-mental-health-problems/mental-health-facts-and-statistics/'),
    'diabetes-uk': ('Diabetes UK', 'https://www.diabetes.org.uk/'),
    'asthma': ('Asthma + Lung UK – Exercise and asthma', 'https://www.asthmaandlung.org.uk/'),
    'nhs-back': ('NHS – Back pain', 'https://www.nhs.uk/conditions/back-pain/'),
    'nhs-benefits': ('NHS – Benefits of exercise', 'https://www.nhs.uk/live-well/exercise/exercise-health-benefits/'),
    'c25k': ('NHS – Couch to 5K', 'https://www.nhs.uk/live-well/exercise/get-running-with-couch-to-5k/'),
    'parkrun': ('parkrun UK', 'https://www.parkrun.org.uk/'),
    'undefeatable': ('We Are Undefeatable', 'https://weareundefeatable.co.uk/'),
    'nice': ('NICE guideline NG246 – Overweight and obesity management', 'https://www.nice.org.uk/guidance/ng246'),
    'nhs-bmi': ('NHS – BMI healthy weight calculator', 'https://www.nhs.uk/health-assessment-tools/calculate-your-body-mass-index/'),
}

TOPICS = [
 dict(slug='healthy-lifestyle', name='Healthy Lifestyle', emoji='seedling', color='#12A27B', tint='#E3F5EE',
      lead='Health is more than not being ill. Small, steady habits for body, mind and social life add up to a better day – and a longer, healthier life.',
      cover='healthy-lifestyle/who-definition'),
 dict(slug='healthy-eating', name='Healthy Eating', emoji='broccoli', color='#E2552F', tint='#FCEBE4',
      lead='No fads, no rules you can’t keep. The UK Eatwell Guide in plain English, plus easy swaps for real life.',
      cover='healthy-eating/balanced-plate'),
 dict(slug='physical-activity', name='Physical Activity', emoji='person_running', color='#1E5BD8', tint='#E6EEFD',
      lead='How much should you really move? The UK guidelines made simple, and ways to fit activity into a busy London week.',
      cover='physical-activity/cover'),
 dict(slug='move-for-your-health', name='Move for Your Health', emoji='anatomical_heart', color='#D93848', tint='#FBE7E9',
      lead='Movement is medicine. What being active does for your heart, blood sugar, mind, bones, back and lungs – and how to stay active safely.',
      cover='move-for-your-health/cover'),
 dict(slug='beat-the-barriers', name='Beat the Barriers', emoji='construction', color='#7A3FD1', tint='#F0E8FC',
      lead='No time, no money, no confidence? Six common barriers to getting active – and a realistic fix for each one.',
      cover='beat-the-barriers/slide-01'),
]

# Article: slug, topic, title, excerpt, img, body (HTML), sources(list of keys), kind ('guide' or 'tip'), mins
A = []
def art(**k): A.append(k)

# ---------------------------------------------------------------- HEALTHY LIFESTYLE
art(slug='what-is-a-healthy-lifestyle', topic='healthy-lifestyle', kind='guide', mins=5,
    title='What does a healthy lifestyle really mean?',
    excerpt='Health isn’t just the absence of illness. Here’s the full picture – and the everyday habits that make the biggest difference.',
    img='healthy-lifestyle/who-definition',
    body='''
<p>The World Health Organization defines health as <em>“a state of complete physical, mental and social well-being and not merely the absence of disease or infirmity.”</em> In other words: feeling well, coping with everyday life and feeling connected to others all count – not just avoiding the doctor.</p>
<h2>The UK picture</h2>
<p>Around <strong>64% of adults in England</strong> are living with overweight or obesity, and more than a third of adults don’t reach the recommended 150 minutes of activity a week. That raises the risk of long-term conditions and puts extra pressure on the NHS. The good news: small daily changes add up.</p>
<h2>The four parts of Total Fitness</h2>
<ul>
<li><strong>Physical</strong> – heart and lung fitness, muscle strength and flexibility.</li>
<li><strong>Mental &amp; emotional</strong> – managing stress and keeping a positive outlook.</li>
<li><strong>Social</strong> – supportive relationships and feeling part of something.</li>
<li><strong>Medical</strong> – staying free from illness, or safely managing a long-term condition.</li>
</ul>
<h2>Four habits that protect you</h2>
<ul>
<li>🚭 <strong>Not smoking</strong> – protects your lungs and heart.</li>
<li>🍷 <strong>No more than 14 units of alcohol a week</strong>, spread over 3 or more days.</li>
<li>🥗 <strong>Eating well and staying active</strong> – for a healthy weight, strong bones and more energy.</li>
<li>😴 <strong>7–9 hours’ sleep</strong> and ways to manage stress.</li>
</ul>
<p>You don’t have to change everything at once. Pick one habit this week and build from there – and if you need support, your GP is a good place to start.</p>''',
    sources=['who', 'hse', 'sport-england', 'nhs-live-well', 'better-health'])

art(slug='health-is-more-than-not-being-ill', topic='healthy-lifestyle', kind='tip', mins=2,
    title='Health is more than not being ill',
    excerpt='The WHO definition of health covers body, mind and social life. Which one needs your attention this week?',
    img='healthy-lifestyle/who-definition',
    body='''<p>According to the World Health Organization, health is <em>“a state of complete physical, mental and social well-being and not merely the absence of disease or infirmity.”</em></p>
<p>That gives us three areas to look after:</p>
<ul><li>💪 <strong>Physical</strong> – moving, eating well, sleeping well.</li><li>🧠 <strong>Mental</strong> – coping with stress and looking after your mood.</li><li>🤝 <strong>Social</strong> – time with people who lift you up.</li></ul>
<p>Which one will you focus on this week?</p>''', sources=['who'])

art(slug='four-parts-of-total-fitness', topic='healthy-lifestyle', kind='tip', mins=2,
    title='The 4 parts of Total Fitness',
    excerpt='Physical, mental, social and medical – how balanced are yours?',
    img='healthy-lifestyle/total-fitness',
    body='''<ul><li>💪 <strong>Physical</strong> – cardiovascular endurance, muscular strength and flexibility.</li>
<li>😌 <strong>Mental &amp; emotional</strong> – managing stress and keeping a positive mindset.</li>
<li>🤗 <strong>Social</strong> – supportive relationships and feeling connected.</li>
<li>🩺 <strong>Medical</strong> – free from illness, or safely managing long-term conditions.</li></ul>
<p>Most of us are stronger in one or two areas than the others. Which one needs a little more attention?</p>''', sources=['nhs-live-well'])

art(slug='four-habits-that-protect-your-health', topic='healthy-lifestyle', kind='tip', mins=2,
    title='4 habits that protect your health',
    excerpt='Not smoking, sensible drinking, eating well and good sleep – what each one does for you.',
    img='healthy-lifestyle/healthy-habits',
    body='''<ul><li>🚭 <strong>Not smoking</strong> – protects your lungs and heart and cuts your risk of cancer and stroke.</li>
<li>🍷 <strong>Alcohol: no more than 14 units a week</strong> – protects your liver, brain and heart. <a href="{root}tools/#alcohol">Check your units</a>.</li>
<li>🥗 <strong>Eat well &amp; stay active</strong> – a healthy weight, strong bones and muscles, more energy.</li>
<li>😴 <strong>7–9 hours’ sleep &amp; less stress</strong> – better recovery, focus and resilience.</li></ul>''',
    sources=['nhs-live-well', 'nhs-alcohol', 'nhs-sleep'])

art(slug='everyday-habits-that-raise-your-risk', topic='healthy-lifestyle', kind='tip', mins=2,
    title='Everyday habits that quietly raise your risk',
    excerpt='Smoking, too much alcohol, ultra-processed food, sitting all day and poor sleep – and one swap to start with.',
    img='healthy-lifestyle/risks',
    body='''<p>🚬 Smoking · 🍺 drinking too much · 🍔 lots of ultra-processed food · 🛋️ long hours of sitting · 🥱 poor sleep.</p>
<p>Over time these can lead to high blood pressure, obesity, heart and circulatory disease, type 2 diabetes, stroke and poorer mental health.</p>
<p>You don’t have to change everything at once – pick one habit to swap out this week.</p>''', sources=['nhs-live-well', 'better-health'])

art(slug='your-health-support-team', topic='healthy-lifestyle', kind='tip', mins=1,
    title='You don’t have to do it alone: your support team',
    excerpt='GP, dietitian, physiotherapist, counsellor – who does what, and where to find trusted information.',
    img='healthy-lifestyle/support-team',
    body='''<ul><li>🩺 <strong>GP</strong> – your first stop for any health worry, and the route to most NHS services.</li>
<li>🥗 <strong>Registered Dietitian</strong> – evidence-based advice on food and nutrition.</li>
<li>🏋️ <strong>Physiotherapist</strong> – help with injuries, pain and moving safely.</li>
<li>💬 <strong>Mental health counsellor</strong> – talking therapies. In England you can refer yourself to NHS Talking Therapies.</li></ul>
<p>For trusted information, use nhs.uk and NHS Better Health.</p>''', sources=['nhs-live-well', 'better-health'])

# ---------------------------------------------------------------- HEALTHY EATING
art(slug='is-your-plate-balanced', topic='healthy-eating', kind='guide', mins=5,
    title='Is your plate actually balanced? The Eatwell Guide explained',
    excerpt='The UK’s official healthy-eating model in plain English – food groups, easy swaps, nutrients and hydration.',
    img='healthy-eating/balanced-plate',
    body='''<p>The <strong>Eatwell Guide</strong> is the UK’s official picture of a healthy, balanced diet. It isn’t about one meal – it shows the balance to aim for across a day or a week.</p>
<h2>Build a balanced plate</h2>
<ol>
<li><strong>Fruit &amp; vegetables</strong> – just over a third of what you eat. Aim for at least 5 portions a day.</li>
<li><strong>Starchy carbohydrates</strong> – another third. Choose wholegrain or higher-fibre versions.</li>
<li><strong>Beans, pulses, fish, eggs, meat &amp; other proteins</strong> – aim for 2 portions of fish a week, one of them oily.</li>
<li><strong>Dairy &amp; alternatives</strong> – choose lower-fat and lower-sugar options.</li>
<li><strong>Oils &amp; spreads</strong> – unsaturated, and in small amounts.</li>
</ol>
<h2>Simple swaps</h2>
<p>Sugary drinks → water. White bread → wholemeal. Crisps → unsalted nuts or fruit. Fried → grilled, steamed or baked.</p>
<h2>Watch the salt, sugar &amp; saturated fat</h2>
<p>Too much raises the risk of obesity, type 2 diabetes, heart disease, high blood pressure and tooth decay. Check front-of-pack labels – more greens, fewer reds.</p>
<h2>Don’t forget drinks</h2>
<p>Aim for 6 to 8 cups or glasses of fluid a day. Water, lower-fat milk and sugar-free drinks, including tea and coffee, all count.</p>
<p>Need tailored advice? Speak to your GP or a Registered Dietitian.</p>''',
    sources=['eatwell', 'five-a-day', 'water', 'bda', 'bnf', 'better-health'])

art(slug='eat-the-rainbow-5-a-day', topic='healthy-eating', kind='tip', mins=2,
    title='Eat the rainbow: your 5 A Day',
    excerpt='At least 5 portions of fruit and veg a day – and fresh, frozen, tinned or dried all count.',
    img='healthy-eating/five-a-day',
    body='''<p>Aim for <strong>at least 5 portions of a variety of fruit and vegetables every day</strong> 🍎🥦🥕🍌🍅</p>
<p>Fresh, frozen, tinned and dried all count. One adult portion is 80g – roughly a handful. 30g of dried fruit counts as a portion, and so does one 150ml glass of fruit juice or smoothie a day (but only one).</p>
<p>Try our <a href="{root}tools/#five">5 A Day counter</a> to see how you’re doing today.</p>''', sources=['five-a-day'])

art(slug='your-plate-balanced', topic='healthy-eating', kind='tip', mins=2,
    title='Your plate, balanced',
    excerpt='The five food groups of the UK Eatwell Guide at a glance.',
    img='healthy-eating/balanced-plate',
    body='''<ol><li>Fruit &amp; vegetables</li><li>Starchy carbohydrates (choose high-fibre)</li><li>Lean proteins</li><li>Dairy &amp; alternatives (lower-fat)</li><li>Oils &amp; spreads (unsaturated, small amounts)</li></ol>
<p>Save it as your plate guide for the week.</p>''', sources=['eatwell'])

art(slug='swap-this-for-that', topic='healthy-eating', kind='tip', mins=1,
    title='Swap this, for that',
    excerpt='Four easy food swaps that make a real difference.',
    img='healthy-eating/swaps',
    body='''<ul><li>🥤 Sugary drinks → 💧 water or sugar-free drinks</li><li>🥖 White bread / pasta → 🍞 wholemeal</li><li>🍫 Crisps / chocolate → 🥜 unsalted nuts or fresh fruit</li><li>🍟 Fried foods → 🍳 grilled, steamed or oven-baked</li></ul>
<p>Small changes, big difference. Which swap will you try first?</p>''', sources=['eatwell', 'better-health'])

art(slug='fibre-first', topic='healthy-eating', kind='tip', mins=1,
    title='Fibre first',
    excerpt='Base your meals on high-fibre starchy carbohydrates – here’s what to pick.',
    img='healthy-eating/fibre-first',
    body='''<p>Base your meals on high-fibre starchy carbohydrates:</p><ul><li>🍞 Wholemeal bread</li><li>🍚 Brown rice</li><li>🥣 Oats</li><li>🥔 Potatoes with their skins on</li></ul>
<p>Fibre supports healthy digestion and helps you feel full. Adults should aim for 30g of fibre a day – most of us get less than that.</p>''', sources=['fibre', 'eatwell'])

art(slug='stay-hydrated', topic='healthy-eating', kind='tip', mins=1,
    title='Stay hydrated: 6 to 8 glasses a day',
    excerpt='How much to drink, what counts, and why it matters.',
    img='healthy-eating/hydration',
    body='''<p>Aim for <strong>6 to 8 cups or glasses of fluid a day</strong>. Water, lower-fat milk and sugar-free drinks, including tea and coffee, all count. You may need more when it’s hot or when you’re active.</p>
<p>Good hydration helps regulate body temperature, supports focus and digestion, and helps prevent headaches and tiredness.</p>
<p>Track it with our <a href="{root}tools/#water">water tracker</a>.</p>''', sources=['water', 'eatwell'])

art(slug='watch-the-salt-sugar-and-fat', topic='healthy-eating', kind='tip', mins=1,
    title='Watch the salt, sugar & saturated fat',
    excerpt='What too much can do, and how food labels help.',
    img='healthy-eating/salt-sugar-fat',
    body='''<p>Too much salt, sugar and saturated fat increases the risk of obesity, type 2 diabetes, heart disease, high blood pressure and tooth decay.</p>
<p>Check food labels and choose lower-salt, lower-sugar options where you can. Need tailored advice? See a Registered Dietitian or your GP.</p>''', sources=['eatwell', 'bda'])

# ---------------------------------------------------------------- PHYSICAL ACTIVITY
art(slug='how-much-should-you-move', topic='physical-activity', kind='guide', mins=5,
    title='How much should you really move?',
    excerpt='The UK Chief Medical Officers’ guidelines for adults, explained – plus the benefits, the 3 types of activity, and when to pause.',
    img='physical-activity/cover',
    body='''<h2>The guidelines (adults 19–64)</h2>
<ul><li>⏱️ <strong>150 minutes of moderate activity a week</strong> – brisk walking, cycling, swimming – <em>or</em> 75 minutes of vigorous activity like running or sport, or a mix of both.</li>
<li>💪 <strong>Strength activities on at least 2 days a week</strong>, working all the major muscle groups.</li>
<li>🪑 <strong>Break up long periods of sitting.</strong></li></ul>
<p>Short bouts of any length count, and you can spread the minutes over the week in whatever way suits you. If you’re starting from nothing, any activity is better than none.</p>
<h2>What it protects you from</h2>
<p>Regular activity lowers your risk of coronary heart disease, type 2 diabetes, high blood pressure, stroke, osteoporosis and some cancers.</p>
<h2>Mix all 3 types</h2>
<p>🚣 <strong>Aerobic</strong> for heart and lungs · 🧗 <strong>Strength</strong> for muscles and bones · 🤸 <strong>Flexibility &amp; balance</strong> for joints and stability.</p>
<h2>Know when to pause</h2>
<p>Put exercise on hold if you have a fever or viral infection, chest pain, dizziness, an acute injury or uncontrolled high blood pressure. Pregnant or managing a long-term condition? Talk to your GP, a physiotherapist or an exercise referral specialist first.</p>
<p>Track your week with our <a href="{root}tools/#activity">activity tracker</a>.</p>''',
    sources=['cmo', 'nhs-activity', 'nhs-benefits', 'undefeatable'])

art(slug='150-minutes-a-week', topic='physical-activity', kind='tip', mins=1,
    title='150 minutes a week',
    excerpt='What the UK guidelines recommend – it’s just over 20 minutes a day.',
    img='physical-activity/150-minutes',
    body='''<p>The UK Chief Medical Officers recommend <strong>150 minutes of moderate activity</strong> a week – brisk walking, swimming or cycling – <strong>or 75 minutes of vigorous activity</strong>.</p><p>That’s just over 20 minutes a day. You’ve got this 💪</p>''', sources=['cmo', 'nhs-activity'])

art(slug='move-more-protect-your-health', topic='physical-activity', kind='tip', mins=1,
    title='Move more, protect your health',
    excerpt='Six conditions regular activity helps prevent.',
    img='physical-activity/prevent',
    body='''<p>Regular physical activity helps prevent:</p><ul><li>❤️ Coronary heart disease</li><li>🩸 Type 2 diabetes</li><li>🩺 High blood pressure</li><li>🧠 Stroke</li><li>🦴 Osteoporosis</li><li>🎗️ Some cancers</li></ul><p>Every active minute counts.</p>''', sources=['nhs-benefits', 'cmo'])

art(slug='mix-all-3-types-of-activity', topic='physical-activity', kind='tip', mins=1,
    title='Mix all 3 types of activity',
    excerpt='Aerobic, strength, flexibility & balance – which one is missing from your week?',
    img='physical-activity/types',
    body='''<ul><li>🚣 <strong>Aerobic</strong> – heart and lung stamina.</li><li>🧗 <strong>Strength</strong> – muscle and bone strength.</li><li>🤸 <strong>Flexibility &amp; balance</strong> – joint range of motion and stability.</li></ul><p>Which one is missing from your week?</p>''', sources=['cmo'])

art(slug='no-time-no-problem', topic='physical-activity', kind='tip', mins=1,
    title='No time? No problem.',
    excerpt='Short brisk walks all add up – plus quick fixes for low confidence, tiredness and tight budgets.',
    img='physical-activity/no-time',
    body='''<p>Break activity into short brisk walks – they all add up.</p>
<ul><li><strong>Low confidence?</strong> Start with beginner sessions, or exercise with a friend.</li><li><strong>Tired or on a budget?</strong> Choose free walks or home workouts, earlier in the day.</li></ul>
<p>Tag a friend and get a walk in the diary this week 👟</p>''', sources=['cmo', 'better-health'])

art(slug='health-vs-fitness', topic='physical-activity', kind='tip', mins=1,
    title='Health vs fitness – what’s the difference?',
    excerpt='Regular moderate movement for health; structured training for fitness. Both matter.',
    img='physical-activity/health-vs-fitness',
    body='''<p>🚶 <strong>General health</strong> comes from regular, moderate daily movement.</p><p>🏋️ <strong>Physical fitness</strong> comes from structured, higher-intensity training that gradually gets harder (progressive overload).</p><p>Both matter – start where you are.</p>''', sources=['cmo'])

art(slug='know-when-to-pause', topic='physical-activity', kind='tip', mins=1,
    title='Know when to pause',
    excerpt='When to put exercise on hold – and who to talk to first.',
    img='physical-activity/pause',
    body='''<p>Put exercise on hold if you have:</p><ul><li>🤒 A fever or viral infection</li><li>💔 Chest pain</li><li>😵 Dizziness</li><li>🩹 An acute injury</li><li>❤️ Uncontrolled high blood pressure</li></ul>
<p>Pregnant or managing a long-term condition? Talk to your GP, a physiotherapist or an exercise referral specialist before starting.</p>
<p class="callout warn">Chest pain that doesn’t go away? Call 999.</p>''', sources=['nhs-activity', 'undefeatable'])

# ---------------------------------------------------------------- MOVE FOR YOUR HEALTH
art(slug='movement-is-medicine', topic='move-for-your-health', kind='guide', mins=6,
    title='Movement is medicine',
    excerpt='What being active does inside your body – for your heart, blood sugar, mind, bones, back and lungs.',
    img='move-for-your-health/cover',
    body='''<p>Regular physical activity can lower your risk of major illnesses like coronary heart disease, stroke, type 2 diabetes and some cancers – and lower your risk of early death by up to 30%.</p>
<h2>❤️ Heart</h2><p>More than 8 million people in the UK live with heart and circulatory disease. Activity helps lower blood pressure, improves cholesterol and keeps your heart muscle strong.</p>
<h2>🩸 Blood sugar</h2><p>Working muscles use glucose for fuel, and regular activity helps your body use insulin better – lowering your risk of type 2 diabetes.</p>
<h2>🧠 Mind</h2><p>Each year, 1 in 4 people in England experience a mental health problem. Moving more can lift your mood, ease stress and help you sleep.</p>
<h2>🦴 Bones &amp; joints</h2><p>Over 50, 1 in 2 women and 1 in 5 men will break a bone because of osteoporosis. Weight-bearing and strength activity help keep bones strong.</p>
<h2>🧘 Back</h2><p>With most back pain, staying active helps you recover faster than resting in bed.</p>
<h2>🫁 Lungs</h2><p>Living with asthma? Warm up gradually, carry your reliever inhaler and use your preventer as prescribed.</p>
<h2>Living with a health condition?</h2><p>Check with your GP or nurse first, start low and go slow, and stop and get help if you feel chest pain, dizziness or unusual breathlessness.</p>''',
    sources=['nhs-benefits', 'bhf', 'diabetes-uk', 'mind', 'ros', 'nhs-back', 'asthma'])

art(slug='8-million-heart-and-circulatory-disease', topic='move-for-your-health', kind='tip', mins=1,
    title='8 million+: protect your heart',
    excerpt='More than 8 million people in the UK live with heart and circulatory disease.',
    img='move-for-your-health/heart-8-million',
    body='''<p>More than <strong>8 million people in the UK</strong> are living with heart and circulatory disease.</p><p>Regular activity is one of the best things you can do for your heart: it helps lower blood pressure, improves cholesterol and keeps your heart muscle strong.</p><p>Start where you are – a brisk 10-minute walk counts 🚶</p>''', sources=['bhf'])

art(slug='build-bones-that-last', topic='move-for-your-health', kind='tip', mins=1,
    title='Build bones that last',
    excerpt='1 in 2 women and 1 in 5 men over 50 will break a bone because of osteoporosis.',
    img='move-for-your-health/bones',
    body='''<p>Over the age of 50, <strong>1 in 2 women and 1 in 5 men</strong> will break a bone because of osteoporosis.</p><p>Weight-bearing and strength activities help keep your bones strong: brisk walking, dancing, stair climbing and strength training.</p><p>It’s never too early – or too late – to start.</p>''', sources=['ros'])

art(slug='your-heart-on-exercise', topic='move-for-your-health', kind='tip', mins=1,
    title='Your heart on exercise',
    excerpt='Blood pressure down, “good” cholesterol up – what activity does for your heart.',
    img='move-for-your-health/heart-on-exercise',
    body='''<ul><li>⬇️ Blood pressure goes down</li><li>⬆️ “Good” HDL cholesterol goes up</li><li>💪 Your heart muscle gets stronger</li><li>〰️ Your blood vessels stay more flexible</li></ul><p>All of this adds up to a lower risk of heart disease and stroke.</p>''', sources=['nhs-benefits', 'bhf'])

art(slug='move-for-your-mind', topic='move-for-your-health', kind='tip', mins=1,
    title='1 in 4: move for your mind',
    excerpt='Each year 1 in 4 people in England experience a mental health problem. Movement can help.',
    img='move-for-your-health/mind',
    body='''<p>Each year, <strong>1 in 4 people in England</strong> experience a mental health problem.</p><p>Moving your body can help you lift your mood, ease stress and anxiety, sleep better and connect with others.</p>
<p class="callout">If you’re struggling, you don’t have to cope alone – talk to your GP or someone you trust. In a crisis, call NHS 111 (option 2) or Samaritans on 116 123.</p>''', sources=['mind', 'nhs-benefits'])

art(slug='back-pain-keep-moving', topic='move-for-your-health', kind='tip', mins=1,
    title='Back pain? Keep moving.',
    excerpt='What to do – and avoid – with most everyday back pain.',
    img='move-for-your-health/back-pain',
    body='''<p>✅ <strong>Do</strong> carry on with daily activities as much as you can, and try walking, swimming, yoga or pilates.</p><p>❌ <strong>Avoid</strong> long periods in bed, and sitting still for hours without a break.</p><p>See a GP if the pain doesn’t improve within a few weeks or keeps getting worse.</p>''', sources=['nhs-back'])

art(slug='stay-active-safely', topic='move-for-your-health', kind='tip', mins=1,
    title='Living with a health condition? Stay active, safely',
    excerpt='Check first, start low, go slow – and know the warning signs.',
    img='move-for-your-health/active-with-condition',
    body='''<ul><li>🩺 Check with your GP or nurse first</li><li>🐢 Start low, go slow</li><li>🔥 Warm up and cool down</li><li>💊 Keep your medication handy (for example an inhaler or glucose tablets)</li></ul>
<p class="callout warn">Stop and get help if you feel chest pain, dizziness or unusual breathlessness.</p>''', sources=['nhs-activity', 'undefeatable'])

# ---------------------------------------------------------------- BEAT THE BARRIERS
art(slug='whats-stopping-you', topic='beat-the-barriers', kind='guide', mins=5,
    title='What’s stopping you? 6 barriers and how to beat them',
    excerpt='No time, no money, too old, the kids, boredom or nerves – a realistic fix for each.',
    img='beat-the-barriers/slide-01',
    gallery=[f'beat-the-barriers/slide-0{i}' for i in range(1, 9)],
    body='''<p>Around 1 in 4 adults in England do less than 30 minutes of physical activity a week – and in London, about a third of adults aren’t meeting the recommended levels. Most of us have a reason. Here are the six we hear most, and a fix for each.</p>
<h2>⏳ “I don’t have time.”</h2><p><strong>Every minute counts.</strong> Activity of any length adds up towards your 150 minutes – take the stairs, walk part of your commute, get out at lunchtime.</p>
<h2>💷 “I can’t afford a gym.”</h2><p><strong>Move for free.</strong> Brisk walks, the free NHS Couch to 5K app, parkrun, home workouts and your local park cost nothing.</p>
<h2>👵 “I’m too old to start.”</h2><p><strong>It’s never too late.</strong> Start gently and build up. Over 65? Add strength and balance activities on 2 days a week.</p>
<h2>🧒 “I’ve got the kids with me.”</h2><p><strong>Make it family time.</strong> Walk or scoot to school, play in the park, have a kitchen disco – kids copy what they see.</p>
<h2>🥱 “I just don’t enjoy exercise.”</h2><p><strong>Find your thing.</strong> It doesn’t have to be the gym – dance, garden, cycle, swim or walk with a friend.</p>
<h2>😰 “I feel nervous and out of place.”</h2><p><strong>Start small, bring a buddy.</strong> Step a little outside your comfort zone at a time. Health worries? Ask your GP.</p>
<p><strong>Your move:</strong> pick one barrier and try one fix this week.</p>''',
    sources=['sport-england', 'london-sport', 'cmo', 'c25k', 'parkrun'])

art(slug='11-8-million-adults-inactive', topic='beat-the-barriers', kind='tip', mins=1,
    title='11.8 million adults do less than 30 minutes a week',
    excerpt='About 1 in 4 adults in England are inactive. Going from nothing to a little makes the biggest difference.',
    img='beat-the-barriers/11-8-million',
    body='''<p>That’s how many adults in England do less than 30 minutes of physical activity a week – roughly 1 in 4 of us.</p><p>The good news: the biggest health gains come from going from nothing to even a little. If you’re starting from zero, a short walk today really does count.</p>''', sources=['sport-england'])

art(slug='150-minutes-is-21-a-day', topic='beat-the-barriers', kind='tip', mins=1,
    title='150 minutes a week is about 21 minutes a day',
    excerpt='Short bouts count – or fit it into one or two longer sessions.',
    img='beat-the-barriers/150-minutes',
    body='''<p>That’s the UK goal for moderate activity. Short bouts of any length count, or you can fit it into 1 or 2 longer sessions if that suits your week better.</p><p>Add strength activities on at least 2 days a week too 💪</p>''', sources=['cmo', 'nhs-activity'])

art(slug='free-ways-to-move', topic='beat-the-barriers', kind='tip', mins=1,
    title='Free ways to move in London',
    excerpt='No gym? No problem. Walks, Couch to 5K, parkrun, home workouts and active travel.',
    img='beat-the-barriers/free-ways',
    body='''<ul><li>🚶 <strong>Brisk walking</strong> – London’s parks, canals and the Thames Path are on your doorstep.</li><li>📱 <strong>NHS Couch to 5K app</strong> – a free plan from the couch to 5K in 9 weeks.</li><li>🏃 <strong>parkrun</strong> – free weekly 5K events: walk, jog or run.</li><li>🏠 <strong>Home workouts</strong> – bodyweight moves, no kit needed.</li><li>🚲 <strong>Active travel</strong> – walk or cycle short trips.</li></ul>''', sources=['c25k', 'parkrun', 'better-health'])

art(slug='myth-vs-fact-exercise', topic='beat-the-barriers', kind='tip', mins=1,
    title='Myth vs fact: exercise edition',
    excerpt='Does it only count at the gym? Are short bursts pointless? Is it too late?',
    img='beat-the-barriers/myths',
    body='''<p>❌ It only counts if you’re sweating at the gym.<br>✅ Brisk walking, gardening, dancing and cycling all count.</p><p>❌ Short bursts are pointless.<br>✅ Activity of any length adds up and benefits your health.</p><p>❌ I’ve left it too late.<br>✅ It’s never too late – start gently and build up.</p>''', sources=['cmo', 'nhs-activity'])

art(slug='small-wins-big-confidence', topic='beat-the-barriers', kind='tip', mins=1,
    title='Small wins, big confidence',
    excerpt='The best way to build belief in yourself is with small, repeatable wins.',
    img='beat-the-barriers/small-wins',
    body='''<p>Believing you can do something is a big part of actually doing it – and the best way to build that belief is with small wins.</p><ol><li>Pick something you know you can do</li><li>Do it 3 times this week</li><li>Notice it feels easier</li><li>Add a little more</li></ol><p>Feeling nervous? Bring a friend along – it’s easier together 🤝</p>''', sources=[])

art(slug='find-your-why', topic='beat-the-barriers', kind='tip', mins=1,
    title='Find your why',
    excerpt='Motivation that lasts comes from within. Finish the sentence: “I want to move more so I can…”',
    img='beat-the-barriers/your-why',
    body='''<p>Motivation that lasts comes from within – knowing what moving more means to <em>you</em>.</p><p>Finish the sentence: <strong>“I want to move more so I can…”</strong></p><ul><li>🧒 keep up with my kids</li><li>😴 sleep better</li><li>😌 feel less stressed</li><li>🏡 stay independent</li><li>💪 feel proud of myself</li></ul>''', sources=[])

ARTICLES = A

CLASSES = [
 dict(id='walk', name='Walk & Talk Coaching', emoji='person_walking', level='Beginner', mins=30, desc='A guided brisk-walk session by phone or video – join from your local park or the Thames Path.'),
 dict(id='strength', name='Strength Basics', emoji='flexed_biceps', level='Beginner', mins=40, desc='Bodyweight strength for all major muscle groups. No kit needed, just a chair and some floor space.'),
 dict(id='mobility', name='Mobility & Stretch', emoji='person_in_lotus_position', level='All levels', mins=30, desc='Gentle flexibility and balance work to ease stiffness after a day at the desk.'),
 dict(id='cardio', name='Low-Impact Cardio', emoji='man_dancing', level='All levels', mins=35, desc='Get your heart rate up without the jumping – kind on knees and neighbours.'),
 dict(id='pilates', name='Core & Pilates', emoji='person_lifting_weights', level='Improver', mins=45, desc='Build core strength and posture with mat-based pilates moves.'),
 dict(id='one2one', name='1:1 Online Coaching', emoji='handshake', level='Personal', mins=45, desc='A one-to-one video session built around your goals, routine and any health conditions.'),
]
# weekday (0=Mon) -> list of (time, class id)
TIMETABLE = {
 0: [('07:00', 'mobility'), ('12:30', 'walk'), ('19:00', 'strength')],
 1: [('07:00', 'cardio'), ('18:30', 'pilates')],
 2: [('07:00', 'mobility'), ('12:30', 'walk'), ('19:00', 'cardio')],
 3: [('07:00', 'strength'), ('18:30', 'pilates')],
 4: [('07:00', 'cardio'), ('12:30', 'walk')],
 5: [('09:00', 'strength'), ('10:30', 'mobility')],
 6: [('10:00', 'walk')],
}
