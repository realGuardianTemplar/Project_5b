import os
import urllib.parse
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# ==================== DATABASE CONFIG ====================
server   = os.environ.get('SQL_SERVER')
database = os.environ.get('SQL_DATABASE')
username = os.environ.get('SQL_USER_NAME')
password = os.environ.get('SQL_PASSWORD')

# Build safe connection string (handles special characters in password)
params = urllib.parse.quote_plus(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER=tcp:{server},1433;"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=60;"
)

app.config['SQLALCHEMY_DATABASE_URI'] = f"mssql+pyodbc:///?odbc_connect={params}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Optional: Login manager setup (if not already present)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
# ========================================================

# Rest of your __init__.py (import views, models, etc.)
from FlaskWebProject import views, models   # adjust if needed
