from app import db

class Debt(db.Model):
    __tablename__ = 'debts'
    
    id = db.Column(db.Integer, primary_key=True)
    debt_owner_name = db.Column(db.String(100), nullable=False)
    debt_owner_phone = db.Column(db.String(20), nullable=False)
    debt_owner_image = db.Column(db.String(255))
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    duration_days = db.Column(db.Integer, nullable=False)
    borrower_name = db.Column(db.String(100), nullable=False)
    borrower_phone = db.Column(db.String(20), nullable=False)
    borrower_image = db.Column(db.String(255))
    bail_name = db.Column(db.String(100), nullable=False)
    bail_phone = db.Column(db.String(20), nullable=False)
    bail_image = db.Column(db.String(255))
