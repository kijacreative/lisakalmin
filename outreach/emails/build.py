#!/usr/bin/env python3
"""Builds the Money Wealth and Miracles December emails as HTML and plain text.

    python3 outreach/emails/build.py

Series 1 (masterclass sign-ups) and Series 2 (full email list) are Kit emails in Lisa's
brand, with a logo that works in dark mode. Series 3 (sourced, cold) is a plain personal
note with no images, for a separate cold-email tool and domain. The copy comes from
outreach/email-masterclass.md, email-main-list.md and email-cold.md; edit it here and rebuild.

Inline markup in the copy: **bold**, [link text](url), and straight quotes, which become
curly ones. Liquid tags ({{ ... }}, {% ... %}) pass through untouched.
"""
import html, os, re

OUT = os.path.dirname(os.path.abspath(__file__))
SITE = 'https://www.lisakalmin.com'
COURSE = SITE + '/course/'

def utm(content, code=False, source='kit', medium='email'):
    q = ('code=MIRACLE200&' if code else '') + f'utm_source={source}'
    if medium: q += f'&utm_medium={medium}'
    return f'{COURSE}?{q}&utm_campaign=mwm-dec&utm_content={content}'

# ---------------------------------------------------------------- brand
C = dict(oat='#F8F4EC', paper='#FDFBF7', ink='#232C26', forest='#2F3B33', mid='#56635B',
         rule='#C9D1C1', rose='#A04E5C', blush='#F1DCDF', sage='#DDE3D3')
# dark mode (Apple Mail, iOS Mail, Outlook for Mac and Outlook.com read these)
D = dict(bg='#141B16', card='#1E2620', text='#E9E3D6', head='#F8F4EC', mid='#A9B4AC',
         rule='#3A463D', blush='#3A272B', sage='#29342C', link='#E3B5BC')
FONT = "'Jost',Helvetica,Arial,sans-serif"
HEAD = "'Plus Jakarta Sans',Helvetica,Arial,sans-serif"

# ---------------------------------------------------------------- inline text
LIQUID = re.compile(r'(\{\{.*?\}\}|\{%.*?%\})')

def smart(s):
    parts = LIQUID.split(s)
    for i in range(0, len(parts), 2):
        t = parts[i]
        t = re.sub(r'(^|[\s(\[—>*])"', r'\1“', t)
        t = t.replace('"', '”').replace("'", '’')
        parts[i] = t
    return ''.join(parts)

def inline(s, strong_cls='s'):
    s = smart(s)
    s = re.sub(r'\*\*(.+?)\*\*', lambda m: f'<strong class="{strong_cls}" style="color:{C["forest"]};">{m.group(1)}</strong>', s)
    s = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', lambda m: f'<a class="a" href="{m.group(2)}" style="color:{C["rose"]};font-weight:700;text-decoration:underline;">{m.group(1)}</a>', s)
    return s

def plain(s):
    s = smart(s).replace('“', '"').replace('”', '"').replace('’', "'")
    s = re.sub(r'\*\*(.+?)\*\*', r'\1', s)
    s = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'\1 (\2)', s)
    return s

# ---------------------------------------------------------------- blocks
# Each block is a tuple. HTML and text renderers below.
def P(t): return ('p', t)
def UL(*items): return ('ul', items)
def OL(*items): return ('ol', items)
def H(t): return ('h', t)
def BTN(label, url): return ('btn', label, url)
def COND(tag, yes, no): return ('cond', tag, yes, no)
def QUOTE(text, who): return ('quote', text, who)
def LISA(note): return ('lisa', note)
def SLOT(note): return ('slot', note)          # {{ message_content }}: optional block typed in Kit
def COURSE_CARD(url, label='See the course and the dates'): return ('course', url, label)
def CLASS_CARD(url, label='Save my free seat'): return ('class', url, label)
def CODE_CARD(url, label='Join for $597', eyebrow='Your thank-you price', who=None): return ('code', url, label, eyebrow, who)

GREET = 'Hi {{ subscriber.first_name | default: "there" }},'

def p_html(t, size=18, lh=28, mb=18, cls='t'):
    return f'<p class="{cls}" style="margin:0 0 {mb}px;font-size:{size}px;line-height:{lh}px;color:{C["ink"]};">{inline(t)}</p>'

def button(label, url, small=False):
    pad, fs = ('14px 28px', 16) if small else ('16px 32px', 17)
    return (f'<table role="presentation" cellpadding="0" cellspacing="0" border="0"><tr>'
            f'<td bgcolor="{C["rose"]}" style="border-radius:999px;background:{C["rose"]};">'
            f'<a href="{url}" style="display:inline-block;padding:{pad};border-radius:999px;background:{C["rose"]};'
            f'font-family:{FONT};font-size:{fs}px;line-height:20px;font-weight:700;color:#ffffff;text-decoration:none;">'
            f'{smart(label)} &rarr;</a></td></tr></table>')

def eyebrow(t, mb=10):
    return (f'<p class="ey" style="margin:0 0 {mb}px;font-size:12px;line-height:16px;letter-spacing:3px;'
            f'text-transform:uppercase;font-weight:500;color:{C["rose"]};">{smart(t)}</p>')

def card(inner, kind='blush'):
    bg = C[kind]
    return (f'<div class="card {kind}" style="background:{bg};border-radius:16px;padding:28px 30px;margin:6px 0 26px;'
            f'font-family:{FONT};color:{C["forest"]};">{inner}</div>')

def list_html(items, ordered):
    rows = []
    for i, it in enumerate(items, 1):
        mark = f'{i}.' if ordered else '&bull;'
        rows.append(f'<p class="t" style="margin:0;padding:5px 0 5px 28px;text-indent:-28px;color:{C["ink"]};">'
                    f'<span class="ey" style="display:inline-block;width:28px;text-indent:0;color:{C["rose"]};font-weight:700;">{mark}</span>{inline(it)}</p>')
    return f'<div style="margin:0 0 22px;">{"".join(rows)}</div>'

