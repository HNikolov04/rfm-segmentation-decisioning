RFM Segmentation & Decisioning — Applied AI Project (TU)
🎓 Университетски проект по Приложен Изкуствен Интелект

Проектът е разработен в рамките на курс по Applied Artificial Intelligence в Технически Университет.
Целта е изграждане на система за RFM сегментиране (Recency–Frequency–Monetary) на клиенти, допълнена с автоматизирана ML сегментация (K-Means) и маркетингови препоръки.

📘 Тема на проекта

RFM Segmentation and Decisioning

Проектът включва:

Изчисляване на RFM показатели от транзакционни данни

Скоране на клиенти чрез квантилно разпределение

Сегментиране чрез правилна система (rule-based)

Сегментиране чрез ML модел (K-Means clustering)

Визуализации и анализ

Предложени маркетингови действия за всеки сегмент

📁 Структура на проекта
rfm-segmentation-decisioning/
├─ data/                          # CSV dataset folder
│   └─ OnlineRetail.csv           # Automatically downloaded
├─ src/                           # Source code
│   ├─ data/                      # Data handling modules
│   │   ├─ download_dataset.py    # Automatic Kaggle dataset download
│   │   └─ load_data.py           # Loads & preprocesses CSV
│   ├─ features/                  # Feature engineering
│   │   └─ rfm_features.py        # Calculates Recency, Frequency, Monetary
│   ├─ models/                    # Machine learning models
│   │   └─ rfm_model.py           # KMeans clustering
│   ├─ visualization/             # Plots and visualizations
│   │   └─ plots.py               # Cluster plots & charts
│   └─ main.py                    # Orchestrates full pipeline
├─ Documentation/                 # Reports, notes, presentations
├─ venv/                           # Python virtual environment
├─ requirements.txt                # Project dependencies
└─ README.md                       # Project overview & instructions

⚙️ Технологии

Python 3.11

pandas, numpy

scikit-learn (K-Means)

matplotlib, seaborn, plotly

Jupyter Notebook / VS Code

▶️ Инструкции за стартиране и setup

1. Проверете версията на Python

python --version


Ако Python не е инсталиран → изтеглете го от python.org
.

2. Създайте виртуална среда (optional, но препоръчително)

py -m venv venv


3. Активиране на виртуалната среда
Windows:

venv\Scripts\activate


macOS / Linux:

source venv/bin/activate


4. Инсталирайте всички зависимости

python -m pip install -r requirements.txt


5. Инсталирайте допълнителни пакети при нужда

python -m pip install <library_name>


6. Стартирайте проекта

python src\main.py


7. Деактивиране на виртуалната среда след работа

deactivate