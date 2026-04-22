# Save the cleaned and preprocessed dataset for future model training and analysis.

import os

output_dir = "../data/processed"
os.makedirs(output_dir, exist_ok=True)

df.to_csv(os.path.join(output_dir, "processed_paysim.csv"), index=False)

print(df.head())