def block_html(b):
    k = b[0]
    if k == 'p': return p_html(b[1])
    if k == 'h':
        return (f'<p class="h" style="margin:8px 0 12px;font-family:{HEAD};font-weight:800;font-size:22px;line-height:28px;'
                f'letter-spacing:-0.3px;color:{C["forest"]};">{smart(b[1])}</p>')
    if k in ('ul', 'ol'): return list_html(b[1], k == 'ol')
    if k == 'btn': return f'<div style="margin:4px 0 26px;">{button(b[1], b[2])}</div>'
    if k == 'cond':
        _, tag, yes, no = b
        return (f'{{% if subscriber.tags contains "{tag}" %}}{"".join(block_html(x) for x in yes)}'
                f'{{% else %}}{"".join(block_html(x) for x in no)}{{% endif %}}')
    if k == 'quote':
        return card(f'<p class="s" style="margin:0 0 12px;font-size:19px;line-height:28px;font-weight:500;color:{C["forest"]};">“{smart(b[1])}”</p>'
                    f'<p class="m" style="margin:0;font-size:15px;line-height:22px;color:{C["mid"]};">{inline(b[2])}</p>', 'sage')
    if k == 'lisa':
        return (f'<p class="ph" style="margin:0 0 18px;padding:10px 14px;border:2px dashed #C99A2E;border-radius:10px;'
                f'background:#FFF4D6;color:#5A4410;font-size:16px;line-height:24px;">{smart(b[1])}</p>')
    if k == 'slot':
        return f'<!-- {b[1]} -->\n<div class="slot">{{{{ message_content }}}}</div>'
    if k == 'course':
        _, url, label = b
        return card(eyebrow('Live group course')
            + f'<p class="h h1" style="margin:0 0 14px;font-family:{HEAD};font-weight:800;font-size:28px;line-height:34px;letter-spacing:-0.5px;color:{C["forest"]};">Money Wealth and Miracles</p>'
            + f'<p class="s" style="margin:0 0 4px;font-size:17px;line-height:26px;"><strong>Begins Monday, December 14</strong></p>'
            + f'<p class="s" style="margin:0 0 4px;font-size:17px;line-height:26px;">Six live sessions on Zoom · 5:30 to 7:00 pm PT</p>'
            + f'<p class="s" style="margin:0 0 22px;font-size:17px;line-height:26px;">Every session recorded · $797</p>'
            + button(label, url))
    if k == 'class':
        _, url, label = b
        return card(eyebrow('Free live masterclass')
            + f'<p class="h h1" style="margin:0 0 14px;font-family:{HEAD};font-weight:800;font-size:28px;line-height:34px;letter-spacing:-0.5px;color:{C["forest"]};">Opening the Flow of Money: Letting Go of Your Stops</p>'
            + f'<p class="s" style="margin:0 0 4px;font-size:17px;line-height:26px;"><strong>Thursday, December 3</strong></p>'
            + f'<p class="s" style="margin:0 0 4px;font-size:17px;line-height:26px;">5:30 to 7:00 pm PT · Live on Zoom</p>'
            + f'<p class="s" style="margin:0 0 22px;font-size:17px;line-height:26px;">Free · 90 minutes with Lisa</p>'
            + button(label, url))
    if k == 'code':
        _, url, label, eb, who = b
        sub = who or 'Paid in full, with the code MIRACLE200'
        return card(eyebrow(eb)
            + f'<p class="h h1" style="margin:0 0 6px;font-family:{HEAD};font-weight:800;font-size:40px;line-height:44px;letter-spacing:-1px;color:{C["forest"]};">$597 '
              f'<span class="m" style="font-family:{FONT};font-weight:400;font-size:22px;letter-spacing:0;color:{C["mid"]};text-decoration:line-through;">$797</span></p>'
            + f'<p class="s" style="margin:0 0 4px;font-size:17px;line-height:26px;">{smart(sub)}</p>'
            + f'<p class="s" style="margin:0 0 18px;font-size:17px;line-height:26px;"><strong>Through Monday, December 14 at 5:30 pm PT</strong></p>'
            + f'<p style="margin:0 0 20px;"><span class="codechip" style="display:inline-block;padding:6px 14px;border:2px dashed {C["rose"]};border-radius:8px;font-size:16px;line-height:20px;font-weight:700;letter-spacing:2px;color:{C["rose"]};">MIRACLE200</span></p>'
            + button(label, url))
    raise ValueError(k)

def block_text(b):
    k = b[0]
    if k == 'p': return plain(b[1])
    if k == 'h': return plain(b[1]).upper()
    if k == 'ul': return '\n'.join('- ' + plain(i) for i in b[1])
    if k == 'ol': return '\n'.join(f'{n}. ' + plain(i) for n, i in enumerate(b[1], 1))
    if k == 'btn': return f'{plain(b[1])}:\n{b[2]}'
    if k == 'cond':
        _, tag, yes, no = b
        return (f'{{% if subscriber.tags contains "{tag}" %}}' + '\n\n'.join(block_text(x) for x in yes)
                + '{% else %}' + '\n\n'.join(block_text(x) for x in no) + '{% endif %}')
    if k == 'quote': return f'"{plain(b[1])}"\n{plain(b[2])}'
    if k == 'lisa': return plain(b[1])
    if k == 'slot': return '{{ message_content }}'
    if k == 'course':
        return ('MONEY WEALTH AND MIRACLES\nBegins Monday, December 14\nSix live sessions on Zoom, 5:30 to 7:00 pm PT\n'
                f'Every session recorded, $797\n\n{b[2]}:\n{b[1]}')
    if k == 'class':
        return ('FREE LIVE MASTERCLASS\nOpening the Flow of Money: Letting Go of Your Stops\nThursday, December 3\n'
                f'5:30 to 7:00 pm PT, live on Zoom\nFree, 90 minutes with Lisa\n\n{b[2]}:\n{b[1]}')
    if k == 'code':
        return (f'{b[3].upper()}\n$597 (regularly $797)\n{plain(b[4] or "Paid in full, with the code MIRACLE200")}\n'
                f'Through Monday, December 14 at 5:30 pm PT\nCode: MIRACLE200\n\n{b[2]}:\n{b[1]}')
    raise ValueError(k)

# ---------------------------------------------------------------- page
DARK_CSS = f"""
  @media (prefers-color-scheme:dark){{
    body,.bg{{background:{D['bg']}!important}}
    .letter{{background:{D['card']}!important}}
    .letter .t,.letter li,.slot,.slot p{{color:{D['text']}!important}}
    .s,.h,.s strong,.letter strong{{color:{D['head']}!important}}
    .m,.foot,.foot a{{color:{D['mid']}!important}}
    .ey,.a,.slot a{{color:{D['link']}!important}}
    .card.blush{{background:{D['blush']}!important}}
    .card.sage{{background:{D['sage']}!important}}
    .codechip{{color:{D['link']}!important;border-color:{D['link']}!important}}
    .rule{{border-color:{D['rule']}!important}}
    .logo-l{{display:none!important}}
    .logo-d{{display:block!important;max-height:none!important;overflow:visible!important}}
  }}
  /* Outlook.com and Outlook apps */
  [data-ogsb] body,[data-ogsb] .bg{{background:{D['bg']}!important}}
  [data-ogsb] .letter{{background:{D['card']}!important}}
  [data-ogsb] .card.blush{{background:{D['blush']}!important}}
  [data-ogsb] .card.sage{{background:{D['sage']}!important}}
  [data-ogsc] .t,[data-ogsc] .slot{{color:{D['text']}!important}}
  [data-ogsc] .s,[data-ogsc] .h,[data-ogsc] strong{{color:{D['head']}!important}}
  [data-ogsc] .m,[data-ogsc] .foot{{color:{D['mid']}!important}}
  [data-ogsc] .ey,[data-ogsc] .a{{color:{D['link']}!important}}
  [data-ogsc] .logo-l{{display:none!important}}
  [data-ogsc] .logo-d{{display:block!important;max-height:none!important;overflow:visible!important}}
"""

LOGO_HTML = f"""<!-- logo: the oat chip version shows everywhere, and blends into the page in light mode.
     Gmail and Outlook can't be told about dark mode, so when they darken the page the chip
     stays a cream label and the logo stays readable. Apple Mail, iOS Mail and Outlook.com
     read the dark-mode styles above and swap in the light logo on its own. -->
<tr><td class="logo-row" style="padding:0 26px 18px;">
<a href="{SITE}/" style="text-decoration:none;">
<img class="logo-l" src="{SITE}/email/logo-email-chip.png" width="208" height="52" alt="Lisa Kalmin" style="display:block;width:208px;height:auto;font-family:{FONT};font-size:22px;font-weight:700;letter-spacing:1px;color:{C['forest']};">
<!--[if !mso]><!--><div class="logo-d" style="display:none;max-height:0;overflow:hidden;mso-hide:all;padding:11px 14px;"><img src="{SITE}/email/logo-email-dark.png" width="180" height="30" alt="Lisa Kalmin" style="display:block;width:180px;height:auto;"></div><!--<![endif]-->
</a>
</td></tr>"""

