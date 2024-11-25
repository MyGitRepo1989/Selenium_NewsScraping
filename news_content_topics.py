import transformers
import pandas as pd
from transformers import pipeline
classifier = pipeline("text-classification", model="classla/multilingual-IPTC-news-topic-classifier", device=-1, max_length=512, truncation=True)


# Read the CSV file
df = pd.read_csv("new_content.csv")

# Initialize an empty list to store classification results
results_list = []

# Iterate through the content in the DataFrame
for index, row in df.iterrows():
    story = row['content_scraped']
    url = row['URL']  # Assuming the 'URL' column exists in the original DataFrame
    title = row.get('Title', None)  # Use `.get()` if 'Title' column might not exist

    # Classify the story
    try:
        classification_results = classifier(str(story))  # Convert to string to avoid errors
        for result in classification_results:
            label = result.get('label', None)
            score = result.get('score', None)
            print(f"Story: {story}\n{label,score}\n __________________")
            # Append the extracted information to results_list
            results_list.append({
                'URL': url,
                'Title': title,
                'content_scraped': story,
                'Label': label,
                'Score': score
            })
    except Exception as e:
        print(f"Error processing story: {story}\n{e}")
        # If classification fails, append None values
        results_list.append({
            'URL': url,
            'Title': title,
            'content_scraped': story,
            'Label': None,
            'Score': None
        })

# Convert the results_list to a DataFrame
df2 = pd.DataFrame(results_list)

# Merge the new DataFrame with the original DataFrame
merged_df = df.merge(df2, on=['URL', 'Title', 'content_scraped'], how='left')

# Save the merged DataFrame to a new CSV file
merged_df.to_csv("classified_news.csv", index=False)

print("Classification and saving completed.")



print("done")