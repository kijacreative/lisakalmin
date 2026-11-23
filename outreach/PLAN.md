# Money Wealth and Miracles: 30 seats by December 14

**Goal:** 30 paid seats, a full room (groups are capped at 30), before doors close **Monday, December 14 at 5:30 pm PT** (Module 1 starts then).
**Today:** 6 booked (Monday, November 23). **Need:** 24 more in 21 days, about 8 a week.
**Offer:** $797 full price. $597 with a $200 code (pay in full). Checkout is the Kit product `lisakalmin.kit.com/products/copy-of-money-wealth-miracles`.

Files in this folder:

| File | What it is |
|---|---|
| `PLAN.md` | This plan: strategy, segments, codes, calendar, setup, tracking |
| `email-main-list.md` | Main list: 5 full-price emails, plus 4 discount emails for people who clicked and didn't buy |
| `email-masterclass.md` | Masterclass registrants and attendees: 7 emails with FLOW200 |
| `email-quiz-nurture.md` | Quiz takers (from ads, cold email, DMs): 4 emails with QUIZ200 |
| `email-cold.md` | Cold sourced list: 4 plain-text emails, by interest segment |
| `dm-followers.md` | Instagram DMs to people who already follow Lisa |
| `dm-prospects.md` | Instagram DMs to a researched list of people who don't follow yet |
| `meta-ads.md` | Meta ads: quiz lead campaign and offer retargeting, with copy and video scripts |

This folder is in `.vercelignore`, so the codes and strategy are not published on lisakalmin.com.

---

## 1. Where the 24 seats come from

The warmest people buy first and cheapest. Spend Lisa's time in order of warmth: masterclass people, then followers who engage, then the main list, then cold.

| Source | Price | Target seats | Why it can work |
|---|---|---|---|
| Masterclass registrants and attendees | $597 (FLOW200) | 7 | They already saw Lisa teach and heard the offer. Many missed the Nov 22 deadline over a weekend. |
| Main list clickers, final week | $597 (MIRACLE200) | 4 | They clicked and looked. A personal note and a price nudge closes some of them. |
| Instagram followers (DMs) | $597 (FRIEND200) | 4 | One-to-one conversations convert far better than broadcasts. |
| Main list, full price (5 emails) | $797 | 3 | Long-time readers who trust Lisa; a few buy at full price every launch. |
| Live "Ask Lisa" Q&A (Dec 9) and 15-minute calls | the person's own code | 2 | Live time with Lisa closes warm people who are on the fence. |
| Referrals from the 6 buyers | $797, or $597 with FRIEND200 | 2 | "Bring a pal" is already in the purchase email; ask each buyer directly too. |
| Meta ads to quiz, then retargeting | $597 (QUIZ200) | 2 | Cold leads rarely buy within 3 weeks, but the quiz builds the list for the next cohort too. |
| Cold email and IG prospects | $597 (QUIZ200 / FRIEND200) | 1 | Small, slow channels this close to the date. Run them light and treat anything as a bonus. |
| **Total** | | **25** | One seat of cushion over the 24 needed. |

With only one seat of cushion, the Q&A and 15-minute calls in section 6 are **planned from the start**, not held back. **If we are behind on Monday, December 7** (fewer than 17 total seats), add the payment plan and widen the DMs (section 6).

---

## 2. Codes and links

Create all four in Kit (Products > Money Wealth and Miracles > Discount codes) as $200 off, pay in full, **expiring Monday, December 14 at 5:30 pm PT**. One code per channel lets us count bookings by channel in Kit's sales report.

| Code | Who gets it | Link |
|---|---|---|
| FLOW200 | Masterclass registrants (reopened) | `https://www.lisakalmin.com/course/?code=FLOW200` |
| MIRACLE200 | Main list people who clicked and didn't buy, final week only | `https://www.lisakalmin.com/course/?code=MIRACLE200` |
| QUIZ200 | Quiz takers from ads and cold email, ad retargeting | `https://www.lisakalmin.com/course/?code=QUIZ200` |
| FRIEND200 | Instagram DMs, and friends of buyers | `https://www.lisakalmin.com/course/?code=FRIEND200` |

Full-price link for the main list: `https://www.lisakalmin.com/course/`

