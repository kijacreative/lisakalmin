# Money Wealth and Miracles: 30 seats by December 14

**Goal:** 30 paid seats, a full room (groups are capped at 30), before doors close **Monday, December 14 at 5:30 pm PT** (Module 1 starts then).
**Today:** 6 booked (Monday, November 23). **Need:** 24 more in 21 days, about 8 a week.
**Offer, in two phases:**
- **Nov 24 to Dec 3: full price, $797, for everyone.** No codes. The masterclass code FLOW200 is retired; its links now show $797 and say the code has expired.
- **Dec 4 to Dec 14 at 5:30 pm PT: $597 with MIRACLE200** (pay in full), for warm people only: masterclass registrants, main list clickers, quiz takers, Instagram conversations, retargeting ads and friends of buyers. The rest of the main list stays at full price, and is excluded from the $597 ads.

Checkout is the Kit product `lisakalmin.kit.com/products/copy-of-money-wealth-miracles`.

Files in this folder:

| File | What it is |
|---|---|
| `PLAN.md` | This plan: strategy, segments, the code, calendar, setup, tracking |
| `email-free-class.md` | **Free masterclass, Thu Dec 3, 5:30 pm PT:** 4 invites to the main list, then 5 emails to registrants that sell the course (Series 4) |
| `email-main-list.md` | Main list: 5 full-price emails, plus 3 MIRACLE200 emails for people who clicked and didn't buy |
| `email-masterclass.md` | Masterclass registrants and attendees: 3 full-price emails, then 4 with MIRACLE200 |
| `email-quiz-nurture.md` | Quiz takers (from ads, cold email, DMs): 4 emails, with the price block swapped on Dec 4 |
| `email-cold.md` | Cold sourced list: 4 plain-text emails, by interest segment |
| `dm-followers.md` | Instagram DMs to people who already follow Lisa |
| `dm-prospects.md` | Instagram DMs to a researched list of people who don't follow yet |
| `meta-ads.md` | Meta ads: quiz lead campaign and retargeting, with copy and video scripts |

This folder is in `.vercelignore`, so the code and strategy are not published on lisakalmin.com.

---

## 1. Where the 24 seats come from

The warmest people buy first. Spend Lisa's time in order of warmth: masterclass people, then followers who engage, then the main list, then cold. The first ten days sell at full price; expect the biggest wave from Dec 4, when MIRACLE200 opens, and in the last 72 hours.

| Source | Price | Target seats | Why it can work |
|---|---|---|---|
| Masterclass registrants and attendees | $797, then $597 from Dec 4 | 7 | They already saw Lisa teach and heard the offer. |
| Main list clickers, final week | $597 (MIRACLE200) | 4 | They clicked and looked. A personal note and a price nudge closes some of them. |
| Instagram followers (DMs) | $797, then $597 from Dec 4 | 4 | One-to-one conversations convert far better than broadcasts. |
| Main list, full price (5 emails) | $797 | 3 | Long-time readers who trust Lisa; a few buy at full price every launch. |
| Live "Ask Lisa" Q&A (Dec 9) and 15-minute calls | $597 (MIRACLE200) | 2 | Live time with Lisa closes warm people who are on the fence. |
| Referrals from the 6 buyers | $797, then $597 from Dec 4 | 2 | "Bring a pal" is already in the purchase email; ask each buyer directly too. |
| Meta ads to quiz, then retargeting | $797, then $597 from Dec 4 | 2 | Cold leads rarely buy within 3 weeks, but the quiz builds the list for the next cohort too. |
| Cold email and IG prospects | $597 (MIRACLE200, cold email 4) | 1 | Small, slow channels this close to the date. Run them light and treat anything as a bonus. |
| **Total** | | **25** | One seat of cushion over the 24 needed. |

With only one seat of cushion, the Q&A and 15-minute calls in section 6 are **planned from the start**, not held back. **If we are behind on Monday, December 7** (fewer than 17 total seats), add the payment plan and widen the DMs (section 6).

---

## 2. The code and links

**One code: MIRACLE200.** Create it in Kit (Products > Money Wealth and Miracles > Discount codes) as $200 off, pay in full, **starting Thursday, December 3 at 5:30 pm PT (when the free class begins, so Lisa can share it at the end) and expiring Monday, December 14 at 5:30 pm PT**. Turn FLOW200 off in Kit. Do not create QUIZ200 or FRIEND200.

| Link | When | Who |
|---|---|---|
| `https://www.lisakalmin.com/course/` | Any time | Everyone. Full price, $797 |
| `https://www.lisakalmin.com/course/?code=MIRACLE200` | From Dec 4 | Warm people listed above. Shows $597 and applies the code at checkout |

**Count bookings by channel with UTMs,** since there's one code: `utm_source` is `kit`, `instagram`, `meta` or `cold`, and `utm_content` names the email or ad (each file lists its own). Example: `https://www.lisakalmin.com/course/?code=MIRACLE200&utm_source=kit&utm_medium=email&utm_campaign=mwm-dec&utm_content=mc-e4`. For DMs and referrals, ask "who told you about it?" in the welcome reply.

