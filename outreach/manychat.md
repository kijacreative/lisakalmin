# ManyChat: MONEY and MIRACLE keyword flows

**Goal:** when someone types a keyword in Lisa's Instagram DMs, a story reply or a comment, ManyChat replies at once. **MONEY** sends the free scorecard. Anyone who takes it joins Kit through the quiz (form 10176902, tag `quiz-lead`) and gets the quiz nurture emails. **MIRACLE** sends the course. People give their email themselves, so they're opted in and Kit can email them.

The stories, posts and DMs already use these two words (`dm-followers.md`, the client deck), so no copy changes are needed elsewhere.

---

## 1. Before you build (about 20 minutes)

1. **Instagram account type:** it must be a Professional account (Creator or Business), connected to a Facebook **Page**. In the Instagram app: Settings > Account type and tools.
2. **Allow message access:** in Instagram, go to Settings > Messages and story replies > Message controls > Connected tools, and turn on **Allow access to messages**. ManyChat can't reply without it.
3. **ManyChat account:** sign up at manychat.com with Lisa's Facebook login, and connect Instagram. (Lisa or you log in; Claude can't sign in for you.)
4. **Plan:** the free plan covers keyword replies. The **Kit integration** (step 5) and the follow-up after a delay need **Pro**. Check current pricing on ManyChat's site; at Lisa's size it's the smallest Pro tier.
5. **Connect Kit:** in ManyChat go to Settings > Integrations > ConvertKit (Kit), and paste the Kit API key from Kit > Settings > Developer. You need this only for the "email it to me" path in Flow A.
6. **Facebook:** ManyChat works with Facebook **Pages**, not personal profiles. `facebook.com/lisa.kalmin` looks like a personal profile, so these flows run on Instagram. If Lisa has a business Page, connect it too and turn on the same keywords for Messenger.

## 2. Tags in ManyChat (and in Kit)

| ManyChat tag | Added when | Used for |
|---|---|---|
| `kw-money` | Flow A starts | Count of scorecard requests |
| `kw-miracle` | Flow B starts | People asking about the course; Lisa follows up by hand |
| `wants-call` | They tap "Ask Lisa a question" | Live chat with Lisa or the team |

Kit tag added through the integration: **`instagram-dm`** (only on the "email it to me" path in Flow A). Add `instagram-dm` to the **L2 Warm** list in `PLAN.md` so these people see the reminder ads.

---

## 3. Flow A · MONEY (the scorecard)

**Triggers** (Automation > New > Instagram), all pointing to the same flow:
- **DM keyword:** message *contains* `money` (any capitalization). Also add `scorecard` and `quiz`, so variations work.
- **Story reply:** reply to any story that *contains* `money`.
- **Post or reel comment:** comment *contains* `money` on the posts you choose. Turn on **public reply to comment**, with three variations so they aren't identical:
  - "Sent you a DM 💛"
  - "Check your DMs, it's on its way"
  - "Just sent it to you!"

**Message A1** (sent right away)

> Hi {{first_name}}! I'm so glad you asked 💛
>
> My Underearning Financial Scorecard shows which money pattern you're running: Manifester, Manager, Clueless or Victim. 30 quick statements, about 5 minutes, and you see your result right away.
>
> [Button: **Send me the scorecard**]

*Why a button first:* Instagram shows a link more reliably after the person taps, and the tap tells ManyChat they're engaged.

**Message A2** (after they tap the button)

> Here it is:
>
> [Button: **Take the scorecard** → `https://www.lisakalmin.com/quiz/?utm_source=instagram&utm_medium=manychat&utm_campaign=mwm-dec&utm_content=money`]
>
> When you see your pattern, reply here and tell me what it was. I'd love to know 🙏

Action: add tag `kw-money`.

**Message A3** (Smart Delay **22 hours**, then a Condition: they did **not** click "Take the scorecard")

> Just making sure this didn't get buried. Your scorecard is here whenever you have 5 minutes:
>
> [Button: **Take the scorecard**] (same link)
>
> [Button: **Email it to me instead**]

*Why 22 hours:* Instagram only lets an automated message go out within 24 hours of the person's last message, so the follow-up has to land before that.

**"Email it to me instead" path**
1. **Message:**
   > Of course! What's the best email for you? I'll send the scorecard link there, plus an occasional note from me. You can unsubscribe anytime.
2. **User Input:** reply type **Email**, saved to the ManyChat email field. ManyChat checks the format; if it's invalid, reply "Hmm, that doesn't look like an email. Could you try again?"
3. **Action:** Kit > **Add tag** `instagram-dm` to that email. This creates the subscriber in Kit.
4. **Message:**
   > Done! Check your inbox in a minute. 💛

