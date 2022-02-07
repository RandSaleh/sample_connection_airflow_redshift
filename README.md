# sample_connection_airflow_redshift
Steps : 
1. create IAM ROLE :
Go to aws management console >> IAM >> roles >> create 
Tusted entity type is : AWS Sevice 
Use case : Redshift : customizable
Add Permissions policies : Allow S3 access. 

2. Create Redshift cluster and associate IAM. 

3. create conenctios on airflow to sue it in the Hooks : 
Airflow console >> admin >> conenctions >>craete  aws credentials 
add connection type : Amazon Web Service
add Key/pass for your user. 
add Extra as : {"region_name": "us-west-2"}

4. create conenction for the Redshift : 
called "redshift"
Connection Type : Postgres 
Host : copy endpoint for the cluster withut the port and the schema name. 
schama : dev 
port : 5439

5. See the Eample Dag. 



