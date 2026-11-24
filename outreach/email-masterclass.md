# Masterclass registrants: full price, then MIRACLE200 from December 4

**Audience:** tag `masterclass-nov19` (everyone who registered on form 10115136), **not** `mwm-buyer`. Where an email differs for people who attended and people who didn't, use Kit's conditional on the `masterclass-attended` tag (shown below).
**Price:**
- Emails 1 to 3 (Nov 24 to Dec 1): **$797**, link `https://www.lisakalmin.com/course/?utm_source=kit&utm_medium=email&utm_campaign=mwm-dec&utm_content=mc-eN`
- Emails 4 to 7 (Dec 4 to Dec 14): **$597 with MIRACLE200**, pay in full, link `https://www.lisakalmin.com/course/?code=MIRACLE200&utm_source=kit&utm_medium=email&utm_campaign=mwm-dec&utm_content=mc-eN`

**Don't mention FLOW200.** It's retired, and its old links now show $797 with "The code FLOW200 has expired."

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

## Masterclass 1 · Tuesday, November 24, 9:00 am PT ($797)

**Subject A:** What happens after you find the stop
**Subject B:** The part we didn't have time for
**Preview:** Finding your stop takes 90 minutes. Letting it go takes a little longer.
**utm_content:** mc-e1

Hi {{ subscriber.first_name | default: "there" }},

{% if subscriber.tags contains "masterclass-attended" %}
Thank you for being with me last Thursday. In 90 minutes, a lot of you found the place where your money story quietly says "this far and no further." I watched it happen on screen after screen.
{% else %}
I missed you last Thursday! If you haven't watched it yet, the replay is the best way to see how I work: [REPLAY LINK] Passcode: [PASSCODE]
{% endif %}

Here's what I've learned in 39 years of doing this work: finding a stop is the beginning. A stop has been there a long time, and it comes back when life gets busy, when a big invoice goes out, when the holidays hit. Letting it go, and setting a new set point that can actually hold more, takes practice and support.

That's what **Money Wealth and Miracles** is for. Six live sessions with me on Zoom, starting **Monday, December 14**, in a small group where I coach you directly, with a breakthrough assignment between every session.

See the course and the dates:
https://www.lisakalmin.com/course/

[sign-off]

P.S. Have a question about whether it's right for you? Just reply. I answer every one myself.

---

## Masterclass 2 · Saturday, November 28, 10:00 am PT ($797)

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

Seeing it is the first step. Letting it go, and setting a new set point that can hold more, is what we do over six sessions in Money Wealth and Miracles, starting Monday, December 14.

See the course:
https://www.lisakalmin.com/course/

[sign-off]

P.S. Reply with your answer to number 3. I'd love to read it.

---

## Masterclass 3 · Tuesday, December 1, 9:00 am PT ($797)

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

Join Money Wealth and Miracles:
https://www.lisakalmin.com/course/

[sign-off]

---

## Masterclass 4 · Friday, December 4, 9:00 am PT (MIRACLE200 opens)

**Subject A:** Starting today: $200 off, for you
**Subject B:** A gift for the people who came to class
**Preview:** $597 for Money Wealth and Miracles, through the day we begin.
**utm_content:** mc-e4

Hi {{ subscriber.first_name | default: "there" }},

We begin in ten days, and I want the people who came to Opening the Flow of Money to be in that room.

So starting today, you can join Money Wealth and Miracles for **$597 instead of $797, with the code MIRACLE200**, through the start of Module 1 on **Monday, December 14 at 5:30 pm PT**. It ends when we begin.

Join for $597:
https://www.lisakalmin.com/course/?code=MIRACLE200

Some of you are thinking, "I got so much from the masterclass, I can take it from here on my own." You might! But a stop is hard to see from the inside. It feels like the truth, not like a belief. That's why I teach this live, in a small group. When I coach someone in the room, I can hear the stop in their words before they can. And when you watch it happen for someone else, you suddenly recognize your own.

[sign-off]

P.S. The $200 off is for paying in full, and the link above applies MIRACLE200 for you.

---

## Masterclass 5 · Tuesday, December 8, 9:00 am PT (MIRACLE200)

**Subject A:** Bring a pal (and both save $200)
**Subject B:** Six days, and a seat for your friend
**Preview:** It's more fun with someone you love in the room.
**utm_content:** mc-e5

Hi {{ subscriber.first_name | default: "there" }},

We begin in six days.

One thing I love about this group is how often people come in pairs: a business partner, a sister, a best friend, a spouse. When you shift your money story alongside someone you see every day, it sticks.

So if someone came to mind while you were in class, invite them. MIRACLE200 works for them too: $597 each, through Monday at 5:30 pm PT.

Join for $597:
https://www.lisakalmin.com/course/?code=MIRACLE200

Forward this email, or send them this link.

[sign-off]

**Optional block if the Dec 9 Q&A runs** (place before the sign-off):

> **Tomorrow: Ask Lisa, live.** A free 45-minute Q&A, Wednesday, December 9, at 5:30 pm PT on Zoom. Bring your biggest money question, and any question about the course. [ZOOM LINK]

---

## Masterclass 6 · Friday, December 11, 9:00 am PT (MIRACLE200)

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
- **Your price:** $597 with MIRACLE200 (regularly $797), pay in full, through Monday at 5:30 pm PT

Join for $597:
https://www.lisakalmin.com/course/?code=MIRACLE200

[sign-off]

---

## Masterclass 7 · Monday, December 14, 8:00 am PT (MIRACLE200)

**Subject A:** Tonight, 5:30 pm PT
**Subject B:** We begin tonight (your $597 ends at 5:30)
**Preview:** The last few hours to join for $597.
**utm_content:** mc-e7

Hi {{ subscriber.first_name | default: "there" }},

Tonight is the night. Money Wealth and Miracles begins at 5:30 pm PT, and your $597 price with MIRACLE200 ends when we start.

Remember the stop you found in class? This is the moment to decide whether it gets to make this decision for you.

Join for $597 before 5:30 pm PT:
https://www.lisakalmin.com/course/?code=MIRACLE200

I'll see you tonight.

[sign-off]

**At 2:00 pm PT:** send the short "3 hours" last call from `email-main-list.md`.
