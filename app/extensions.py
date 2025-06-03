from flask_sqlalchemy import SQLAlchemy

# Extension for SQLAlchemy instance
# Initialized in app factory

db: SQLAlchemy = SQLAlchemy()
