# SRE Team Implementations

Once your organization has **established key SRE practices** and started hiring and training, you can consider **how to implement your SRE team**.  

Implementation will vary depending on your organization's size and where you are in your SRE journey.  

We've categorized recommended implementations into **six types**:

---

## 1. Kitchen Sink / Everything SRE

- **Scope:** Usually unbounded. Good for organizations with **few applications or user journeys**.  
- **Benefits:**  
  - No coverage gaps, as only one team is in place.  
  - Easy to spot patterns across services.  
  - Acts as glue between disparate developer teams.  
- **Disadvantages:**  
  - Risk of overloading the team due to lack of a defined charter.  
  - Shallow contributions as complexity grows.  
  - Issues can impact the entire business.

---

## 2. Infrastructure SRE

- **Focus:** Behind-the-scenes tasks to help other teams; maintaining **shared infrastructure services**.  
- **Recommended for:** Companies with **several development teams**.  
- **Benefits:**  
  - Product developers maintain user-facing products without divergence.  
  - SREs focus on **reliable infrastructure**.  
- **Disadvantages:**  
  - Issues can affect the whole business.  
  - Lack of direct customer contact may misalign improvements with user experience.  
  - Splitting infrastructure teams can lead to duplication and inefficiency.

---

## 3. Tools-Focused SRE

- **Focus:** Build software tools for **measuring, maintaining, and improving reliability**.  
- **Recommended for:** Organizations needing **specialized reliability tooling**.  
- **Disadvantages:**  
  - Risk of solving the wrong problems or drifting into infrastructure work.  
  - Can increase toil if not properly chartered.

---

## 4. Product / Application SRE

- **Focus:** Improve reliability of a **critical application or business area**.  
- **Recommended for:** Organizations with existing kitchen sink, infrastructure, or tools-focused SRE teams.  
- **Benefits:**  
  - Clear focus and direct alignment with business priorities.  
- **Disadvantages:**  
  - Growth requires new product teams.  
  - Risk of duplication of infrastructure or divergence of practices.

---

## 5. Embedded SRE

- **Focus:** SREs embedded **with developer teams**, usually project- or time-bound.  
- **Benefits:**  
  - Focused expertise applied to specific problems.  
  - Side-by-side demonstration of SRE practices.  
- **Disadvantages:**  
  - Can lead to **lack of standardization** across teams.  
  - Less opportunity for peer mentoring.

---

## 6. Consulting SRE

- **Focus:** Similar to embedded SREs, but **less hands-on**; typically **avoid changing code or configuration**.  
- **Recommended for:** Large organizations or when **existing SRE teams are overextended**.  
- **Benefits:**  
  - Supports scaling SRE impact indirectly.  
- **Disadvantages:**  
  - May lack sufficient context to advise effectively.  
  - Can be perceived as hands-off despite potential impact.

---

> **Key Consideration:**  
> Assess your organization’s maturity for SRE adoption and identify **training needs** before creating your first team.  

The next module covers **how Google can help your organization get started with SRE**.
