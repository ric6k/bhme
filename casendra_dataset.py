from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from config import secure_connect_path

import os

os.system("gdown 1QNrHVfmo3PZAPJTgX0xy_CIZwP7fwWmP >/dev/null 2>&1")


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

# Fetch 1000 rows from the table
def fetch_data_from_cassandra():
    data = session.execute("""select * from dev."3" where "English" = '' limit 1000 ALLOW FILTERING;""")
    lenght = 0
    for row in data:
        lenght += 1
        mrtext = row[0]
        # translate the text to English & Hindi and add it to the table
        add_data_to_cassandra(mrtext)
        print(f"\n {lenght}  \n")
    print(f"\nTotal number of rows translated is {lenght}\n")
    
# Translate the text to Hindi & Marathi
def add_data_to_cassandra(mrtext):
    
    english = g_translation_function_mr_en(mrtext)
    hindi = g_translation_function_mr_hi(mrtext)
    try:
        # Insert the translated text into the table
        english = english.replace("'","")
        hindi = hindi.replace("'","")
        query_result = session.execute(f"""UPDATE dev."3" SET "English" = '{english}', "Hindi" = '{hindi}' WHERE mrtext = '{mrtext}';""")
    except Exception as e:
        print(e)
        print("\nError in adding data to cassandra\n")
    #print(f"\nTranslated text is {english} {hindi}\n")


fetch_data_from_cassandra()