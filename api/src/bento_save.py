import bentoml
import joblib

model = joblib.load("model.pkl")

saved_model = bentoml.sklearn.save_model("SVR", model)
print(f"Model saved: {saved_model}")