def sign_off_html(line):
    return (f'<div class="px" style="padding:4px 40px 30px;font-family:{FONT};font-size:18px;line-height:28px;">'
            f'<p class="t" style="margin:0 0 4px;color:{C["ink"]};">{smart(line)}</p>'
            f'<p class="s" style="margin:0 0 18px;font-weight:700;color:{C["forest"]};">Lisa</p>'
            f'<p class="m" style="margin:0;font-size:14px;line-height:21px;color:{C["mid"]};"><strong class="s" style="color:{C["forest"]};">Lisa Kalmin</strong><br>'
            f'Transformational Mindset Wizard<br>Author of <em>The Problem Is How You See the Problem</em></p></div>')

SIGN_TEXT = 'Lisa Kalmin\nTransformational Mindset Wizard\nAuthor of "The Problem Is How You See the Problem"'

def page(e):
    blocks = list(e['body'])
    if not any(b[0] == 'slot' for b in blocks):
        blocks.append(SLOT('Kit needs this tag. Leave the editor body empty; anything typed there appears here.'))
    body = ''.join(block_html(b) for b in blocks)
    ps = ''
    if e.get('ps'):
        ps = (f'<div class="px rule" style="padding:24px 40px 34px;border-top:1px solid {C["rule"]};font-family:{FONT};font-size:17px;line-height:26px;">'
              + ''.join(block_html(b).replace('font-size:18px;line-height:28px', 'font-size:17px;line-height:26px') for b in e['ps'])
              + '</div>')
    pre = html.escape(smart(e['preview']))
    return f"""<!doctype html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="x-apple-disable-message-reformatting">
<meta name="color-scheme" content="light dark">
<meta name="supported-color-schemes" content="light dark">
<title>{html.escape(smart(e['subject_a']))}</title>
<!--
  {e['series']} · {e['id']}
  Send: {e['send']}
  Audience: {e['audience']}
  Subject A: {smart(e['subject_a'])}
  Subject B: {smart(e['subject_b'])}
  Preview text: {smart(e['preview'])}
  Kit: paste this whole file as a custom HTML template for this one email (Kit requires the
  {{{{ message_content }}}} tag, placed below). Leave the editor body empty unless you want the
  optional block noted next to the tag.{(' ' + e['note']) if e.get('note') else ''}
-->
<!--[if mso]><noscript><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml></noscript><![endif]-->
<link href="https://fonts.googleapis.com/css2?family=Jost:ital,wght@0,400;0,500;0,700;1,400&family=Plus+Jakarta+Sans:wght@800&display=swap" rel="stylesheet">
<style>
  :root{{color-scheme:light dark;supported-color-schemes:light dark}}
  body{{margin:0;padding:0;width:100%!important;background:{C['oat']};-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%}}
  table{{border-collapse:collapse;mso-table-lspace:0;mso-table-rspace:0}}
  img{{border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic}}
  a{{color:{C['rose']}}}
  .slot p{{margin:0 0 18px;font-size:18px;line-height:28px;color:{C['ink']}}}
  .slot blockquote{{margin:6px 0 24px;padding:22px 26px;background:{C['blush']};border-left:4px solid {C['rose']};border-radius:0 14px 14px 0;color:{C['forest']}}}
  .slot a{{color:{C['rose']};font-weight:700}}
  @media (max-width:620px){{
    .container{{width:100%!important}}
    .px{{padding-left:22px!important;padding-right:22px!important}}
    .logo-row{{padding-left:8px!important}}
    .card{{padding:24px 20px!important}}
    .h1{{font-size:26px!important;line-height:32px!important}}
  }}{DARK_CSS}</style>
</head>
<body class="bg" style="margin:0;padding:0;background:{C['oat']};">
<div style="display:none;max-height:0;overflow:hidden;mso-hide:all;font-size:1px;line-height:1px;color:{C['oat']};opacity:0;">{pre}{'&#8199;&#65279;&#847;' * 40}</div>

<table role="presentation" class="bg" width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="{C['oat']}" style="background:{C['oat']};">
<tr><td align="center" style="padding:24px 10px;">
<table role="presentation" class="container" width="600" cellpadding="0" cellspacing="0" border="0" style="width:600px;max-width:600px;">

{LOGO_HTML}

<tr><td class="letter" bgcolor="{C['paper']}" style="background:{C['paper']};border-radius:18px;font-family:{FONT};font-size:18px;line-height:28px;color:{C['ink']};">
<div class="px" style="padding:36px 40px 6px;">
{p_html(GREET)}
{body}
</div>
{sign_off_html(e['sign'])}
{ps}
</td></tr>

<tr><td class="px foot" style="padding:26px 40px 8px;font-family:{FONT};font-size:13px;line-height:20px;color:{C['mid']};text-align:center;">
<p style="margin:0 0 8px;">You’re receiving this at {{{{ subscriber.email_address }}}} because you joined Lisa Kalmin’s list.</p>
<p style="margin:0 0 8px;"><a href="{{{{ unsubscribe_url }}}}" style="color:{C['mid']};text-decoration:underline;">Unsubscribe</a> &nbsp;·&nbsp; <a href="{{{{ subscriber_preferences_url }}}}" style="color:{C['mid']};text-decoration:underline;">Update your preferences</a></p>
<p style="margin:0;">{{{{ address }}}}</p>
</td></tr>

</table>
</td></tr>
</table>
</body>
</html>
"""

def text(e):
    parts = [f"Subject A: {plain(e['subject_a'])}", f"Subject B: {plain(e['subject_b'])}",
             f"Preview text: {plain(e['preview'])}", f"Send: {e['send']}", f"Audience: {e['audience']}", '-' * 60, '', GREET]
    parts += [block_text(b) for b in e['body']]
    parts += [plain(e['sign']) + '\nLisa', SIGN_TEXT]
    parts += [block_text(b) for b in e.get('ps', [])]
    return '\n\n'.join(p for p in parts if p) + '\n'

# ---------------------------------------------------------------- Series 1: masterclass sign-ups
S1 = 'Series 1 · Masterclass sign-ups'
A1 = 'tag masterclass-nov19, not mwm-buyer'
FLOW = 'To your abundant flow!'
mc = lambda n: utm(f'mc-e{n}')
mcc = lambda n: utm(f'mc-e{n}', code=True)
QA = 'Optional, if the Dec 9 Ask Lisa Q&A runs: type it in the Kit editor body and it shows here.'

