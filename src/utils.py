# Data Validation Function

def data_validate(df, name="Dataset"):
    print(f"\n---- {name} Validation ----")

    print("Shape:", df.shape)

    # Check missing values
    if df.isna().sum().sum() == 0:
        print("No missing values")
    else:
        print("Missing values:")
        print(df.isna().sum())

    # Check duplicates
    dup = df.duplicated().sum()
    print("Duplicates:", dup)

    print("Columns:", list(df.columns))
    print("----------------------------")
