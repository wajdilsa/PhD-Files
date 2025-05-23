# -*- coding: utf-8 -*-
"""Yemen Case Simulation

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wgHuvWy_YBhOBNLbiJq3NByUlQjeLENH
"""

import random
import matplotlib.pyplot as plt

def simulate_smart_city(years, initial_population, energy_demand, water_availability,
                        waste_generation, building_efficiency, public_transport_share,
                        green_infrastructure, temp_increase, rainfall_variability,
                        policy_effectiveness, community_engagement):
    population = initial_population
    water_stress = population / water_availability
    waste_accumulated = 0
    renewable_energy_penetration = 0  # Initialize renewable energy penetration

    results = {
        'population': [],
        'emissions': [],
        'water_stress': [],
        'waste_accumulated': []
    }

    for year in range(years):
        # Population Growth
        population_growth = population * random.uniform(0, 0.05)  # 0-5% growth rate
        population += population_growth

        # Energy Demand and Emissions
        energy_demand *= random.uniform(1, 1.1)  # 0-10% growth rate
        energy_demand *= (1 - building_efficiency / 10)  # Adjust for building efficiency
        renewable_energy_penetration = random.uniform(0, 1)  # 0-100% penetration
        emissions = energy_demand * (1 - renewable_energy_penetration) * (1 - public_transport_share)  # Adjust for public transport

        # Water Stress
        water_availability *= (1 + rainfall_variability)  # Adjust for rainfall variability
        water_stress = population / water_availability

        # Waste Accumulation
        waste_generated = population * waste_generation * (1 - green_infrastructure)  # Adjust for green infrastructure
        waste_accumulated += waste_generated * 365  # Annual accumulation

        # Climate Change Impact
        temp_increase += random.uniform(0, 0.04)  # Simulate gradual temperature increase
        energy_demand *= (1 + temp_increase / 100)  # Increased demand due to temperature

        # Policy and Community Impact
        emissions *= (1 - policy_effectiveness/10)  # Policy reduces emissions
        waste_accumulated *= (1 - community_engagement/10)  # Engagement reduces waste

        # Store Results
        results['population'].append(population)
        results['emissions'].append(emissions)
        results['water_stress'].append(water_stress)
        results['waste_accumulated'].append(waste_accumulated)

    return results

# Example Simulation
years = 20
initial_population = 100000
energy_demand = 500000  # kWh
water_availability = 1000000  # cubic meters
waste_generation = 1  # kg per capita per day
building_efficiency = 5
public_transport_share = 0.3
green_infrastructure = 0.1
temp_increase = 0
rainfall_variability = 0
policy_effectiveness = 6
community_engagement = 7

# Multiple Iterations
num_iterations = 100
all_results = {key: [[] for _ in range(num_iterations)] for key in ['population', 'emissions', 'water_stress', 'waste_accumulated']}

for i in range(num_iterations):
    results = simulate_smart_city(years, initial_population, energy_demand, water_availability,
                                  waste_generation, building_efficiency, public_transport_share,
                                  green_infrastructure, temp_increase, rainfall_variability,
                                  policy_effectiveness, community_engagement)
    for key in results:
        all_results[key][i] = results[key]

# Plotting Results
plt.figure(figsize=(12, 8))

for key in all_results:
    plt.subplot(2, 2, list(all_results.keys()).index(key) + 1)
    for i in range(num_iterations):
        plt.plot(range(years), all_results[key][i], alpha=0.5)  # Plot each iteration with transparency
    plt.xlabel('Year')
    plt.ylabel(key)
    plt.title(f'Simulated {key} Over Time')

plt.tight_layout()
plt.show()




# Sensitivity Analysis for building_efficiency
efficiency_values = np.linspace(0, 10, 11)  # Test efficiency from 0 to 10%
emissions_results = []

for efficiency in efficiency_values:
    results = simulate_smart_city(years, initial_population, energy_demand, water_availability,
                                  waste_generation, efficiency, public_transport_share,
                                  green_infrastructure, temp_increase, rainfall_variability,
                                  policy_effectiveness, community_engagement)
    emissions_results.append(results['emissions'])

# Plotting
plt.figure()
for i in range(num_iterations):
    for j, efficiency in enumerate(efficiency_values):
        plt.plot(range(years), emissions_results[j][i], alpha=0.3, label=f'Efficiency: {efficiency:.1f}%' if i == 0 else "")
