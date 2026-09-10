"""
AChE Inhibitor Prediction — Command Line Interface
Load the trained Random Forest model and predict activity for any SMILES.
"""

import gzip
import joblib
import numpy as np
from rdkit import Chem
from rdkit.Chem import rdFingerprintGenerator


def load_model(path="AChE_Final_RF_model.pkl.gz"):
    """Load the compressed Random Forest model."""
    with gzip.open(path, "rb") as f:
        return joblib.load(f)


def predict_smiles(smiles, model=None, threshold=0.60):
    """
    Predict AChE activity for a given SMILES string.

    Args:
        smiles: SMILES string of the compound
        model: pre-loaded model (optional)
        threshold: decision threshold (default 0.60)

    Returns:
        (probability, label) tuple
    """
    if model is None:
        model = load_model()

    gen = rdFingerprintGenerator.GetMorganGenerator(radius=2, fpSize=2048)
    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        return None, "Invalid SMILES"

    fp = np.array(gen.GetFingerprint(mol)).reshape(1, -1)
    prob = model.predict_proba(fp)[0, 1]
    label = "Active" if prob >= threshold else "Inactive"

    return prob, label


if __name__ == "__main__":
    print("=" * 50)
    print("AChE Inhibitor Prediction")
    print("=" * 50)
    print("Loading model...")
    model = load_model()
    print("Model loaded.\n")

    while True:
        smiles = input("Enter SMILES (or 'quit' to exit): ").strip()
        if smiles.lower() in ("quit", "exit", "q"):
            break
        if not smiles:
            continue

        prob, label = predict_smiles(smiles, model=model)
        if prob is None:
            print(f"  Error: {label}\n")
        else:
            print(f"  Predicted probability: {prob:.3f}")
            print(f"  Classification: {label}\n")