series1 = [
dict(id='mc-1', send='Tuesday, November 24, 9:00 am PT', price='$797',
  subject_a='What happens after you find the stop', subject_b="The part we didn't have time for",
  preview='Finding your stop takes 90 minutes. Letting it go takes a little longer.',
  note='Replace [REPLAY LINK] and [PASSCODE] before scheduling.',
  body=[
    COND('masterclass-attended',
      [P('Thank you for being with me last Thursday. In 90 minutes, a lot of you found the place where your money story quietly says "this far and no further." I watched it happen on screen after screen.')],
      [P("I missed you last Thursday! If you haven't watched it yet, the replay is the best way to see how I work: **[REPLAY LINK]** Passcode: **[PASSCODE]**")]),
    P("Here's what I've learned in 39 years of doing this work: finding a stop is the beginning. A stop has been there a long time, and it comes back when life gets busy, when a big invoice goes out, when the holidays hit. Letting it go, and setting a new set point that can actually hold more, takes practice and support."),
    P("That's what **Money Wealth and Miracles** is for. Six live sessions with me on Zoom, starting **Monday, December 14**, in a small group where I coach you directly, with a breakthrough assignment between every session."),
    COURSE_CARD(mc(1)),
  ],
  ps=[P("**P.S.** Have a question about whether it's right for you? Just reply. I answer every one myself.")]),

dict(id='mc-2', send='Saturday, November 28, 10:00 am PT', price='$797',
  subject_a='Which stop did you find?', subject_b='The stop that showed up for you',
  preview='A short exercise to do this weekend, with or without me.',
  body=[
    P('I hope you had a warm Thanksgiving.'),
    P('I want to give you something to try this weekend, whether or not you join the course.'),
    P("In class we talked about stops, the places where your money story quietly says \"this far and no further.\" Here's a five-minute way to find yours:"),
    OL('Finish this sentence three times, fast, without editing: **"Money is..."**',
       'Then this one: **"People who have a lot of money are..."**',
       'Then: **"If I had twice the income, I\'d be afraid that..."**'),
    P("Read what you wrote. One of those lines will have a charge to it. That's your stop."),
    P('Seeing it is the first step. Letting it go, and setting a new set point that can hold more, is what we do over six sessions in Money Wealth and Miracles, starting Monday, December 14.'),
    COURSE_CARD(mc(2), 'See the course'),
  ],
  ps=[P("**P.S.** Reply with your answer to number 3. I'd love to read it.")]),

dict(id='mc-3', send='Tuesday, December 1, 9:00 am PT', price='$797',
  subject_a='$25,000 and a $12M deal (and what actually changed)', subject_b='What happened after they found their stop',
  preview='Two students, in their own words.',
  note='Replace the yellow [LISA: ...] box with her own words before scheduling.',
  body=[
    P('I shared these stories in class. I want to tell you what was underneath them.'),
    P('**Megan**, Head of Design at a creative agency, generated over $25,000 on top of her normal income before the course had even ended. **K.Y.** closed a $12M deal after joining, and two more just under $1M.'),
    P('(Results vary, and none of this is a promise of income.)'),
    P('Neither of them learned a secret strategy. What changes in this course is what you can see. When you can finally see the stop that has been setting your ceiling, you act differently, and money follows the action.'),
    LISA('[LISA: one or two lines here on what you saw shift for Megan or K.Y., in your words.]'),
    P("That's the whole idea behind my book, and the course: **the problem is how you see the problem.**"),
    P('We start in two weeks, Monday, December 14 at 5:30 pm PT. Six live sessions, each one recorded.'),
    COURSE_CARD(mc(3), 'Join Money Wealth and Miracles'),
  ]),

dict(id='mc-4', send='Friday, December 4, 9:00 am PT (MIRACLE200 opens)', price='$597 with MIRACLE200',
  subject_a='Starting today: $200 off, for you', subject_b='A gift for the people who came to class',
  preview='$597 for Money Wealth and Miracles, through the day we begin.',
  body=[
    P('We begin in ten days, and I want the people who came to Opening the Flow of Money to be in that room.'),
    P('So starting today, you can join Money Wealth and Miracles for **$597 instead of $797, with the code MIRACLE200**, through the start of Module 1 on **Monday, December 14 at 5:30 pm PT**. It ends when we begin.'),
    CODE_CARD(mcc(4), eyebrow='A thank-you for coming to class'),
    P('Some of you are thinking, "I got so much from the masterclass, I can take it from here on my own." You might! But a stop is hard to see from the inside. It feels like the truth, not like a belief.'),
    P("That's why I teach this live, in a small group. When I coach someone in the room, I can hear the stop in their words before they can. And when you watch it happen for someone else, you suddenly recognize your own."),
  ],
  ps=[P('**P.S.** The $200 off is for paying in full, and the button above applies MIRACLE200 for you.')]),

dict(id='mc-5', send='Tuesday, December 8, 9:00 am PT', price='$597 with MIRACLE200',
  subject_a='Bring a pal (and both save $200)', subject_b='Six days, and a seat for your friend',
  preview="It's more fun with someone you love in the room.",
  body=[
    P('We begin in six days.'),
    P('One thing I love about this group is how often people come in pairs: a business partner, a sister, a best friend, a spouse. When you shift your money story alongside someone you see every day, it sticks.'),
    P('So if someone came to mind while you were in class, invite them. **MIRACLE200 works for them too:** $597 each, through Monday at 5:30 pm PT.'),
    CODE_CARD(mcc(5), eyebrow='For you and a friend', who='$597 each, paid in full, with MIRACLE200'),
    P('Forward this email, or send them this link: [lisakalmin.com/course](' + utm('mc-e5-friend', code=True) + ')'),
    SLOT(QA + ' Suggested: "Tomorrow: Ask Lisa, live. A free 45-minute Q&A, Wednesday, December 9, at 5:30 pm PT on Zoom. [ZOOM LINK]"'),
  ]),

dict(id='mc-6', send='Friday, December 11, 9:00 am PT', price='$597 with MIRACLE200',
  subject_a='Before the weekend gets busy', subject_b='A quiet decision',
  preview='Money Wealth and Miracles begins Monday. Your $597 ends when we start.',
  body=[
    P('The weekend before the holidays gets full fast, so I wanted to reach you while it\'s quiet.'),
    P("On Monday evening, a small group of us will meet for the first time and start rewriting the money stories we were handed. I'd love for you to be in that room."),
    H("Here's everything in one place"),
    UL('**Six live sessions on Zoom:** Dec 14, Jan 5, Jan 18, Jan 28, Feb 4, Feb 11, 5:30 to 7:00 pm PT, all recorded',
       '**Live coaching and Q&A** with me in every session',
       '**Weekly breakthrough assignments**',
       '**A private WhatsApp group** of Co-Miracle Makers'),
    CODE_CARD(mcc(6)),
  ]),

dict(id='mc-7', send='Monday, December 14, 8:00 am PT', price='$597 with MIRACLE200',
  subject_a='Tonight, 5:30 pm PT', subject_b='We begin tonight (your $597 ends at 5:30)',
  preview='The last few hours to join for $597.',
  note='At 2:00 pm PT the same day, send last-call.html from Series 2.',
  body=[
    P('Tonight is the night. Money Wealth and Miracles begins at **5:30 pm PT**, and your $597 price with MIRACLE200 ends when we start.'),
    P('Remember the stop you found in class? This is the moment to decide whether it gets to make this decision for you.'),
    CODE_CARD(mcc(7), label='Join before 5:30 pm PT', eyebrow='Last day'),
    P("I'll see you tonight."),
  ]),
]
for e in series1: e.update(series=S1, audience=A1, sign=FLOW)
# Dec 3 class registrants finish Series 4 on Dec 5, then get the same last three emails
for e in series1:
    if e['id'] in ('mc-5', 'mc-6', 'mc-7'): e['audience'] = 'tag masterclass-nov19 or masterclass-dec3, not mwm-buyer'

