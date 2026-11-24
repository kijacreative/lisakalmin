# Meta ads: quiz leads, then retarget with the offer

**Two campaigns:**

1. **Quiz leads** (cold): ads send people to the Underearning Financial Scorecard at `/quiz/`. The email gate captures them into Kit (form 10176902), and `email-quiz-nurture.md` sells the course.
2. **Retargeting** (warm): people who took the quiz, visited the course page, engaged with Lisa, or are on her lists see the course. **Nov 28 to Dec 3 at full price** (ads R2 and R3, no code). **From Fri Dec 4, the $597 offer with MIRACLE200** (ads R1, R3 with its last card swapped, and R4 from Dec 11).

**Dates:** Wed Nov 25 to Mon Dec 14, 5:30 pm PT.
**Suggested budget:** about **$1,600 total**.

| Campaign | Nov 25 to Dec 7 | Dec 8 to Dec 11 | Dec 12 to Dec 14 | Total |
|---|---|---|---|---|
| Quiz leads | $60 a day | $60 a day | off | about $1,020 |
| Offer retargeting (from Nov 28) | $20 a day | $40 a day | $60 a day | about $550 |

Realistic expectation: $4 to $8 a lead in this space, so roughly 130 to 250 quiz leads. Cold leads seldom buy a $597 course within 3 weeks, so plan for 1 to 2 seats from ads, and a much bigger waitlist for the next cohort. Retargeting the lists Lisa already has (masterclass, main list, engagers) is where the near-term seats come from.

---

## 1. Tracking setup (do this first)

The site has Google Tag Manager (GTM-PCBSRF9P) but no Meta pixel yet. The quiz already sends the conversion event to GTM.