plt.xlabel('Year')
plt.ylabel('Emissions')
plt.title('Sensitivity Analysis: Impact of Building Efficiency on Emissions')
plt.legend()
plt.show()



import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Data for the chart
data = {
    'Demographic Group': ['Internally Displaced Persons (IDPs)', 'Youth (under 25 years old)', 'Elderly (60 years and older)', 'Women', 'Men'],
    'Percentage': [15, 65, 5, 49, 51]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create the bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x='Demographic Group', y='Percentage', data=df, palette='viridis')

# Add title and labels
plt.title('Demographic Distribution in Sana\'a City')
plt.xlabel('Demographic Group')
plt.ylabel('Percentage')

# Rotate x labels for better readability
plt.xticks(rotation=45, ha='right')

# Show the chart
plt.tight_layout()

plt.show()

import matplotlib.pyplot as plt

# Data from your table
components = ['Technology & Infrastructure', 'Energy & Environment', 'Water Resources',
               'Urban Planning & Infrastructure', 'Health & Well-being',
               'Socio Economic Development', 'Governance & Policy',
               'Education & Research', 'AI & Machine Learning']
num_studies = [39, 26, 14, 5, 26, 6, 10, 9, 10]

# Plotting
plt.figure(figsize=(10, 6))  # Adjust figure size as needed
plt.bar(components, num_studies, color='skyblue')
plt.xlabel('Main Component')
plt.ylabel('Number of Case Studies')
plt.title('Distribution of Case Studies by Main Component in Yemen')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.show()

import spacy
from sentence_transformers import SentenceTransformer
import nltk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load spaCy and SentenceTransformer models
nlp = spacy.load("en_core_web_md")
embedder = SentenceTransformer('all-mpnet-base-v2')

# Load case study data (replace with your actual data sources)
case_studies = {
    "Sana'a": "text_from_sanaa_case_study.txt",
    "Baghdad": "text_from_baghdad_case_study.txt",
    "Dubai": "text_from_dubai_case_study.txt",
    "London": "text_from_london_case_study.txt"
}

# Function to preprocess text
def preprocess_text(text):
    doc = nlp(text)
    return [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]

# Function to generate embeddings
def get_embeddings(text):
    tokens = preprocess_text(text)
    return embedder.encode(' '.join(tokens))

# Create a dataframe to store case study data and embeddings
data = []
for city, text_file in case_studies.items():
    with open(text_file, 'r') as file:
        text = file.read()
        embedding = get_embeddings(text)
        data.append({"City": city, "Text": text, "Embedding": embedding})
df = pd.DataFrame(data)

# Analyze Themes (Example: Keyword Extraction)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def extract_keywords(text, num_keywords=10):
    words = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(words)
    keywords = [word for word, pos in tagged if pos.startswith('NN')]  # Nouns
    freq_dist = nltk.FreqDist(keywords)
    return freq_dist.most_common(num_keywords)

df['Keywords'] = df['Text'].apply(extract_keywords)

# Visualize Themes (Example: Word Clouds)
from wordcloud import WordCloud

for city in case_studies:
    text = ' '.join(df[df['City'] == city]['Text'].iloc[0])
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.title(f"Word Cloud for {city}")
    plt.show()

import numpy as np

# ... (your existing simulate_smart_city function)

# Sensitivity Analysis for building_efficiency
efficiency_values = np.linspace(0, 10, 11)  # Test efficiency from 0 to 10%
emissions_results = []

for efficiency in efficiency_values:
    results = simulate_smart_city(years, initial_population, energy_demand, water_availability,
                                  waste_generation, efficiency, public_transport_share,
                                  green_infrastructure, temp_increase, rainfall_variability,
                                  policy_effectiveness, community_engagement)
    emissions_results.append(results['emissions'])

# Plotting
plt.figure()
for i in range(num_iterations):
    for j, efficiency in enumerate(efficiency_values):
        plt.plot(range(years), emissions_results[j][i], alpha=0.3, label=f'Efficiency: {efficiency:.1f}%' if i == 0 else "")
plt.xlabel('Year')
plt.ylabel('Emissions')
plt.title('Sensitivity Analysis: Impact of Building Efficiency on Emissions')
plt.legend()
plt.show()

import random
import matplotlib.pyplot as plt
import numpy as np

