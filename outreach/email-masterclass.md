# Masterclass registrants: reopened $200 offer (FLOW200)

**Audience:** tag `masterclass-nov19` (everyone who registered on form 10115136), **not** `mwm-buyer`. Where an email differs for people who attended and people who didn't, use Kit's conditional on the `masterclass-attended` tag (shown below).
**Price:** $597 with FLOW200, through Monday, December 14 at 5:30 pm PT. Pay in full.
**Link:** `https://www.lisakalmin.com/course/?code=FLOW200&utm_source=kit&utm_medium=email&utm_campaign=mwm-dec&utm_content=mc-eN`
**Before sending email 1:** move the course page deadline to Dec 14 (see `PLAN.md`, section 2) and test the link.

Conditional snippet for Kit:

```
{% if subscriber.tags contains "masterclass-attended" %}...attended copy...{% else %}...missed copy...{% endif %}
```

Sign-off for every email:

```
To your abundant flow!
Lisa

Lisa Kalmin
Transformational Mindset Wizard
Author of "The Problem Is How You See the Problem"
```

---

## Masterclass 1 · Tuesday, November 24, 9:00 am PT

**Subject A:** I reopened your $200
**Subject B:** Your masterclass price is back
**Preview:** $597 for Money Wealth and Miracles, now through the day we begin.
**utm_content:** mc-e1

Hi {{ subscriber.first_name | default: "there" }},

The $200 masterclass price for Money Wealth and Miracles ended Sunday night. I've decided to reopen it for you.

Here's why. The deadline landed on the weekend right after class, right before Thanksgiving, and I would rather you decide from a clear place than from a countdown. A money decision made in a rush is exactly the kind of stop we work on together.

So your price is back: **$597 instead of $797, with the code FLOW200**, all the way until we begin on **Monday, December 14 at 5:30 pm PT**. It won't be extended past that, because that's when the group starts.

Join for $597:
https://www.lisakalmin.com/course/?code=FLOW200

{% if subscriber.tags contains "masterclass-attended" %}
You felt what happens in 90 minutes when a stop comes to the surface. Money Wealth and Miracles is six of those sessions, with time between them to actually live the shift, and me coaching you through it.
{% else %}
If you didn't make it live, the replay is still waiting for you, and it's the best way to see how I work before you decide. [REPLAY LINK] Passcode: [PASSCODE]
{% endif %}

[sign-off]

P.S. Your code is FLOW200. The $200 off is for paying in full, and the link above applies it for you.

---

## Masterclass 2 · Saturday, November 28, 10:00 am PT

**Subject A:** Which stop did you find?
**Subject B:** The stop that showed up for you
**Preview:** A short exercise to do this weekend, with or without me.
**utm_content:** mc-e2

Hi {{ subscriber.first_name | default: "there" }},

I hope you had a warm Thanksgiving.

I want to give you something to try this weekend, whether or not you join the course.

In class we talked about stops, the places where your money story quietly says "this far and no further." Here's a five-minute way to find yours:

1. Finish this sentence three times, fast, without editing: **"Money is..."**
2. Then this one: **"People who have a lot of money are..."**
3. Then: **"If I had twice the income, I'd be afraid that..."**

Read what you wrote. One of those lines will have a charge to it. That's your stop.

Seeing it is the first step. Letting it go, and setting a new set point that can hold more, is what we do over six sessions in Money Wealth and Miracles.

Your price is $597 with FLOW200, through Monday, December 14:
https://www.lisakalmin.com/course/?code=FLOW200

[sign-off]

P.S. Reply with your answer to number 3. I'd love to read it.

---

## Masterclass 3 · Tuesday, December 1, 9:00 am PT

**Subject A:** $25,000 and a $12M deal (and what actually changed)
**Subject B:** What happened after they found their stop
**Preview:** Two students, in their own words.
**utm_content:** mc-e3

Hi {{ subscriber.first_name | default: "there" }},

I shared these stories in class. I want to tell you what was underneath them.

**Megan**, Head of Design at a creative agency, generated over $25,000 on top of her normal income before the course had even ended. **K.Y.** closed a $12M deal after joining, and two more just under $1M.

(Results vary, and none of this is a promise of income.)

Neither of them learned a secret strategy. What changes in this course is what you can see. When you can finally see the stop that has been setting your ceiling, you act differently, and money follows the action. [LISA: one or two lines here on what you saw shift for Megan or K.Y., in your words, would make this email.]

