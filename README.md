# Food Service Establishment (FSE) Compliance Rating System

## Overview

This project provides a Python script (`fse_assessment.py`) to assess and rate Food Service Establishments (FSEs) based on their compliance with food safety regulations. It calculates a total score from a checklist, assigns a star rating, and generates a summary message for the FSE owner/manager.

This system was developed to assist in the study: "ASSESSMENT OF FOOD SERVICE ESTABLISHMENTS COMPLIANCE WITH FOOD SAFETY REGULATIONS KUMASI METROPOLIS OF ASHANTI REGION, GHANA" by a final year student of Akenten Appiah-Menkah University of Skills Training and Entrepreneurial Development (AAMUSTED), in collaboration with the Environmental Health Unit of KMA.

## `fse_assessment.py` Script

The core logic of the assessment system is contained in `fse_assessment.py`.

### Running the Script

To run the script and see an example of its output:

```bash
python fse_assessment.py
```

This will execute the example usage within the script, demonstrating the calculation of a total score, assignment of a star rating, and generation of an assessment message based on sample data.

### Core Components

#### 1. FSE Data Structure

Each FSE is represented as a Python dictionary with the following structure:

```python
fse_data = {
    "background_info": {
        "name": "The Delicious Place",
        "address": "123 Food Street, Kumasi",
        "manager_name": "Ama Mensah",
        "manager_contact": "0201234567",
        "date_of_assessment": "2023-10-27",
        "assessor_name": "Kwame Osei"
    },
    "scores": {
        "documentation": 15,  # out of 20
        "personal_hygiene": 18, # out of 20
        "material_sourcing": 17, # out of 20
        "water_sources_storage": 8,  # out of 10
        "waste_disposal": 19,      # out of 20
        "cleaning": 7             # out of 10
    },
    "total_score": None,  # Calculated by the script
    "star_rating": None   # Assigned by the script
}
```

#### 2. `calculate_total_score(scores: dict) -> int`

-   **Purpose:** Calculates the total compliance score for an FSE.
-   **Input:** A dictionary (`scores`) containing the scores for each of the 6 checklist parts.
-   **Output:** The total score (out of 100).
-   **Scoring Breakdown:**
    -   Documentations: 20 marks
    -   Personal Hygiene of Food handlers: 20 marks
    -   Material sourcing: 20 marks
    -   Water Sources and Storage: 10 marks
    -   Waste Disposal: 20 marks
    -   Cleaning: 10 marks

#### 3. `assign_star_rating(total_score: int) -> str`

-   **Purpose:** Assigns a star rating based on the total score.
-   **Input:** The total score (0-100).
-   **Output:** A string representing the star rating.
-   **Star Rating Criteria:**
    -   **5 Stars:** 90-100
    -   **4 Stars:** 80-89
    -   **3 Stars:** 70-79
    -   **2 Stars:** 60-69
    -   **1 Star:** Below 60

#### 4. `generate_assessment_message(fse_name: str, total_score: int, star_rating: str, manager_name: str, date_of_assessment: str) -> str`

-   **Purpose:** Generates a formatted text message summarizing the assessment outcome for the facility owner/manager.
-   **Input:** FSE's name, total score, star rating, manager's name, and date of assessment.
-   **Output:** A formatted string message.

## Future Enhancements

Potential future enhancements include:
-   User interface for data entry (CLI, Web UI).
-   Persistent data storage (CSV, SQLite, or other databases).
-   Integration with SMS gateway services for automated message delivery.
-   Reporting and analytics features.
