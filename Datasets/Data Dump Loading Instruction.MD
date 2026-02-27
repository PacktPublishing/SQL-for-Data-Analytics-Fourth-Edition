# Data Dump Loading Instruction

Please be advised that to load the data.dump file into your PostgreSQL database, you must first execute the following two statements inside your psql command:

<pre>
CREATE ROLE azure_pg_admin WITH LOGIN PASSWORD 'your_password';
CREATE ROLE junshan WITH LOGIN PASSWORD 'your_password';
</pre>
