def calculate_total_score(scores: dict) -> int:
    """
    Calculates the total score for an FSE based on individual section scores.

    Args:
        scores: A dictionary containing the scores for each part:
                {
                    "documentation": int,
                    "personal_hygiene": int,
                    "material_sourcing": int,
                    "water_sources_storage": int,
                    "waste_disposal": int,
                    "cleaning": int
                }

    Returns:
        The total score (out of 100).
    """
    total_score = (
        scores.get("documentation", 0) +
        scores.get("personal_hygiene", 0) +
        scores.get("material_sourcing", 0) +
        scores.get("water_sources_storage", 0) +
        scores.get("waste_disposal", 0) +
        scores.get("cleaning", 0)
    )
    return total_score

# Example usage (will be expanded later):
if __name__ == "__main__":
    sample_scores = {
        "documentation": 15,
        "personal_hygiene": 18,
        "material_sourcing": 17,
        "water_sources_storage": 8,
        "waste_disposal": 19,
        "cleaning": 7
    }
    total = calculate_total_score(sample_scores)
    print(f"Sample FSE Total Score: {total}/100")

    sample_fse_data_example = {
        "background_info": {
            "name": "The Delicious Place",
            "address": "123 Food Street, Kumasi",
            "manager_name": "Ama Mensah",
            "manager_contact": "0201234567",
            "date_of_assessment": "2023-10-27",
            "assessor_name": "Kwame Osei"
        },
        "scores": sample_scores,
        "total_score": None,
        "star_rating": None
    }

    # Calculate and update the total score in the main data structure
    sample_fse_data_example["total_score"] = calculate_total_score(sample_fse_data_example["scores"])
    print(f"Updated FSE Data with Total Score: {sample_fse_data_example['total_score']}")


def assign_star_rating(total_score: int) -> str:
    """
    Assigns a star rating based on the total score.

    Args:
        total_score: The total score achieved by the FSE (0-100).

    Returns:
        A string representing the star rating (e.g., "5 Stars", "1 Star").
    """
    if not 0 <= total_score <= 100:
        raise ValueError("Total score must be between 0 and 100.")

    if total_score >= 90:
        return "5 Stars"
    elif total_score >= 80:
        return "4 Stars"
    elif total_score >= 70:
        return "3 Stars"
    elif total_score >= 60:
        return "2 Stars"
    else:
        return "1 Star"

if __name__ == "__main__":
    # ... (previous example code remains the same)
    sample_scores = {
        "documentation": 15,
        "personal_hygiene": 18,
        "material_sourcing": 17,
        "water_sources_storage": 8,
        "waste_disposal": 19,
        "cleaning": 7
    }
    total = calculate_total_score(sample_scores)
    print(f"Sample FSE Total Score: {total}/100")

    star_rating = assign_star_rating(total)
    print(f"Sample FSE Star Rating: {star_rating}")

    sample_fse_data_example = {
        "background_info": {
            "name": "The Delicious Place",
            "address": "123 Food Street, Kumasi",
            "manager_name": "Ama Mensah",
            "manager_contact": "0201234567",
            "date_of_assessment": "2023-10-27",
            "assessor_name": "Kwame Osei"
        },
        "scores": sample_scores,
        "total_score": None,
        "star_rating": None
    }

    sample_fse_data_example["total_score"] = total # Use the already calculated total
    sample_fse_data_example["star_rating"] = star_rating # Use the already calculated star_rating
    print(f"Updated FSE Data: {sample_fse_data_example}")


def generate_assessment_message(fse_name: str, total_score: int, star_rating: str, manager_name: str, date_of_assessment: str) -> str:
    """
    Generates a formatted text message summarizing the assessment outcome.

    Args:
        fse_name: Name of the Food Service Establishment.
        total_score: The total score achieved.
        star_rating: The assigned star rating.
        manager_name: Name of the facility owner/manager.
        date_of_assessment: Date the assessment was conducted.

    Returns:
        A formatted string message.
    """
    message = (
        f"Dear {manager_name},\n\n"
        f"This message is to inform you about the recent food safety assessment for {fse_name} conducted on {date_of_assessment}.\n\n"
        f"Outcome:\n"
        f"- Total Score: {total_score}/100\n"
        f"- Rating: {star_rating}\n\n"
        f"Thank you for your cooperation.\n"
        f"KMA Environmental Health Unit & AAMUSTED Research Team."
    )
    return message

if __name__ == "__main__":
    # ... (previous example code)
    sample_scores = {
        "documentation": 15,
        "personal_hygiene": 18,
        "material_sourcing": 17,
        "water_sources_storage": 8,
        "waste_disposal": 19,
        "cleaning": 7
    }
    total = calculate_total_score(sample_scores)
    # print(f"Sample FSE Total Score: {total}/100") # Already printed

    star_rating = assign_star_rating(total)
    # print(f"Sample FSE Star Rating: {star_rating}") # Already printed

    sample_fse_data = { # Renamed for clarity from sample_fse_data_example
        "background_info": {
            "name": "The Delicious Place",
            "address": "123 Food Street, Kumasi",
            "manager_name": "Ama Mensah",
            "manager_contact": "0201234567",
            "date_of_assessment": "2023-10-27",
            "assessor_name": "Kwame Osei"
        },
        "scores": sample_scores,
        "total_score": total,
        "star_rating": star_rating
    }
    # print(f"Updated FSE Data: {sample_fse_data}") # Already printed

    assessment_message = generate_assessment_message(
        fse_name=sample_fse_data["background_info"]["name"],
        total_score=sample_fse_data["total_score"],
        star_rating=sample_fse_data["star_rating"],
        manager_name=sample_fse_data["background_info"]["manager_name"],
        date_of_assessment=sample_fse_data["background_info"]["date_of_assessment"]
    )
    print("\n--- Assessment Message ---")
    print(assessment_message)