def simulate_smart_city(years, initial_population, energy_demand, water_availability,
                        waste_generation, building_efficiency, public_transport_share,
                        green_infrastructure, temp_increase, rainfall_variability,
                        policy_effectiveness, community_engagement):
    population = initial_population
    water_stress = population / water_availability
    waste_accumulated = 0
    renewable_energy_penetration = 0  # Initialize renewable energy penetration

    results = {
        'population': [],
        'emissions': [],
        'water_stress': [],
        'waste_accumulated': []
    }

    for year in range(years):
        # Population Growth
        population_growth = population * random.uniform(0, 0.05)  # 0-5% growth rate
        population += population_growth

        # Energy Demand and Emissions
        energy_demand *= random.uniform(1, 1.1)  # 0-10% growth rate
        energy_demand *= (1 - building_efficiency / 10)  # Adjust for building efficiency
        renewable_energy_penetration = random.uniform(0, 1)  # 0-100% penetration
        emissions = energy_demand * (1 - renewable_energy_penetration) * (1 - public_transport_share)  # Adjust for public transport

        # Water Stress
        water_availability *= (1 + rainfall_variability)  # Adjust for rainfall variability
        water_stress = population / water_availability

        # Waste Accumulation
        waste_generated = population * waste_generation * (1 - green_infrastructure)  # Adjust for green infrastructure
        waste_accumulated += waste_generated * 365  # Annual accumulation

        # Climate Change Impact
        temp_increase += random.uniform(0, 0.04)  # Simulate gradual temperature increase
        energy_demand *= (1 + temp_increase / 100)  # Increased demand due to temperature

        # Policy and Community Impact
        emissions *= (1 - policy_effectiveness / 10)  # Policy reduces emissions
        waste_accumulated *= (1 - community_engagement / 10)  # Engagement reduces waste

        # Store Results
        results['population'].append(population)
        results['emissions'].append(emissions)
        results['water_stress'].append(water_stress)
        results['waste_accumulated'].append(waste_accumulated)

    return results

# Example Simulation
years = 20
initial_population = 100000
energy_demand = 500000  # kWh
water_availability = 1000000  # cubic meters
waste_generation = 1  # kg per capita per day
building_efficiency = 5
public_transport_share = 0.3
green_infrastructure = 0.1
temp_increase = 0
rainfall_variability = 0
policy_effectiveness = 6
community_engagement = 7

# Multiple Iterations
num_iterations = 100
all_results = {key: [[] for _ in range(num_iterations)] for key in ['population', 'emissions', 'water_stress', 'waste_accumulated']}

for i in range(num_iterations):
    results = simulate_smart_city(years, initial_population, energy_demand, water_availability,
                                  waste_generation, building_efficiency, public_transport_share,
                                  green_infrastructure, temp_increase, rainfall_variability,
                                  policy_effectiveness, community_engagement)
    for key in results:
        all_results[key][i] = results[key]

# Plotting Results
plt.figure(figsize=(12, 8))

for key in all_results:
    plt.subplot(2, 2, list(all_results.keys()).index(key) + 1)
    for i in range(num_iterations):
        plt.plot(range(years), all_results[key][i], alpha=0.5)  # Plot each iteration with transparency
    plt.xlabel('Year')
    plt.ylabel(key)
    plt.title(f'Simulated {key} Over Time')

plt.tight_layout()
plt.show()

# Sensitivity Analysis for building_efficiency
efficiency_values = np.linspace(0, 10, 11)  # Test efficiency from 0 to 10%
emissions_results = []

for efficiency in efficiency_values:
    emissions_list = []
    for _ in range(num_iterations):
        results = simulate_smart_city(years, initial_population, energy_demand, water_availability,
                                      waste_generation, efficiency, public_transport_share,
                                      green_infrastructure, temp_increase, rainfall_variability,
                                      policy_effectiveness, community_engagement)
        emissions_list.append(results['emissions'])
    emissions_results.append(emissions_list)

# Plotting
plt.figure()
for j, efficiency in enumerate(efficiency_values):
    for i in range(num_iterations):
        if i == 0:  # Add label only for the first plot in the group
            plt.plot(range(years), emissions_results[j][i], alpha=0.3, label=f'Efficiency: {efficiency:.1f}%')
        else:
            plt.plot(range(years), emissions_results[j][i], alpha=0.3)
plt.xlabel('Year')
plt.ylabel('Emissions')
plt.title('Sensitivity Analysis: Impact of Building Efficiency on Emissions')
plt.legend()
plt.show()