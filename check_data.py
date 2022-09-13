from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from config import secure_connect_path
from keys import CLIENT_SECRET,CLIENT_ID
from query_set import query_dict
from translater import g_translation_function_mr_en,g_translation_function_mr_hi
from tqdm import tqdm
import os
import time

os.system("gdown 1QNrHVfmo3PZAPJTgX0xy_CIZwP7fwWmP >/dev/null 2>&1")

#configs
cloud_configs= {
        'secure_connect_bundle': secure_connect_path
}

print("\nConnecting to Cassandra...\n")

auth_provider = PlainTextAuthProvider(CLIENT_ID,CLIENT_SECRET)
cluster = Cluster(cloud=cloud_configs, auth_provider=auth_provider)
session = cluster.connect()

print("\nConnected to cluster\n")

row1 = session.execute("""select Count(*) from dev."3" where "English" = '' ALLOW FILTERING;""")
row2 = session.execute("""select Count(*) from dev."3";""")

if row1 or row2:
    print("\nRemaining to do",row1.one()[0],"\n")
    print("\nDone till now",row2.one()[0]-row1.one()[0],"\n")
else:
    print("An error occurred.")
    
