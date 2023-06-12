import os
from pynaturalist import API


# Set up your iNaturalist API credentials
INATURALIST_USERNAME = 'your_username'
INATURALIST_PASSWORD = 'your_password'


# Initialize the API client
api = API()

# Log in to iNaturalist
api.login(username=INATURALIST_USERNAME, password=INATURALIST_PASSWORD)


def upload_image_to_inaturalist(image_path):
    # Upload the image to iNaturalist
    observation = api.create_observation(photo_path=image_path)

    # Retrieve the observation ID
    observation_id = observation['id']

    # Get computer vision species recommendations for the observation
    recommendations = api.get_computer_vision_recommendations(observation_id=observation_id)

    # Extract the recommended species
    recommended_species = [rec['taxon']['name'] for rec in recommendations]

    return recommended_species


# Path to your image file
image_path = 'path_to_your_image.jpg'

# Upload the image and get species recommendations
species_recommendations = upload_image_to_inaturalist(image_path)

# Print the recommended species
print("Recommended species:")
for species in species_recommendations:
    print(species)
