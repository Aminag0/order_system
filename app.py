from flask import Flask, render_template, request, redirect, url_for, flash
from config import Config
from models import db, Order, ActionLog
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


# Create DB tables immediately (Flask 3.0+)
with app.app_context():
    db.create_all()

def log_action(order, action_type, user='Developer'):
    log = ActionLog(action_type=action_type, performed_by=user, order=order)
    db.session.add(log)
    db.session.commit()

@app.route('/orders')
def list_orders():
    orders = Order.query.all()
    return render_template('orders.html', orders=orders)

@app.route('/orders/new', methods=['GET','POST'])
def new_order():
    if request.method == 'POST':
        o = Order(
            num_items=int(request.form['num_items']),
            delivery_date=datetime.strptime(request.form['delivery_date'], '%Y-%m-%d'),
            sender_name=request.form['sender_name'],
            recipient_name=request.form['recipient_name'],
            recipient_address=request.form['recipient_address']
        )
        db.session.add(o)
        db.session.commit()
        log_action(o, 'Created')
        flash('Order created.')
        return redirect(url_for('list_orders'))
    return render_template('order_form.html', order=None)

@app.route('/orders/<int:id>/edit', methods=['GET','POST'])
def edit_order(id):
    o = Order.query.get_or_404(id)
    if request.method == 'POST':
        o.num_items = int(request.form['num_items'])
        o.delivery_date = datetime.strptime(request.form['delivery_date'], '%Y-%m-%d')
        o.sender_name = request.form['sender_name']
        o.recipient_name = request.form['recipient_name']
        o.recipient_address = request.form['recipient_address']
        db.session.commit()
        log_action(o, 'Edited')
        flash('Order updated.')
        return redirect(url_for('list_orders'))
    return render_template('order_form.html', order=o)

@app.route('/orders/<int:id>/deliver', methods=['POST'])
def deliver_order(id):
    o = Order.query.get_or_404(id)
    o.status = 'Delivered'
    db.session.commit()
    log_action(o, 'Marked Delivered')
    flash('Order marked as delivered.')
    return redirect(url_for('list_orders'))

@app.route('/orders/<int:id>/delete', methods=['POST'])
def delete_order(id):
    o = Order.query.get_or_404(id)
    log_action(o, 'Deleted')
    db.session.delete(o)
    db.session.commit()
    flash('Order deleted.')
    return redirect(url_for('list_orders'))

@app.route('/logs')
def view_logs():
    logs = ActionLog.query.order_by(ActionLog.timestamp.desc()).all()
    return render_template('logs.html', logs=logs)

if __name__ == '__main__':
    app.run(debug=True)
