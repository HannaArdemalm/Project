import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data into a Pandas DataFrame
file_path = 'siren_data_train.csv'
df = pd.read_csv(file_path)

# Exclude 'near_fid' and 'near_angle' as they might not be suitable for certain plots
features_to_plot = df.columns.difference(['near_fid', 'near_angle', 'heard'])

# Plot 'heard' as a function of the other columns
for feature in features_to_plot:
    plt.figure(figsize=(10, 6))
    
    if df[feature].dtype == 'object':
        # Categorical feature: Bar plot
        sns.countplot(x=feature, hue='heard', data=df)
    else:
        # Numerical feature: Box plot
        sns.boxplot(x='heard', y=feature, data=df)
    
    plt.title(f'Heard as a function of {feature}')
    plt.xlabel(f'Is the siren heard?')
    plt.ylabel('Count' if df[feature].dtype == 'object' else feature)
    plt.legend(title='Heard', labels=['No', 'Yes'])
    plt.show()

