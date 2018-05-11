import app from app
import db from db

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()