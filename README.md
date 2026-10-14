# Student Performance Analysis

## 1. Internship Week and Task Summary

**Internship:** AI/ML Internship at WeIntern  
**Week:** Week 1  
**Task:** Student Performance Dataset Analysis

The objective of this task is to analyze student performance data, identify patterns related to academic scores, and present useful findings through data visualization and a business insight report.

## 2. Dataset Used

The project uses the Student Performance dataset, which initially contained 25,000 records and 14 columns. After removing duplicate records, 15,000 records remained.

The dataset includes age, gender, parent education, study hours, attendance percentage, internet access, extra activities, study method, subject scores, overall score, and final grade.

## 3. Libraries and Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Google Colab
- GitHub

## 4. Steps Performed

1. Loaded and inspected the dataset.
2. Checked missing values and duplicate records.
3. Removed duplicate records and saved the cleaned dataset.
4. Examined dataset features and descriptive statistics.
5. Created visualizations to understand score distributions and group comparisons.
6. Analyzed correlations between numerical features.
7. Prepared written observations and a business insight report.
8. Organized project files and screenshots in GitHub.

## 5. Key Findings

- Study hours have a strong positive correlation with overall scores (approximately 0.91).
- Attendance percentage has a weak positive correlation with overall scores (approximately 0.29).
- Mathematics, Science, and English scores have strong positive correlations with overall scores.
- Most overall scores fall approximately between 40 and 90.
- Correlation does not prove causation.

## 6. Project Folder Structure

```text
aiml-week1-assignment/
├── data/
│   ├── raw/
│   └── cleaned/
├── notebooks/
│   └── week1_analysis.ipynb
├── outputs/
│   └── charts/
├── reports/
│   └── business_insight_report.pdf
├── src/
│   └── helper_scripts.py
├── screenshots/
├── README.md
└── requirements.txt
```

## 7. Execution Instructions

1. Clone or download this repository.
2. Open `notebooks/week1_analysis.ipynb` in Google Colab or Jupyter Notebook.
3. Upload or locate the dataset files in the appropriate folders.
4. Update the dataset path in the notebook if necessary.
5. Run the notebook cells in order to reproduce the analysis and visualizations.

## 8. Screenshots and Outputs

The `screenshots/` folder contains previews of the dataset, missing-value summary, score distribution, correlation heatmap, and business report.

The `outputs/charts/` folder contains the generated visualization images.

The `reports/` folder contains the business insight report in PDF format.

## 9. Author Details

**Author:** Fathimath Basna T M  
**Qualification:** Bachelor of Computer Applications (BCA)  
**Area of Interest:** Artificial Intelligence, Machine Learning, and Data Science

## 10. Conclusion

This project demonstrates basic data cleaning, exploratory data analysis, visualization, and interpretation of student performance data. The findings can help identify patterns in academic performance and areas for further investigation.
