"""
03_Assortment_Recommendation.py
Purpose:
- Recommend the best product assortment for each store based on weighted score
- Uses Units Sold, Revenue, and Profit to generate a composite score
"""

# STEP 1: IMPORTS
import pandas as pd
import os

# STEP 2: LOAD DATA
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # folder of this script
data_path = os.path.join(BASE_DIR, "../Data/final_prepared.csv")

df = pd.read_csv(data_path, parse_dates=["date"])
print("✅ Data Loaded Successfully!")
print("Rows:", df.shape[0], "Columns:", df.shape[1])

# STEP 3: CREATE WEIGHTED SCORE
df["weighted_score"] = (
    (df["units_sold"] * 0.40) +
    (df["revenue"] * 0.30) +
    (df["profit"] * 0.30)
)

print("✅ Weighted score column added!")

# STEP 4: STORE-WISE TOP 10 PRODUCT RECOMMENDATION
store_reco = df.groupby(["store_type", "category"], as_index=False).agg(
    total_units=("units_sold", "sum"),
    total_revenue=("revenue", "sum"),
    total_profit=("profit", "sum"),
    total_weighted_score=("weighted_score", "sum")
)

store_reco = store_reco.sort_values(["store_type", "total_weighted_score"], ascending=[True, False])

top_n = 10
final_reco = store_reco.groupby("store_type").head(top_n)

print("\n✅ Top 10 Recommended Categories per Store Type:")
print(final_reco.head(20))

# STEP 5: SAVE OUTPUT
output_path = os.path.join(BASE_DIR, "../Outputs/store_assortment_recommendation.csv")
final_reco.to_csv(output_path, index=False)
print(f"\n🎉 Assortment file saved at: {output_path}")

print("\n🚀 Process Completed Successfully!")
