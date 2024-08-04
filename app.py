from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os
from forms import DebtForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/deyn'  # Update here
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
db = SQLAlchemy(app)

from models import Debt

@app.route('/')
def index():
    total_debts = Debt.query.count()
    total_debt_amount = db.session.query(db.func.sum(Debt.amount)).scalar() or 0
    return render_template('index.html', total_debts=total_debts, total_debt_amount=total_debt_amount)

@app.route('/add_debt', methods=['GET', 'POST'])
def add_debt():
    form = DebtForm()
    if form.validate_on_submit():
        debt_owner_image = save_image(form.debt_owner_image.data)
        borrower_image = save_image(form.borrower_image.data)
        bail_image = save_image(form.bail_image.data)
        
        debt = Debt(
            debt_owner_name=form.debt_owner_name.data,
            debt_owner_phone=form.debt_owner_phone.data,
            debt_owner_image=debt_owner_image,
            amount=form.amount.data,
            duration_days=form.duration_days.data,
            borrower_name=form.borrower_name.data,
            borrower_phone=form.borrower_phone.data,
            borrower_image=borrower_image,
            bail_name=form.bail_name.data,
            bail_phone=form.bail_phone.data,
            bail_image=bail_image
        )
        db.session.add(debt)
        db.session.commit()
        flash('Debt added successfully!', 'success')
        return redirect(url_for('debts'))
    return render_template('add_debt.html', form=form)

@app.route('/debts')
def debts():
    debts = Debt.query.all()
    return render_template('debts.html', debts=debts)


@app.route('/view_debt/<int:id>')
def view_debt(id):
    debt = Debt.query.get_or_404(id)
    return render_template('view_debt.html', debt=debt)

@app.route('/edit_debt/<int:id>', methods=['GET', 'POST'])
def edit_debt(id):
    debt = Debt.query.get_or_404(id)
    form = DebtForm(obj=debt)
    if form.validate_on_submit():
        form.populate_obj(debt)
        db.session.commit()
        flash('Debt updated successfully!', 'success')
        return redirect(url_for('view_debt', id=debt.id))
    return render_template('add_debt.html', form=form)

@app.route('/delete_debt/<int:id>', methods=['POST'])
def delete_debt(id):
    debt = Debt.query.get_or_404(id)
    db.session.delete(debt)
    db.session.commit()
    flash('Debt deleted successfully!', 'success')
    return redirect(url_for('debts'))


def save_image(image_file):
    if image_file:
        filename = secure_filename(image_file.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image_file.save(image_path)
        return filename  # Return just the filename
    return None

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
