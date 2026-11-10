# Masterclass funnel: Opening the Flow of Money

Three connected assets with one goal: free registrations for Lisa's live masterclass, which leads into Money Wealth and Miracles.

| Asset | File | URL on the site |
|---|---|---|
| Landing page | `masterclass/index.html` | `/masterclass/` |
| Confirmation page | `masterclass/thank-you/index.html` | `/masterclass/thank-you/` |
| Email invite #1 (Kit HTML) | `email/invite-1.html` | paste into Kit |
| Email invite #1 (plain text) | `email/invite-1.txt` | paste into Kit |
| Shared event settings | `masterclass/event.js` | used by both pages |

## Setup before launch

1. **Event settings** (`masterclass/event.js`): set `start` and `end` as Pacific time with the offset (for example `2026-12-02T17:30:00-08:00`). Both pages then fill in the date, start the countdown and switch on the calendar buttons. Until then the copy shows `[DATE]`, `[START]` and `[END]`.
2. **Registration:** create a Kit form (first name and email), set its redirect to `/masterclass/thank-you/`, and put its subscription URL in `registerUrl`. Until that is set, the form runs in preview mode and goes straight to the thank-you page without sending anything.
3. **Zoom:** put the Zoom link in `zoomUrl` so it goes into the calendar invites. The link itself reaches people through your Kit confirmation email.
4. **Money-stop tags:** create four small Kit forms, each set to add one tag (never-enough, undercharge, avoid-looking, in-and-out), and put their form IDs in `tagForms`. The thank-you page sends the registrant's email to the form for the answer they tap. Test one end to end in Kit before launch.
5. **Email:** upload `email/logo-email.png` to Kit and use its URL for `[LOGO URL]`. Replace `[DATE]`, `[START]`, `[END]` and `[REGISTER LINK]` (the landing page URL). Kit adds the required unsubscribe and address footer to broadcasts.
6. **Welcome video** (optional): swap the placeholder on the thank-you page for the embed once Lisa records it.

## Things to confirm with Lisa

- **Replay:** the FAQ answer encourages people to come live and makes no promise either way. Update it once the replay policy is decided.
- **Gas-tank opener:** written in Lisa's voice from the brief. She should read it and make it hers.
- **Testimonials:** used exactly as supplied. Nicole's second point is paraphrased outside the quote marks, because it was given as a summary rather than her words. The income disclaimer sits under both income cards and in the footer.

## Final copy

### Landing page

**Hero**
- Eyebrow: FREE LIVE MASTERCLASS
- Headline: Money is still flowing, even now. Let it flow to you.
- Subhead: The economy isn't what limits your income. Your relationship with money is, and the hidden stops inside it. In 90 minutes, find your stops and set a new money set point.
- Title: Opening the Flow of Money: Letting Go of Your Stops
- Details: [DATE] · [START] to [END] PT · Live on Zoom
- Form: First name, Email, button "Save my free seat"
- Under the button: Free. 90 minutes. Your Zoom link arrives by email.
- Countdown: Class starts in (days, hours, minutes, seconds)
- Photo caption: Your host, Lisa Kalmin. Transformational Mindset Wizard

**Problem**
- Eyebrow: Does this sound familiar?
- Headline: You work hard, and money still feels harder than it should.
- 01: Money is on your mind all the time, and it feels like stress, not support.
- 02: You know what your work is worth, and you still charge less.
- 03: Money comes in, and then it goes right back out.
- Bridge: None of this means something is wrong with you. It means there is a stop, a place where your money story quietly says "this far and no further." Stops can be found, and they can be let go.

**Outcomes**
- Headline: In 90 minutes, you'll:
- Find your hidden money stops, and where they started.
- See money as energy you can attract, not just numbers you chase.
- Set a new income set point that doesn't depend on the news.
- Leave with 4 actions you can take the same day.
- Button: Save my free seat. Beside it: Free, live on Zoom. [DATE].

**Proof**
- Large quote: "Lisa is one of the most effective people I know at coaching." Nicole Kalil, Founder and CEO, WomanWhisperer. Line under it: Nicole says Lisa's trainings changed the trajectory of her life.
- Card: $25,000+. Generated on top of her normal income, before the program had even ended. Megan Caldera, Head of Design, Level 3 Design Group. Results vary. Individual experiences are not a promise of income.
- Card: $12M. After joining Money Wealth and Miracles, closed a $12M deal, and two more just under $1M. K.Y. Results vary. Individual experiences are not a promise of income.
- Card: "Life-changing." That is how Kris described the class. Kris C.
- Button: Save my free seat

**About Lisa**
- Headline: Meet Lisa Kalmin.
- Lisa Kalmin is a transformational mindset coach, the Transformational Mindset Wizard, who helps people change their relationship with money from the inside out.
- For 26 years she has helped people see the problem differently, so they can finally act differently. More than 30,000 people have trained with her.
- She is the author of The Problem Is How You See the Problem. This class puts that idea to work on your money.
- Credentials: 26 years of experience · 30,000+ people trained · Author

