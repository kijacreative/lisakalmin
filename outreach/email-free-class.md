# Free masterclass, Thursday December 3: emails (Series 4)

**The class:** Opening the Flow of Money: Letting Go of Your Stops. Thursday, December 3, 5:30 to 7:00 pm PT, live on Zoom, free. Registration page: `https://www.lisakalmin.com/masterclass/`.
**Goal:** fill the class from the main list (and the Meta ads in `meta-ads.md`, section 5c), then sell Money Wealth and Miracles to everyone who registers. Every email after sign-up points to the course, and the class ends with the $597 attendee price (MIRACLE200).

The finished emails are in `outreach/emails/4-free-class-dec3/` (Kit HTML and plain text). The copy lives in `outreach/emails/build.py`; edit it there and run `python3 outreach/emails/build.py`.

## Kit setup (before the first invite on Fri Nov 27)

1. **Tag:** create `masterclass-dec3`.
2. **Form 10243223** (uid `0ce5f9fb73`) is the new form on `/masterclass/`, separate from the Nov 19 form (10115136). In Kit:
   - **Tag:** Automations > Rules: subscribes to form 10243223 > add tag `masterclass-dec3`. Make sure this form doesn't also add `masterclass-nov19`.
   - **Redirect:** in the form's settings, set "after subscribing" to `https://www.lisakalmin.com/masterclass/thank-you/`. The page normally sends people there itself; Kit's redirect is the fallback if that fails.
   - **Incentive email:** if the form has double opt-in on, turn it off, or people won't be subscribed (or tagged) until they click a confirm link.
3. **Confirmation email:** make `reg-0.html` the first email for this form (a one-email sequence or automation on the `masterclass-dec3` tag, sent right away). The old `email/confirmation.html` still has the Nov 19 date and Zoom link.
4. **Zoom:** create the Dec 3 meeting. Put its link in `reg-0`, `reg-1` and `reg-2` (`[ZOOM LINK]`), and in `masterclass/event.js` (`zoomUrl`) so the calendar buttons carry it.
5. **MIRACLE200:** set the code's start in Kit to **Thursday, December 3 at 5:30 pm PT** (it was Dec 4, 12:00 am), so Lisa can share it at the end of class. The course page already shows $597 from that moment.
6. **After class:** tag live attendees `masterclass-dec3-attended` from Zoom's attendance report, before `reg-3` goes out at 7:15 pm. Add the replay link to `reg-3` and `reg-4` (`[REPLAY LINK]`).

## Schedule

| Email | Send | To | Subject A |
|---|---|---|---|
| `inv-1` | Fri Nov 27, 10:00 am PT | Main list, not registered | You're invited: a free evening with me |
| `inv-2` | Mon Nov 30, 9:00 am PT | Main list, not registered | "There's never quite enough" |
| `main-1` | Tue Dec 1, 9:00 am PT | Main list (Series 2; its P.S. now invites to the class) | The money story you didn't choose |
| `inv-3` | Wed Dec 2, 9:00 am PT | Main list, not registered | Tomorrow night, 5:30 pm PT |
| `inv-4` | Thu Dec 3, 2:00 pm PT | Main list, not registered | Today at 5:30 pm PT |
| `reg-0` | Right away on sign-up | Registrants | You're in! Your Zoom link for Thursday |
| `reg-1` | Wed Dec 2, 9:00 am PT | `masterclass-dec3` | Tomorrow: what to bring |
| `reg-2` | Thu Dec 3, 4:30 pm PT | `masterclass-dec3` | We start in one hour |
| `reg-3` | Thu Dec 3, 7:15 pm PT | `masterclass-dec3` (attended and missed versions in one email) | Your attendee price (and the replay) |
| `reg-4` | Sat Dec 5, 10:00 am PT | `masterclass-dec3` | What happens after you find the stop |
| `mc-5` to `mc-7` | Dec 8, 11 and 14 | `masterclass-nov19` **or** `masterclass-dec3` (Series 1) | Bring a pal… / Before the weekend… / Tonight |

"Main list, not registered" means the Series 2 audience (full list, excluding `masterclass-nov19`, `mwm-buyer` and new quiz leads), also excluding `masterclass-dec3` at send time.

**Changes to the other series:**
- **Series 2 `main-2`** (the Megan testimonial) moves from Thu Dec 3 to **Sat Dec 5, 10:00 am PT**, so the list doesn't get a course email on class day.
- **Series 2 from `main-2` on** excludes `masterclass-dec3`: registrants get Series 4 and then Series 1 instead.
- **Series 1 `mc-5` to `mc-7`** also go to `masterclass-dec3`, without `mwm-buyer`.

## How sign-up promotes the course

- **Thank-you page** (`/masterclass/thank-you/`): the course card with the $597 attendee price "for live attendees", shared at the end of class.
- **`reg-0`:** after the Zoom link and calendar buttons, a short section on the course, "stay to the end" for the $200 attendee price, and a course card.
- **`reg-1`:** what to bring, Megan's quote, and a heads-up about the thank-you price.
- **`reg-3` and `reg-4`:** the MIRACLE200 card, $597 through Dec 14 at 5:30 pm PT.
- **The site pop-up** invites visitors to the class until it starts. Registrants don't see it again.
