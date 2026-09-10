# AChE Inhibitor Prediction Using Machine Learning

## Overview

This project focuses on the identification of potential inhibitors against
human Acetylcholinesterase (AChE) using a machine learning-based workflow
followed by molecular docking and ADMET profiling.

## Target

- Protein: Human Acetylcholinesterase (AChE)
- UniProt ID: P22303
- Therapeutic relevance: Alzheimer's disease

## Machine Learning

Experimental compound activity data were obtained from BindingDB.

The machine learning workflow included:

- Data preprocessing
- Molecular fingerprint generation
- Morgan fingerprints (2048 bits, radius 2)
- Scaffold-based train/test validation
- SMOTE applied only to the training data
- Random Forest classification
- Model performance evaluation

### Model

- Algorithm: Random Forest
- Validation: Scaffold Test
- PR-AUC: 0.9631

The complete workflow is available in the Jupyter Notebook, while the
trained model is provided as a `.pkl` file.

## Molecular Docking

Selected compounds were evaluated using molecular docking.

Docking results are provided in:

`Docking/AChE_DOCK_results.csv`

The final shortlisted candidate was further examined for protein-ligand
interactions using molecular visualization.

## ADMET Profiling

ADMET profiling was performed for the final shortlisted candidate using
KCSM.

The selected KCSM results are provided in:

`ADMET/Final_Candidate_KCSM_ADMET.csv`

## Repository Contents

- `Machine_Learning/` — ML notebook, trained Random Forest model, and model results
- `Docking/` — molecular docking results
- `ADMET/` — KCSM ADMET results for the final candidate
- `Figures/` — final AChE-ligand interaction visualization

## Workflow

BindingDB experimental data  
↓  
Data preprocessing  
↓  
Morgan molecular fingerprints  
↓  
Random Forest classification  
↓  
Candidate selection  
↓  
Molecular docking  
↓  
Protein-ligand interaction analysis  
↓  
KCSM ADMET profiling

## Conclusion

This computational workflow was used to prioritize potential AChE inhibitor
candidates for further investigation. The final candidate was evaluated
through molecular docking, interaction analysis, and ADMET prediction.
