# Meta ads: quiz leads, then retarget with the offer

**Two campaigns:**

1. **Quiz leads** (cold): ads send people to the Underearning Financial Scorecard at `/quiz/`. The email gate captures them into Kit (form 10176902), and `email-quiz-nurture.md` sells the course.
2. **Retargeting** (warm): people who took the quiz, visited the course page, engaged with Lisa, or are on her lists see the course. **Nov 28 to Dec 3 at full price** (ads R2 and R3, no code). **From Fri Dec 4, the $597 offer with MIRACLE200** (ads R1, R3 with its last card swapped, and R4 from Dec 11).

**Plus, inside Campaign 1: the free class ad set (ads M1 to M3, section 5c).** From Fri Nov 27 to Thu Dec 3 at 3:00 pm PT, ads invite cold audiences to Lisa's free masterclass on Thursday, December 3. Registering puts them in Kit (form 10115136, tag `masterclass-dec3`), where Series 4 sells the course.

**Dates:** Wed Nov 25 to Mon Dec 14, 5:30 pm PT.
**Suggested budget:** about **$1,600 total**.

| Campaign | Nov 25 to Dec 7 | Dec 8 to Dec 11 | Dec 12 to Dec 14 | Total |
|---|---|---|---|---|
| Quiz leads | $60 a day | $60 a day | off | about $1,020 |
| Offer retargeting (from Nov 28) | $20 a day | $40 a day | $60 a day | about $550 |
| Free class ad set (Nov 27 to Dec 3, 3 pm) | $35 a day | off | off | about $240 |

With the class ad set, the total is about **$1,850**. To keep it at $1,600, run the quiz ad sets at $35 a day from Nov 27 to Dec 3 instead.

Realistic expectation: $4 to $8 a lead in this space, so roughly 130 to 250 quiz leads. Cold leads seldom buy a $597 course within 3 weeks, so plan for 1 to 2 seats from ads, and a much bigger waitlist for the next cohort. Retargeting the lists Lisa already has (masterclass, main list, engagers) is where the near-term seats come from.

---

## 1. Tracking setup (do this first)

The site has Google Tag Manager (GTM-PCBSRF9P) but no Meta pixel yet. The quiz already sends the conversion event to GTM.

