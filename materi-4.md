# Data Modelling

# Fact Table Structure

# 3. Update Records

```
dbt run --full-refresh --select models/l1/stg_products.sql
dbt run --full-refresh --select models/l1/stg_users.sql
dbt run --full-refresh --select models/l1/stg_orders.sql
dbt run --full-refresh --select models/l1/stg_order_detail.sql
dbt run --full-refresh --select models/l1+



dbt run --full-refresh --select models/l2/dim_products.sql
dbt run --full-refresh --select models/l2/dim_users.sql
dbt run --full-refresh --select models/l2/fact_orders_order_detail.sql
dbt run --full-refresh --select models/l2+

```

## Product

## User

## Order




# Data Visualization

Data visualization is the graphical representation of information and data. By using visual elements like charts, graphs, maps, and other visual tools, data visualization provides an accessible way to see and understand trends, outliers, and patterns in data. It helps to convert complex data sets into a visual context, making it easier to comprehend and analyze the information.

In this material, we are going to use Amazon QuickSight for Data Visualization tool. It offers seamless integration with several source tables (Redshift, RDS, etc) within the AWS environment. Meanwhile, it offers flexibility, since it can be accessed from anywhere through a web browser that convenience for a remote and distributed team. 

To create an account in AWS QuickSight and start a free trial, follow these steps:

## Step 1: Access QuickSight
1. **Sign In to AWS Management Console:**
   - Go to the [AWS Management Console](https://aws.amazon.com/console/) and sign in with your AWS credentials.

2. **Navigate to QuickSight:**
   - In the AWS Management Console, type "QuickSight" in the search bar and select Amazon QuickSight from the results.

## Step 2: Sign Up for QuickSight Free Trial
1. **Start QuickSight:**
   - Click on the “Sign up for QuickSight” button.

2. **Choose Edition:**
   - Choose "Enterprise edition" for a free 30-day trial. QuickSight offers two editions: Standard and Enterprise. The free trial is available for the Enterprise edition, which provides additional features.

3. **Fill in User Details:**
   - Provide the required information, such as your QuickSight account name and notification email address.
   - Choose your region (where you want QuickSight to be hosted).

4. **Create QuickSight Account:**
   - Review the pricing information (though you will be on a free trial) and click “Finish” to create your QuickSight account.

## Step 3: Explore QuickSight
1. **Initial Setup:**
   - After account creation, you can start using QuickSight immediately.
   - You will be taken to the QuickSight dashboard.

2. **Connect Data Sources:**
   - Click on “Manage Data” to connect to various data sources like Amazon S3, Redshift, RDS, and more.

3. **Create Analysis:**
   - Click on “New Analysis” to start creating visualizations and analyses using your data.

### Tips:
- **Free Tier Usage:** During the free trial, you can use QuickSight without incurring charges. After the trial, you will be charged based on your usage according to the pricing plan of the selected edition.
- **Monitor Usage:** Keep track of your usage in the AWS Billing and Cost Management Dashboard to avoid unexpected charges once the trial ends.

By following these steps, you can successfully create an AWS QuickSight account and start a free trial to explore its data visualization and analysis capabilities.

To connect Amazon Redshift to Amazon QuickSight, follow these steps:


## Connect Redshift to Quicksight

### Prerequisites:
1. **AWS Account:** Ensure you have an AWS account with appropriate permissions to access both Amazon Redshift and Amazon QuickSight.
2. **Amazon Redshift Cluster:** Ensure your Amazon Redshift cluster is up and running.
3. **VPC Configuration:** Ensure that your Redshift cluster is in the same VPC as your QuickSight instance or that you have configured the necessary networking to allow connections.

#### Step 1: Prepare Amazon Redshift
1. **Obtain Redshift Cluster Details:**
   - Redshift cluster endpoint.
   - Database name.
   - User credentials (username and password).

2. **Security Group Configuration:**
   - Ensure the security group associated with your Redshift cluster allows inbound traffic on the port Redshift is using (default is 5439).
   - Add QuickSight IP ranges to the inbound rules if necessary. QuickSight IP ranges can be found in the [AWS IP address ranges JSON](https://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html).

#### Step 2: Configure Amazon QuickSight
1. **Sign In to QuickSight:**
   - Go to the QuickSight console and sign in.

2. **Manage Data Sources:**
   - In the QuickSight console, go to the "Manage Data" page from the menu.

3. **Create a New Data Source:**
   - Click on "New Data Source."
   - Select "Redshift" as the data source type.

4. **Fill in Redshift Connection Details:**
   - **Data Source Name:** Provide a name for your data source.
   - **Cluster:** Select "Provide cluster details manually" if your cluster isn't listed.
   - **Cluster ID:** Enter your Redshift cluster's endpoint (excluding the port number).
   - **Port:** Default is 5439 (or the port your cluster uses).
   - **Database Name:** Enter your Redshift database name.
   - **Database User:** Enter your Redshift username.
   - **Database Password:** Enter your Redshift password.

5. **Authentication:**
   - Choose "Stored credentials" for ease of use unless you have a more secure setup with AWS Secrets Manager or IAM roles.

6. **Advanced Settings (if needed):**
   - You can specify a role if you are using IAM role-based authentication.

7. **Create Data Source:**
   - Click "Create Data Source" and then click "Create Data Source" again in the pop-up.

#### Step 3: Create Datasets in QuickSight
1. **Choose Your Data Source:**
   - After creating the data source, select it from your list of data sources.

2. **Select Database and Tables:**
   - Choose the database and the specific tables you want to use.

3. **Prepare Data:**
   - QuickSight will prompt you to prepare the data. You can choose to edit/prepare the data in SPICE (Super-fast, Parallel, In-memory Calculation Engine) or query directly from Redshift.

4. **Visualize Data:**
   - After preparation, you can create analyses and visualizations using the datasets you just created.

### Additional Tips:
- **SPICE Capacity:** If using SPICE, ensure you have enough capacity. SPICE accelerates data analysis but has limits based on your QuickSight edition.
- **Scheduled Refreshes:** Configure scheduled refreshes for your datasets if you're using SPICE to keep your data up-to-date.
- **Security and Permissions:** Ensure proper IAM roles and policies are configured to allow QuickSight to access Redshift.

By following these steps, you can successfully connect Amazon Redshift to Amazon QuickSight and start creating insightful visualizations from your Redshift data.