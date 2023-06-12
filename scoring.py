from pynaturalist import API

# Set up your iNaturalist API credentials
INATURALIST_USERNAME = 'your_username'
INATURALIST_PASSWORD = 'your_password'

# Initialize the API client
api = API()

# Log in to iNaturalist
api.login(username=INATURALIST_USERNAME, password=INATURALIST_PASSWORD)


def get_user_observation_count_within_radius(username, taxon_id, latitude, longitude, radius):
    # Get the observations of the taxon within the specified circular area made by the user
    observations = api.get_observations(
        taxon_id=taxon_id,
        geo=True,
        lat=latitude,
        lng=longitude,
        radius=radius,
        user_login=username
    )

    return len(observations)


# Provide the username, taxon ID, latitude, and longitude for the center point
desired_username = 'target_user'
desired_taxon_id = 12345
center_latitude = 37.7749
center_longitude = -122.4194

# Define the radii in meters
radii = [10, 100, 1000, 10000, 100000, 1000000, 10000000]

# Iterate over the radii and get the observation count for the user and taxon
for radius in radii:
    observation_count = get_user_observation_count_within_radius(
        desired_username, desired_taxon_id, center_latitude, center_longitude, radius
    )
    print(f"Observation count for user {desired_username} and taxon ID {desired_taxon_id} within {radius} meters: {observation_count}")

# Get the observation count for the user and taxon without a specific radius (all observations)
all_observation_count = get_user_observation_count_within_radius(
    desired_username, desired_taxon_id, center_latitude, center_longitude, None
)
print(f"Observation count for user {desired_username} and taxon ID {desired_taxon_id} of all observations: {all_observation_count}")