# ---------------------------------------------------------------- Series 2: full email list
S2 = 'Series 2 · Full email list'
A2 = 'full Kit list, excluding masterclass-nov19, masterclass-dec3, mwm-buyer and new quiz leads'
A2b = A2 + ', and from Dec 7 also excluding mwm-clicked'
ABUND = 'To your abundance!'
mn = lambda n: utm(f'main-e{n}')
ck = lambda n: utm(f'clk-e{n}', code=True)
CLICK = 'In Kit, every course link in this email should add the tag mwm-clicked (link action, or a Rule: clicks a link > add tag).'

series2 = [
dict(id='main-1', send='Tuesday, December 1, 9:00 am PT', audience=A2, note=CLICK,
  subject_a="The money story you didn't choose", subject_b='Where did you learn what money means?',
  preview="It was handed to you before you could say no. You can rewrite it.",
  body=[
    P('Quick question. When you were growing up, what did money sound like in your house?'),
    P('For some of us it was silence. For some it was arguing at the kitchen table. For some it was "we can\'t afford that," said so often it became a fact about who we were.'),
    P("Here is what I have seen in 39 years of coaching: that early money story doesn't stay in childhood. It becomes a set point. You can work harder, earn more, learn every strategy, and still find money drifting back to the same level, because the story underneath hasn't changed."),
    P("That's not a character flaw. It's a way of seeing. And **the problem is how you see the problem:** when the way you see money shifts, what you do with it shifts too."),
    P('That is exactly what we do together in **Money Wealth and Miracles**, my live six-session course that begins **Monday, December 14**. Over six evenings on Zoom, in a small group, you will:'),
    OL('Find the beliefs that have been quietly running your money, and where they came from.',
       'See money as an exchange of energy and value, not just numbers to chase.',
       "Set a new set point that can hold more wealth, so it doesn't leak back out."),
    P('I keep the group small, 15 to 30 people, so I can coach you directly.'),
    COURSE_CARD(mn(1)),
  ],
  ps=[P('**P.S.** Not ready for six weeks? Start with one evening. This Thursday, **December 3, at 5:30 pm PT**, I\'m teaching a free 90-minute masterclass, Opening the Flow of Money. [Save your free seat](' + SITE + '/masterclass/?utm_source=kit&utm_medium=email&utm_campaign=mwm-dec3&utm_content=main-e1-ps' + ')'),
      P('And hit reply to tell me one sentence your family used to say about money. I read every reply.')]),

dict(id='main-2', send='Saturday, December 5, 10:00 am PT (moved from Dec 3, the class day)', audience=A2, note=CLICK,
  subject_a='"Why didn\'t anyone tell me this before?"', subject_b='What happened for Megan (and $25,000)',
  preview='What people say after the course, in their own words.',
  body=[
    P('I want to share something one of my students wrote, because she says it better than I can.'),
    P('Megan is Head of Design at a creative agency. She joined Money Wealth and Miracles wanting a better relationship with money. Here is what she told me:'),
    QUOTE("She drops personal coaching knowledge as well as practical knowledge that I felt like I missed in high school and college. Since starting the program I have generated over $25,000.00 on top of my normal income, and the program isn't even over!", '**Megan**, Head of Design'),
    P('Another student, K.Y., closed a $12M deal after joining, and two more just under $1M.'),
    P("(Results vary, and none of this is a promise of income. What I can promise is that you will see your money story clearly, and you'll have the tools and the support to change it.)"),
    P('What made the difference for them wasn\'t a new budgeting trick. It was seeing, maybe for the first time, the place where they had been quietly saying "this far and no further." Once you can see that stop, you can let it go.'),
    QUOTE("Having direct access to Lisa is immeasurable. I noticed myself a few times asking, why didn't anyone tell me this before?", 'A Money Wealth and Miracles student'),
    P('We begin Monday, December 14, at 5:30 pm PT. Six live sessions, 90 minutes each, every one recorded.'),
    COURSE_CARD(mn(2), 'Join Money Wealth and Miracles'),
  ]),

dict(id='main-3', send='Sunday, December 6, 4:00 pm PT', audience=A2, note=CLICK,
  subject_a='Your six evenings with me (the dates)', subject_b='What actually happens inside Money Wealth and Miracles',
  preview='Six live sessions, Dec 14 to Feb 11. Here is what each one feels like.',
  body=[
    P("A few people have asked what Money Wealth and Miracles is actually like, so here's the inside view."),
    H('Six live sessions on Zoom, 5:30 to 7:00 pm PT'),
    UL('**Module 1:** Monday, December 14', '**Module 2:** Tuesday, January 5', '**Module 3:** Monday, January 18',
       '**Module 4:** Thursday, January 28', '**Module 5:** Thursday, February 4', '**Module 6:** Thursday, February 11'),
    P("Every session is recorded, so if life happens you won't miss a thing."),
    P("**What a session feels like:** I teach a shift, we do the exercise together, and then I coach people live on what came up. You'll often learn as much from watching someone else's breakthrough as from your own."),
    P('**Between sessions:** a breakthrough assignment that puts the shift to work in your real life, and a private WhatsApp group where your Co-Miracle Makers share wins and questions.'),
    P('**Notice the timing.** We start in December and finish in February. That means you walk into the new year with a new money set point, instead of making another resolution on top of the old one.'),
    COURSE_CARD(mn(3), 'Reserve my spot'),
  ],
  ps=[P('**P.S.** Not sure where you stand? Take my free 5-minute scorecard and find your Money Mindset Pattern first: [lisakalmin.com/quiz](' + SITE + '/quiz/?utm_source=kit&utm_medium=email&utm_campaign=mwm-dec&utm_content=main-e3)')]),

dict(id='main-4', send='Wednesday, December 9, 9:00 am PT', audience=A2b, note=CLICK,
  subject_a='"I\'ll do it when I have more money"', subject_b='The most common money stop I hear',
  preview="It sounds like common sense. It's actually the stop.",
  body=[
    P('The most common thing I hear before someone joins a course like this is: "I\'ll do it when I have more money."'),
    P("It sounds like common sense. And I want to be gentle here, because sometimes it's true, and you should always take care of your basic needs first."),
    P('But often it is the stop itself, speaking. It\'s the same voice that says "when I\'m more established, I\'ll raise my rates," and "when things calm down, I\'ll look at my finances." The "when" keeps moving, and the set point stays where it is.'),
    P("Here's another way to see it. The people who generate the most change in my courses aren't the ones who had the most money when they started. They're the ones who decided that their relationship with money was worth investing in, now."),
    P('Money Wealth and Miracles begins **Monday, December 14 at 5:30 pm PT**. Enrollment closes when Module 1 starts.'),
    P('If this is your year to stop waiting for "when," I would love to have you in the room.'),
    COURSE_CARD(mn(4), 'Join us'),
    SLOT(QA + ' Suggested: "Tonight: Ask Lisa, live. A free 45-minute Q&A tonight, Wednesday, December 9, at 5:30 pm PT on Zoom. Bring your biggest money question. [ZOOM LINK]"'),
  ],
  ps=[P("**P.S.** Have a question about whether it's right for you? Just reply. I answer every one myself.")]),

dict(id='main-5', send='Monday, December 14, 8:00 am PT', audience=A2b, note=CLICK,
  subject_a='Doors close tonight at 5:30', subject_b='We begin tonight',
  preview="Money Wealth and Miracles starts in a few hours. Here's your seat.",
  body=[
    P('Tonight at 5:30 pm PT, Money Wealth and Miracles begins, and enrollment closes when we start.'),
    P('If you\'ve been reading these emails and feeling a small "yes" in your chest, I\'d trust that.'),
    H("Here's what you're saying yes to"),
    UL('Six live sessions with me, December 14 to February 11, all recorded', 'Live coaching and Q&A in every session',
       'Weekly breakthrough assignments', 'A small group of Co-Miracle Makers and a private WhatsApp community'),
    COURSE_CARD(mn(5), 'Reserve my spot before 5:30 pm PT'),
    P("I can't wait to begin."),
  ]),

# clicker emails: the final-week price for people who clicked and didn't buy. Kept as notes, not promotions.
dict(id='clicker-1', send='Tuesday, December 8, 10:00 am PT', audience='tag mwm-clicked, not mwm-buyer (broadcast to the tag at send time)',
  subject_a='I noticed you looked', subject_b='A note just for you, {{ subscriber.first_name | default: "friend" }}',
  preview="You took a look at Money Wealth and Miracles. Here's something to help.",
  body=[
    P('I noticed you took a look at Money Wealth and Miracles, and I wanted to write to you directly.'),
    P("When someone looks and doesn't join, it's usually one of three things: the timing, the money, or a quiet question about whether this will really work for them."),
    P("I can't fix the timing (we start next Monday, December 14). But I can help with the other two."),
    P("**The money:** for the people who looked, I'm opening a special price. **$597 instead of $797, with the code MIRACLE200**, through the start of Module 1 on Monday at 5:30 pm PT. The button below has it ready for you."),
    P("**Whether it will work for you:** hit reply and tell me what you're hoping to change about money. I'll tell you honestly whether I think this course is the right next step."),
    BTN('Join for $597', ck(1)),
  ],
  ps=[P('**P.S.** The $200 off is for paying in full, and it ends when we begin, Monday, December 14 at 5:30 pm PT.')]),

dict(id='clicker-2', send='Friday, December 11, 9:00 am PT', audience='tag mwm-clicked, not mwm-buyer',
  subject_a='Your questions, answered', subject_b='"Is this right for me?"',
  preview="The four questions I'm asked most, plus your $597 price.",
  body=[
    P("Here are the questions I've been answering this week, in case one of them is yours."),
    H('"What if I miss a session?"'),
    P("Every session is recorded, and you get the replay. Come live when you can, because that's where the coaching happens."),
    H('"Is this about budgeting or investing?"'),
    P("No. This isn't stock tips or a spreadsheet. It's the layer underneath: what you believe about money, where that came from, and how it shapes what you charge, earn, keep and receive."),
    H('"I\'ve done money work before. Is this different?"'),
    P("Most people in the room have. What's different is live coaching in a small group. I see your stop in real time, and we work it right there."),
    H('"Can I afford it right now?"'),
    P('Only you know that, and please take care of your basics. If it\'s a stretch that feels exciting rather than frightening, that is often the exact edge where the set point moves.'),
    P('Your price is still **$597 with MIRACLE200**, through Monday, December 14 at 5:30 pm PT.'),
    BTN('Join for $597', ck(2)),
  ]),

dict(id='clicker-3', send='Monday, December 14, 8:00 am PT', audience='tag mwm-clicked, not mwm-buyer',
  subject_a='Tonight we begin (your $597 ends at 5:30)', subject_b='Last few hours',
  preview='Module 1 is tonight at 5:30 pm PT.',
  body=[
    P('Tonight at 5:30 pm PT we begin Money Wealth and Miracles, and your $597 price with MIRACLE200 ends when we start.'),
    P("If something in you has kept clicking on this all week, I'd listen to it."),
    BTN('Join for $597 before 5:30 pm PT', ck(3)),
    P("I'd love to see you tonight."),
  ]),

dict(id='last-call', send='Monday, December 14, 2:00 pm PT',
  audience='tags mwm-clicked, masterclass-nov19 and quiz-lead, not mwm-buyer (all were offered MIRACLE200)',
  subject_a='3 hours', subject_b='We begin at 5:30', preview='We begin at 5:30 pm PT.',
  body=[
    P('Three hours from now, our group meets for the first time.'),
    P('There\'s still a seat for you, at **$597 with MIRACLE200**.'),
    BTN('Take my seat', utm('last-call', code=True)),
    P('See you at 5:30.'),
  ]),
]
for e in series2: e.update(series=S2, sign=ABUND)