**Is this for you?**
- For you if: you run a business, coach, consult or work as a professional, and money feels tight or stressful · you earn less than you believe you are worth · money comes in, then goes right back out · you are open to seeing money as energy, not just math.
- Not for you if: you want stock tips or a get-rich-quick system · you are looking for budgeting software, tax or investment advice · you would rather not look honestly at your own money story.

**FAQ**
- Is it really free? Yes. The masterclass is free, and there is nothing to buy to attend. At the end of class, Lisa shares how you can keep going with her if you want to. That part is completely optional.
- Will there be a replay? Plan to be there live if you can. The shifts happen while you do the exercises with Lisa in real time, and you can ask her your questions directly.
- I've attended before. Should I come again? Yes. Every class uncovers new layers. The stop you meet this time may not be the one you met last time, and a new set point is worth setting more than once.
- What happens after I register? You'll go straight to a confirmation page, and your Zoom link will arrive by email. Add the class to your calendar, and bring a journal and a pen.

**Final CTA**
- Headline: Your new set point starts here.
- [DATE] · [START] to [END] PT · Live on Zoom
- Button: Save my free seat. Sign-off: To your abundant flow! Lisa

### Confirmation page

- Headline: You're in! Your seat is saved.
- Sub: Thank you, {first name}. I can't wait to open the flow of money with you.
- Card: Opening the Flow of Money: Letting Go of Your Stops · [DATE] · [START] to [END] PT · Live on Zoom
- Note: Your link is in your inbox. If you don't see it in a few minutes, check your promotions or spam folder.
- Buttons: Add to Google Calendar · Add to Apple / Outlook
- Steps: 1) Check your inbox: find the email with your Zoom link and save it, or star it. 2) Add it to your calendar: use the buttons above so the time is blocked and you get a reminder. 3) Grab a journal: bring a journal and a pen. You'll want to write down what comes up.
- Question: Which money stop sounds most like you? Tap one. It helps me shape the class around the people in the room.
- Answers and replies:
  - There's never quite enough. → "Never quite enough" is one of the most common stops, and we'll find where it started.
  - I undercharge or give it away. → The pause before you name your price is exactly where we'll look.
  - Money feels stressful, so I avoid looking. → Avoiding is how a lot of us cope with money stress, and in class we'll make looking feel safe.
  - Money comes in, then goes right back out. → There's a set point at work, and we'll reset it together.
- Video: A welcome from Lisa. Sixty seconds before we meet.
- Bottom: Want to go deeper? At the end of class, I'll share how you can keep going with me. To your abundant flow! Lisa

### Email

See `email/invite-1.txt` for the full copy, subject lines and preview text.

## Why each design choice helps conversion

**Landing page**
- **No menu, one action.** The logo isn't a link and there is no navigation, so the only thing to do is register. Every button scrolls to the same form and puts the cursor in the first-name field.
- **Form in the first screen.** On desktop the form sits beside the headline. On a phone it starts within the first screen, and the button follows within one scroll. Two fields only, because each extra field costs sign-ups.
- **The headline answers the objection first.** "Money is still flowing, even now" meets the economy worry before the visitor raises it. The subhead turns it into Lisa's promise.
- **A doorway of daylight behind Lisa.** Her photo sits in an arched door with a warm glow, carrying the door motif from the homepage and making a free class with a stranger feel personal and safe.
- **An honest countdown.** It counts to the real start time and disappears when class begins. No fake timers or "only 3 seats left."
- **Naming the feeling before the fix.** The problem section uses the visitor's own words (stress, undercharging, money in and out) and reframes it as a stop rather than a flaw, which lowers shame and raises hope.
- **Proof right after the promise.** Nicole's quote is set large on dark green for contrast, and the income results lead with the number. Disclaimers sit under each income claim, so the results read as credible rather than hype.
- **"Not for you if" builds trust.** Excluding stock-tip seekers makes the right people feel the class is truly for them.
- **The FAQ handles the last doubts:** "is it really free" and "I've been before" are the two that most often stop a click.
- **Button repeated 4 times,** plus a pinned button on phones once the form scrolls away.
- **Fast and readable.** No 3D scene or framework, one preloaded hero image, lazy images below the fold, and text contrast above WCAG AA (rose on oat about 5.6:1, white on rose about 5.9:1).

**Confirmation page**
- **The seat feels real.** A big check mark, their first name and the class details confirm the yes and reduce no-shows.
- **Calendar buttons first.** A blocked calendar slot is the strongest predictor of showing up. The .ics file adds a 30-minute reminder.
- **One-tap question.** It's easy to answer and it segments the list in Kit, so Lisa can follow up with the stop each person named. The reply makes them feel heard straight away.
- **A soft bridge to the paid program.** One sentence plants the idea of going deeper without selling before class.

**Email**
- **Live text and simple blocks.** It reads fully with images off, keeps Outlook buttons rounded through VML, and stacks on phones.
- **A personal opening.** The gas-tank line is relatable before any pitch, and the event card with its button lands inside the first screen.
- **Three identical buttons.** In the event card, after the proof, and in the P.S., which is often the most-read part of an email. The P.S. speaks to past attendees, who are the warmest audience.
- **Two subject lines to A/B test.** A is curiosity ("Is it flowing to you?"); B is specific ("hidden stops," "free class").
