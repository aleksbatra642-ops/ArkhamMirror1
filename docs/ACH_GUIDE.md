# 🕵️ Analysis of Competing Hypotheses (ACH)

<p align="center">
  <img src="assets/images/ACH_1.png" alt="ACH Step 1 - Hypotheses" width="800">
</p>

> **"The hypothesis with the most evidence is not necessarily correct. The hypothesis with the least contradictions often is."**
> — *Richards Heuer, CIA Analyst*

**Analysis of Competing Hypotheses** is a rigorous analytic technique developed by the U.S. Intelligence Community to overcome cognitive biases that plague human decision-making. ArkhamMirror brings this powerful methodology to investigative journalists, researchers, and analysts with a modern, interactive implementation.

---

## 📑 Table of Contents

1. [Why ACH?](#-why-ach)
2. [Feature Highlights](#-feature-highlights)
3. [Keyboard Shortcuts](#-keyboard-shortcuts)
4. [The 8-Step Process](#-the-8-step-process)
   - [Step 1: Brainstorm Hypotheses](#step-1-brainstorm-hypotheses)
   - [Step 2: Gather Evidence](#step-2-gather-evidence)
   - [Step 3: Create the Matrix](#step-3-create-the-matrix)
   - [Step 4: Refine the Matrix](#step-4-refine-the-matrix-diagnosticity)
   - [Step 5: Draw Conclusions](#step-5-draw-conclusions)
   - [Step 6: Analyze Consistency](#step-6-analyze-consistency)
   - [Step 7: Sensitivity Analysis](#step-7-sensitivity-analysis)
   - [Step 8: Milestones & Export](#step-8-milestones--export)
5. [Methodology Deep Dive](#-methodology-deep-dive)
6. [Tips for Best Results](#-tips-for-best-results)

---

## 🧠 Why ACH?

Traditional analysis is vulnerable to **confirmation bias** — the tendency to seek out and remember information that supports what we already believe. We build narratives around the first plausible explanation and unconsciously filter out contradictory evidence.

ACH flips the script:

| Traditional Analysis | ACH Approach |
|:---|:---|
| ❌ "What evidence supports my theory?" | ✅ "What evidence **contradicts** each theory?" |
| ❌ Stops at the first plausible explanation | ✅ Systematically tests **all** explanations |
| ❌ Confirmation bias goes unnoticed | ✅ Bias made **visible** in the matrix |
| ❌ Conclusions are hard to defend | ✅ Conclusions are **auditable and transparent** |

---

## ✨ Feature Highlights

ArkhamMirror's ACH implementation goes beyond the classic paper-based method:

| Feature | Description |
|:---|:---|
| 🤖 **AI Assistance** | Generate hypotheses, find evidence, get rating suggestions, and challenge your thinking with Devil's Advocate mode |
| 📂 **Corpus Integration** | Import evidence directly from your uploaded documents with source links |
| 📊 **Auto-Scoring** | Real-time inconsistency scores and hypothesis rankings |
| 🔬 **Sensitivity Analysis** | "What if" scenarios to test how robust your conclusions are |
| 📄 **Professional Export** | PDF, Markdown, and JSON exports with AI disclosure flags |
| 📜 **Milestones & Indicators** | Track decision points and future indicators to watch |

---

## ⌨️ Keyboard Shortcuts

Speed through your analysis with these shortcuts (active on the Matrix step):

| Key | Action |
|:---:|:---|
| <kbd>↑</kbd> <kbd>↓</kbd> <kbd>←</kbd> <kbd>→</kbd> | Navigate between cells |
| <kbd>Tab</kbd> | Move to next cell |
| <kbd>1</kbd> | **Very Consistent** (CC) |
| <kbd>2</kbd> | **Consistent** (C) |
| <kbd>3</kbd> | **Neutral** (N) |
| <kbd>4</kbd> | **Inconsistent** (I) |
| <kbd>5</kbd> | **Very Inconsistent** (II) |
| <kbd>Ctrl</kbd>+<kbd>K</kbd> | Open Global Search |
| <kbd>Esc</kbd> | Deselect / Close dialogs |

---

## 📋 The 8-Step Process

ArkhamMirror guides you through the complete ACH methodology with an interactive step-by-step wizard. Each step builds on the previous one, creating a rigorous analytical framework.

---

### Step 1: Brainstorm Hypotheses

> **Goal**: Define all possible explanations for your problem — including ones you think are unlikely.

<p align="center">
  <img src="assets/images/ACH_1.png" alt="Step 1 - Hypotheses" width="800">
</p>

The first step is to list every hypothesis that could explain the situation. The key is to be **comprehensive**, not restrictive. Include hypotheses that seem unlikely — ACH works by elimination, so you need candidates to eliminate.

For each hypothesis, provide:

- **Title**: A short, descriptive name (e.g., "Inside Job by CFO")
- **Description**: A fuller explanation of what this hypothesis claims

#### Challenge Your Thinking (Devil's Advocate)

<p align="center">
  <img src="assets/images/ACH_1a.png" alt="Challenge Feature" width="700">
</p>

Use the **😈 Challenge** feature to stress-test your hypotheses. The AI will:

- Point out hypotheses you may have overlooked
- Identify assumptions you're making
- Suggest alternative framings of the problem

#### AI-Assisted Hypothesis Generation

<p align="center">
  <img src="assets/images/ACH_1b.png" alt="AI Hypothesis Generation" width="700">
</p>

Click the **✨ AI Suggest** button to have the AI generate hypotheses based on:

- Your stated focus question
- Evidence already in your corpus
- Common patterns in similar investigations

> **💡 Pro Tip**: Force yourself to include at least one hypothesis you *don't* believe. If your analysis can't eliminate it, you may be missing something.

---

### Step 2: Gather Evidence

> **Goal**: List all significant items of evidence, arguments, and assumptions.

<p align="center">
  <img src="assets/images/ACH_2.png" alt="Step 2 - Evidence" width="800">
</p>

Evidence in ACH includes:

- **Facts**: Concrete, verifiable information
- **Arguments**: Logical inferences that follow from facts
- **Assumptions**: Beliefs taken for granted (mark these clearly!)

#### AI Evidence Suggestions

<p align="center">
  <img src="assets/images/ACH_2a.png" alt="AI Evidence Suggestions" width="700">
</p>

Let the AI scan your corpus and suggest relevant evidence. It will:

- Search your uploaded documents for relevant facts
- Identify key statements that relate to your hypotheses
- Highlight potentially diagnostic information

#### Adding Evidence Manually

<p align="center">
  <img src="assets/images/ACH_2b.png" alt="Add Evidence Modal" width="700">
</p>

For each piece of evidence, provide:

- **Content**: What is the evidence? Be specific.
- **Source**: Where did it come from? (Document name, page number, etc.)
- **Credibility**: How reliable is this source? (High / Medium / Low)

#### Importing from Your Corpus

<p align="center">
  <img src="assets/images/ACH_2c.png" alt="Import Evidence Modal" width="700">
</p>

Click **📂 Import from Corpus** to search your uploaded documents:

1. Enter a search query or browse by entity
2. Select relevant excerpts
3. Evidence is imported with automatic source linking

> **💡 Pro Tip**: High-quality evidence is *specific and verifiable*. "Company was struggling" is weak. "Q3 revenue dropped 40% YoY per SEC filing" is strong.

---

### Step 3: Create the Matrix

> **Goal**: Rate every piece of evidence against every hypothesis.

<p align="center">
  <img src="assets/images/ACH_3.png" alt="Step 3 - Matrix Overview" width="800">
</p>

This is the heart of ACH. For each cell in the matrix, you ask: **"If this hypothesis were true, how consistent is this evidence with it?"**

#### The Analysis Matrix

<p align="center">
  <img src="assets/images/ACH_3a.png" alt="Analysis Matrix" width="700">
</p>

The matrix displays:

- **Rows**: Each piece of evidence
- **Columns**: Each hypothesis
- **Cells**: Your consistency ratings

#### Rating Scale

| Rating | Meaning | When to Use |
|:---:|:---|:---|
| **CC** | Very Consistent | Evidence strongly supports this hypothesis |
| **C** | Consistent | Evidence is compatible with this hypothesis |
| **N** | Neutral | Evidence is irrelevant to this hypothesis |
| **I** | Inconsistent | Evidence is hard to explain if this hypothesis is true |
| **II** | Very Inconsistent | Evidence would be nearly impossible if this hypothesis is true |

#### AI Matrix Assistance

<p align="center">
  <img src="assets/images/ACH_3b.png" alt="AI Matrix Assistance" width="700">
</p>

Click the **✨** icon to get AI-suggested ratings. The AI:

- Reads the evidence text and your document context
- Considers logical implications for each hypothesis
- Provides explanations for its suggested ratings

> **⚠️ Important**: AI suggestions are *starting points*. Always review and adjust based on your domain expertise.

---

### Step 4: Refine the Matrix (Diagnosticity)

> **Goal**: Focus on evidence that actually helps distinguish between hypotheses.

<p align="center">
  <img src="assets/images/ACH_4.png" alt="Step 4 - Diagnosticity" width="800">
</p>

Not all evidence is equally useful. **Diagnostic evidence** is rated differently across hypotheses — it helps you distinguish between them. **Non-diagnostic evidence** is rated the same for all hypotheses — it doesn't help you decide.

#### Evidence Details and Quick Views

<p align="center">
  <img src="assets/images/ACH_4a.png" alt="Evidence and Quick Views" width="700">
</p>

Use the quick view panel to:

- See the full evidence text at a glance
- Review source documents
- Check credibility ratings
- Identify which evidence is most diagnostic

| Diagnosticity | Description | Action |
|:---|:---|:---|
| 🔴 **High** | Different ratings across hypotheses | Keep and scrutinize closely |
| 🟡 **Medium** | Some variation in ratings | May be useful |
| ⚪ **Low** | Same rating for all hypotheses | Consider removing to reduce noise |

> **💡 Pro Tip**: If all your evidence is "Consistent" across all hypotheses, you haven't found any disconfirming evidence. Go back and look harder!

---

### Step 5: Draw Conclusions

> **Goal**: Review the evidence matrix and identify patterns.

<p align="center">
  <img src="assets/images/ACH_5.png" alt="Step 5 - Conclusions" width="800">
</p>

Now it's time to step back and look at the big picture. What does your matrix reveal?

#### Evidence and Matrix Overview

<p align="center">
  <img src="assets/images/ACH_5a.png" alt="Evidence and Matrix View" width="700">
</p>

Review the complete matrix to identify:

- Hypotheses with the most inconsistencies (likely to be wrong)
- Hypotheses with few or no inconsistencies (candidates for being correct)
- Evidence that is particularly powerful (highly diagnostic)

ACH conclusions are based on **disconfirmation**, not confirmation:

> 🏆 **The "winner" is the hypothesis with the LOWEST inconsistency score** — the one that is hardest to disprove.

---

### Step 6: Analyze Consistency

> **Goal**: Calculate consistency scores and rank hypotheses.

<p align="center">
  <img src="assets/images/ACH_6.png" alt="Step 6 - Consistency Analysis" width="800">
</p>

This step automates the scoring process to give you objective rankings.

#### Consistency Checks and Hypothesis Scoring

<p align="center">
  <img src="assets/images/ACH_6a.png" alt="Consistency Checks and Scoring" width="700">
</p>

The system calculates:

- **Inconsistency Score**: Weighted sum of I and II ratings for each hypothesis
- **Consistency Score**: Weighted sum of C and CC ratings
- **Overall Ranking**: Hypotheses sorted by likelihood

| Inconsistency Score | Interpretation |
|:---:|:---|
| 0-2 | Very strong candidate |
| 3-5 | Plausible, minor issues |
| 6-10 | Significant problems |
| 10+ | Likely incorrect |

---

### Step 7: Sensitivity Analysis

> **Goal**: Test how robust your conclusion is. What if key evidence is wrong?

<p align="center">
  <img src="assets/images/ACH_7.png" alt="Step 7 - Sensitivity Analysis" width="800">
</p>

Even the best analysis depends on assumptions. Sensitivity analysis asks: **"What would change my conclusion?"**

#### Notes and Sensitivity Setup

<p align="center">
  <img src="assets/images/ACH_7a.png" alt="Notes and Sensitivity Analysis" width="700">
</p>

Document your thinking:

- **Key Assumptions**: What must be true for your conclusion to hold?
- **Critical Evidence**: Which evidence items are most important?
- **Vulnerabilities**: What could overturn your conclusion?

#### Sensitivity Analysis Results

<p align="center">
  <img src="assets/images/ACH_7b.png" alt="Sensitivity Analysis Results" width="700">
</p>

Click **🔬 Run Sensitivity Analysis** to automatically:

1. Identify which evidence items are most impactful
2. Simulate removing each piece of evidence
3. Flag items that would **change the winning hypothesis**

Evidence marked as **🔴 Critical** means:
> If this evidence were removed or proven false, a *different* hypothesis would win.

**Action**: Double-check the source and credibility of all critical evidence. Can you corroborate it?

---

### Step 8: Milestones & Export

> **Goal**: Track decision milestones, set future indicators, and export your analysis.

<p align="center">
  <img src="assets/images/ACH_8.png" alt="Step 8 - Milestones and Export" width="800">
</p>

The final step helps you document decisions and prepare for the future.

#### Adding Milestones

<p align="center">
  <img src="assets/images/ACH_8a.png" alt="Add Milestone Modal" width="700">
</p>

Milestones capture key decision points in your investigation:

- When you reached a significant conclusion
- When new evidence changed your analysis
- When you ruled out a hypothesis

#### AI Milestone Suggestions

<p align="center">
  <img src="assets/images/ACH_8b.png" alt="AI Milestone Suggestions" width="700">
</p>

Let AI help identify significant milestones by analyzing:

- Changes in hypothesis rankings over time
- Key pieces of evidence that shifted your analysis
- Decision points worth documenting

#### Future Indicators

<p align="center">
  <img src="assets/images/ACH_8c.png" alt="Future Indicators and Milestones" width="700">
</p>

Set up **Future Indicators** — things to watch for that would:

- Confirm your leading hypothesis
- Resurrect a rejected hypothesis
- Introduce a new hypothesis entirely

This transforms ACH from a one-time analysis into an **ongoing analytical framework**.

#### Export with AI Disclosure

<p align="center">
  <img src="assets/images/ACH_8e.png" alt="Export PDF Modal" width="700">
</p>

Export your analysis in multiple formats:

- **PDF**: Professional report with color-coded matrix
- **Markdown**: Clean text for wikis and version control
- **JSON**: Structured data for archival

All exports include an **AI Disclosure** section that flags:

- Which hypotheses were AI-suggested
- Which evidence items were AI-imported
- Which ratings were AI-assisted

---

## � Sample PDF Report

See what your exported analysis looks like:

<p align="center">
  <img src="assets/images/ACH_altPDFa.png" alt="PDF Report Page 1" width="600">
</p>

<p align="center">
  <img src="assets/images/ACH_altPDFb.png" alt="PDF Report Page 2" width="600">
</p>

<p align="center">
  <img src="assets/images/ACH_altPDFc.png" alt="PDF Report Page 3" width="600">
</p>

---

## 📚 Methodology Deep Dive

### Why Do We Count Inconsistencies, Not Consistencies?

The core insight of ACH is that **confirmation bias makes it easy to find supporting evidence for almost any theory**. If you look hard enough, you can find "evidence" that aliens built the pyramids.

What's much harder is explaining away a **flat contradiction**. A single piece of truly inconsistent evidence can be enough to reject a hypothesis entirely.

> 🧪 Science works the same way: theories are never "proven," only "not yet disproven."

### The Cognitive Biases ACH Addresses

| Bias | Problem | How ACH Helps |
|:---|:---|:---|
| **Confirmation Bias** | Seeking evidence that confirms beliefs | Forces you to look for *disconfirming* evidence |
| **Satisficing** | Stopping at "good enough" | Requires testing *all* hypotheses |
| **Anchoring** | First impression dominates | Matrix makes all hypotheses equal |
| **Groupthink** | Consensus overrides analysis | Explicit process invites challenge |
| **Availability Heuristic** | Recent/memorable events seem more likely | Evidence is evaluated systematically |

### Historical Context

ACH was developed by **Richards J. Heuer Jr.** at the CIA in the 1980s. His book *Psychology of Intelligence Analysis* remains a foundational text for analysts worldwide. The method was designed specifically to:

1. Make the analytic process **explicit** and transparent
2. Force analysts to consider **all** possibilities
3. Provide an **audit trail** for decisions
4. Help teams with different backgrounds reach **consensus**

---

## 💡 Tips for Best Results

### ✅ Do

- **Cast a wide net**: Include hypotheses you think are unlikely
- **Be specific**: Vague evidence is useless evidence
- **Mark assumptions**: If it's not a verifiable fact, say so
- **Use credibility ratings**: Not all sources are equal
- **Run sensitivity analysis**: Know your vulnerabilities
- **Set future indicators**: Keep the analysis alive
- **Document everything**: Future-you will thank present-you

### ❌ Don't

- **Don't stop at the first good answer**: That's what ACH is designed to prevent
- **Don't treat AI suggestions as gospel**: They're starting points, not conclusions
- **Don't ignore inconvenient evidence**: If you can't explain it, your hypothesis has a problem
- **Don't forget to update**: As new evidence arrives, re-run the analysis

---

## 🚀 Ready to Start?

Navigate to **ACH** in the sidebar to begin your first analysis. The step-by-step wizard will guide you through the entire process.

<p align="center">
  <a href="../README.md">← Back to Main Documentation</a>
</p>
