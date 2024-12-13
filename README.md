# Ganga Bhumi Club

A login page made for Task round of **Ganga Bhumi Club**

[Live demo can be Found here](https://ganga-bhumi-club.vercel.app/)

[Create Your Own clone &nbsp;![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fpr13260%2FGangaBhumiClub%2Ftree%2Fmain&env=MONGO_URI&envDescription=Your%20mongoDB%20URL%20%5BRefer%20to%20Readme.md%20file%20in%20repo%20to%20know%20more%5D&envLink=https%3A%2F%2Fgithub.com%2Fpr13260%2FGangaBhumiClub%2Fblob%2Fmain%2FREADME.md&redirect-url=https%3A%2F%2Fgithub.com%2Fpr13260&demo-title=A%20login%20page&demo-description=A%20login%20page%20made%20for%20Task%20round%20of%20Ganga%20Bhumi%20Club%20Live%20demo%20can%20be%20Found%20here&demo-url=https%3A%2F%2Fganga-bhumi-club.vercel.app%2F)

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
