# Movie Database Project

## Getting Started

### Prerequisites

#### - **Python 3.x**
#### - **PostgreSQL**
#### - **Virtual Environment** for Python

### Setup Instructions

#### #1. **Clone the repository**:
   git clone <-repository-url->
   
   cd <-repository-folder->

#### #2. Create a virtual environment:
python -m venv venv

#### #3. Activate the virtual environment:
Windows: venv\Scripts\activate
macOS/Linux: source venv/bin/activate

#### #4. Install dependencies:
pip install -r requirements.txt

#### #5. Configure the Database:
Create a .env file in the root directory of the project (you can copy from .env.example if available).
Set up the following environment variables in .env:
DATABASE_HOST=localhost
DATABASE_USER=your_db_user
DATABASE_PASSWORD=your_db_password
DATABASE_NAME=your_db_name
DATABASE_PORT=5432  # Change if necessary

#### #6. Run the Program:
Start the program by running the run.py file:
python run.py

### Project Structure
- run.py: The main script to execute the program.
- config.py: Loads environment variables and manages database configuration.
- requirements.txt: Lists the project dependencies for easy installation.
- .env: Contains database connection details (not included in the repository).
  
### Dependencies
- certifi: Certificate validation for HTTPS requests
- charset-normalizer: Character encoding detection
- idna: Internationalized Domain Names support
- peewee: ORM for interacting with PostgreSQL
- psycopg2: PostgreSQL database adapter
- python-dotenv: Loads environment variables from .env files
- requests: Simplifies API requests
- urllib3: HTTP client for Python
  
