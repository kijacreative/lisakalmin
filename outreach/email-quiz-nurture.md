# Quiz takers: from scorecard to course

**Audience:** new quiz leads from Kit form 10176902 after Nov 23 (from Meta ads, cold email, DMs, the site pop-up), **not** `mwm-buyer` and **not** `masterclass-nov19`.
**How:** a Kit sequence triggered by the quiz form. It starts the day after `email/quiz-confirmation` (which already sends the result).
**Price, in two phases:**
- **Until Dec 3:** full price, $797. Link `https://www.lisakalmin.com/course/?utm_source=kit&utm_medium=email&utm_campaign=mwm-dec&utm_content=quiz-eN`
- **From Dec 4:** $597 with MIRACLE200 through Monday, December 14 at 5:30 pm PT. Link `https://www.lisakalmin.com/course/?code=MIRACLE200&utm_source=kit&utm_medium=email&utm_campaign=mwm-dec&utm_content=quiz-eN`

**On the morning of Friday, December 4,** edit emails 2, 3 and 4 in the Kit sequence: replace each **Price block (until Dec 3)** with its **Price block (from Dec 4)**. Then send the **Dec 4 broadcast** below to everyone tagged `quiz-lead` so earlier quiz takers hear about it too.

**Late leads:** someone who takes the quiz on Dec 11 won't reach email 4 before close. So also send **Quiz 4** as a broadcast to `quiz-lead` on **Sunday, December 13**, and the 2:00 pm "3 hours" last call on Dec 14 (in `email-main-list.md`). After December 14, swap this sequence's course emails for the waitlist.

Pattern-specific opening lines use the existing custom field `money_mindset_pattern`.

---

## Quiz 1 · 1 day after the quiz (no price)

**Subject A:** What your pattern is really saying
**Subject B:** About your {{ subscriber.money_mindset_pattern | capitalize }} result
**Preview:** Your score isn't a verdict. It's a map.
**utm_content:** quiz-e1

Hi {{ subscriber.first_name | default: "there" }},

Yesterday you took the Underearning Financial Scorecard. I want to tell you what I'd say if we were sitting across from each other.

{% if subscriber.money_mindset_pattern == "manifester" %}
You're a Money Manifester. You already believe in your value, and you create value for others. What you're missing isn't confidence, it's access to the next level. That usually means there is one quiet stop left, and it's the hardest kind to see because everything else is working.
{% elsif subscriber.money_mindset_pattern == "manager" %}
You're a Money Manager. You work at it, and sometimes it works. But even when money is there, the worry is too. That tells me you're managing money from a place of "getting," and what's missing is flow, the feeling that money can come to you, not just be chased.
{% elsif subscriber.money_mindset_pattern == "clueless" %}
Your pattern is Money Unaware, and please hear this: that is not a judgment about your intelligence. It means you're working hard and feeling disconnected from what money is doing. That disconnection was learned, which means it can be unlearned.
{% elsif subscriber.money_mindset_pattern == "victim" %}
Your pattern is Money Resigned. I know that's hard to read. But the fact that you took the scorecard means some part of you is ready to step out of the loop. The feeling that "the system is rigged" is real, and it's also a way of seeing, which means it can change.
{% else %}
Whatever your score, it isn't a verdict. It's a map of the beliefs you were handed about money.
{% endif %}

Every pattern on that scorecard comes back to one thing: a money set point you didn't choose. I teach people to find it, let it go, and set a new one in my live course, **Money Wealth and Miracles**, which begins **Monday, December 14**.

See the course:
https://www.lisakalmin.com/course/

To your abundance!
Lisa

P.S. Hit reply and tell me which statement on the scorecard hit hardest. I read every reply.

---

## Quiz 2 · 2 days after the quiz

**Subject A:** "Why didn't anyone tell me this before?"
**Subject B:** What happens when your pattern shifts
**Preview:** Two students, in their own words.
**utm_content:** quiz-e2

Hi {{ subscriber.first_name | default: "there" }},

One of my students, Megan, said this after joining Money Wealth and Miracles:

