# AI-Generated Ad Copy Hallucination Guardrails & Assertion Validator

> Catch AI ad copy hallucinations and fake discounts before launching ad spend. Rule-based assertion validator for advertising claims.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Format: CLI_SCRIPT](https://img.shields.io/badge/Format-CLI--SCRIPT-green.svg)](#)
[![Tier: 2](https://img.shields.io/badge/Tier-2-orange.svg)](#)
[![Region: MENA](https://img.shields.io/badge/Region-Egypt%20%7C%20GCC%20%7C%20Saudi-purple.svg)](#)
[![Tests: Passing](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)](#)
[![Owner: mahmoudabdelnaby1](https://img.shields.io/badge/Owner-mahmoudabdelnaby1-blue.svg)](https://github.com/mahmoudabdelnaby1)

---

## 📌 Problem Statement & Target Persona

### Target Persona
**PRO** operating in high-growth e-commerce, digital publishing, and direct-response marketing across Saudi Arabia, UAE, and Egypt.

### Core Problem
Develop a pure Python ad copy guardrails validator (`copy_guardrails.py`): 1) Ingests generated ad copy CSV files and a JSON configuration of authorized claims (Max Discount %, Allowed Shipping Terms, Return Window Days), 2) Flags unauthorized discount codes, extreme superlatives ('100% cure'), or hallucinated guarantees, 3) Outputs a pass/flagged CSV and terminal summary.

---

## 🛠️ Repository Architecture & Deliverables

This repository provides self-contained, documented implementations and specifications:

- `config/authorized_offer_bounds.sample.json`
- `examples/unreviewed_ad_copy_sample.csv`
- `LICENSE`
- `README.md`
- `reports/flagged_claims_report.csv`
- `src/copy_guardrails.py`
- `tests/test_guardrails.py`


---

## 🚀 Quick Start & How to Run Locally

### Run Test Suite Locally
```bash
# Ensure no bytecode generation
export PYTHONDONTWRITEBYTECODE=1  # Linux / macOS
$env:PYTHONDONTWRITEBYTECODE="1"  # Windows PowerShell

# Run Python unittest discovery
python -m unittest discover -s tests
```

### Run CLI Script
```bash
python src/copy_guardrails.py --help
```

---

## 📊 Sample Input & Output Fixtures

> **Data Disclosure:** Any included sample data is illustrative and may be synthetic; it is not a measured customer result or market benchmark unless a source and collection method are stated alongside it. These files run offline with standard libraries and require no paid third-party API credentials.

```json
{
  "domain": "career",
  "repository": "ai-ad-copy-hallucination-guardrails",
  "status": "READY_FOR_LOCAL_REVIEW",
  "license": "MIT"
}
```

---

## ⚠️ Known Technical & Domain Constraints

- **Factual Assertion Validation:** Compares generated copy against verified product specification sheets to catch fabricated features or false pricing.
- **Regulatory Claims Screening:** Flags unsubstantiated claims ('#1 Doctor Recommended', 'Guaranteed Cure') that trigger regulatory advertising penalties.
- **Automated CI/CD Quality Gate:** Integrates into content generation pipelines to block hallucinated copy before human editorial review.

---

## 📚 Primary Documentation & Verifiable References

- [FTC Guidelines Concerning Use of Endorsements in Advertising](https://www.ftc.gov/) - Regulatory standards prohibiting false, unsubstantiated, or misleading promotional claims.
- [Saudi General Authority for Media Regulation (GAMR): Advertising Integrity](https://gcam.gov.sa/) - Statutory rules requiring demonstrable veracity in commercial advertising.
- [W3C Semantic Validation Specifications](https://www.w3.org/) - Standards for structured entity extraction and claim verification.

---


## 👤 Maintainer & License

- **Author & Maintainer:** [Mahmoud Abdelnaby](https://github.com/mahmoudabdelnaby1) (`@mahmoudabdelnaby1`)
- **License:** [MIT License](LICENSE) - Open-source, auditable, and freely adaptable for internal enterprise or commercial use.
