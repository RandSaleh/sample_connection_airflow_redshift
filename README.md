# sample_connection_airflow_redshift
Steps : 
creating Redshift aws cluster with open TCP/IP traffic : 
- create security group 
1.AWS Concole >> EC2 >> From the left hand view [Network & Security] >> security group 
2.create new security group [redshift_security_group]
3. Add inbound rule 
[Redshift	TCP	5439	0.0.0.0/0 ]

- create IAM ROLE :
1.Go to aws management console >> IAM >> roles >> create 
Tusted entity type is : AWS Sevice 
Use case : Redshift : customizable
2.Add Permissions policies : Allow S3 access. 

-  Create Redshift cluster
1. attach IAM Role 
2. allow public accessability 
3. add security group [redshift_security_group] 

- create airflow-redshift connection 
1. airflow concole >> Admin >> Connection >> new Connection 
name "redshift"
Connection Type : Postgres, install it via : pip install apache-airflow-providers-postgres[amazon]
Host : copy endpoint for the cluster withut the port and the schema name. 
schama : dev 
port : 5439
login : is username/password for your user [that have admin accessability].

3. create conenctios on airflow for aws credentials : 
Airflow console >> admin >> conenctions >>craete  aws credentials 
add connection type : Amazon Web Service
add AWS Access Key ID/AWS Secret Access Key	 for your user. 
add Extra as : {"region_name": "us-west-2"}


5. See the Eample Dag. 



