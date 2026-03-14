# Toil and Automation in Site Reliability Engineering (SRE)

A Google SRE once said:

> "If a human operator needs to touch your system during normal operations, you have a bug. The definition of normal changes as your systems grow."

A key pillar of **Google's DevOps philosophy** is leveraging **tooling and automation**.  
This allows engineering teams to focus on **development work** instead of operational work.

SRE teams aim to eliminate operational work known as **toil**.

---

# What is Toil?

**Toil** is work directly tied to a service that is:

- Manual
- Repetitive
- Automatable
- Tactical
- Lacks enduring value
- Scales linearly as the service grows

Toil is **not simply administrative work** or work that people dislike. Administrative tasks such as meetings or HR paperwork can still be important but are **not tied to running a production service**.

By reducing toil, SREs can focus their time on:

- Reducing future toil
- Adding service features
- Improving reliability
- Improving performance
- Improving resource utilization

---

# Reliability vs Engineering in SRE

Earlier discussions focused on the **reliability** part of Site Reliability Engineering.

Reducing toil and scaling services represents the **engineering** part of SRE.

Engineering work allows SRE teams to:

- Scale services effectively
- Manage systems more efficiently
- Operate beyond the capability of traditional development or operations teams

To maintain this balance, SREs should spend **less than 50% of their time on toil**.

This distinction separates **SRE roles from traditional operations roles**.

---

# Why Toil is a Problem

Excessive toil can create several organizational issues.

## Career Stagnation
Team members may struggle to progress in their careers if they spend too little time on meaningful projects.

While undesirable work may sometimes be rewarded, **it cannot form the foundation of a long-term career**.

---

## Low Morale

Everyone has a limit for repetitive work.

Too much toil can lead to:

- Burnout
- Boredom
- Discontent

---

## Role Confusion

At Google, SRE is clearly defined as an **engineering organization**.

When SRE teams perform excessive operational toil, it confuses other teams about the true role of SRE.

---

## Slower Progress

Excessive manual work reduces productivity.

If SRE teams are busy reacting to operational tasks, **feature delivery slows down**.

---

## Setting Bad Precedents

If SRE teams accept too much operational toil:

- Developers may shift more operational responsibilities to SRE
- Other teams may begin to expect SREs to handle these tasks

This reinforces the problem.

---

## Team Attrition

Too much toil can push talented engineers to leave for more rewarding roles.

Highly skilled engineers typically seek **challenging and meaningful work**.

---

## Breach of Trust

New hires joining SRE expecting engineering project work may feel misled if they are assigned mostly operational toil.

This negatively impacts morale and trust within the team.

---

# Is Toil Always Bad?

Not necessarily.

A **small amount of toil can have benefits**, such as:

- Providing predictable tasks
- Delivering quick wins
- Creating a sense of accomplishment
- Offering low-risk activities

Some engineers even enjoy certain repetitive tasks.

However, **toil should never be the primary responsibility of an SRE**.

Toil becomes **toxic when experienced in large quantities**.

---

# Managing Toil

Toil must remain **a bounded part of the SRE role**.

If SREs spend all their time on operational work, they are essentially performing traditional **system administration tasks**, which DevOps aims to reduce.

A common guideline:

**Toil should not exceed 50% of an SRE’s time.**

The remaining time should be dedicated to **engineering projects**.

---

# Priorities for SRE Project Work

SRE project work should focus on:

1. Work that impacts or may impact the team's **Service Level Objectives (SLOs)**
2. Work that **reduces existing toil**

---

# Automation: The Key to Reducing Toil

A fundamental SRE principle is:

> **Automate this year's job away.**

This means continuously identifying:

- What tasks should be automated
- Under what conditions automation should occur
- How automation should be implemented

Automation provides several important benefits.

---

# Benefits of Automation

## Consistency

Humans are prone to errors, especially when performing repetitive tasks.

Automation ensures:

- Consistent execution
- Reduced mistakes
- Improved reliability
- Better data quality

---

## Platform Creation

Automation systems can evolve into **platforms** that support multiple services.

A centralized system allows bugs to be **fixed once in one location** instead of correcting them across multiple people or teams.

---

## Speed and Accuracy

Automated systems can:

- Execute tasks faster than humans
- Perform tasks with greater accuracy
- Export performance metrics easily

---

## Faster Problem Resolution

Automation that runs frequently can detect and resolve issues earlier.

This reduces:

- Time spent troubleshooting
- Cleanup work after failures

Early detection lowers the **overall cost of maintaining the system**.

---

## Faster Reaction Time

Machines react faster than humans.

For large-scale production systems, automation becomes **essential for survival**, as manual work quickly becomes unmanageable.

---

## Time Savings

Although automation requires an upfront investment in development time, once implemented:

- Ongoing training is minimized
- Tasks can be executed by anyone
- Processes become standardized

---

# Challenges with Automation Adoption

Organizations that do not commonly use automation may experience **resistance to change** when introducing SRE practices.

Teams may initially be hesitant to modify familiar workflows.

---

# Next Topic

The next topic explores **the psychology behind resistance to change** and how organizations can help teams successfully adopt **SRE practices**.
