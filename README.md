
# 📊 Task 8 - Sales Performance Dashboard

## ✅ Objective
To build an interactive dashboard that shows:
- Sales trends over months
- Sales distribution by region and category
- Key business insights based on data visualization

## 🧰 Tools Used
- **Power BI** for dashboard creation
- **Python (pandas)** for date formatting
- **Dataset**: Superstore_Sales.csv (Kaggle)

## 🧼 Data Preprocessing
- Converted `Order Date` from MM/DD/YYYY to DD/MM/YYYY format using Python.
- Added a derived `MonthYear` column for visualizing trends over time in correct chronological order.

## 📈 Visuals Included
- **Line Chart** – Sales trend over months
- **Bar Chart** – Regional sales comparison
- **Donut Chart** – Sales by category
- **Slicer** – Region filter for interactivity
- **Cards** - Sales and Profit

## 💡 Key Insights
1. Sales peaked in March and November, indicating strong seasonal performance.
2. West region consistently outperformed others in total sales.
3. Technology category generated the highest revenue.
4. Central region underperformed in Q2 when filtered using slicer.

## 📁 Files Included
- `sales performance dashboard.pbix` – Power BI file
- `Superstore_Sales_Cleaned.csv` – Cleaned dataset (with reformatted date)
- `Sales_Performance_Dashboard_Presentation.pptx` – Final presentation file
- `README.md` – Project documentation
- `dashboard screenshot.png` - Dashboard Screenshot
- Original and Cleaned data in csv format
