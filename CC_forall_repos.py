import csv

import csvwriter as csvwriter
from  google.cloud import bigquery
from google.oauth2 import service_account
import google.auth
from google.cloud import bigquery_storage
import json
import pandas as pd

credentials = service_account.Credentials.from_service_account_file(
'C:\\Users\\ASUS\\Documents\\ResearchMaterial\\github-project-310921-189911271191.json')
project_id = 'github-project-310921'

bqclient = bigquery.Client(credentials=credentials, project=project_id)
bqstorageclient = bigquery_storage.BigQueryReadClient(credentials=credentials)
client = bigquery.Client(credentials= credentials,project=project_id)

print(client.project)

query_job = bqclient.query("""
    SELECT *
    FROM github-project-310921.githubproject_rawdataset.2011_data where type='PushEvent' """).result().to_dataframe(bqstorage_client=bqstorageclient)


print(query_job.loc[:,"repo"])
print(pd.json_normalize(query_job.loc[:,"repo"]))
print(query_job.head())
df1 = pd.DataFrame(query_job['repo'].values.tolist())
df1.columns = 'repo.'+ df1.columns
print(df1.head())

df3 = pd.DataFrame(query_job['actor'].values.tolist())
df3.columns = 'actor.'+ df3.columns
print(df3.head())

df4 = pd.DataFrame(query_job['org'].values.tolist())
df4.columns = 'org.'+ df4.columns
print(df4.head())

col = query_job.columns.difference(['repo','actor','org'])
df = pd.concat([query_job[col], df1,df3,df4],axis=1)
print (df)

# df.to_csv(r'C:\\Users\\ASUS\\Documents\\ResearchMaterial\\CitingRef\\gcp.csv',index=False)

print(df['actor.id'].head())
a1_grpbyrepoid=df.groupby(["repo.id","actor.id"])["actor.id"].count().reset_index(name="push_eventsby_contributor")

print(a1_grpbyrepoid.head())


#def core_Contributors(a1_grpbyrepoid):
#     a3=singlerepo_df.set_index('actor.id').T.to_dict('list')
#     print(a3.head())
#
# print("##############",a1_grpbyrepoid)

d={}
for i in a1_grpbyrepoid['repo.id'].unique():
    d[i] = [{a1_grpbyrepoid['actor.id'][j]: a1_grpbyrepoid['push_eventsby_contributor'][j]} for j in
            a1_grpbyrepoid[a1_grpbyrepoid['repo.id'] == i].index]
dic_keys=list(d.keys())
dic_Values = list(d.values())
print("keys",dic_keys,type(dic_keys))
print("values",dic_Values)

sum_list=[]
avg_list = []
for values in dic_Values:
    print("values in first iteration",values)
    print(type(values))
    for j in values:
        print(j)
        print(type(j))
        for k in j.keys():
            a=int(j[k])
             # print("values in second iteration",j,list(j.values()),type(list(j.values())))
             # a=int(str(j.values()))
            sum_list.append(a)
            print(sum_list)
    avg= sum(sum_list) / len(sum_list)
    print("######avg",round(avg))
    avg_list.append(round(avg))
    sum_list.clear()

print("keys list",dic_keys)
print("avg_list",avg_list)

i=0
count=0
count_dict={}
from collections import defaultdict
final_dic = defaultdict(list)
key_val_dict =defaultdict(list)
val_list=[]
final_valuelist =[]
for repoid in dic_keys:
    for values in d[repoid]:
        print(repoid,values)
        for k in values.keys():
            if avg_list[i] < int(values[k]):
                count = count + 1
                print("condition success")
                #final_valuelist.append({k: values[k]})
                #print(final_valuelist)
                final_dic[repoid].append({k: values[k]})
                count_dict[repoid]=count
                print("repoid is",repoid,"user id",k)
                val_list.append(k)
        print("valuelist inside 2nd for loop",val_list)
    print("valuelist inside 1st for loop",val_list)
    key_val_dict[repoid].append(val_list)
    print("inside for key value dict ",key_val_dict)
    i=i+1
    final_valuelist.clear()
    count=0
    val_list.clear()
print(final_dic)
print(key_val_dict)

print("#####keys",final_dic.keys(),"#### values",final_dic.values())

repo_userid_list=[]

for repoid in final_dic.keys():
     for values in final_dic[repoid]:
         print("###values",values,type(values))
         for j in values.keys():
             print("@@@@",j)
             repo_userid_list.append([repoid,j])
             print(repo_userid_list)

df2 = pd.DataFrame(repo_userid_list, columns =['repo.id', 'actor.id'])
print(df2.head())

df2.to_csv(r'C:\\Users\\ASUS\\Documents\\ResearchMaterial\\CitingRef\\repo_withCC.csv',index=False)
filename_finaldic = "C:\\Users\\ASUS\\Documents\\ResearchMaterial\\CitingRef\\dict_output.txt"
filename_contricount = "C:\\Users\\ASUS\\Documents\\ResearchMaterial\\CitingRef\\contricount.txt"
j=0
with open(filename_finaldic,'w') as output:
    writer = csv.writer(output)
    for k, v in final_dic.items():
        writer.writerow([k] + v)
        j=j+1

with open(filename_contricount,'w') as output:
    writer = csv.writer(output)
    for i in count_dict.items():
        writer.writerow(i)

#core_Contributors(a1_grpbyrepoid)


data_items = count_dict.items()
data_list = list(data_items)

df1 = pd.DataFrame(data_list)
df1.columns=["repo.id","number of contributors",]
print(df1)

repo_countbycontri=df1.groupby("number of contributors")["repo.id"].count().reset_index(name='number_of_repos')
print(repo_countbycontri.head())
repo_countbycontri.to_csv(r'C:\\Users\\ASUS\\Documents\\ResearchMaterial\\CitingRef\\repo_count_bycontri.csv',index=False)

