# JobPostings-EDA-Task

                         REPORT
Exploratory Data Analysis of Job Market Trends Using Multi-Platform Job Postings.
1. Introduction
This report presents a full analytical workflow applied to a job-market dataset containing information on companies, job postings, salaries, skills, and posting dates. The aim of the project was to perform data cleaning, preprocessing, feature engineering, and exploratory data analysis (EDA) to extract insights on salary distributions, job trends, and skill frequency patterns. The analysis was completed using Python, with libraries including Pandas, NumPy, Matplotlib, and  Seaborn.
2. Data Collection
Before beginning the analysis, the dataset had to be acquired from an external source. Using the Adzuna API, a large-scale dataset consisting of approximately 37,000 job-market records was successfully retrieved. The API provided structured information related to job postings, including titles, companies, skills, salaries, and posting dates.
<img width="1009" height="404" alt="image" src="https://github.com/user-attachments/assets/c1a55399-1761-4ff4-b322-7ebf498f09f5" />
Once the data was extracted, it was downloaded locally in CSV format. However, due to the dataset’s size and to ensure easier access, reproducibility, and collaboration, the CSV file was subsequently uploaded to a public GitHub repository. This enabled the dataset to be accessed via a direct URL, allowing any user to load it programmatically into Python using pd.read_csv().
<img width="1009" height="408" alt="image" src="https://github.com/user-attachments/assets/058b159e-dcef-4b70-9caa-422c79269415" />
3. Data Cleaning
The data cleaning process involved several systematic steps to prepare the dataset for deeper analysis.
3.1 Handling Missing Values
Missing values were identified using df.isnull().sum().
To address incomplete entries:
	Categorical columns such as Company and Skills were filled with the placeholder "Not Provided".
	Numerical columns were handled separately during later stages (e.g., salary cleaning).
3.2 Data Type Fixes
The Created_Date column was converted into a proper datetime format using pd.to_datetime().
Rows with invalid dates were coerced to NaT and handled accordingly.
3.3 Outlier Removal and Salary Cleaning
Salary fields (Salary_Min, Salary_Max) were converted to numeric values and sanitized.
Rows with unrealistic values (e.g., negative salaries or zeros) were removed, producing a cleaner subset called salary_df.
4. Feature Engineering
To enhance the analytical potential of the dataset, new variables were engineered.
4.1 Temporal Features
From the Created_Date column, the following attributes were extracted:
	Year
	Month
	Season (derived from month using a custom function)
These features enabled trend analysis across time.
4.2 Experience Level Categorisation
The numerical column representing years of experience (Experience_Years) was converted into qualitative categories using a custom function:
	Junior
	Mid-Level
	Senior
This allowed for grouped analysis of salary by experience.
4.3 Salary Aggregation
A new column, Salary_Avg, was created to provide a single representative figure per job posting, calculated as the mean of minimum and maximum salary ranges.

5. Exploratory Data Analysis (EDA)
A series of visual and statistical analyses were conducted to uncover patterns in job titles, salaries, countries, and skills.
5.1 Salary Distributions
Using boxplots and distribution graphs:
	Salary varied significantly across experience levels.
	Senior roles showed higher spreads and higher median salaries.
	Country-based salary plots revealed geographic disparities.
5.2 Correlation Analysis
A correlation matrix heatmap was produced for numerical variables.
Key observations included:
	Strong correlations between salary components.
	Moderate relationships between experience and salary.
5.3 Trend Analysis Over Time
Line plots showed monthly trends in average salary:
	Certain months displayed higher offered salaries, indicating seasonal job-market patterns.
5.4 Job Title Frequency
A bar chart of the top 20 most common job titles was generated:
	Titles such as Data Engineer, Data Analyst, Data Scientist, and AI Engineer appeared most frequently.
5.5 Geographic Job Distribution
A country-based job frequency plot highlighted:
	Countries with the highest number of job postings.
	Regional concentrations of technical roles.
5.6 Skills Analysis
By parsing and counting unique skills:
	The most in-demand skills were extracted and visualised.
	Skills such as Machine Learning, Research, Python and SQL dominated.
6. Results and Findings
The analysis produced several important insights:
1.	Salary Variability:
Salary levels depend strongly on both country and experience level.
2.	Temporal Trends:
Hiring peaks were observed in particular months, indicating seasonality in recruitment.
3.	Geographical Concentration:
Certain countries had disproportionately high job postings, reflecting active tech job markets.
4.	Skill Demand:
Programming, data analysis, and machine learning skills were the most frequently required.
7. Conclusion
The workflow implemented demonstrates a complete end-to-end data analysis pipeline. The project encompassed data cleaning, engineering, and extensive exploratory analysis. Through systematic transformation and visualisation, the dataset revealed meaningful patterns related to salary trends, job distributions, and skill requirements in the job market.
8. References
	Python libraries: Pandas, NumPy, Matplotlib, Seaborn
	Dataset source: GitHub (Loaded via URL)
	Custom functions created within the analysis notebook



