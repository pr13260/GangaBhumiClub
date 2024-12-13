# GangaBhumiClub

A login page made for Task round of **GangaBhumiClub**

## Installation

Follow these steps to set up the Flask application and configure MongoDB.

### Prerequisites

- Python 3.12.x
- pip (Python package installer)
- MongoDB account

### Step 1: Clone the repository

```bash
git clone https://github.com/pr13260/GangaBhumiClub.git
cd GangaBhumiClub
```

### Step 2: Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set up MongoDB

1. Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) and create an account.
2. Create a new cluster.
3. In the cluster, click on "Connect" and follow the instructions to whitelist your IP address and create a database user.
4. Choose "Connect your application" and copy the connection string.

### Step 5: Configure environment variables

Create a `.env` file in the root directory of your project and add the following:

```plaintext
FLASK_ENV=development
MONGO_URI=your_mongodb_connection_string
```

Replace `your_mongodb_connection_string` with the connection string you copied from MongoDB Atlas.

### Step 6: Run the application

```bash
flask --app app run --host=0.0.0.0 --port 8080 
```

Your Flask application should now be running and connected to MongoDB.