# ---------------------------------------------------------------- Series 3: sourced (cold)
# Plain personal notes. No logo, images, tracking pixel or brand styling: those mark a cold email
# as marketing and push it to Promotions or spam. One link at most. Sent from a separate domain.
qz = SITE + '/quiz/?utm_source=cold&utm_campaign=mwm-dec&utm_content={{segment}}'
SIG = ('Lisa Kalmin\nTransformational mindset coach · Author, "The Problem Is How You See the Problem"\nCosta Mesa, CA\n\n'
       '[postal address] · Not for you? Reply "no thanks" and I won\'t write again.')
series3 = [
dict(id='cold-1', send='Day 1 (from Monday, November 30)', subject_a='quick question, {{first_name}}', subject_b='{{segment_word}} and money',
  body=['{{hook}}',
        "I've coached people on their relationship with money for 39 years, and the pattern is almost never a lack of skill. It's a set point, an old money story that quietly decides how much is \"enough.\"",
        'Curious: does that land for you, or is it off base?']),
dict(id='cold-2', send='Day 3, same thread', subject_a='re: quick question, {{first_name}}', subject_b=None,
  body=['Following up with something useful either way.',
        "I built a 5-minute scorecard that shows which money pattern you're running: Manifester, Manager, Unaware or Resigned. It's free, and you get your result right away.",
        ('link', qz),
        'Most {{segment_word}} who take it tell me the result is uncomfortably accurate.']),
dict(id='cold-3', send='Day 6', subject_a='the "this far and no further" thing', subject_b=None,
  body=['One idea from my work that might be worth 30 seconds.',
        'Most people have a "stop" with money, a point where their story quietly says "this far and no further." You see it when a great month is followed by a slow one, or when you raise your rates and then discount them back down.',
        "The stop isn't a strategy problem, which is why new strategies don't fix it. It's a way of seeing. When the way you see money shifts, what you do with it shifts too.",
        'If you want to find yours, the scorecard takes 5 minutes:', ('link', qz)]),
dict(id='cold-4', send='Day 10, on or after Friday, December 4 (uses MIRACLE200)', subject_a='last note from me', subject_b=None,
  body=["I'll leave it here, I don't want to crowd your inbox.",
        "If any of this has been relevant: I'm running a small live group course called Money Wealth and Miracles, six evenings on Zoom with me, starting Monday, December 14. It's for {{segment_word}} who know they're worth more than they're earning and want to change the story underneath.",
        "There's $200 off with the code MIRACLE200 until we start:",
        ('link', COURSE + '?code=MIRACLE200&utm_source=cold&utm_campaign=mwm-dec&utm_content={{segment}}'),
        'Either way, thank you for reading, and I wish you a very abundant new year.']),
]

