Sentiment Analysis Web App (Flask + TextBlob)

A simple and interactive web application that performs sentiment analysis on user-entered text using Flask and TextBlob.
The app classifies text as Positive, Negative, or Neutral and displays polarity and subjectivity scores.

🚀 Features

✔ User-friendly web interface
✔ Real-time sentiment analysis
✔ Displays:

Sentiment Label (Positive / Negative / Neutral)

Polarity Score (-1 to +1)

Subjectivity Score (0 to 1)
✔ Built using Python Flask backend
✔ Styled frontend using HTML & CSS

🧠 What is Sentiment Analysis?

Sentiment Analysis is a Natural Language Processing (NLP) technique used to determine whether a piece of text expresses:

Positive emotion 😊

Negative emotion 😞

Neutral tone 😐

This app uses TextBlob, a Python NLP library, to calculate:

Metric	Meaning
Polarity	Measures positivity/negativity (-1 = negative, +1 = positive)
Subjectivity	Measures opinion vs fact (0 = factual, 1 = opinionated)
🛠 Technologies Used

Python 3

Flask – Web framework

TextBlob – Sentiment analysis

HTML5 & CSS3 – Frontend design

📁 Project Structure
sentiment_app/
│
├── app.py              # Flask backend logic
├── requirements.txt    # Required Python libraries
└── templates/
    └── index.html      # Frontend UI

⚙️ Installation & Setup
1️⃣ Clone or Download Project
git clone https://github.com/your-username/sentiment-analysis-flask.git
cd sentiment-analysis-flask


(Or download and extract the folder manually.)

2️⃣ Install Dependencies
pip install -r requirements.txt
python -m textblob.download_corpora

3️⃣ Run the Application
python app.py


Now open your browser and go to:

http://127.0.0.1:5000/

🧪 Example Usage

Input Text:

I absolutely love this project. It's amazing!

Output:

Sentiment: Positive 😊

Polarity: 0.8

Subjectivity: 0.75

🧩 How It Works

User enters text in the web form

Flask sends the text to the backend

TextBlob analyzes the text sentiment

Polarity and subjectivity are calculated

Sentiment is classified and shown on the page

📌 Future Improvements

🔹 Add sentiment-based color themes
🔹 Store history of analyzed texts
🔹 Add graphical charts for sentiment
🔹 Deploy on cloud (Render / Heroku / PythonAnywhere)

🎓 Learning Outcomes

This project helps you understand:

Flask web development

Integrating NLP into web apps

Using TextBlob for sentiment analysis

Handling forms and dynamic templates

📄 License

This project is open-source and free to use for educational purposes.