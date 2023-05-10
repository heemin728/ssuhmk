import pandas as pd

# Read Csv file and store it into 'data' dataFrame.
data = pd.read_csv('train_data/train_task_3_4.csv')

# Group the data by QuestionId and calculate the mean of 'isCorreect' column
# and 'UserID' column for each group . Then store the result into 'quality_data' dataFrame.
quality_data = data.groupby('QuestionId').agg({'IsCorrect': 'mean', 'UserId': 'count'}).reset_index()

# Rename the columns..
quality_data.rename(columns={'IsCorrect': 'Accuracy', 'UserId': 'AnswerCount'}, inplace=True)

# Calculate qualityScore using mutiplying the accuracy and answercount columns 
quality_data['QualityScore'] = quality_data['Accuracy'] * quality_data['AnswerCount']

# Calculate Ranking of qualitysocre bt ascending order using rank function
quality_data['Ranking'] = quality_data['QualityScore'].rank(ascending=False).astype(int)

sorted_data = quality_data.sort_values('QualityScore', ascending=False)

# Drop useless columns in sorted_data
sorted_data = sorted_data.drop(['Accuracy', 'AnswerCount', 'QualityScore'], axis=1)

# Save outputs to csv file
sorted_data.to_csv('20203083.csv', index=False)
