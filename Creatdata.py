import pandas as pd

# อ่านไฟล์ Excel
file_path = '/Users/np_sut/project_python_github/Thermal_modeling_2024/Thermal_modeling.csv'

# อ่านข้อมูล
df = pd.read_csv(file_path)

# 1. กรองข้อมูล
high_sales = df[df['Sales'] > 1000]

# 2. คำนวณยอดขายรวมตามภูมิภาค
sales_by_region = df.groupby('Region')['Sales'].sum()

# 3. บันทึกผลลัพธ์
high_sales.to_csv('high_sales.csv', index=False)
sales_by_region.to_csv('sales_by_region.csv')

print("การประมวลผลข้อมูลเสร็จสิ้น")