**Site: done.** `course/index.html` shows $597 for `?code=MIRACLE200` only between Dec 4 at 12:00 am PT and Dec 14 at 5:30 pm PT. Before Dec 4 the same link shows $797 with no code. After the deadline, and for FLOW200 at any time, it shows $797 and "The code … has expired." Any other code is ignored. To preview a date, add `&at=2026-12-05T10:00:00-08:00` to the link (display only; Kit still checks the code).

---

## 3. Segments in Kit

| Segment / tag | Built from | Used for |
|---|---|---|
| `mwm-buyer` | Kit purchase of the product | **Excluded from everything below.** Add an automation: purchase > add tag > remove from all sequences. |
| `masterclass-nov19` | Form 10115136 (registered), plus a Zoom attendee import tagged `masterclass-attended` | Masterclass drip |
| Main list | Everyone else who is subscribed | Main list drip. **Exclude** `masterclass-nov19`, `mwm-buyer`, and anyone added after Nov 23 by the quiz |
| `mwm-clicked` | Link trigger: clicks a course link in main list emails 1 to 5 | MIRACLE200 emails in the final week |
| `quiz-lead` | Form 10176902 (quiz) | Quiz nurture sequence and the Dec 4 and Dec 13 broadcasts |
| `cold-quiz` | Quiz takers whose UTM is `utm_source=cold` | Quiz nurture (same sequence) |

**The open-and-click rule.** A click is the real signal (opens are unreliable since Apple Mail Privacy Protection marks most emails as opened). In Kit, for each course link in main list emails 1 to 5, set the link to add the tag `mwm-clicked`. On Monday, December 7, everyone with `mwm-clicked` and without `mwm-buyer` moves to the MIRACLE200 emails and **stops getting the full-price emails 4 and 5**, so no one sees two prices. Anyone who clicks email 4 or 5 also gets the tag, and so joins the later MIRACLE200 sends.

**Lists for Meta, with booked people removed.** Three Kit segments are exported and uploaded as Meta custom audiences (details and refresh days in `meta-ads.md`, section 3):

- **L1 Booked:** tag `mwm-buyer`. Excluded from every ad. Refreshed every morning.
- **L2 Warm, not booked:** `masterclass-nov19`, `quiz-lead`, `instagram-dm` or `mwm-clicked`, and not `mwm-buyer`. Retargeted in both phases.
- **L3 Main list, full price only:** everyone else, not `mwm-buyer`. Retargeted at full price until Dec 3, then **excluded** from the $597 ads, so the main list never sees MIRACLE200 in an ad.

**Exclude Canada and the EU from cold email.** Canada's anti-spam law (CASL) and the GDPR require consent first.

---

## 4. Calendar

Pacific time. Main list gets a quiet Thanksgiving week after the masterclass push. Everything before Dec 4 is full price.

| Date | Email | Instagram | Ads | Lisa |
|---|---|---|---|---|
| **Mon Nov 23** | | | Pixel and Lead event set up | Approve copy, record 3 short videos (scripts in `meta-ads.md`) |
| **Tue Nov 24** | Masterclass 1: "What happens after the stop" ($797) | Followers DM round 1 (warmest 50) | | Text or call each of the 6 buyers: thank you, and who should come with you? |
| Wed Nov 25 | | Story: poll + "DM me MONEY" | Quiz lead campaign live | |
| Thu Nov 26 | Thanksgiving, no sends | | | |
| Fri Nov 27 | | | | |
| **Sat Nov 28** | Masterclass 2: the stop you found ($797) | Followers DM round 2 | Retargeting live (full price) | |
| Sun Nov 29 | | Prospects: warm-up begins (comments) | | |
| Mon Nov 30 | Cold email 1 (low volume) | | | |
| **Tue Dec 1** | Main 1 / Masterclass 3 ($797) | Followers DM round 3 | | |
| Wed Dec 2 | Cold email 2 | Prospects DM 1 | | |
| **Thu Dec 3** | Main 2 | Story: testimonial + "DM me MIRACLE" | Refresh L1, L2, L3 uploads | |
| **Fri Dec 4** | **MIRACLE200 opens.** Masterclass 4 / quiz leads broadcast | DMs: MIRACLE200 to every open thread | Retargeting switches to the $597 ads; L3 (main list) moves to exclusions | |
| Sat Dec 5 | | Prospects DM 2 | | |
| **Sun Dec 6** | Main 3 ($797), with the Dec 9 Q&A invite | | | |
| **Mon Dec 7** | Cold email 3. Build the `mwm-clicked` segment | Check-in: are we at 17? | | Payment plan and wider DMs if behind |
| **Tue Dec 8** | Clickers 1 (MIRACLE200) / Masterclass 5 | Final-week nudge to warm DM threads | Retargeting budget up; refresh L2 and L3 | |
| **Wed Dec 9** | Main 4 (full price, clickers excluded) | | | Live "Ask Lisa" Q&A, 5:30 pm |
| Thu Dec 10 | Cold email 4 (MIRACLE200) | Story: "4 days" countdown | | |
| **Fri Dec 11** | Clickers 2 / Masterclass 6 | Prospects DM 3 | | |
| Sat Dec 12 | | | Lead campaign off, all budget to retargeting | |
| **Sun Dec 13** | Quiz leads "doors close tomorrow" broadcast | Story: "Tomorrow" | | |
| **Mon Dec 14, 8 am** | Main 5 / Clickers 3 / Masterclass 7 / quiz leads | Last-call DMs to every open thread | | |
| **Mon Dec 14, 2 pm** | Last call (short) to all non-buyers who clicked, registered or took the quiz | Story: "3 hours" | | |
| **5:30 pm** | Doors close. Module 1 begins | | Ads off | |

