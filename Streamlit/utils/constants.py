FEATURE_ORDER = [
    "age", "job", "marital", "education", "default", "housing", "loan",
    "contact", "month", "day_of_week", "duration", "campaign", "pdays",
    "previous", "poutcome", "emp.var.rate", "cons.price.idx",
    "cons.conf.idx", "euribor3m", "nr.employed", "was_previously_contacted"
]

JOBS = [
    "admin.", "blue-collar", "entrepreneur", "housemaid", "management",
    "retired", "self-employed", "services", "student", "technician",
    "unemployed", "unknown"
]

MARITALS = ["married", "single", "divorced", "unknown"]

EDUCATIONS = [
    "university.degree", "high.school", "basic.9y", "basic.6y",
    "basic.4y", "professional.course", "illiterate", "unknown"
]

DEFAULTS = ["no", "unknown", "yes"]
HOUSINGS  = ["yes", "no", "unknown"]
LOANS     = ["no", "yes", "unknown"]
CONTACTS  = ["cellular", "telephone"]

MONTHS = ["mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec", "jan", "feb"]
DAYS   = ["mon", "tue", "wed", "thu", "fri"]

POUTCOMES = ["nonexistent", "failure", "success"]

# Default / sample values used for the CSV template
SAMPLE_ROW = {
    "age": 35,
    "job": "admin.",
    "marital": "married",
    "education": "university.degree",
    "default": "no",
    "housing": "yes",
    "loan": "no",
    "contact": "cellular",
    "month": "may",
    "day_of_week": "mon",
    "duration": 200,
    "campaign": 2,
    "pdays": 999,
    "previous": 0,
    "poutcome": "nonexistent",
    "emp.var.rate": -1.8,
    "cons.price.idx": 92.893,
    "cons.conf.idx": -46.2,
    "euribor3m": 1.313,
    "nr.employed": 5099.1,
    "was_previously_contacted": 0
}

MODEL_PATH = "models/best_model.joblib"
