import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import joblib
import pandas as pd
import numpy as np
import streamlit as st

from utils.custom_transformers import P95Capper
from utils.constants import FEATURE_ORDER, MODEL_PATH

sys.modules["__main__"].P95Capper = P95Capper

if "__mp_main__" not in sys.modules:
    sys.modules["__mp_main__"] = sys.modules["__main__"]
sys.modules["__mp_main__"].P95Capper = P95Capper


@st.cache_resource
def load_model():
    import types
    import pickle

    class DebugUnpickler(pickle.Unpickler):
        def find_class(self, module, name):
            st.write(f"Looking for: {module}.{name}")
            return super().find_class(module, name)

    import io
    with open(MODEL_PATH, "rb") as f:
        data = f.read()
    
    try:
        DebugUnpickler(io.BytesIO(data)).load()
    except Exception as e:
        st.write(f"Debug error: {e}")

    obj = joblib.load(MODEL_PATH)
    pipeline = obj["model"]
    return pipeline, float(obj["best_score"])


def predict(df, pipeline):
    df = df[FEATURE_ORDER].copy()
    probas = pipeline.predict_proba(df)[:, 1]
    preds  = (probas >= 0.5).astype(int)
    return preds, probas
