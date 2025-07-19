# 🗃️ SQL INSERT Generator

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-red?style=for-the-badge&logo=streamlit)
![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-green?style=for-the-badge&logo=pandas)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

An interactive web application that converts your Excel and CSV files into error-free SQL `INSERT` queries, tailored for different database dialects with advanced options.

---

![License: MIT](...)

---
### 🚀 [Try the Live Demo!](https://spreadsheet-to-sql-importer.streamlit.app/)

---

### ✨ Application Interface

![SQL Insert Generator Interface](https://i.imgur.com/rkTCXKr.png)

---

## 🚀 Key Features

* **Instant Data Preview:** See the first few rows of your file as soon as you upload it to ensure you're working with the correct data.
* **Advanced SQL Options:**
    * **Target Database:** Choose between MS SQL Server, PostgreSQL, and MySQL dialects.
    * **Table Name:** Optionally set the table name yourself or use the file name.
    * **INSERT Type:** Generate separate `INSERT` queries for each row or a single, combined (multi-row) `INSERT` query for all data.
    * **Empty Cell Handling:** Decide whether empty cells in your file are represented as `NULL` or empty string (`''`) in SQL.
* **Multi-Sheet Support:** For Excel files with multiple sheets, select which sheet you want to process.
* **User-Friendly Interface:** All controls, settings, and results are presented clearly on a single screen.
* **Help Menu:** Integrated `❓` help menu for quick guidance on using the application.
* **SQL Download:** Download the generated SQL code as a `.sql` file with one click.

---

## 🛠️ Technologies Used

* **Python:** The core programming language of the application.
* **Streamlit:** The main library for building the interactive web interface.
* **Pandas:** Powerful data library for reading, processing, and analyzing Excel and CSV files.

---

## ⚙️ Installation and Local Usage

To run the project on your own computer, follow these steps:

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_PROJECT.git](https://github.com/YOUR_USERNAME/YOUR_PROJECT.git)
    cd YOUR_PROJECT
    ```

2.  **Install Required Libraries:**
    *(It is recommended to create a virtual environment.)*
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: Create a `requirements.txt` file in your project folder containing `streamlit`, `pandas`, `openpyxl`.)*

3.  **Start the Application:**
    ```bash
    streamlit run app.py
    ```
    This command will start the application on a local server and automatically open it in your browser.

---

## ☁️ Deploying Online (Streamlit Community Cloud)

The easiest way to share this app with friends who don't know Python is to publish it online for free.

1.  Upload your project to a GitHub repository.
2.  Go to `share.streamlit.io` and log in with your GitHub account.
3.  Click the **"New app"** button, select your repository, and press **"Deploy!"**.
4.  In a few minutes, you'll have a link like `your-project-name.streamlit.app`!

---

## 🤝 Contributing

If you'd like to contribute, please open an issue or submit a pull request. All contributions are welcome!

---

## 📄 License

Bu proje, MIT Lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakınız.