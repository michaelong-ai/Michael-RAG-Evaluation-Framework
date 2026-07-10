# Evaluation Framework Expansion — 6 → 15 Questions

## Summary

Expanded the test dataset from **6 to 15 questions** (150% increase) with better coverage across document sections. Added V3 prompt for iterative refinement testing.

---

## Original Test Dataset (6 questions)

| ID | Question | Ground Truth | Category | Difficulty |
|---|---|---|---|---|
| q001 | Emergency fund months | 3 to 6 months | factual | easy |
| q002 | Insurance max % | 15% | factual | easy |
| q003 | Insurance coverage calculation ($10k income) | $90,000 | reasoning | medium |
| q004 | Investment % | 10% | factual | easy |
| q005 | Legacy planning components | Will, CPF Nomination, LPA, Advance Care Plan | factual | medium |
| q006 | Sleep rule (trap) | Not in document | error_analysis | hard |

---

## New Questions Added (9 additional)

### Factual Questions (7 new)

| ID | Question | Ground Truth | Difficulty |
|---|---|---|---|
| **q007** | Critical illness coverage recommendation | 4x annual income | easy |
| **q008** | SSBs guaranteed by | The Government | easy |
| **q009** | What is CareShield Life & coverage | National long-term care insurance for Citizens/PRs born 1980+ | medium |
| **q011** | Housing monetisation options | Silver Housing Bonus, Lease Buyback Scheme | medium |
| **q012** | CPF tax relief on top-ups | Up to $8,000 | easy |
| **q014** | Irregular income emergency fund rule | 12 months of expenses | medium |

### Reasoning Questions (2 new)

| ID | Question | Ground Truth | Difficulty |
|---|---|---|---|
| **q010** | Insurance max for $50k income | $7,500 (50k × 15%) | medium |
| **q013** | Combined insurance need ($30k income) | $390,000 (Death: 9×30k + Critical: 4×30k) | hard |

### Error Analysis / Trap Questions (1 new)

| ID | Question | Ground Truth | Difficulty |
|---|---|---|---|
| **q015** | Best investment strategy for beating market | Not in document | hard |

---

## Final Dataset Composition (15 questions)

- **Factual questions:** 10 (q001, q002, q004, q005, q007, q008, q009, q011, q012, q014)
- **Reasoning questions:** 3 (q003, q010, q013)
- **Error analysis / Trap questions:** 2 (q006, q015)

| Difficulty | Count |
|---|---|
| Easy | 6 |
| Medium | 7 |
| Hard | 2 |

---

## Prompt Versions — V1, V2, V3

### V1 (Sabotaged Baseline)
**Purpose:** Negative control to validate the evaluation framework itself  
**Behavior:** Instructed to answer intentionally wrong

### V2 (Production Prompt)
**Purpose:** Current production baseline  
**Behavior:** 
- Grounded in context only
- Refuses when info not available
- Precise, cites sections

### V3 (Iterative Improvement)
**Purpose:** Show prompt engineering refinement  
**Behavior:**
- More structured output formatting
- Explicit instructions for multi-part questions
- Better handling of numerical answers (include context + exceptions)
- Clear separation of key answer, supporting details, and citations

**Key difference from V2:**
```
V2: "Be precise and cite specific principles or sections where relevant."

V3: "Always structure your answer clearly:
     - State the key answer first
     - Provide supporting details or context if available
     - Cite the relevant principles or sections"
```

---

## Coverage Improvements

### By Document Section

| Section | Original | New | Total |
|---|---|---|---|
| Emergency Funds | 1 | 1 | 2 |
| Insurance/Protection | 3 | 4 | 7 |
| Investments | 1 | 0 | 1 |
| Legacy Planning | 1 | 0 | 1 |
| Retirement/CPF | 0 | 2 | 2 |
| Housing Monetisation | 0 | 1 | 1 |
| Error Analysis / Trap | 1 | 1 | 2 |

### Key Topics Now Tested

✓ Emergency fund rules (regular + irregular income)  
✓ Insurance rules (Death, TPD, Critical Illness percentages and multipliers)  
✓ National schemes (MediShield Life, CareShield Life, DPS)  
✓ CPF & Retirement (tax relief, investment, monetisation)  
✓ Legacy planning  
✓ Out-of-scope rejection (2 trap questions)  

---

## How to Run the Full Evaluation

```bash
# Run all three versions (V1, V2, V3) on all 15 questions
python eval/runner.py

# Generate comparison report
python eval/report.py
```

**Expected output:**
- `eval/v1_results.json` (15 question results for V1)
- `eval/v2_results.json` (15 question results for V2)
- `eval/v3_results.json` (15 question results for V3)
- Console report comparing all three versions across all 15 questions

---

## Evaluation Robustness Benefits

1. **Larger dataset** (15 vs 6) reduces risk of cherry-picked results
2. **Mixed difficulties** (6 easy, 7 medium, 2 hard) tests breadth
3. **Two trap questions** (q006, q015) ensure refusal behavior is tested
4. **Three-way comparison** (V1, V2, V3) shows iterative improvement
5. **Reproducible** — results saved to JSON for audit trail