**In Kit:** create a Rule or a one-email automation: **tag added `instagram-dm` → send "Your scorecard"**, using the Kit template:
- **Subject:** Your money scorecard
- **Body:**
  > Hi {{ subscriber.first_name | default: "there" }}, here's the Underearning Financial Scorecard you asked for on Instagram. It takes about 5 minutes, and you'll see your Money Mindset Pattern right away.
  - Button: **Take the scorecard**, linked to `https://www.lisakalmin.com/quiz/?utm_source=instagram&utm_medium=email&utm_campaign=mwm-dec`
  - Sign-off: "To your abundance! Lisa"
- When they take the quiz, the quiz form tags them `quiz-lead`, and the nurture sequence takes over.

---

## 4. Flow B · MIRACLE (the course)

**Triggers:**
- **DM keyword:** message contains `miracle`, `course` or `mwm`.
- **Story reply:** reply contains `miracle`.
- **Comment:** comment contains `miracle`, with the public reply "Sent you the details in DM 💛".

**Message B1** (right away). This message has two versions: **swap them on the morning of Friday, December 4**, the same day as the email and ad switch.

*Until Dec 3 (full price):*

> Hi {{first_name}}! Here's everything about **Money Wealth and Miracles** 💛
>
> Six live evenings on Zoom with me, starting Monday, December 14 at 5:30 pm PT, in a small group where I coach you directly. Every session is recorded.
>
> Tuition is $797.
>
> [Button: **See the course** → `https://www.lisakalmin.com/course/?utm_source=instagram&utm_medium=manychat&utm_campaign=mwm-dec&utm_content=miracle`]
> [Button: **Ask Lisa a question**]

*From Dec 4 (MIRACLE200):*

> Hi {{first_name}}! Here's everything about **Money Wealth and Miracles** 💛
>
> Six live evenings on Zoom with me, starting Monday, December 14 at 5:30 pm PT, in a small group where I coach you directly. Every session is recorded.
>
> Until we begin, it's **$597 instead of $797 with the code MIRACLE200**. The link below has it ready for you.
>
> [Button: **Join for $597** → `https://www.lisakalmin.com/course/?code=MIRACLE200&utm_source=instagram&utm_medium=manychat&utm_campaign=mwm-dec&utm_content=miracle`]
> [Button: **Ask Lisa a question**]

Action: add tag `kw-miracle`.

**"Ask Lisa a question" path**
1. **Message:**
   > Of course! Type your question here and I'll answer you personally, usually within a day.
2. **Action:** add tag `wants-call`, **pause automation for 24 hours** (so the bot doesn't talk over Lisa), and **notify** Lisa or the team: Action > Notify admins, by email or the ManyChat app.

**Message B2** (Smart Delay 22 hours; Condition: did not click the course button; and **not** before a price change). This is a short nudge.

> One more thing: every session is recorded, so if an evening doesn't work, you won't miss anything. Here's the link again whenever you're ready:
>
> [Button: same as B1]

**After December 14, 5:30 pm PT:** change B1 to the waitlist:

> We've just begun this round! Want to be first to hear when the next one opens?

Then use the same "email" path as Flow A, but tag `mwm-waitlist` in Kit.

---

## 5. Default reply and live chat

- **Default reply** (any DM that matches no keyword): **off**. People writing to Lisa personally shouldn't get a bot.
- **Live chat:** Lisa or the team reads the ManyChat Live Chat inbox once a day. Filter by `wants-call` and `kw-miracle` first. A short personal reply from Lisa to every `kw-miracle` person is the highest-converting move in this whole plan.

## 6. Test before the Nov 25 story

From a second Instagram account (not Lisa's):
1. **DM "money":** A1 should arrive, then A2 after you tap. Open the link, take the quiz with a test email, and check that Kit tagged it `quiz-lead`.
2. **Reply "MONEY" to a test story** (close friends only): the same flow should run.
3. **Comment "money" on a post:** you should get a public reply and a DM.
4. **Email path:** tap "Email it to me instead" (temporarily set A3's delay to 1 minute for the test), enter a test email, then check that Kit tags it `instagram-dm` and sends "Your scorecard".
5. **DM "miracle":** B1 should arrive, with the price that's correct for today.
6. **Clean up:** set A3's delay back to 22 hours, and delete the test subscribers in Kit.

## 7. Calendar

| Date | Change in ManyChat |
|---|---|
| Wed Nov 25 | Flows live before the first MONEY story |
| Fri Dec 4, morning | Swap B1 to the MIRACLE200 version |
| Mon Dec 14, 5:30 pm PT | Swap B1 to the waitlist version |

## 8. What to count

ManyChat shows, for each flow: runs, button clicks and link clicks. Each Friday, add these to the pace check in `PLAN.md`:
- MONEY runs
- scorecard clicks
- MIRACLE runs
- course clicks

Course visits from these flows carry `utm_medium=manychat`, so they show up wherever the other channels' UTMs are counted.
