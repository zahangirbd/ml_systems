from pprint import pprint
from feast import FeatureStore
feature_store = FeatureStore('.')  # Initialize the feature store

# feature services are: driver_activity_v1, driver_activity_v2, driver_activity_v3
feature_service = feature_store.get_feature_service('driver_activity_v1')
feature_vector = feature_store.get_online_features(
	features = feature_service,
	entity_rows = [
		# {join_key: entity_value}
		{
			"driver_id": 1001,
			"val_to_add": 1000,
			"val_to_add_2": 2000,
		},
		{
			"driver_id": 1002,
			"val_to_add": 1001,
			"val_to_add_2": 2002,
		},
    ],
).to_dict()
pprint(feature_vector)	