def cold_text(e):
    lines = [f"Subject: {plain(e['subject_a'])}"]
    if e['subject_b']: lines.append(f"Subject B: {plain(e['subject_b'])}")
    lines += [f"Send: {e['send']}", 'Tool: cold-email tool on the separate domain, never Kit', '-' * 60, '', 'Hi {{first_name}},', '']
    for b in e['body']:
        lines += [b[1] if isinstance(b, tuple) else plain(b), '']
    lines += ['Lisa', '', '--', SIG]
    return '\n'.join(lines) + '\n'

def cold_html(e):
    st = 'margin:0 0 16px;'
    rows = []
    for b in e['body']:
        if isinstance(b, tuple): rows.append(f'<p style="{st}"><a href="{b[1]}">{html.escape(b[1].split("?")[0].replace("https://", ""))}</a></p>')
        else: rows.append(f'<p style="{st}">{html.escape(plain(b)).replace("&quot;", chr(34))}</p>')
    sig = html.escape(SIG).replace('&quot;', '"').replace('\n', '<br>')
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light dark"><title>{html.escape(plain(e['subject_a']))}</title>
<!-- Series 3 · Sourced list · {e['id']} · {e['send']}
     A plain personal note on purpose: no logo, images or brand styling, so it reads (and is filtered)
     like a one-to-one email. The colors are left to the mail app, so dark mode is handled by the app.
     Paste into the cold-email tool's HTML editor, or use the .txt version. -->