Add UTMs so Google Analytics can tell channels apart, for example `&utm_source=kit&utm_medium=email&utm_campaign=mwm-dec&utm_content=mc-e1`. Each email file lists its own `utm_content`.

**Site: done.** `course/index.html` now honours any `?code=` link until `2026-12-14T17:30:00-08:00`: it shows $597, the code, "Good through Monday, December 14 at 5:30 pm PT", the label "Your price", and passes `?promo=CODE` to Kit's checkout. The codes themselves still have to exist in Kit, or checkout will reject them.

---

## 3. Segments in Kit

| Segment / tag | Built from | Used for |
|---|---|---|
| `mwm-buyer` | Kit purchase of the product | **Excluded from everything below.** Add an automation: purchase > add tag > remove from all sequences. |
| `masterclass-nov19` | Form 10115136 (registered), plus a Zoom attendee import tagged `masterclass-attended` | Masterclass drip |
| Main list | Everyone else who is subscribed | Main list drip. **Exclude** `masterclass-nov19`, `mwm-buyer`, and anyone added after Nov 23 by the quiz |
| `mwm-clicked` | Link trigger: clicks a course link in main list emails 1 to 3 (and 4 to 5) | Discount emails in the final week |
| `quiz-lead` | Form 10176902 (quiz) | Quiz nurture sequence |
| `cold-quiz` | Quiz takers whose UTM is `utm_source=cold` | Quiz nurture (same sequence) |

**The open-and-click rule.** A click is the real signal (opens are unreliable since Apple Mail Privacy Protection marks most emails as opened). In Kit, for each course link in main list emails 1 to 3, set the link to add the tag `mwm-clicked`. On Monday, December 7, everyone with `mwm-clicked` and without `mwm-buyer` moves to the discount emails and **stops getting the full-price emails 4 and 5**, so no one sees two prices. Anyone who clicks email 4 or 5 also gets the tag, and so joins the later discount sends.

**Exclude Canada and the EU from cold email.** Canada's anti-spam law (CASL) and the GDPR require consent first.

---

## 4. Calendar

Pacific time. Main list gets a quiet Thanksgiving week after the masterclass push.

| Date | Email | Instagram | Ads | Lisa |
|---|---|---|---|---|
| **Mon Nov 23** | | | Pixel and Lead event set up | Approve copy, record 3 short videos (scripts in `meta-ads.md`) |
| **Tue Nov 24** | Masterclass 1: "I reopened your $200" | Followers DM round 1 (warmest 50) | | Text or call each of the 6 buyers: thank you, and who should come with you? |
| Wed Nov 25 | | Story: poll + "DM me MONEY" | Quiz lead campaign live | |
| Thu Nov 26 | Thanksgiving, no sends | | | |
| Fri Nov 27 | | | | |
| **Sat Nov 28** | Masterclass 2: the stop you found | Followers DM round 2 | Retargeting live | |
| Sun Nov 29 | | Prospects: warm-up begins (comments) | | |
| Mon Nov 30 | Cold email 1 (low volume) | | | |
| **Tue Dec 1** | Main 1 / Masterclass 3 | Followers DM round 3 | | |
| Wed Dec 2 | Cold email 2 | Prospects DM 1 | | |
| **Thu Dec 3** | Main 2 | Story: testimonial + "DM me MIRACLE" | | |
| Fri Dec 4 | Masterclass 4 | Prospects DM 2 | | |
| **Sun Dec 6** | Main 3, with the Dec 9 Q&A invite | | | |
| **Mon Dec 7** | Cold email 3. Build the `mwm-clicked` segment | Check-in: are we at 17? | | Payment plan and wider DMs if behind |
| **Tue Dec 8** | Clickers 1 (MIRACLE200) / Masterclass 5 | Final-week nudge to warm DM threads | Retargeting budget up | |
| **Wed Dec 9** | Main 4 (full price, clickers excluded) | | | Live "Ask Lisa" Q&A, 5:30 pm |
| Thu Dec 10 | Cold email 4 | Story: "4 days" countdown | | |
| **Fri Dec 11** | Clickers 2 / Masterclass 6 | Prospects DM 3 | | |
| Sat Dec 12 | | | Lead campaign off, all budget to retargeting | |
| **Sun Dec 13** | Quiz nurture "doors close tomorrow" broadcast | Story: "Tomorrow" | | |
| **Mon Dec 14, 8 am** | Main 5 / Clickers 3 / Masterclass 7 / quiz leads | Last-call DMs to every open thread | | |
| **Mon Dec 14, 2 pm** | Last call (short) to all non-buyers who clicked or registered | Story: "3 hours" | | |
| **5:30 pm** | Doors close. Module 1 begins | | Ads off | |