> "She drops personal coaching knowledge as well as practical knowledge that I felt like I missed in high school and college. Since starting the program I have generated over $25,000.00 on top of my normal income, and the program isn't even over!"

Another student, K.Y., closed a $12M deal after joining, and two more just under $1M.

(Results vary, and none of this is a promise of income.)

Neither of them came in with the "right" pattern. They came in willing to look honestly at their money story, the same thing you just did with the scorecard.

**Price block (until Dec 3):**

We begin Monday, December 14. Six live sessions with me, small group, every session recorded.

Join Money Wealth and Miracles:
https://www.lisakalmin.com/course/

**Price block (from Dec 4):**

Because you took the scorecard, I'd like you to have **$200 off: $597 instead of $797 with the code MIRACLE200**, through Monday, December 14 at 5:30 pm PT, when the group begins.

Join for $597:
https://www.lisakalmin.com/course/?code=MIRACLE200

To your abundance!
Lisa

---

## Quiz 3 · 4 days after the quiz

**Subject A:** Six evenings with me
**Subject B:** What Money Wealth and Miracles actually looks like
**Preview:** The dates, how a session works, and how to join.
**utm_content:** quiz-e3

Hi {{ subscriber.first_name | default: "there" }},

Here's what Money Wealth and Miracles looks like from the inside.

**Six live sessions on Zoom with me**, 90 minutes each, 5:30 to 7:00 pm PT: Monday Dec 14, Tuesday Jan 5, Monday Jan 18, Thursday Jan 28, Thursday Feb 4, Thursday Feb 11. All recorded.

**In each session** I teach a shift, we do the exercise together, and I coach people live on what comes up.

**Between sessions** you get a breakthrough assignment and a private WhatsApp group with your fellow Co-Miracle Makers.

**The group is small**, 15 to 30 people, so I can coach you directly.

You'll finish in February with a new set point, before most people have even remembered their resolutions.

**Price block (until Dec 3):**

Tuition is $797 for all six sessions:
https://www.lisakalmin.com/course/

**Price block (from Dec 4):**

Join for $597 with MIRACLE200, through Dec 14 at 5:30 pm PT:
https://www.lisakalmin.com/course/?code=MIRACLE200

To your abundance!
Lisa

---

## Quiz 4 · 6 days after the quiz (and broadcast Sunday, December 13)

**Subject A:** We begin Monday, December 14
**Subject B:** Enrollment closes when we start
**Preview:** Money Wealth and Miracles starts Monday, December 14 at 5:30 pm PT.
**utm_content:** quiz-e4

Hi {{ subscriber.first_name | default: "there" }},

Money Wealth and Miracles begins **Monday, December 14 at 5:30 pm PT**, and enrollment closes when we start.

Your scorecard showed you a pattern. The course is where you change it, live, with me and a small group who are doing the same work.

**Price block (until Dec 3):**

Join us:
https://www.lisakalmin.com/course/

**Price block (from Dec 4; use this one for the Dec 13 broadcast):**

Your $200 off with MIRACLE200 ends when we start. Join for $597:
https://www.lisakalmin.com/course/?code=MIRACLE200

If you have a question first, just reply. I'll answer it myself.

To your abundance!
Lisa

---

## Dec 4 broadcast · Friday, December 4, 11:00 am PT

**Audience:** `quiz-lead`, not `mwm-buyer`, not `masterclass-nov19`.
**Subject A:** $200 off, starting today
**Subject B:** For the people who took my scorecard
**Preview:** $597 for Money Wealth and Miracles, through December 14.
**utm_content:** quiz-dec4

Hi {{ subscriber.first_name | default: "there" }},

You took my Underearning Financial Scorecard, which means you've already done the bravest part: looking honestly at your money story.

Starting today, I'd like you to have **$200 off Money Wealth and Miracles: $597 instead of $797 with the code MIRACLE200**, through the start of Module 1 on Monday, December 14 at 5:30 pm PT.

Six live sessions with me on Zoom, a small group, live coaching every session, and every session recorded.

Join for $597:
https://www.lisakalmin.com/course/?code=MIRACLE200

To your abundance!
Lisa

P.S. The $200 off is for paying in full, and it ends when we begin.
