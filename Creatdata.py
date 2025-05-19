import pandas as pd

# อ่านไฟล์ Excel
file_path = '/Users/np_sut/project_python_github/Thermal_modeling_2024/Thermal_modeling.xlsx'

# อ่านทั้งหมด sheet
all_sheets = pd.read_excel(file_path, sheet_name=None)
print("Sheets in workbook:", list(all_sheets.keys()))

# อ่าน sheet เฉพาะ
df = pd.read_excel(file_path, sheet_name='Sheet1')

# แสดงข้อมูล
print("\nData in Sheet1:")
print(df.head())  # แสดง 5 แถวแรก

# แสดงสถิติพื้นฐาน
print("\nSummary statistics:")
print(df.describe())
