📘 MongoDB ETL Project (Python + Pandas)

This project performs a simple ETL pipeline using:

MongoDB (local: mongodb://localhost:27017/)

Python

Pandas

The pipeline loads a MongoDB collection, cleans & transforms the data, and writes the transformed data back into a new MongoDB collection.

📂 Project Structure

MongoDB Project/

│── readme.md

│── src/

│   ├── connection.py     # MongoDB connection functions

│   ├── extract.py        # get_data() function to extract data from MongoDB

│   ├── transform.py      # Data cleaning & transformation logic

│   ├── load.py           # load_to_mongo() to write DataFrame back to MongoDB

│   ├── main.py           # Orchestrates the full ETL pipeline

🔧 Technologies Used

Python 3.x

Pandas

PyMongo

Local MongoDB Server

🚀 Workflow Overview

1. Extract

extract.py contains:

get_data(database, collection)


This reads a MongoDB collection into a pandas DataFrame, converting _id values to strings.

2. Transform

transform.py applies cleaning:

Convert date fields to datetime

Normalize strings (project_manager, status, etc.)

Convert list of technologies → comma-separated string

Remove duplicates

Reset index

3. Load

load.py contains a single simple load function:

load_to_mongo(df, db_name, collection_name)


This:

Connects to Mongo

Drops the target collection if it exists

Inserts all DataFrame rows into MongoDB

4. Orchestration (main.py)

main.py ties everything together:

Extract raw data

Transform it

Load the cleaned data into a new MongoDB collection

▶️ How to Run the Project

1️⃣ Install dependencies

pip install pandas pymongo

2️⃣ Start MongoDB locally

mongod

3️⃣ Run the ETL pipeline

python src/main.py

📘 Example Flow (main.py)

raw = get_data("PythonLearningDB", "First_project")

clean = transform_data(raw)

load_to_mongo(clean, "PythonLearningDB", "First_project_clean")

🧹 Transformations Applied

Convert start_date and end_date → datetime

Title-case project_manager and status

Uppercase project IDs

Strip whitespace from all string fields

Convert technologies list → "React, Node.js, MongoDB" format

Drop duplicates

📦 Output

After running the ETL:

A new collection First_project_clean will be created

It will contain only cleaned & standardized documents

All dates are stored as proper MongoDB datetime

Technologies are stored as a single comma-separated string

🛠 Troubleshooting

❗ No data found

Your MongoDB collection is empty — check if documents exist.

❗ Connection refused

Ensure MongoDB server is running:

mongod

❗ Datetime fields appear as "None" in DataFrame

Check your date formats, or ensure they exist in the MongoDB documents.

👤 Author

Sandeep Reddy

Python • MongoDB • Data Engineering ETL