</head>
<body style="margin:0;padding:16px;font-family:-apple-system,Helvetica,Arial,sans-serif;font-size:15px;line-height:22px;">
<div style="max-width:560px;">
<p style="{st}">Hi {{{{first_name}}}},</p>
{''.join(rows)}
<p style="{st}">Lisa</p>
<p style="margin:24px 0 0;font-size:13px;line-height:19px;opacity:.75;">--<br>{sig}</p>
</div>
</body></html>
"""

# ---------------------------------------------------------------- Series 4: the free class on Dec 3
S4 = 'Series 4 · Free masterclass, Thursday Dec 3'
A4i = 'full Kit list, excluding masterclass-dec3 (already registered), mwm-buyer and new quiz leads'
A4r = 'tag masterclass-dec3, not mwm-buyer'
mcl = lambda c: f'{SITE}/masterclass/?utm_source=kit&utm_medium=email&utm_campaign=mwm-dec3&utm_content={c}'
r4 = lambda n: utm(f'dec3-r{n}')
r4c = lambda n: utm(f'dec3-r{n}', code=True)
GCAL = ('https://calendar.google.com/calendar/render?action=TEMPLATE&text=Opening+the+Flow+of+Money+with+Lisa+Kalmin'
        '&dates=20261204T013000Z/20261204T030000Z&details=Your+Zoom+link+is+in+your+confirmation+email.+Bring+a+journal+and+a+pen.')
ICS = SITE + '/masterclass/masterclass.ics'
INV = 'Invite. Kit broadcast. Exclude anyone tagged masterclass-dec3 at send time, so people who registered stop getting invites.'
REG = 'Registrants. Kit broadcast to the tag (or the Dec 3 sequence). Replace [ZOOM LINK] / [REPLAY LINK] before scheduling.'

series4 = [
# ---- invites to the main list
dict(id='inv-1', send='Friday, November 27, 10:00 am PT', audience=A4i, note=INV,
  subject_a="You're invited: a free evening with me", subject_b='Where does your money stop?',
  preview='Thursday, December 3, 5:30 pm PT. 90 minutes, live, free.',
  body=[
    P("I'm opening my virtual classroom for one evening, and I'd love for you to come."),
    P('On **Thursday, December 3, at 5:30 pm PT**, I\'m teaching a free live masterclass on Zoom: **Opening the Flow of Money: Letting Go of Your Stops.**'),
    P('Here\'s the idea. Most of us have a place in our money story that quietly says "this far and no further." It might sound like "there\'s never quite enough," or a pause before you name your price, or money that comes in and goes right back out. That place is a stop, and once you can see it, you can let it go.'),
    P('In 90 minutes together, you will:'),
    UL('Find your hidden money stops, and where they started',
       'See money as energy you can attract, not just numbers you chase',
       "Set a new income set point that doesn't depend on the news",
       'Leave with 4 actions you can take the same day'),
    CLASS_CARD(mcl('inv-1')),
  ],
  ps=[P("**P.S.** Been to one of my classes before? Come again. Every class uncovers a new layer, and the stop you meet this time may not be the one you met last time.")]),

dict(id='inv-2', send='Monday, November 30, 9:00 am PT', audience=A4i, note=INV,
  subject_a='"There\'s never quite enough"', subject_b='The pause before you name your price',
  preview='Four money stops. Which one sounds like you?',
  body=[
    P('Which of these sounds most like you?'),
    OL("There's never quite enough, no matter how much comes in.",
       'You undercharge, or give it away.',
       'Money feels stressful, so you avoid looking.',
       'Money comes in, then goes right back out.'),
    P("None of these means something is wrong with you. Each one is a stop: a belief you picked up long ago that sets a ceiling on how much money feels safe to have."),
    P('Here is what I have seen in 39 years of coaching more than 50,000 people: you can work harder, earn more, learn every strategy, and money still drifts back to the same level until the stop underneath it is seen.'),
    P("This Thursday, I'll help you find yours, live, in a free 90-minute masterclass. Bring a journal. You'll want to write down what comes up."),
    CLASS_CARD(mcl('inv-2')),
  ],
  ps=[P('**P.S.** Reply with the number that sounds most like you. I read every reply, and it helps me shape the class.')]),

dict(id='inv-3', send='Wednesday, December 2, 9:00 am PT', audience=A4i, note=INV,
  subject_a='Tomorrow night, 5:30 pm PT', subject_b='Save your seat for tomorrow',
  preview='A free live masterclass with me. 90 minutes on Zoom.',
  body=[
    P('Tomorrow evening I\'m teaching **Opening the Flow of Money**, free and live on Zoom, and there\'s still room for you.'),
    QUOTE('Lisa is one of the most effective people I know at coaching.', '**Nicole Kalil**, Founder and CEO, WomanWhisperer'),
    P("Come as you are. You don't need to prepare anything except a journal and 90 minutes for yourself. I'll take you through the exercises live, and you can ask me your questions directly."),
    CLASS_CARD(mcl('inv-3')),
  ]),

dict(id='inv-4', send='Thursday, December 3, 2:00 pm PT', audience=A4i, note=INV,
  subject_a='Today at 5:30 pm PT', subject_b='We start in a few hours',
  preview='The free masterclass is tonight. Your seat is still open.',
  body=[
    P('Quick note: **Opening the Flow of Money** is tonight at **5:30 pm PT**, live on Zoom.'),
    P("If money has felt tighter than it should this year, give yourself these 90 minutes. Register now and your Zoom link arrives by email right away."),
    CLASS_CARD(mcl('inv-4'), 'Save my seat for tonight'),
    P('See you there.'),
  ]),

# ---- after sign-up: every email points toward Money Wealth and Miracles
dict(id='reg-0', send='Right away, when someone registers (the first email of the Dec 3 sequence, or the form\'s confirmation)', audience=A4r, note=REG,
  subject_a="You're in! Your Zoom link for Thursday", subject_b='Your seat is saved (Dec 3, 5:30 pm PT)',
  preview='Save this email. Your link and calendar buttons are inside.',
  body=[
    P("You're in! I'm so glad you're coming."),
    H('Opening the Flow of Money'),
    P('**Thursday, December 3**, 5:30 to 7:00 pm PT, live on Zoom.'),
    BTN('Join on Zoom', '[ZOOM LINK]'),
    P('Star this email so the link is easy to find, and add the class to your calendar: [Google Calendar](' + GCAL + ') or [Apple / Outlook](' + ICS + ').'),
    P('Bring a journal and a pen. You\'ll want to write down what comes up.'),
    H('Where this can lead'),
    P('The masterclass opens the door. **Money Wealth and Miracles** is where you walk through it: six live sessions with me, starting **Monday, December 14**, where you rewrite the money story you grew up with in a small group.'),
    P("**Stay to the end on Thursday:** I'll share a $200 attendee price for the course, just for the people in class."),
    COURSE_CARD(r4(0), "See what's inside the course"),
  ],
  ps=[P("**P.S.** Hit reply and tell me which money stop sounds most like you. I'll shape the class around the people in the room.")]),

dict(id='reg-1', send='Wednesday, December 2, 9:00 am PT', audience=A4r, note=REG,
  subject_a='Tomorrow: what to bring', subject_b='See you tomorrow at 5:30 pm PT',
  preview='A journal, a pen, and one question.',
  body=[
    P("We meet tomorrow, **Thursday at 5:30 pm PT**, and I'm already looking forward to it."),
    P('To get the most from our 90 minutes:'),
    OL('**Bring a journal and a pen.** The exercises work best on paper.',
       '**Find a quiet spot** where you can talk out loud if I call on you.',
       '**Bring one money question** you\'ve never quite been able to answer.'),
    BTN('Your Zoom link', '[ZOOM LINK]'),
    P('One more thing. Here is what Megan, a Head of Design, wrote after she went from this class into Money Wealth and Miracles:'),
    QUOTE("She drops personal coaching knowledge as well as practical knowledge that I felt like I missed in high school and college.", '**Megan**, Head of Design'),
    P("I'll tell you more about the course at the end of class, along with a thank-you price for the people who are there."),
  ]),

dict(id='reg-2', send='Thursday, December 3, 4:30 pm PT', audience=A4r, note=REG,
  subject_a='We start in one hour', subject_b='Your Zoom link (5:30 pm PT)',
  preview='Here is your link. Doors open at 5:25.',
  body=[
    P('We start in one hour. Grab your journal, and come a few minutes early so you\'re settled.'),
    BTN('Join on Zoom at 5:30 pm PT', '[ZOOM LINK]'),
    P("Stay until the end: that's when I share the attendee price for Money Wealth and Miracles. See you soon!"),
  ]),

dict(id='reg-3', send='Thursday, December 3, 7:15 pm PT (right after class)', audience=A4r,
  note=REG + ' Tag live attendees masterclass-dec3-attended from the Zoom attendance report before sending. MIRACLE200 must already work in Kit (set its start to Dec 3, 5:30 pm PT).',
  subject_a='Your attendee price (and the replay)', subject_b='$200 off, as promised',
  preview='$597 for Money Wealth and Miracles, through the day we begin.',
  body=[
    COND('masterclass-dec3-attended',
      [P('Thank you for tonight. I watched so many of you find your stop on screen, and I hope you felt how much lighter money gets the moment you can see it.'),
       P('As promised, here is your attendee price for **Money Wealth and Miracles**:')],
      [P("I missed you tonight! The replay is here for a few days: **[REPLAY LINK]**"),
       P('Watch it this week, and the attendee price for **Money Wealth and Miracles** is yours too:')]),
    CODE_CARD(r4c(3), eyebrow='Your attendee price'),
    P('Finding a stop is the beginning. Letting it go, and holding a new set point when life gets busy, takes practice and support. That is what the six sessions are for: live coaching with me, a breakthrough assignment between every session, and a small group cheering you on.'),
    P('We begin **Monday, December 14 at 5:30 pm PT**. The $597 price ends when we start.'),
  ],
  ps=[P('**P.S.** Not sure it\'s right for you? Just reply. I answer every message myself.')]),

dict(id='reg-4', send='Saturday, December 5, 10:00 am PT', audience=A4r, note=REG,
  subject_a='What happens after you find the stop', subject_b='The part we didn\'t have time for',
  preview='A stop comes back when life gets busy. Here is how to keep it gone.',
  body=[
    P("It's been two days since class. Can I ask you something? Has the stop come back yet?"),
    P('For most people it does, often the first time a big bill arrives or an invoice goes out. That\'s not failure. A stop has been there a long time, and one evening can show it to you, but it takes repetition to set a new set point that holds.'),
    P("That's why I teach Money Wealth and Miracles live, over six sessions. When I coach someone in the room, I can hear the stop in their words before they can. And when you watch it happen for someone else, you suddenly recognize your own."),
    QUOTE("Having direct access to Lisa is immeasurable. I noticed myself a few times asking, why didn't anyone tell me this before?", 'A Money Wealth and Miracles student'),
    CODE_CARD(r4c(4), eyebrow='Your attendee price'),
  ],
  ps=[P("**P.S.** Missed class? The replay is still up for one more day: **[REPLAY LINK]**")]),
]
for e in series4: e.update(series=S4, sign=FLOW)

# ---------------------------------------------------------------- write
def write(path, s):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f: f.write(s)

folders = {'1-masterclass': series1, '2-main-list': series2, '4-free-class-dec3': series4}
for folder, emails in folders.items():
    for e in emails:
        write(f'{OUT}/{folder}/{e["id"]}.html', page(e))
        write(f'{OUT}/{folder}/{e["id"]}.txt', text(e))
for e in series3:
    write(f'{OUT}/3-sourced/{e["id"]}.html', cold_html(e))
    write(f'{OUT}/3-sourced/{e["id"]}.txt', cold_text(e))

# preview page: every email side by side in light and dark
cards = []
for folder, title, emails in [('1-masterclass', 'Series 1 · Masterclass sign-ups', series1),
                              ('2-main-list', 'Series 2 · Full email list', series2),
                              ('3-sourced', 'Series 3 · Sourced list (plain text)', series3),
                              ('4-free-class-dec3', 'Series 4 · Free masterclass, Thursday Dec 3', series4)]:
    cards.append(f'<h2>{title}</h2>')
    for e in emails:
        cards.append(f'<p class="meta"><b>{e["id"]}</b> · {html.escape(e["send"])} · {html.escape(plain(e["subject_a"]))}</p>'
                     f'<div class="pair"><iframe src="{folder}/{e["id"]}.html"></iframe>'
                     f'<iframe class="dark" src="{folder}/{e["id"]}.html"></iframe></div>')
write(f'{OUT}/index.html', f"""<!doctype html><html><head><meta charset="utf-8"><title>MWM December emails</title>
<style>body{{font-family:Helvetica,Arial,sans-serif;margin:24px;background:#eee}}.pair{{display:flex;gap:16px;margin-bottom:28px}}
iframe{{width:620px;height:900px;border:1px solid #ccc;background:#fff}}iframe.dark{{color-scheme:dark}}.meta{{margin:6px 0}}</style></head>
<body><h1>Money Wealth and Miracles · December emails</h1><p>Left: light mode. Right: dark mode (browsers that pass dark mode into frames).</p>{''.join(cards)}</body></html>
""")
print('built', sum(len(x) for x in folders.values()) + len(series3), 'emails')