1. **Meta pixel through GTM** on every page, plus the **Conversions API** (GTM server-side, or Meta's CAPI Gateway) so iOS and ad-blocked visitors still count.
2. **`Lead` event:** when Kit accepts a quiz signup, the quiz page pushes `{ event: 'quiz_lead', money_mindset_pattern, money_mindset_score }` to the dataLayer (done). In GTM, add a Custom Event trigger for `quiz_lead` and a Meta `Lead` tag on it, passing the pattern as `content_name` from a Data Layer Variable.
2b. **Class `Lead` event:** when Kit accepts a masterclass registration, the masterclass page pushes `{ event: 'class_lead', class_date: '2026-12-03' }` to the dataLayer (done). Add a Custom Event trigger for `class_lead` and a second Meta `Lead` tag on it with `content_name: 'masterclass-dec3'`, so the class ad set can optimize for sign-ups. In Ads Manager, make a custom conversion on `Lead` where content_name contains `masterclass` if you want the quiz and class counts separate.
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

| D. Free class (Nov 27 to Dec 3, 3 pm PT) | Advantage+ audience, with the interests from A as suggestions. Ads M1 to M3, sending people to `/masterclass/`. Optimize for the `Lead` event from the class form (section 1, step 2b) | $35 |

**Exclude** from all ad sets: **L1 Booked** and the pixel `Purchase` event, people who already took the quiz (pixel `Lead`, 180 days), and **L2 Warm, not booked** (they get retargeting instead). Lists are defined in section 3.

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
- **On Dec 4:** pause the full-price ads and turn on the MIRACLE200 ads in the same ad set, so learning carries over. In the same edit, move **L3** from the audience to the exclusions.

**Audience, Nov 28 to Dec 3 (full-price ads):**

- Took the quiz (pixel `Lead`, 30 days)
- Visited `/course/` (30 days) or `/masterclass/` (60 days)
- Engaged with Lisa's Instagram or Facebook page (60 days)
- Watched 50% or more of any Lisa video ad (30 days)
- Uploaded lists: **L2 Warm, not booked** and **L3 Main list, full price only** (below)

**Audience, Dec 4 to Dec 14 ($597 ads):** the same, **minus L3**. The main list is left off the MIRACLE200 ads: Lisa's call, so people who were only offered $797 by email don't see $597 in their feed. L3 is added as an **exclusion**, which also removes main list people who show up through site visits or engagement.

**Exclude, always:** **L1 Booked** and the pixel `Purchase` event (180 days).

### Uploaded lists: built in Kit, with booked people removed

Meta can only leave out buyers it knows about, so every list we upload must already have the booked people taken out, and we upload the buyers as their own list to exclude. Build each as a Kit segment, export the subscribers as CSV (email, first name), and upload to Meta as a customer list custom audience with the same name.

| List | Kit segment | Used as | Refresh |
|---|---|---|---|
| **L1 Booked** | Tag `mwm-buyer` (everyone who has bought, including the original 6) | Exclusion in **every** campaign and ad set, lead ads included | Every morning, so new buyers stop seeing ads within a day |
| **L2 Warm, not booked** | Tag `masterclass-nov19` **or** `quiz-lead` **or** `mwm-clicked`, **and not** `mwm-buyer` | Retargeting audience, both phases | Dec 3 (before $597 opens), Dec 8 (after the clicker segment), Dec 11 |
| **L3 Main list, full price only** | All subscribers, **not** `masterclass-nov19`, `quiz-lead`, `mwm-clicked` or `mwm-buyer` | Retargeting audience until Dec 3, **exclusion** from Dec 4 | Same days as L2, so people who click move from L3 to L2 |

Before uploading, check the 6 current buyers are tagged `mwm-buyer` in Kit; if they bought before the tag automation existed, add the tag by hand. Lookalikes (campaign 1, ad set B) can still be built from the whole Kit list: a lookalike is a model, not people who see the ads.

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

### Ad L4 · "Worth more" (portrait)

**Primary text:**
Most people are worth more than they let themselves receive. Not because of skill, but because of an old money story that sets the limit.

The free 5-minute scorecard shows the money pattern underneath, so you can finally change it.

**Headline:** What's your money pattern?
**Description:** Free money mindset scorecard
**Visual:** Lisa's portrait (yellow wrap) above the line "Most people are worth more than they let themselves receive." in large type on forest green.

*Changed from the first draft:* "You know in your heart you are worth more than you are paid" and the headline "Worth more than you're paid?" tell the viewer something about their own pay, which Meta's personal attributes policy rejects. The new line talks about people in general.

### Ad L5 · "Not a budgeting quiz"

**Primary text:**
This isn't a budgeting quiz, and there's no spreadsheet.

It's 30 honest statements about what you believe about money. Your score reveals one of four Money Mindset Patterns, and what's keeping wealth from sticking.

Created by Lisa Kalmin, author of The Problem Is How You See the Problem.

**Headline:** The money quiz that isn't about math
**Description:** Free · 5 minutes · instant result

---

## 5b. Quiz ad images (ready to upload)

Designed in Lisa's site brand and rendered at Meta's sizes in `outreach/ads/png/`. The source pages are in `outreach/ads/src/`. To change a word, edit the HTML and re-render it with headless Chrome at the size below. Stories versions keep words out of the top 300 px and bottom 400 px, where Instagram draws its own controls.

| Ad | Feed, 4:5 (1080x1350) | Stories and Reels, 9:16 (1080x1920) |
|---|---|---|
| L1 "Which one is yours?" | `patterns-feed.png` | `patterns-story.png` |
| L1 carousel, 6 cards (1080x1080) | `carousel-1.png` to `carousel-6.png` | (use `patterns-story.png`) |
| L3 "A great month. A slow one. Again." | `setpoint-feed.png` | `setpoint-story.png` |
| L4 Portrait | `quote-feed.png` | `quote-story.png` |
| L5 "Not a budgeting quiz" | `notbudget-feed.png` | `notbudget-story.png` |

| R2 Testimonial | `testimonial-feed.png` | `testimonial-story.png` |
| R3 What's included, carousel (1080x1080) | `included-1.png` to `included-5.png`; on Dec 4 swap card 5 for `included-5-code.png` | (use `testimonial-story.png` until Dec 3) |
| R4 Countdown | `countdown-3-feed.png` (Dec 11 and 12), `countdown-tomorrow-feed.png` (Dec 13), `countdown-today-feed.png` (Dec 14) | the same names with `-story` |

L2 and R1 are Lisa's own videos (scripts V1 and V2), so they have no designed image. All the ads, with copy buttons for every field, are also on one page: https://claude.ai/artifact/LkHf3U7d8oDquEFoaMQyPq In Ads Manager, upload both sizes to each ad and use **Customize placements** so Stories and Reels get the 9:16 image.

## 5c. Free class ads (Dec 3): copy and images

**Goal:** new email addresses. Every ad sends people to the free class page, `https://www.lisakalmin.com/masterclass/?utm_source=meta&utm_medium=paid&utm_campaign=mwm-dec3&utm_content=<ad>`, where they register with first name and email. The class itself, and Series 4 after it, sell the course, so the ads never mention a price.
**Run:** Fri Nov 27 to Thu Dec 3 at 3:00 pm PT, then turn the ad set off (people need time to get the Zoom link). **CTA button:** Sign up. **Exclude** `masterclass-dec3` (upload the tag as a list on Dec 1) and the class `Lead` event.

| Ad | Feed, 4:5 (1080x1350) | Stories and Reels, 9:16 (1080x1920) | utm_content |
|---|---|---|---|
| M1 Lisa's portrait, "Money is still flowing" | `class-invite-feed.png` | `class-invite-story.png` | `m1-invite` |
| M2 "Four quiet money stops" | `class-stops-feed.png` | `class-stops-story.png` | `m2-stops` |
| M3 Save the date, Dec 3 | `class-date-feed.png` | `class-date-story.png` | `m3-date` |

### Ad M1 · "Money is still flowing" (portrait)

**Primary text:**
The economy isn't what limits most people's income. Their relationship with money is, and the quiet "stops" inside it.

Join Lisa Kalmin for a free 90-minute live masterclass, Opening the Flow of Money, on Thursday, December 3, at 5:30 pm PT on Zoom. Find your stops, see where they started, and leave with a new money set point and 4 actions for the same day.

39 years of coaching. 50,000+ people trained. Free to attend.

**Headline:** Free live class with Lisa, Dec 3
**Description:** 90 minutes on Zoom · free

### Ad M2 · "Four quiet money stops"

**Primary text:**
"There's never quite enough." The pause before naming a price. Not looking, because looking is stressful. Money in, money right back out.

These are money stops: old beliefs that quietly cap how much money feels safe to have. They can be found, and they can be let go.

On Thursday, December 3, Lisa Kalmin is teaching a free live masterclass on exactly this. Bring a journal.

**Headline:** Find your money stops, free
**Description:** Live on Zoom · Thu, Dec 3

### Ad M3 · Save the date

**Primary text:**
Save the date: Thursday, December 3, 5:30 to 7:00 pm PT.

Opening the Flow of Money: Letting Go of Your Stops is a free live masterclass with transformational coach Lisa Kalmin, author of The Problem Is How You See the Problem. Come as you are, ask your questions live, and set a new money set point before the year ends.

Seats are free. The Zoom link arrives by email.

**Headline:** Save your free seat for Dec 3
**Description:** 5:30 pm PT · live on Zoom

*Policy check:* none of the three tells the viewer they're broke or under-earning, and none mentions income results. They talk about people in general and about the class.

## 6. Retargeting ads: copy

Links: the full-price link until Dec 3, the MIRACLE200 link from Dec 4 (section 3), each with `&utm_content=<ad>`. CTA **Sign up** or **Learn more**.

| Ad | Runs | Price |
|---|---|---|
| R2 Testimonial | Nov 28 to Dec 3 | $797, no code |
| R3 Carousel | Nov 28 to Dec 14 | $797 until Dec 3, then swap card 5 to MIRACLE200 |
| R1 Video | Dec 4 to Dec 14 (main list excluded) | $597 with MIRACLE200 |
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