---

## 5. Setup checklist (in order)

1. **Kit discount codes:** create FLOW200 (reopen or recreate), MIRACLE200, QUIZ200, FRIEND200, all expiring Dec 14 at 5:30 pm PT.
2. **Course page:** deadline moved to Dec 14 (done). After deploying and creating the codes in Kit, open each `?code=` link through to Kit's checkout and confirm $597.
3. **Kit tags and automations:** `mwm-buyer` on purchase (and remove from all sequences); link triggers for `mwm-clicked`; import Zoom attendees as `masterclass-attended`.
4. **Meta pixel and Conversions API** through GTM (GTM-PCBSRF9P), with a `Lead` tag triggered by the `quiz_lead` dataLayer event the quiz now sends and a `Purchase` event on Kit's purchase (Kit's own Meta pixel setting on the product, or the thank-you redirect). Details in `meta-ads.md`.
5. **Consent bar:** the site defaults ad cookies to denied for every visitor until they click Accept. For US visitors that throws away most pixel data and makes ads expensive. Consider granting by default in the US and keeping the opt-in for the EU, UK and Canada.
6. **Cold email:** a separate sending domain and inbox in a cold-email tool (Instantly, Smartlead or similar), **never Kit** (Kit's terms ban purchased or scraped lists, and it would hurt the main list's deliverability). See `email-cold.md`.
7. **ManyChat** (optional, recommended) for "DM me MONEY" keyword replies on Instagram, so story replies get the quiz link instantly.

---

## 6. Accelerators

Items 1 and 2 are part of the 30-seat plan from the start. Items 3 and 4 are for falling behind (under 10 on Nov 30, or under 17 on Dec 7).

1. **Live "Ask Lisa" Q&A, Wednesday, December 9, 5:30 to 6:15 pm PT on Zoom.** Free, for masterclass registrants, main list clickers, quiz leads and DM threads. 30 minutes of coaching on a real money question from the group, then 10 minutes on the course and the code. Live events convert warm people far better than another email. Invite blocks are in `email-masterclass.md` and `email-main-list.md`; use them (they're marked optional there). Also invite quiz leads and open DM threads.
2. **15-minute "Is this right for me?" calls with Lisa.** Offer them by reply to anyone who clicked twice or asked a question. A personal call closes the people who are on the fence about money or time.
3. **Payment plan** (only if the price is the stated objection): for example 2 payments of $398.50 at full price. The current copy says "pay in full to receive the $200 discount," so a plan stays at full price.
4. **Wider DMs:** the next 100 followers, with Lisa's voice notes, and ask each buyer for one name.

Do **not** extend the deadline past Module 1. The start date is the real reason to decide now, and keeping it honest matters for the next cohort.

---

## 7. Tracking: one row a day

| Date | Seats total | FLOW200 | MIRACLE200 | QUIZ200 | FRIEND200 | Full price | Quiz leads (ads) | Cost per lead | DM threads open |
|---|---|---|---|---|---|---|---|---|---|
| Nov 23 | 6 | | | | | | | | |

Pace check: 10 by Nov 30, 17 by Dec 7, 30 by Dec 14. Most launches close a large share of their sales in the last 72 hours, so being at 17 on Dec 7 is on track, not behind.

---

## 8. Things to confirm with Lisa

- She is comfortable reopening the $200 for masterclass people (copy is honest about it being a reopen).
- Whether Module sessions are recorded (the replay and purchase emails say every session is recorded; the emails here repeat it).
- Whether to run the December 9 Q&A, and whether 15-minute calls are on offer.
- Testimonials and numbers are used exactly as on the site, each with "Results vary."
- Instagram DMs come from Lisa's account. If an assistant sends them, they should still sound like Lisa, and Lisa takes any call or voice note herself.