---

## 5. Setup checklist (in order)

1. **Kit discount code:** create MIRACLE200, $200 off, pay in full, live Dec 4 at 12:00 am PT to Dec 14 at 5:30 pm PT. Turn FLOW200 off.
2. **Course page:** done (section 2). After deploying, check `?code=MIRACLE200` shows $797 now, and with `&at=2026-12-05T10:00:00-08:00` shows $597. On Dec 4, click through to Kit's checkout and confirm $597.
3. **Kit tags and automations:** `mwm-buyer` on purchase (and remove from all sequences); tag the 6 current buyers `mwm-buyer` by hand if they aren't already; link triggers for `mwm-clicked`; import Zoom attendees as `masterclass-attended`. Then build the L1, L2 and L3 segments and upload them to Meta (section 3).
4. **Meta pixel and Conversions API** through GTM (GTM-PCBSRF9P), with a `Lead` tag triggered by the `quiz_lead` dataLayer event the quiz now sends and a `Purchase` event on Kit's purchase (Kit's own Meta pixel setting on the product, or the thank-you redirect). Details in `meta-ads.md`.
5. **Consent bar:** the site defaults ad cookies to denied for every visitor until they click Accept. For US visitors that throws away most pixel data and makes ads expensive. Consider granting by default in the US and keeping the opt-in for the EU, UK and Canada.
6. **Cold email:** a separate sending domain and inbox in a cold-email tool (Instantly, Smartlead or similar), **never Kit** (Kit's terms ban purchased or scraped lists, and it would hurt the main list's deliverability). See `email-cold.md`.
7. **ManyChat** for the MONEY (scorecard) and MIRACLE (course) keyword replies on Instagram. Full setup, copy and tests: `manychat.md`. Live before the Nov 25 story.
8. **On Dec 4:** swap the price block in quiz nurture emails 2 to 4 (`email-quiz-nurture.md`), and switch retargeting to the $597 ads (`meta-ads.md`).

---

## 6. Accelerators

Items 1 and 2 are part of the 30-seat plan from the start. Items 3 and 4 are for falling behind (under 9 on Nov 30, or under 17 on Dec 7).

1. **Live "Ask Lisa" Q&A, Wednesday, December 9, 5:30 to 6:15 pm PT on Zoom.** Free, for masterclass registrants, main list clickers, quiz leads and DM threads. 30 minutes of coaching on a real money question from the group, then 10 minutes on the course and MIRACLE200. Live events convert warm people far better than another email. Invite blocks are in `email-masterclass.md` and `email-main-list.md`; use them (they're marked optional there). Also invite quiz leads and open DM threads.
2. **15-minute "Is this right for me?" calls with Lisa.** Offer them by reply to anyone who clicked twice or asked a question. A personal call closes the people who are on the fence about money or time.
3. **Payment plan** (only if the price is the stated objection): for example 2 payments of $398.50 at full price. The $200 off is for paying in full, so a plan stays at full price.
4. **Wider DMs:** the next 100 followers, with Lisa's voice notes, and ask each buyer for one name.

Do **not** open MIRACLE200 early or extend it past Module 1. The dates are the honest reason to decide, and keeping them matters for the next cohort.

---

## 7. Tracking: one row a day

| Date | Seats total | Full price ($797) | MIRACLE200 ($597) | Source (UTM or "who told you") | Quiz leads (ads) | Cost per lead | DM threads open |
|---|---|---|---|---|---|---|---|
| Nov 23 | 6 | | | | | | |

Pace check: 9 by Nov 30, 17 by Dec 7, 30 by Dec 14. Full price slows the first ten days; MIRACLE200 opening on Dec 4 and the last 72 hours carry most of the sales, so 17 on Dec 7 is on track.

---

## 8. Things to confirm with Lisa

- Whether Module sessions are recorded (the replay and purchase emails say every session is recorded; the emails here repeat it).
- Whether to run the December 9 Q&A, and whether 15-minute calls are on offer.
- Testimonials and numbers are used exactly as on the site, each with "Results vary."
- Instagram DMs come from Lisa's account. If an assistant sends them, they should still sound like Lisa, and Lisa takes any call or voice note herself.
