from crewai.tools import tool

# Navigation Tools
@tool("get_navigation_results")
def get_navigation_results(ID: str, room: str) -> dict:
    """
    Get the result of the navigation task.

    Args:
        ID (str): The ID of the HCW
        room (str): The room number of the patient

    Returns:
        dict: Dictionary containing location, path planned, and any issues reported
    """
    return {"Location": "Location of the human care worker #80 is at (Hallway B, near Nurse Station 2), and the patient room is at (ER-12).",
            "Path Planned": "Proceeding from Hallway B, turning left at Intersection C, then moving straight past ER-10 and ER-11 to reach ER-12.",
            "Issue Reported": "HCW #80 is currently unavailable due to an urgent call. Attempted contact, but no response."
    }

# Onboarding Info Collection Tools
@tool("get_onboarding_information") 
def get_onboarding_information(ID: str) -> dict:
    """
    Get the information for HCW onboarding.

    Args:
        ID (str): The ID of the HCW

    Returns:
        dict: Dictionary containing ID, name, specialty, experience, 
              patient room number, time of arrival, and any issues reported
    """
    # Function logic here
    return {
        "ID": "#90",
        "name": "Dr. XXX",
        "specialty": "Emergency Physician - Trauma & Critical Care", 
        "experience": "10 years",
        "patient_room_number": "ER-12",
        "time_of_arrival": "2025-04-01T14:30:00Z",
        "Issue Reported": None
    }

# Information Display Tools
@tool("get_display_information")
def get_display_information() -> dict:
    """
    Get information to be shared on the info sharing display.

    Returns:
        dict: Dictionary containing role assignments, patient room number,
              patient condition and any issues
    """
    return {
        "Role Assignment": {
            "HCW": {
                "HCW #01": "Human Leader",
                "HCW #72": "Physician", 
                "HCW #90": "Physician"
            },
            "Robot": {
                "Robot #01": "Nurse",
                "Robot #02": "Technician"
            }
        },
        "patient_room_number": "ER-12",
        "patient_condition": "Severe Trauma",
        "Issue Reported": None
    }
