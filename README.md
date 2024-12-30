# 📰 Fake News Detection and Fact-Checking System

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg?style=flat-square&logo=python)](https://www.python.org/)
![License](https://camo.githubusercontent.com/6cd0120cc4c5ac11d28b2c60f76033b52db98dac641de3b2644bb054b449d60c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4d49542d79656c6c6f772e737667)



A machine learning-based system that detects fake news and checks the factual correctness of news content using external APIs and datasets. This project aims to enhance media reliability by leveraging cutting-edge AI techniques.

---

## 🚀 Project Overview

In today's world, fake news spreads rapidly across digital platforms, creating misinformation and confusion. Our *Fake News Detection and Fact-Checking System* automatically verifies the authenticity of news articles and provides factual corrections using a fact-checking API.

### Key Features
- **Fake News Detection:** Classifies news articles as true or fake using machine learning models trained on labeled datasets.
- **Fact Checking:** Takes the entered news and returns factually verified information.
- **User-Friendly Interface:** A web-based system with a simple, intuitive design for users to input news articles.
- **Modular Design:** Clear separation between news detection and fact-checking components, enabling easy updates.

---

## 📋 Table of Contents
1. [Project Objectives](#objectives)
2. [Technology Stack](#tech-stack)
3. [Data Preprocessing](#data-preprocessing)
4. [Model Training](#model-training)
5. [Fact-Checking](#fact-checking)
6. [Challenges](#challenges)
7. [Future Scope](#future-scope)
8. [How to Run](#how-to-run)
9. [Contributing](#contributing)
10. [License](#license)

---

## 🎯 Objectives <a name="objectives"></a>

1. Identify and detect fake news articles.
2. Provide accurate fact-checks for the input text.
3. Ensure a reliable and user-friendly interface to enhance user experience.
4. Improve accuracy through model optimization.

---

## 🛠️ Technology Stack <a name="tech-stack"></a>

- **Programming Language:** Python
- **Machine Learning:** Scikit-learn, TensorFlow
- **Web Framework:** Django
- **Database:** SQLite for storage of user-submitted news articles
- **Frontend:** HTML5, CSS3, Bootstrap
- **APIs:** External Fact-Checking API

---

## 🧹 Data Preprocessing <a name="data-preprocessing"></a>

- Datasets: `true.csv`, `false.csv` from Kaggle.
- Preprocessing steps include:
  - Cleaning and normalizing the text.
  - Tokenization and vectorization (TF-IDF).
  - Handling missing or noisy data.

---

## 🧠 Model Training <a name="model-training"></a>

- **Classifier Used:** Logistic Regression, Random Forest, or other classifiers.
- **Metrics:** Accuracy, Precision, Recall, F1 Score.
- **Training Process:**
  - Train the model on a dataset containing true and false news articles.
  - Test and evaluate model performance using cross-validation.

---

## 🔎 Fact-Checking <a name="fact-checking"></a>

The fact-checking feature uses an external API to:
- Extract key information from the news article.
- Return verified factual content to counter the input news.
- Display corrected information in the web app.

---

## ⚔️ Challenges <a name="challenges"></a>

1. **Data Imbalance:** Balancing true and false news in the dataset.
2. **Fact-Checking API:** Finding an efficient, accurate API for real-time fact-checking.
3. **Accuracy:** Continuously improving the model's performance and reliability.

---

## 🚀 Future Scope <a name="future-scope"></a>

- **Expand the Dataset:** Continuously improve detection accuracy with larger datasets.
- **API Integration:** Enhance the fact-checking feature with more reliable and broader APIs.
- **Multi-language Support:** Add support for fake news detection in various languages.

---

## 🏃 How to Run <a name="how-to-run"></a>

### Running the Application:
  - Python 3.9

1. Clone the repository:
   ```bash
   https://github.com/Tech2Saini/FakeNewsDetection.git
   ```
2. Navigate to the project directory:
   ```bash
   cd fake-news-detection
   ```
3. Prerequisites:
  - Required Python libraries (install via `requirements.txt`):
    ```bash
    pip install -r requirements.txt
    ```
  
4. Run the Flask app:
   ```bash
   python manage.py runserver
   ```
5. Access the application on `http://127.0.0.1:8000/` in your browser.

---

## 🤝 Contributing <a name="contributing"></a>

We welcome contributions to this project! Feel free to:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.

---


## 💬 Contact

For any queries or suggestions, feel free to reach out:
- **LinkedIn:** [Monu Saini](https://www.linkedin.com/in/monupydev)

---

## 📜 License <a name="license"></a>

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
