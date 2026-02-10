# UX Research Best Practice: Designing Exercises for Participants

A curated repository of best practice from leading UXR authors and practitioners, with specific focus on exercise design and working with young people (13-25).

---

## Contents

1. [Key Authors & Their Contributions](#key-authors--their-contributions)
2. [Think-Aloud Protocols](#think-aloud-protocols)
3. [Task & Scenario Design](#task--scenario-design)
4. [Working with Young People](#working-with-young-people)
5. [Warm-Up & Rapport Building](#warm-up--rapport-building)
6. [Moderation Techniques](#moderation-techniques)
7. [Common Mistakes to Avoid](#common-mistakes-to-avoid)
8. [Remote Testing Considerations](#remote-testing-considerations)
9. [Post-Task & Debriefing](#post-task--debriefing)
10. [Supplementary Exercises](#supplementary-exercises)

---

## Key Authors & Their Contributions

### Steve Krug
**Key works:** *Don't Make Me Think*, *Rocket Surgery Made Easy*

Krug's philosophy centres on **simplicity and pragmatism**. His core contributions:
- Early and frequent testing beats elaborate one-off studies
- Test scripts should include: "We are testing our site, not you, so there is nothing wrong that you can do"
- Focus on finding the **most important problems** (no one has resources to fix them all)
- Free test scripts available: [sensible.com/downloads](https://sensible.com/download-files/)

### Jakob Nielsen (Nielsen Norman Group)
**Key works:** *Usability Engineering*, 10 Usability Heuristics

Nielsen's foundational principles:
- **5 users identify ~85% of usability problems** – many small tests beat few large ones
- Test with **representative customers using realistic tasks**
- Well-crafted scenarios provide just enough context without revealing solutions
- Task quality directly determines insight quality

> "Elaborate usability tests are a waste of resources. The best results come from testing no more than 5 users and running as many small tests as you can afford."
> — [NN/g](https://www.nngroup.com/articles/usability-101-introduction-to-usability/)

### Erika Hall
**Key work:** *Just Enough Research*

Hall's pragmatic approach:
- Four areas of context to understand about users before any design project
- Efficient, focused research that directly informs decisions
- Avoid research theatre – only gather data you'll actually use

> [Full interview with Erika Hall on better research and design](https://dscout.com/people-nerds/erika-hall-better-research-and-design)

---

## Think-Aloud Protocols

### What It Is
Participants verbalise their thoughts while performing tasks—what they're looking at, thinking, doing, and feeling. Nielsen calls this "the #1 usability tool."

> [Thinking Aloud: The #1 Usability Tool - NN/g](https://www.nngroup.com/articles/thinking-aloud-the-1-usability-tool/)

### Two Approaches

| Aspect | Concurrent Think-Aloud (CTA) | Retrospective Think-Aloud (RTA) |
|--------|------------------------------|----------------------------------|
| **When** | During task performance | After task completion (often with video playback) |
| **Pros** | Real-time reactions; detects navigation issues, graphics problems, error message confusion | No interference with natural behaviour; more explanations and design recommendations |
| **Cons** | May alter behaviour; cognitive load on participant | Memory decay; requires recording setup |
| **Best for** | System redesign focus; live problem identification | Expert users; eye-tracking studies; detailed reflection |

> [Concurrent vs Retrospective Think-Aloud Comparison](https://medium.com/@cheeweiyan/retrospective-vs-concurrent-think-aloud-4e44e5d60143)

### Practical Tips for Think-Aloud

1. **Warm participants up** with a simple practice task (e.g., "describe putting staples in a stapler while you do it" – Ericsson & Simon)
2. **Prompt gently** when they fall silent: "What are you thinking?" or "Keep talking"
3. **Minimise moderator interaction** in classic protocol – only remind to keep talking
4. **Use the echo technique**: repeat their last phrase with slight interrogatory tone to encourage elaboration without leading
5. **Accept imperfection**: most people self-edit; your job is to get as close to raw stream of thought as possible

> [Lyssna Think-Aloud Protocol Guide](https://www.lyssna.com/guides/think-aloud-protocol/)

---

## Task & Scenario Design

### Core Principles

**1. Goal-oriented, not step-oriented**
Transform research questions into realistic actions participants would actually perform.

❌ "Click on Benefits in the main menu"
✅ "Find information about what's included in the employee package"

**2. Avoid UI terminology**
Never use words that appear in the interface—this biases behaviour.

❌ "Sign up for the weekly newsletter"
✅ "Find a way to get information on upcoming events sent to your email regularly"

**3. Provide context, not instructions**
Scenarios should feel like real situations, not test questions.

❌ "Use the search function to find savings accounts"
✅ "You've just received a bonus and want to start saving for a holiday. What would you do?"

**4. If it takes a story to explain, it's not realistic**
Complex backstories signal the task may not reflect genuine user goals.

> [NN/g: Turn User Goals into Task Scenarios](https://www.nngroup.com/articles/task-scenarios-usability-testing/)

### The "Goldilocks" Balance

| Too Vague | Just Right | Too Prescriptive |
|-----------|------------|------------------|
| "Explore the app" | "You want to learn about budgeting basics. Find a lesson that interests you and complete it." | "Tap the home button, select Level 1, tap Lesson 3, answer the questions" |

### Task Writing Checklist

- [ ] Describes a **goal**, not steps
- [ ] **Avoids UI language** (button names, menu labels)
- [ ] Includes **enough context** to feel realistic
- [ ] **Doesn't reveal the solution** path
- [ ] Is **achievable** within session time
- [ ] Reflects **actual user motivations**

> [dscout: How to Write More Effective Usability Testing Tasks](https://dscout.com/people-nerds/usability-task-writing)

---

## Working with Young People

### Age Band Considerations

| Age | Key Characteristics | Session Implications |
|-----|---------------------|---------------------|
| **13-15** | Need strong scaffolding; still developing research abilities; may copy task wording into searches | Shorter tasks; clearer instructions; more check-ins |
| **16-18** | Higher scepticism; real-money relevance emerging; peer influence strong | Avoid condescension; acknowledge their expertise in their world |
| **18-25** | Some to full independence; varied financial experience | Can handle complexity; treat as adult participants |

### Critical Success Factors

**1. Never condescend**
> "Nothing turns off teenagers more than someone speaking to them condescendingly. The same rule applies as in research generally: you're the apprentice and they're the master."
> — [Blink UX](https://blinkux.com/ideas/ux-research-for-kids-and-teens)

**2. Session length matters**
- **90 minutes** works well for teens (accounts for more device switching, higher complexity, chatty participants)
- Build in **buffer time** for tech issues and tangents
- Expect **distraction** – plan shorter task blocks

**3. Attention span realities**
- Gen Z average attention span: **8 seconds** (vs 12 for millennials)
- Meta research: under-25s switch focus every **39 seconds**
- TikTok videos under 15 seconds have **80% completion**; over 30 seconds see significant drop

**Implication**: Design exercises with quick wins and visible progress. Long, complex tasks will lose them.

> [NN/g: Usability Testing with Minors - 16 Tips](https://www.nngroup.com/articles/usability-testing-minors/)

### Recruitment & Consent

- **Parental/guardian consent required** for under-18s
- Social media ads effective for reaching teens "where they are"
- **Pre-call day before** helps build comfort and troubleshoot tech

> [AnswerLab: Conducting UX Research with Teens](https://www.answerlab.com/insights/teen-ux-research)

### Warm-Up for Young People

Warm-ups are **especially critical** for teens:
- Ease into questions; let them talk about their favourite things first
- Find a **relatable moment** or small bonding point
- Don't just say "okay, cool" – engage briefly in conversation

Example openers:
- "What apps have you been using a lot lately?"
- "What do you usually do when you're bored on your phone?"
- "Who do you follow that's good at explaining things?"

---

## Warm-Up & Rapport Building

### Why It Matters
> "Sessions without a warm-up are good but never great."

Use the **first 5-7 minutes** to build connection before any research questions.

### Structure

```
Introduction (2 min)
├── Thank them for participating
├── Explain what will happen (and won't)
├── Emphasise: testing the product, not them
└── Ask permission to record

Warm-up Questions (5-7 min)
├── Easy personal questions
├── Find connection points
└── Get them comfortable talking

Transition to Tasks
└── "Great, now I'd like to see how you use..."
```

### Effective Warm-Up Questions

**Universal openers:**
- "Tell me a bit about yourself"
- "What do you like to do in your spare time?"

**Context-relevant (for Money Monsters):**
- "How do you usually learn new things – videos, apps, asking people?"
- "Have you ever tried any apps like Duolingo or similar?"
- "What's something you've been trying to get better at recently?"

**For teens specifically:**
- "What's the last thing you watched/played that you'd actually recommend?"
- "If you had to teach a friend something, how would you do it?"

### Pre-Session Rapport

**Day before:** Quick phone/video call to:
- Introduce yourself
- Review logistics
- Build initial comfort
- Troubleshoot tech requirements

> [dscout: The Interview Balancing Act](https://www.dscout.com/people-nerds/interview-balancing)

---

## Moderation Techniques

### The Golden Rule
**You are the apprentice; they are the master.** Your job is to learn from them, not guide them.

### During Tasks

| Do | Don't |
|----|----|
| Use open-ended prompts: "What are you thinking?" | Ask leading questions: "Is that button confusing?" |
| Echo their words: "You said 'weird'—what did you mean?" | Interpret their behaviour: "So you found that frustrating" |
| Note **facts and observations** | Record your **assumptions** |
| Stay neutral in body language | Nod/smile when they're going wrong (gives false encouragement) |
| Let silence happen | Rush to fill pauses |

### Useful Prompts

**When they're stuck:**
- "What would you normally do here?"
- "What are you looking for?"
- "What did you expect to happen?"

**When they succeed too quickly:**
- "Walk me through what you just did"
- "What made you choose that option?"

**When they're silent:**
- "Keep talking, please"
- "What's going through your mind?"

**At natural breakpoints:**
- "On a scale of 1-5, how easy was that?"
- "Anything surprise you there?"

### Note-Taking

- **Have a dedicated observer/note-taker** – moderating and note-taking simultaneously is nearly impossible
- **Record observations, not interpretations** (participant frowned ≠ participant disliked)
- **Debrief immediately** after each session with note-taker

> [NN/g: Talking with Users in a Usability Test](https://www.nngroup.com/articles/talking-to-users/)

---

## Common Mistakes to Avoid

### Facilitation Errors

| Mistake | Why It Happens | Fix |
|---------|---------------|-----|
| **Leading questions** | Hypothesis confirmation; wanting to help | Pre-write questions; use "what" not "do you think" |
| **Helping when stuck** | Discomfort watching struggle | Embrace productive struggle; redirect with questions |
| **Excessive encouragement** | Social nicety | Neutral responses: "Thank you" vs "Great job!" |
| **Filling silence** | Awkwardness | Wait 5-7 seconds before prompting |
| **Interpreting behaviour** | Pattern-matching from experience | Record facts; interpret in analysis |

### Task Design Errors

| Mistake | Example | Fix |
|---------|---------|-----|
| **Using UI terminology** | "Tap the Settings icon" | "Change your preferences" |
| **Being too specific** | "Find the Level 2 Budget lesson" | "Find something that would help you manage money better" |
| **Being too vague** | "Explore the app" | "You want to learn about saving—find somewhere to start" |
| **Unrealistic scenarios** | Complex backstory | Simple, relatable situations |

### Bias Traps

1. **Confirmation bias**: Seeing what you expect to see
2. **Anchoring**: First impression colours everything
3. **Social desirability**: Participants saying what they think you want
4. **Observer effect**: Behaviour changes because they're watched

**Mitigation:**
- Debrief after each session
- Have multiple observers
- Look for disconfirming evidence in analysis
- Triangulate with other data sources

> [MeasuringU: 9 Biases in Usability Testing](https://measuringu.com/ut-bias/)

---

## Remote Testing Considerations

### Technology Setup

**Pre-session (day before):**
- 15-minute tech check with participant
- Verify screen share works
- Test audio quality
- Send clear written instructions

**During session:**
- Start meeting before participant arrives
- All observers join with video/audio muted
- Have backup communication channel (phone number)
- Build 10-15 min buffer for troubleshooting

### Task Delivery

- **Send task text via chat** (not just spoken)
- Ask participant to **read aloud** before starting
- Use numbered tasks for easy reference

### Remote-Specific Challenges

| Challenge | Solution |
|-----------|----------|
| Harder to read body language | Ask more check-in questions |
| Tech failures mid-session | Have backup plan; don't panic |
| Participant distraction | Keep tasks shorter; more varied |
| Screen share lag | Build in pauses; don't rush |

### Tool Selection

Choose tools that:
- Are easy for participants to install
- Work across operating systems
- Have reliable screen share + audio
- Allow recording

Common choices: Zoom, Lookback, UserTesting

> [NN/g: Remote Moderated Usability Tests](https://www.nngroup.com/articles/moderated-remote-usability-test/)

---

## Post-Task & Debriefing

### Post-Task Questions (After Each Task)

**Single Ease Question (SEQ):**
> "Overall, how easy or difficult was this task?"
> (7-point scale: Very Difficult to Very Easy)

Simple, quick, captures immediate perception. Compare across tasks to identify problem areas.

**Follow-up probes:**
- "What was the hardest part?"
- "Was there anything unexpected?"
- "What would you do differently?"

### Post-Test Questionnaire

**System Usability Scale (SUS):**
- 10 Likert-scale questions
- Produces score 0-100
- Industry standard; allows benchmarking
- Administer **immediately** after session ends

> [MeasuringU: Measuring Usability with the SUS](https://measuringu.com/sus/)

### Debriefing Structure (5-10 min)

```
Overall Impressions
├── "What stood out to you most?"
├── "How would you describe this to a friend?"
└── "What would make you want to use this again?"

Targeted Follow-Up
├── Revisit any notable moments
├── Clarify ambiguous behaviours
└── Explore unvoiced reactions

Closing
├── "Anything else you'd like to share?"
├── Thank them
└── Explain what happens next
```

### For Young People

- Keep questionnaires **short**
- Consider **verbal administration** of SUS (reading 10 questions feels like a test)
- Allow **informal closing chat** – good insights often come when "the session is over"

---

## Supplementary Exercises

Beyond think-aloud tasks, consider these for variety and depth:

### Card Sorting

**What:** Participants organise labelled cards into groups that make sense to them

**When to use:**
- Understanding mental models
- Testing navigation/IA assumptions
- Early in design process

**Types:**
- **Open**: Participants create their own categories
- **Closed**: Pre-defined categories provided
- **Hybrid**: Mix of both

**Watch out:** Engagement drops after ~40 cards

> [NN/g: Card Sorting](https://www.nngroup.com/articles/card-sorting-definition/)

### First Click Testing

**What:** Where do participants click first when given a task?

**When to use:**
- Testing navigation clarity
- Validating design assumptions
- Quick quantitative signal

### 5-Second Test

**What:** Show interface for 5 seconds, ask what they remember

**When to use:**
- Testing first impressions
- Value proposition clarity
- Visual hierarchy effectiveness

**Especially useful for:** Landing pages, onboarding screens

### Comparison/Preference Testing

**What:** Show multiple design options, ask for preferences and reasoning

**When to use:**
- Choosing between design directions
- Understanding what drives appeal
- When you have genuine design alternatives

**For Money Monsters:** Consider showing competitor examples and asking what appeals/doesn't

---

## Quick Reference: Session Flow

```
Before Session
├── Tech check (day before)
├── Review tasks and script
└── Brief observers

Session Start (5-7 min)
├── Welcome and thank
├── Explain format
├── Consent and recording
└── Warm-up questions

Core Tasks (40-50 min)
├── Task 1 → Post-task question
├── Task 2 → Post-task question
├── [...]
└── Think-aloud throughout

Debrief (5-10 min)
├── Overall impressions
├── Follow-up on notable moments
├── Closing questions
└── Administer SUS

After Session
├── Immediate observer debrief
├── Note outstanding questions
└── Prep for next session
```

---

## Key Sources & Further Reading

### Books
- Krug, S. *Don't Make Me Think* (3rd ed.)
- Krug, S. *Rocket Surgery Made Easy* — [Free test scripts](https://sensible.com/download-files/)
- Hall, E. *Just Enough Research*
- Nielsen, J. *Usability Engineering*

### Essential Articles
- [NN/g: Turn User Goals into Task Scenarios](https://www.nngroup.com/articles/task-scenarios-usability-testing/)
- [NN/g: Write Better Qualitative Usability Tasks](https://www.nngroup.com/articles/better-usability-tasks/)
- [NN/g: Thinking Aloud - The #1 Usability Tool](https://www.nngroup.com/articles/thinking-aloud-the-1-usability-tool/)
- [NN/g: Usability Testing with Minors](https://www.nngroup.com/articles/usability-testing-minors/)
- [NN/g: Talking with Users in a Usability Test](https://www.nngroup.com/articles/talking-to-users/)
- [dscout: How to Write More Effective Usability Testing Tasks](https://dscout.com/people-nerds/usability-task-writing)
- [MeasuringU: Seven Tips for Writing Usability Task Scenarios](https://measuringu.com/task-tips/)

### Working with Young People
- [AnswerLab: Conducting UX Research with Teens](https://www.answerlab.com/insights/teen-ux-research)
- [Blink UX: Conducting UX Research with Kids and Teens](https://blinkux.com/ideas/ux-research-for-kids-and-teens)
- [NN/g: Teenager's UX: Designing for Teens](https://www.nngroup.com/articles/usability-of-websites-for-teenagers/)

### Measurement
- [MeasuringU: Measuring Usability with the SUS](https://measuringu.com/sus/)
- [NN/g: Measuring Perceived Usability](https://www.nngroup.com/articles/measuring-perceived-usability/)

---

*Compiled for Money Monsters User Testing, February 2026*
