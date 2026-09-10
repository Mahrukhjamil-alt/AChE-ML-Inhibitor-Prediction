# AChE Inhibitor Prediction Using Machine Learning

A computational drug-discovery pipeline for identifying potential inhibitors of human Acetylcholinesterase (AChE), combining **machine learning**, **molecular docking**, **protein–ligand interaction analysis**, and **ADMET profiling**.

## Target

| Property | Value |
|----------|-------|
| Protein | Human Acetylcholinesterase (AChE) |
| PDB ID | [4EY7](https://www.rcsb.org/structure/4EY7) |
| Therapeutic area | Alzheimer's disease |
| Binding pocket | CASTp-identified pocket |

## Machine Learning Pipeline

Experimental compound activity data were obtained from **BindingDB**.

1. Data preprocessing and cleaning
2. **Morgan fingerprints** (2048 bits, radius 2) via RDKit
3. **Scaffold-based train/test split** (no scaffold leakage)
4. **SMOTE** oversampling — applied to training data only
5. **Random Forest** classification
6. Threshold tuning using out-of-fold predictions

### Model Performance (Scaffold Test Set)

| Metric | Value |
|--------|-------|
| Accuracy | 0.8501 |
| Precision | 0.7382 |
| Recall | 0.6024 |
| F1-score | 0.6634 |
| MCC | 0.5731 |
| ROC-AUC | 0.8523 |
| PR-AUC | 0.6712 |
| Decision threshold | 0.60 |

Complete workflow: [`01_model_training.ipynb`](01_model_training.ipynb)

## Molecular Docking

**Receptor preparation:**
- AChE structure (PDB: 4EY7) from the Protein Data Bank
- Prepared with **UCSF ChimeraX**
- Binding pocket identified using **CASTp**

**Docking:**
- Software: **autodock vina in PyRx**
- Results: [`AChE_docking_results.csv`](AChE_docking_results.csv)

### Top 6 Docking Candidates

| Rank | Compound | Binding Affinity (kcal/mol) |
|------|----------|----------------------------|
| 1 | CHEMBL4524111 | −8.9 |
| 2 | CHEMBL205940 | −8.8 |
| 3 | CHEMBL1677 | −8.7 |
| 4 | CHEMBL609150 | −7.7 |
| 5 | CHEMBL206093 | −7.6 |
| 6 | CHEMBL207777 | −7.5 |

**Pocket residues:** Glu81, Gly82, Met85, Asp131, Val132, Ala434, Thr436, Leu437, Ser438, Trp439, Tyr449, Glu452, Ile457, Arg463, Asn464, Tyr465.

Compounds with poor docking scores or insufficient pocket interactions were excluded. Two compounds were shortlisted for ADMET evaluation.

## Final Candidate

| Property | Value |
|----------|-------|
| ChEMBL ID | CHEMBL206093 |
| PubChem CID | [11681391](https://pubchem.ncbi.nlm.nih.gov/compound/11681391) |

### ADMET Profile (pKCSM Predictions)

| Parameter | Prediction |
|-----------|-----------|
| Intestinal absorption | 91.54% |
| P-gp substrate | No |
| AMES toxicity | No |
| hERG I inhibitor | No |
| hERG II inhibitor | Yes |
| Hepatotoxicity | Yes |
| CYP3A4 substrate | Yes |
| CYP1A2 inhibitor | Yes |
| CYP2C19 inhibitor | Yes |
| CYP2C9 inhibitor | Yes |
| CYP3A4 inhibitor | Yes |

**Interpretation:** Favorable absorption (91.5%), not AMES-mutagenic, not a P-gp substrate. However, hERG II inhibition and hepatotoxicity flags require experimental validation. Multiple CYP450 inhibitions suggest possible drug–drug interaction risk.

## Workflow
BindingDB data → Preprocessing → Morgan fingerprints → Random Forest
→ Candidate screening → CASTp pocket identification → PyRx docking
→ Interaction analysis → Shortlisting → KCSM ADMET → Final candidate

text

## Repository Contents

| File | Description |
|------|-------------|
| `01_model_training.ipynb` | Complete ML workflow |
| `AChE_final_scaffold_results.csv` | Final model performance |
| `AChE_docking_results.csv` | Molecular docking results |
| `AChE_Final_RF_model.pkl.gz` | Trained Random Forest model (compressed) |

## Usage

### Load the trained model and predict activity of any compound

The trained Random Forest model is saved in compressed form. You can load it and predict whether a new compound is **Active** or **Inactive** against AChE without re-training:

```python
import gzip, joblib
import numpy as np
from rdkit import Chem
from rdkit.Chem import rdFingerprintGenerator

# Step 1: Load the pre-trained Random Forest model
with gzip.open("AChE_Final_RF_model.pkl.gz", "rb") as f:
    model = joblib.load(f)

# Step 2: Generate Morgan fingerprint (must match training settings)
gen = rdFingerprintGenerator.GetMorganGenerator(radius=2, fpSize=2048)

smiles = "CC(=O)Oc1ccccc1C(=O)O"   # aspirin — replace with any SMILES
mol = Chem.MolFromSmiles(smiles)
fp = np.array(gen.GetFingerprint(mol)).reshape(1, -1)

# Step 3: Predict probability and apply tuned threshold (0.60)
prob = model.predict_proba(fp)[0, 1]
label = "Active" if prob >= 0.60 else "Inactive"

print(f"SMILES: {smiles}")
print(f"Predicted probability: {prob:.3f} → {label}")
Install dependencies
bash
pip install pandas numpy scikit-learn xgboost imbalanced-learn rdkit matplotlib joblib
#Limitations
Recall = 0.60 — the model misses ~40% of true actives; suitable for prioritization, not exhaustive screening.

SMOTE on binary fingerprints can generate chemically unrealistic synthetic vectors.

Docking used a rigid-receptor protocol without formal redocking RMSD validation; results are preliminary.

No experimental validation of the final candidate.

ADMET predictions are from KCSM — computational only.

Applicability domain was not formally assessed.

#Data Sources
Activity data: BindingDB

Protein structure: PDB 4EY7

ADMET predictions: pKCSM

Author
Mahrukh Jamil
GitHub: @Mahrukhjamil-alt
