from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# 🔥 Better dataset (expand this later)
texts = [
    # resumes
    open("data/resume1.txt").read(),
    open("data/resume2.txt").read(),
    open("data/resume3.txt").read(),

    # non resumes
    open("data/article1.txt").read(),
    open("data/news1.txt").read(),
    open("data/blog1.txt").read(),
]

labels = [1,1,1,1, 0,0,0,0]

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(texts)

model = LogisticRegression()
model.fit(X, labels)

# 🔥 Save inside models folder
joblib.dump(model, "models/resume_model.pkl")
joblib.dump(vectorizer, "models/vectorizer.pkl")

print("✅ Model trained and saved in models/")