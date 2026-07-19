import joblib

feature_names = joblib.load("models/feature_names.pkl")
model = joblib.load("models/pcos_model.pkl")
scaler = joblib.load("models/scaler.pkl")

print("=" * 40)
print("MODEL INFORMATION")
print("=" * 40)

print("Model:")
print(model)

print("\nNumber of Features:")
print(len(feature_names))

print("\nFeature Names:")
for i, feature in enumerate(feature_names, start=1):
    print(f"{i}. {feature}")

print("\nScaler expects:")
print(scaler.n_features_in_)