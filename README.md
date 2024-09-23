# AI-Powered Grant Allocation Tool

This tool helps philanthropic organizations rank grant applicants based on customizable scoring criteria such as impact, financial health, and geographic focus. By providing a CSV file of applicants' data, the tool calculates weighted scores for each applicant and returns a ranked recommendation list for grant distribution.

## Features
- Customizable weighting for impact, financial health, and geographic focus.
- Easy-to-use CSV input format.
- Sorted recommendations based on calculated scores.
- Simple, adaptable codebase for further customization.

## How It Works
1. **Input CSV**: Upload a CSV file with columns for `applicant_name`, `impact_score`, `financial_health_score`, and `geographic_focus_score`.
2. **Weighted Scoring**: The tool applies a weighted score based on user-defined criteria.
3. **Output**: A sorted recommendation list based on the calculated score is provided, helping organizations prioritize grant funding.

## Example
Here’s an example of the CSV structure required for the tool:

```csv
applicant_name,impact_score,financial_health_score,geographic_focus_score
Organization A,8,7,9
Organization B,9,6,8
Organization C,7,8,6
```

## How to Use
1. Clone or download the repository.
2. Prepare your CSV file following the example structure.
3. Run the Python script:
   ```bash
   python grant_allocation_tool.py
   ```
4. Adjust the weights in the script to reflect your organization’s priorities:
   ```python
   weights = {
       'impact_score': 0.5,
       'financial_health_score': 0.3,
       'geographic_focus_score': 0.2
   }
   ```

## Requirements
- Python 3.x
- `pandas` library

To install dependencies, run:
```bash
pip install pandas
```

## License
This project is licensed under the [MIT License](LICENSE).

## Contributing
Feel free to submit issues or pull requests if you have any improvements or suggestions!
