from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from config import secure_connect_path
from keys import CLIENT_SECRET,CLIENT_ID
from query_set import query_dict
from translater import g_translation_function_mr_en,g_translation_function_mr_hi

#configs
cloud_configs= {
        'secure_connect_bundle': secure_connect_path
}
print("\nConnecting to Cassandra...\n")

auth_provider = PlainTextAuthProvider(CLIENT_ID,CLIENT_SECRET)
cluster = Cluster(cloud=cloud_configs, auth_provider=auth_provider)
session = cluster.connect()

print("\nConnected to cluster\n")

def insert_data_for_dataset(data):
        try:
                row = session.execute(f"""INSERT INTO dev."3" ("mrtext","English","Hindi") VALUES ('{data}', '','');""")
        except Exception as e:
                print(e)
                print("\nError in adding data to cassandra\n")