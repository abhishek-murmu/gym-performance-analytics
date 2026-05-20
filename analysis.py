import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns   

df= pd.read_excel('gym_logs.xlsx')

#convert the date column to datetime format
df['Duration_min'] = pd.to_numeric(
    df['Duration_min'], errors='coerce'

)

#    -------------------------------
#  BASIC ANALYSIS
#    -------------------------------    

print(df.head())

print("\nAverage Workout Duration:")
print(df['Duration_min'].mean())    

print("\nLongest Workout:")
print(df['Duration_min'].max())

print("\nTop Weight Per Exercise:")
print(df.groupby('Exercise')['Weight_kg'].max())

#    -------------------------------
#  VISUALIZATION
# -----------------------------------

exercise_stats = df.groupby('Exercise').agg({
    'Sets':'mean',
    'Reps':'mean',
    'Weight_kg':'mean',
    'Duration_min':'mean'
})

plt.figure(figsize=(10, 6))

sns.heatmap(
    exercise_stats,
    annot= True,
    cmap='coolwarm',
    linewidths=0.5,
    fmt=".1f"

)

plt.title("Gym Workout Analysis")

plt.show()

#--------------------------------
#WORKOUT FREQUNCY ANALYSIS
#--------------------------------

workout_days = df.groupby('Date').size()

plt.figure(figsize=(12, 5))

workout_days.plot(kind='line', marker='o')

plt.title("Workout Frequency Over Time")
plt.xlabel("Date")          
plt.ylabel("Number of Workouts")

plt.tight_layout()

plt.show()

#--------------------------------
# IMPROVEMENT COMPARISON
#--------------------------------

date = sorted(df['Date'].unique())

if len(date) >= 2:
    latest_date = date[-1]
    previous_date = date[-2]

    latest_workout = df[df['Date'] == latest_date]
    previous_workout = df[df['Date'] == previous_date]  

# Weight compariosn
latest_weight = latest_workout.groupby('Exercise')['Weight_kg'].max()
previous_weight = previous_workout.groupby('Exercise')['Weight_kg'].max()

print("\nWeight Improvement Report\n")

for exercise in latest_weight.index:
    if exercise in previous_weight.index:

        diff = latest_weight[exercise] - previous_weight[exercise]
        
        if diff > 0 :
            print(f"{exercise}: +{diff:.1f} kg improvement")

        elif diff < 0:
            print(f"{exercise}: {diff:.1f} kg decrease")

        else:
            print(f"{exercise}: No change in weight")

#Reps compariosn
latest_reps = latest_workout.groupby('Exercise')['Reps'].max()
previous_reps = previous_workout.groupby('Exercise')['Reps'].max()

print("\nReps Improvement Report\n")

for exercise in latest_reps.index:

   if exercise in previous_reps.index:
       
       diff = latest_reps[exercise] - previous_reps[exercise]

       if diff > 0:
           print(f"{exercise}: +{diff} reps improvement")

       elif diff < 0:
           print(f"{exercise}:{diff} reps decrease")
       else:
           print(f"{exercise}: No change in reps")

