# Slack Reminders for Assigned Reviewers with Pending Questionnaire Work

![rw-book-cover](https://linear.app/static/apple-touch-icon.png)

## Metadata
- Author: [[linear.app]]
- Full Title: Slack Reminders for Assigned Reviewers with Pending Questionnaire Work
- Category: #articles
- Summary: Legora team members assigned to review questionnaires will get Slack reminders if they have pending work. Reminders stop once the review starts or the questionnaire is fully approved. If Slack is unavailable, reminders are sent by email instead.
- URL: https://linear.app/ethira/issue/E-1458/slack-reminders-for-assigned-reviewers-with-pending-questionnaire-work

## Full Document
* 🙂 As a **Legora team member** assigned to review questions or answers in a questionnaire,
* 📦 I want to **receive a Slack reminder when I have pending questionnaire work that hasn't been acted on**,
* 🏆 So that **questionnaires don't stall because I missed the initial notification, and clients aren't left waiting.**

#### Context

The initial "answers ready" notification (​[⁠ E-1266 Slack Notification When AI-Generated Answers Are Ready for Review](https://linear.app/ethira/issue/E-1266/slack-notification-when-ai-generated-answers-are-ready-for-review)⁠) is a one-time DM when AI finishes generating answers. If the reviewer misses it or deprioritizes it, there is no follow-up. This ticket adds periodic Slack reminders for any assigned reviewer who has not yet started reviewing. This is an explicit requirement in the Trust Exchange scope document. This ticket depends on the fallback channel configuration being enforced (prerequisite ticket) so there is always a channel available for reminders when the questionnaire has no dedicated Slack channel.

* ❌ Sending reminders for questionnaires where no reviewer is assigned — only assigned reviewers are nudged.
* ❌ Configuring reminder frequency per user — start with a single workspace-level default cadence.
* ❌ Reminders after the questionnaire has been fully approved and published — reminders stop once the questionnaire is no longer pending review.
* ❌ Replacing the initial one-time notification (​[⁠ E-1266 Slack Notification When AI-Generated Answers Are Ready for Review](https://linear.app/ethira/issue/E-1266/slack-notification-when-ai-generated-answers-are-ready-for-review)⁠) — reminders are in addition to it, not instead of it.

#### Acceptance criteria

* ✅ Given a questionnaire has an assigned reviewer and answers are pending review; when a configured amount of time passes without any review action; then the reviewer receives a Slack DM reminding them they have pending work with a direct link to the questionnaire.
* ✅ Given the reviewer has started reviewing (at least one answer acted on); when the next reminder interval arrives; then no reminder is sent.
* ✅ Given the questionnaire is fully approved and published; when the next reminder interval arrives; then no reminder is sent.
* ✅ Given no reviewer is assigned to a questionnaire; when the reminder interval arrives; then no Slack message is sent.
* ✅ Given the workspace has no Slack integration; when a reminder would be due; then it falls back to an email reminder instead.
* ✅ Given a reviewer has multiple questionnaires pending; when a reminder is sent; then each pending questionnaire is listed in a single message rather than sending one message per questionnaire.
