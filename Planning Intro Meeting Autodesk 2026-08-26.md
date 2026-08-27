---
categories:
  - "[[Areas]]"
domain: clients
created: 2026-08-26
project: null
attendees:
  - Mathias Tømmerbakk Schumacher
  - Thor Bossuyt
  - Hugo Bohlin Willfors
tags:
  - meeting
  - autodesk
---
# Planning — intro meeting @ Autodesk

**Date:** 2026-08-26
**Attendees:** Mathias Tømmerbakk Schumacher, Thor Bossuyt, Hugo Bohlin Willfors
**Source:** Teams transcript (AI-generated, Swedish)

## Summary

Kick-off/greet meeting for the Autodesk engagement. Thor pointed out a handover gap: there was a sales process where the engagement was discussed, Mathias wrote the proposal, but Thor and Hugo weren't part of those meetings and the engagement hasn't been fully aligned internally. Agreed to treat this meeting as the kick-off: recap the goal, what we're trying to achieve, and what Mathias is working on right now, then agree on what's most important next.

The bulk of the meeting (middle ~49 min not captured in transcript fragments) covered planning a **1-hour workshop** for Autodesk:

- The workshop will be a **live demo built from a written markdown file** with slides/steps (presented via Claude — no PowerPoint, no HTML).
- Demo idea: show how an agent can be **sandboxed with Docker** (e.g. Sandcastle, a Matt Pocock-style sandbox, or plain docker) so the agent can only write to the volume/folder it's given — and cannot do anything outside it.
- Mathias will focus on **permissions, auto mode, and branch protection**.
- Hugo will research the Docker-sandboxing angle separately and find a relevant blog post or example to borrow from, so Mathias can focus on the rest.
- Mathias sends the markdown presentation to Hugo for review tonight or early tomorrow; Hugo reviews before the workshop.

## Action items

- [ ] **Hugo** — Research Docker-based agent sandboxing (Sandcastle / Matt Pocock / plain docker); find a relevant blog post or example we can borrow for the workshop demo
- [ ] **Mathias** — Prepare the 1-hour workshop as a markdown file with slides/steps, live demo (no PPT/HTML); cover how to use Docker, permissions, auto mode, and branch protection
- [ ] **Mathias** — Send the markdown presentation to Hugo (tonight or early tomorrow) when ready or when input is wanted
- [ ] **Hugo** — Review Mathias's presentation file (early tomorrow morning or tonight) before the workshop
- [ ] **All** — Close the handover gap: recap engagement goal, what we're aiming for, and what's most important next; align on the proposal/sales-process context from before the engagement

## Raw transcript (as captured, partial)

> Note: the Teams transcript only captured fragments — the first ~1 min and the last ~3 min. The middle of the meeting is missing. AI-generated, may be inaccurate.

### 0:08 — 0:54 (opening)

**Thor:** OK exakt, men samtidigt blir det en liten greet. Hur går det inte att träffat henne? Jag har inte träffat henne. Vi på något sätt en handover från.

**Thor:** Det fanns en säljprocess där det pratades om måste vi börja deras, men jag och hugo. Vi var inte med i möten du var med och skrev proposal. Jag var med och läste proposedel efter det är det skrev vi. Det känns som att vi inte riktigt. Vi har inte snackat med guru om engagemanget, så att det kanske också är bra att se det som en meeting greet kick off och bara så här recappa. OK, men det här är målet, är vi överens om det? Där vill vi uppnå och det här jobbar Mathias på just nu.

**Thor:** Vad är viktigast härnäst? Sen är frågan om vi har tid att?

### 49:55 — 52:35 (workshop planning)

**Mathias:** Så är. Vår kanske det här blir lite sån där... och så tar vi deep day vid enon. Så som dockorna eller så här boxing, en aning där.

**Hugo:** Ja exakt det, det är svårt vad workshopen när man är jättelång bara.

**Mathias:** Nej, en timme.

**Hugo:** OK. Ja, då får vi se lite vad du hinner förbereda också. Jag tänker att ett jätte enkelt sätt att visa på typ hur man skulle kunna använda docker, det är att använda typ någonting som antingen sandcastle som mats pocock eller bara en vanlig docker. Och sen så här, jag tänker att det viktigaste där är väl bara så här. Ja, den kan bara skriva till de volymer som man har.

**Hugo:** Och den skulle ha kunnat göra någonting utanför det folder som det är i, liksom.

**Mathias:** Ja, där det. Docker, lägg en agent i gent sandboxing. Som gör exakt det här.

**Hugo:** Just det oj. Vi kan... ni har eller liksom boxar. Vad sjukt. Ja, just det, jag är intresserad av det här ändå, så jag kan göra lite research på det här också och se om jag kan hitta något relevant. En bloggpost eller någonting om det här, där vi bara skulle kunna sno något exempel. Om du vill?

**Mathias:** Ja, det hade varit perfekt, gärna det.

**Hugo:** Så hinner ju du fokusera på liksom hur man jobbar med permissions, så auto mode och sånt där, ja, branch protection.

**Hugo:** Kort, du får säga om du. Jag vet inte hur presenterar du det här? Brukar du skapa någon powerpoint eller gör du det bara liksom presentera det?

**Mathias:** Ja... skriven markdown fil med liksom slides och steps, och så ser jag att det är Claude, inte en HTML.

**Hugo:** OK bra, ja. Ja, båda... live. Vi behöver bara skriva markdown filer.

**Hugo:** OK ja men nice, men du kan väl bara skicka den när du är färdig eller när du vill ha input på någonting, så kan jag ju reviewa den innan. Ja, ant tidigt imorgon eller ikväll.

**Hugo:** Ha det bra, nice. OK, kriga på.

**Mathias:** Tack, nu ska vi snacka...

*Thor stopped transcription*
