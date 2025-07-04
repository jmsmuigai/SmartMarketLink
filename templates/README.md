# 🌾 SmartMarketLink

> Empowering Farmers with Real-Time Market Intelligence  
> Built by **James Mukoma Mburu** — Garissa, Kenya

---

## 📍 Problem

Farmers in remote and arid regions like Garissa often:
- Sell produce without knowing the fair market price
- Get exploited by middlemen
- Lack tools to make informed selling decisions

---

## 💡 Solution

**SmartMarketLink** is a lightweight web platform that:
- Lets farmers search for crop prices by region
- Displays real-time price data using a CSV dataset
- Built using Python (Flask) — works offline with potential for USSD/SMS integration

---

## 🛠️ Tech Stack

- Python + Flask
- HTML (Jinja templates)
- CSV data (can be replaced by an API)
- GitHub for version control
- Google Slides for pitch deck

---

## 🚀 How It Works

1. Farmer types a crop name (e.g., maize)
2. App returns matching market prices in different locations
3. Easy-to-use interface; scalable to SMS & USSD platforms

---

## 📸 Screenshots

### 🏠 Home Page
![Home](screenshots/index.png)

### 📈 Results Page
![Results](screenshots/results.png)

---

## 📊 Pitch Deck

🔗 [View SmartMarketLink Pitch Deck on Google Slides](https://docs.google.com/presentation/d/1SkbJq5mCVhqUmG3O3h9TBqpxnMmQAc_HcGEC3tYxLq0/edit?usp=sharing)

---

## 🧪 How to Run Locally

```bash
git clone https://github.com/jmsmuigai/SmartMarketLink.git
cd SmartMarketLink
pip install flask pandas
python app.py
