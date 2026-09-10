# AChE Inhibitor Prediction Using Machine Learning

## Overview

This project focuses on the identification of potential inhibitors against human Acetylcholinesterase (AChE) using a computational workflow combining machine learning, molecular docking, protein–ligand interaction analysis, and ADMET profiling.

## Target

* Protein: Human Acetylcholinesterase (AChE)
* PDB ID: 4EY7
* Therapeutic relevance: Alzheimer's disease

## Machine Learning

Experimental compound activity data were obtained from BindingDB.

The machine learning workflow included:

* Data preprocessing
* Molecular fingerprint generation
* Morgan fingerprints (2048 bits, radius 2)
* Scaffold-based train/test validation
* SMOTE applied only to the training data
* Random Forest classification
* Model performance evaluation

### Final Random Forest Performance

| Metric    |  Value |
| --------- | -----: |
| Accuracy  | 0.8501 |
| Precision | 0.7382 |
| Recall    | 0.6024 |
| F1-score  | 0.6634 |
| MCC       | 0.5731 |
| ROC-AUC   | 0.8523 |
| PR-AUC    | 0.6712 |
| Threshold |   0.60 |

The complete machine-learning workflow is provided in the Jupyter Notebook.
### Protein Preparation

* AChE structure (PDB ID: 4EY7) obtained from the Protein Data Bank.
* Protein structure prepared and refined using **UCSF ChimeraX**.
* Unwanted protein chain was removed.
* Water molecules were handled during structure preparation.
* The prepared protein was saved and used as the receptor for **PyRx molecular docking**.

## Molecular Docking

Molecular docking was performed using PyRx to evaluate the binding of selected compounds against the identified AChE binding pocket.

The binding pocket was identified using CASTp.
### Top 6 Docking Candidates

Based on the best docking binding affinity, six compounds were selected for further interaction analysis:

| Rank | Compound      | Best Binding Affinity (kcal/mol) |
| ---- | ------------- | -------------------------------: |
| 1    | CHEMBL4524111 |                             -8.9 |
| 2    | CHEMBL205940  |                             -8.8 |
| 3    | CHEMBL1677    |                             -8.7 |
| 4    | CHEMBL609150  |                             -7.7 |
| 5    | CHEMBL206093  |                             -7.6 |
| 6    | CHEMBL207777  |                             -7.5 |

These six compounds were subsequently evaluated for their interactions with the CASTp-identified binding pocket. Compounds that showed relatively low docking scores and/or insufficient interactions with the selected pocket residues were excluded. Two compounds were shortlisted for further ADMET evaluation, and CHEMBL206093 was selected as the final candidate based on the KCSM ADMET assessment.

### CASTp Pocket Residues

The selected pocket included:

**Glu81, Gly82, Met85, Asp131, Val132, Ala434, Thr436, Leu437, Ser438, Trp439, Tyr449, Glu452, Ile457, Arg463, Asn464, and Tyr465.**

Docking results are provided in:

`AChE _DOCK_results.csv`

Following docking, protein–ligand interaction analysis was performed to evaluate interactions with the selected pocket residues.

Compounds that showed relatively low docking scores and did not demonstrate clear interactions with the selected pocket residues were excluded from further consideration.

Two compounds were shortlisted for further evaluation. Among the shortlisted compounds, the final candidate was selected based on its ADMET profile.

## Final Candidate

* **ChEMBL ID:** CHEMBL206093
* **PubChem CID:** 11681391

The final candidate was subjected to further ADMET evaluation using KCSM.

## ADMET Profiling

KCSM was used to evaluate the predicted absorption, distribution, metabolism, and toxicity properties of the final candidate.

Selected predictions included:

| Parameter             | KCSM Prediction |
| --------------------- | --------------: |
| Intestinal absorption |         91.538% |
| P-gp substrate        |              No |
| AMES toxicity         |              No |
| hERG I inhibitor      |              No |
| hERG II inhibitor     |             Yes |
| Hepatotoxicity        |             Yes |
| CYP3A4 substrate      |             Yes |
| CYP1A2 inhibitor      |             Yes |
| CYP2C19 inhibitor     |             Yes |
| CYP2C9 inhibitor      |             Yes |
| CYP3A4 inhibitor      |             Yes |

These results are computational predictions and require experimental validation.
**Interpretation:** The candidate shows favorable absorption (91.5% intestinal 
absorption) and is not predicted to be AMES-mutagenic or a P-gp substrate — 
positive early drug-likeness signals. However, it is flagged for hERG II 
inhibition and hepatotoxicity, both common liabilities at this stage that 
would need experimental validation before further development. Inhibition 
of multiple CYP450 isoforms (1A2, 2C19, 2C9, 3A4) also suggests possible 
drug-drug interaction risk, an important consideration for lead optimization.

## Workflow

BindingDB experimental data
↓
Data preprocessing
↓
Morgan molecular fingerprints
↓
Random Forest classification
↓
Candidate screening
↓
CASTp pocket identification
↓
PyRx molecular docking
↓
Protein–ligand interaction analysis
↓
Shortlisting of candidates
↓
KCSM ADMET profiling
↓
Final candidate selection

## Repository Contents

* `Untitled19.ipynb` — complete machine-learning workflow
* `AChE_final_scaffold_results.csv` — final model performance
* `AChE _DOCK_results.csv` — molecular docking results
* `README.md` — project description and summary

## Conclusion

This computational workflow was used to prioritize potential AChE inhibitor candidates. Machine learning was used for activity prediction and candidate screening, followed by molecular docking and interaction analysis. Two compounds were shortlisted, and CHEMBL206093 (PubChem CID 11681391) was selected as the final candidate based on its subsequent ADMET profile.

The results provide a computational basis for further investigation of potential AChE inhibitors.
