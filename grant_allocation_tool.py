
import pandas as pd

# Define the scoring function
def calculate_score(applicant, weights):
    """
    Calculate a weighted score for each grant applicant.
    :param applicant: Dictionary containing applicant data
    :param weights: Dictionary containing the weight for each criterion
    :return: Weighted score
    """
    score = (applicant['impact_score'] * weights['impact_score'] +
             applicant['financial_health_score'] * weights['financial_health_score'] +
             applicant['geographic_focus_score'] * weights['geographic_focus_score'])
    return score

# Function to process the CSV and return recommendations
def recommend_grants(applicants_file, weights):
    """
    Recommend grants based on applicants' data and custom scoring criteria.
    :param applicants_file: Path to the CSV file containing applicants' data
    :param weights: Dictionary of scoring weights for each criterion
    :return: DataFrame of applicants with their calculated scores
    """
    # Load applicants data from CSV
    applicants = pd.read_csv(applicants_file)
    
    # Apply the scoring function to each applicant
    applicants['calculated_score'] = applicants.apply(lambda x: calculate_score(x, weights), axis=1)
    
    # Sort applicants based on the calculated score
    sorted_applicants = applicants.sort_values(by='calculated_score', ascending=False)
    
    return sorted_applicants

# Example weights
weights = {
    'impact_score': 0.5,
    'financial_health_score': 0.3,
    'geographic_focus_score': 0.2
}

# Example CSV data (simulating what would be in the CSV file for testing)
data = {
    'applicant_name': ['Organization A', 'Organization B', 'Organization C'],
    'impact_score': [8, 9, 7],
    'financial_health_score': [7, 6, 8],
    'geographic_focus_score': [9, 8, 6]
}

# Convert the sample data into a CSV for testing
df = pd.DataFrame(data)
df.to_csv("sample_applicants.csv", index=False)

# Test the recommendation function
sorted_applicants = recommend_grants("sample_applicants.csv", weights)

print(sorted_applicants)