1. **Meta pixel through GTM** on every page, plus the **Conversions API** (GTM server-side, or Meta's CAPI Gateway) so iOS and ad-blocked visitors still count.
2. **`Lead` event:** when Kit accepts a quiz signup, the quiz page pushes `{ event: 'quiz_lead', money_mindset_pattern, money_mindset_score }` to the dataLayer (done). In GTM, add a Custom Event trigger for `quiz_lead` and a Meta `Lead` tag on it, passing the pattern as `content_name` from a Data Layer Variable.
3. **`ViewContent`** on `/course/`, and **`InitiateCheckout`** on clicks of the checkout buttons.
4. **`Purchase`:** add the pixel ID in Kit's product settings if available, otherwise create the conversion from the Kit purchase redirect page.
5. **Consent:** the site denies ad cookies for everyone until they click Accept. For US traffic this hides most conversions, which makes Meta's optimization guess blindly and raises the cost per lead. Grant by default for US visitors and keep the opt-in for the EU, UK and Canada.
6. **Test** with Meta's Test Events tool: take the quiz end to end and see `Lead` arrive.

---

## 2. Campaign 1: Quiz leads

- **Objective:** Leads. Conversion location: Website. Optimize for the `Lead` event.
- **Fallback:** if the pixel isn't firing reliably by Nov 25, optimize for Landing Page Views for the first 3 days and switch once `Lead` events flow.
- **Budget:** Advantage campaign budget, $60 a day.
- **Placements:** Advantage+ placements. Check that Reels and Stories crops look right.
- **Location:** United States. (If Lisa wants a local edge, add a separate small ad set for Southern California.)
- **Age:** 35 to 65+. **Gender:** all, but expect delivery to lean women, which matches the course.

**Ad sets** (test for 3 to 4 days, then move budget to the winner):

| Ad set | Audience | Daily |
|---|---|---|
| A. Interests | Interests such as: law of attraction, abundance, personal development, life coaching, Mel Robbins, Gabrielle Bernstein, Hay House, Oprah, The Secret, entrepreneurship, women in business, small business owners | $25 |
| B. Lookalike | 1 to 3% lookalike of Lisa's Kit list, masterclass registrants and course buyers (upload the email lists) | $20 |
| C. Advantage+ audience | Broad, with Lisa's lists as audience suggestions | $15 |

**Exclude** from all ad sets: course buyers, people who already took the quiz (pixel `Lead`, 180 days), and the uploaded masterclass list (they get retargeting instead).

**Kill and scale rules**

- After an ad spends $40 with no lead, pause it.
- Cost per lead over $10 after 3 days, pause the ad set.
- Under $5 a lead, raise that ad set's budget by 20% every 2 days.
- Refresh creative if frequency passes 3.

---

## 3. Campaign 2: Offer retargeting

- **Objective:** Sales, optimize for `Purchase` (or `InitiateCheckout` if there are too few purchases to learn from, which is likely).
- **Starts:** Sat Nov 28. Budget ramps up in the final week (table above).
- **Link until Dec 3:** `https://www.lisakalmin.com/course/?utm_source=meta&utm_medium=paid&utm_campaign=mwm-dec-retarget`
- **Link from Dec 4:** `https://www.lisakalmin.com/course/?code=MIRACLE200&utm_source=meta&utm_medium=paid&utm_campaign=mwm-dec-retarget`
- **On Dec 4:** pause the full-price ads and turn on the MIRACLE200 ads in the same ad set, so learning carries over.

**Audience (one ad set, combined):**

- Took the quiz (pixel `Lead`, 30 days)
- Visited `/course/` (30 days) or `/masterclass/` (60 days)
- Engaged with Lisa's Instagram or Facebook page (60 days)
- Watched 50% or more of any Lisa video ad (30 days)
- Uploaded lists: main Kit list and masterclass registrants

**Exclude:** course buyers.

Note: from Dec 4 the ads show MIRACLE200 publicly, so the rest of the main list may see $597 even though their emails say $797. That's acceptable for the final ten days; if Lisa prefers, exclude the uploaded main list from retargeting from Dec 4 and keep only quiz takers, site visitors, engagers and masterclass registrants.

---

## 4. Ad policy notes

- **Don't call out a person's finances.** Meta's personal attributes policy rejects ads that imply the viewer is broke, in debt or under-earning ("Are you under-earning?", "Struggling with money?"). Talk about people in general ("Many high achievers under-earn without realizing it") or about the quiz itself.
- **No income promises.** Leave Megan's $25,000 and K.Y.'s $12M out of cold lead ads. In retargeting, a testimonial can mention them only with "Results vary. Not a promise of income." on the creative or in the text.
- **Special ad category:** a coaching course isn't a credit, housing or employment ad. If Meta flags it as Financial products and services, appeal, or accept the category (it only narrows targeting options).

---

## 5. Quiz lead ads: copy

Each ad uses CTA **Learn more** (or **Take quiz** where offered), headline under 40 characters, and link `https://www.lisakalmin.com/quiz/?utm_source=meta&utm_medium=paid&utm_campaign=mwm-dec-quiz&utm_content=<ad>`

### Ad L1 · "The scorecard" (static or carousel)

**Primary text:**
Many high achievers under-earn without realizing it. They overwork, undercharge, and feel like money should be easier by now.

The Underearning Financial Scorecard shows which of four money patterns you're running: Manifester, Manager, Clueless or Victim. 30 quick statements, about 5 minutes, and your result appears right away.

Free, from transformational coach Lisa Kalmin (39 years, 50,000+ people trained).

**Headline:** What's your money pattern?
**Description:** Free 5-minute scorecard
**Visual:** the four pattern names on cream cards against Lisa's forest green, with "Which one are you?" Carousel version: one card per pattern with its one-line description.

### Ad L2 · "The family sentence" (Lisa video, script V1)

**Primary text:**
What did money sound like in your house growing up?

Silence? Arguing? "We can't afford that"?

That early story becomes a set point. Find out which pattern it left you with. Free 5-minute scorecard from Lisa Kalmin.

**Headline:** Find your money pattern in 5 min
**Description:** Free, instant result

### Ad L3 · "This far and no further"

**Primary text:**
Ever have a great month followed by a slow one, again and again?

That's often a money set point at work, an old story that quietly says "this far and no further." Strategy alone doesn't move it. Seeing it does.

Take Lisa Kalmin's free Underearning Financial Scorecard and see your pattern in 5 minutes.

**Headline:** See your money set point
**Description:** Free scorecard · 5 minutes
**Visual:** a simple line chart that rises and falls back to the same level, with "Your money set point" across it.

### Ad L4 · "Worth more" (static quote)

**Primary text:**
"You know in your heart you are worth more than you are paid."

If that sentence landed, take the free 5-minute scorecard. It shows the money pattern underneath, so you can finally change it.

**Headline:** Worth more than you're paid?
**Description:** Free money mindset scorecard
**Visual:** the quote in large serif type on cream, Lisa's small portrait and name in the corner.

### Ad L5 · "Not a budgeting quiz"

**Primary text:**
This isn't a budgeting quiz, and there's no spreadsheet.

It's 30 honest statements about what you believe about money. Your score reveals one of four Money Mindset Patterns, and what's keeping wealth from sticking.

Created by Lisa Kalmin, author of The Problem Is How You See the Problem.

**Headline:** The money quiz that isn't about math
**Description:** Free · 5 minutes · instant result

---

## 6. Retargeting ads: copy

Links: the full-price link until Dec 3, the MIRACLE200 link from Dec 4 (section 3), each with `&utm_content=<ad>`. CTA **Sign up** or **Learn more**.

| Ad | Runs | Price |
|---|---|---|
| R2 Testimonial | Nov 28 to Dec 3 | $797, no code |
| R3 Carousel | Nov 28 to Dec 14 | $797 until Dec 3, then swap card 5 to MIRACLE200 |
| R1 Video | Dec 4 to Dec 14 | $597 with MIRACLE200 |
| R4 Countdown | Dec 11 to Dec 14 | $597 with MIRACLE200 |

### Ad R1 · "You know your pattern" (Lisa video, script V2) · from Dec 4

**Primary text:**
You've seen your money pattern. Now let's change it.

Money Wealth and Miracles is Lisa Kalmin's live group course: six evenings on Zoom, Dec 14 to Feb 11, with live coaching in every session and a small group of 15 to 30.

$200 off with MIRACLE200 until we begin, Monday Dec 14 at 5:30 pm PT.

**Headline:** $597 with code MIRACLE200
**Description:** Live with Lisa · starts Dec 14

### Ad R2 · Testimonial (static) · Nov 28 to Dec 3

**Primary text:**
"Having direct access to Lisa is immeasurable. I noticed myself a few times asking, why didn't anyone tell me this before?"

Money Wealth and Miracles starts Monday, December 14. Six live sessions with Lisa Kalmin, all recorded, in a small group of 15 to 30.

**Headline:** Why didn't anyone tell me this?
**Description:** Live course · starts Dec 14
**Visual:** the quote on cream with Lisa's photo.

### Ad R3 · What's included (carousel)

Cards:
1. "6 live sessions with Lisa" · Dec 14 to Feb 11, 90 minutes, all recorded
2. "Live coaching in every session" · your questions, answered in real time
3. "Weekly breakthrough assignments" · put the shift to work
4. "A private WhatsApp group" · your Co-Miracle Makers
5. Until Dec 3: "Starts Monday, December 14" · groups of 15 to 30. From Dec 4: "$597 with MIRACLE200" · until Dec 14 at 5:30 pm PT

**Primary text:** Start the new year with a new money set point. Money Wealth and Miracles, live with Lisa Kalmin, begins Monday, December 14.
**Headline:** Money Wealth and Miracles

### Ad R4 · Countdown (Dec 11 to Dec 14 only)

**Primary text:**
We begin Monday, December 14 at 5:30 pm PT, and enrollment closes when we start.

Six live sessions with Lisa Kalmin to rewrite the money story you grew up with. $597 with MIRACLE200 until the doors close.

**Headline:** Doors close Monday 5:30 pm PT
**Description:** Last chance for $200 off
**Visual:** Lisa's photo with "3 days" (then "Tomorrow", "Today") swapped in each day.

---

## 7. Video scripts for Lisa (record on Nov 23 or 24)

Vertical 9:16, phone on a tripod at eye level, window light, 20 to 35 seconds. Add burned-in captions (most people watch muted). Hook in the first 2 seconds.

### V1 · Lead ad: "The family sentence" (about 30 s)

> What did money sound like in your house growing up?
> *(beat)*
> For some of us it was silence. For some it was "we can't afford that."
> Here's what I've learned in 39 years of coaching: that early story becomes a set point. You can work harder and still find money drifting back to the same level.
> I made a free 5-minute scorecard that shows your money pattern. Tap the link and find yours.

### V2 · Retargeting: "You've seen your pattern" (about 30 s)

> If you took my scorecard, you've seen your money pattern.
> Seeing it is the first step. Changing it is what we do in Money Wealth and Miracles, my live group course.
> Six evenings with me on Zoom, starting December 14, in a small group where I coach you directly.
> The link has everything. I'd love to see you there.

(No code in the script, so the same video can run in both phases; the code goes in the ad's text and headline.)

### V3 · Retargeting, final days: "We begin Monday" (about 20 s)

> On Monday night, a small group of us will meet for the first time and start rewriting the money stories we were handed.
> There are still seats, and your $200 off with MIRACLE200 ends when we start, Monday at 5:30 Pacific.
> Come join us.

Also cut a 15-second version of V1 for Stories and Reels.

---

## 8. What to watch each day

| Metric | Healthy | Act if |
|---|---|---|
| Cost per quiz lead | $4 to $8 | over $10 for 3 days |
| Landing page to lead rate on `/quiz/` | 25%+ | under 15%: test the quiz intro text |
| Link click-through rate | 1%+ | under 0.7%: new hooks |
| Retargeting frequency | under 5 a week | over 7: add fresh creative |
| Sales with `utm_source=meta` | 1 to 2 by Dec 14 | |