That's the whole idea behind my book, and the course: the problem is how you see the problem.

We start in two weeks, Monday, December 14 at 5:30 pm PT. Six live sessions, each one recorded.

Join for $597 with FLOW200:
https://www.lisakalmin.com/course/?code=FLOW200

[sign-off]

---

## Masterclass 4 · Friday, December 4, 9:00 am PT

**Subject A:** "I can do this on my own"
**Subject B:** Why I don't teach this as a video course
**Preview:** The part you can't do alone.
**utm_content:** mc-e4

Hi {{ subscriber.first_name | default: "there" }},

Some of you are thinking, "I got so much from the masterclass, I can probably take it from here on my own."

You might! And I want you to keep using what you learned.

But here's what I've seen over 39 years: a stop is hard to see from the inside. It feels like the truth, not like a belief. That's why I teach this live, in a small group. When I coach someone in the room, I can hear the stop in their words before they can. And when you watch it happen for someone else, you suddenly recognize your own.

Then there's the part between sessions: the weekly breakthrough assignment, and a WhatsApp group full of people who are making the same shift. That's what keeps the new set point from drifting back to the old one.

If you'd like to talk about whether it's right for you, just reply. I read and answer every message myself.

Your $597 price with FLOW200 is good through Monday, December 14 at 5:30 pm PT:
https://www.lisakalmin.com/course/?code=FLOW200

[sign-off]

---

## Masterclass 5 · Tuesday, December 8, 9:00 am PT

**Subject A:** Bring a pal (and both save $200)
**Subject B:** Six days, and a seat for your friend
**Preview:** It's more fun with someone you love in the room.
**utm_content:** mc-e5

Hi {{ subscriber.first_name | default: "there" }},

We begin in six days.

One thing I love about this group is how often people come in pairs: a business partner, a sister, a best friend, a spouse. When you shift your money story alongside someone you see every day, it sticks.

So if someone came to mind while you were in class, invite them. Your FLOW200 code works for them too: $597 each, through Monday at 5:30 pm PT.

Join for $597:
https://www.lisakalmin.com/course/?code=FLOW200

Forward this email, or send them this link.

[sign-off]

**Optional block if the Dec 9 Q&A runs** (place before the sign-off):

> **Tomorrow: Ask Lisa, live.** A free 45-minute Q&A, Wednesday, December 9, at 5:30 pm PT on Zoom. Bring your biggest money question, and any question about the course. [ZOOM LINK]

---

## Masterclass 6 · Friday, December 11, 9:00 am PT

**Subject A:** Before the weekend gets busy
**Subject B:** A quiet decision
**Preview:** Money Wealth and Miracles begins Monday. Your $597 ends when we start.
**utm_content:** mc-e6

Hi {{ subscriber.first_name | default: "there" }},

The weekend before the holidays gets full fast, so I wanted to reach you while it's quiet.

On Monday evening, a small group of us will meet for the first time and start rewriting the money stories we were handed. I'd love for you to be in that room.

Here's everything in one place:

- **Six live sessions on Zoom:** Dec 14, Jan 5, Jan 18, Jan 28, Feb 4, Feb 11, 5:30 to 7:00 pm PT, all recorded
- **Live coaching and Q&A** with me in every session
- **Weekly breakthrough assignments**
- **A private WhatsApp group** of Co-Miracle Makers
- **Your price:** $597 with FLOW200 (regularly $797), pay in full, through Monday at 5:30 pm PT

Join for $597:
https://www.lisakalmin.com/course/?code=FLOW200

[sign-off]

---

## Masterclass 7 · Monday, December 14, 8:00 am PT

**Subject A:** Tonight, 5:30 pm PT
**Subject B:** We begin tonight (your $597 ends at 5:30)
**Preview:** The last few hours to join at your masterclass price.
**utm_content:** mc-e7

Hi {{ subscriber.first_name | default: "there" }},

Tonight is the night. Money Wealth and Miracles begins at 5:30 pm PT, and your $597 price with FLOW200 ends when we start.

Remember the stop you found in class? This is the moment to decide whether it gets to make this decision for you.

Join for $597 before 5:30 pm PT:
https://www.lisakalmin.com/course/?code=FLOW200

I'll see you tonight.

[sign-off]

**At 2:00 pm PT:** send the short "3 hours" last call from `email-main-list.md` with FLOW200.
