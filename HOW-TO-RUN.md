1. Install Airflow:
   ```shell
   pip install apache-airflow
   ```
2. Initialize the SQLLite local database
   ```shell
   AIRFLOW_HOME=$(pwd) airflow db init
   ```
3. Migrate the DB:
   ```shell
   AIRFLOW_HOME=$(pwd) airflow db migrate
   ```
4. Run a standalone app:
   ```shell
   AIRFLOW_HOME=$(pwd) airflow standalone
   ```