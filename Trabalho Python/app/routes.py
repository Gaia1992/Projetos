from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import Product, Movement, User
from .forms import ProductForm, MovementForm, UserForm
from . import db

main_bp = Blueprint('main', __name__)

def admin_required():
    return current_user.is_authenticated and current_user.role == 'admin'

@main_bp.route('/')
@login_required
def dashboard():
    products = Product.query.order_by(Product.name.asc()).all()
    low_stock = [p for p in products if p.quantity < p.min_quantity]
    return render_template('dashboard.html', products=products, low_stock=low_stock)

@main_bp.route('/products')
@login_required
def products():
    items = Product.query.order_by(Product.name.asc()).all()
    return render_template('products.html', items=items)

@main_bp.route('/products/new', methods=['GET','POST'])
@login_required
def product_new():
    if not admin_required():
        flash('Apenas administradores podem cadastrar produtos.', 'warning')
        return redirect(url_for('main.products'))
    form = ProductForm()
    if form.validate_on_submit():
        p = Product(
            name=form.name.data.strip(),
            sku=(form.sku.data or '').strip() or None,
            description=form.description.data,
            quantity=form.quantity.data or 0,
            min_quantity=form.min_quantity.data or 0,
            price=form.price.data or 0.0
        )
        db.session.add(p)
        db.session.commit()
        flash('Produto cadastrado.', 'success')
        return redirect(url_for('main.products'))
    return render_template('product_form.html', form=form, title='Novo Produto')

@main_bp.route('/products/<int:pid>/edit', methods=['GET','POST'])
@login_required
def product_edit(pid):
    if not admin_required():
        flash('Apenas administradores podem editar produtos.', 'warning')
        return redirect(url_for('main.products'))
    p = Product.query.get_or_404(pid)
    form = ProductForm(obj=p)
    if form.validate_on_submit():
        p.name = form.name.data.strip()
        p.sku = (form.sku.data or '').strip() or None
        p.description = form.description.data
        p.quantity = form.quantity.data or 0
        p.min_quantity = form.min_quantity.data or 0
        p.price = form.price.data or 0.0
        db.session.commit()
        flash('Produto atualizado.', 'success')
        return redirect(url_for('main.products'))
    return render_template('product_form.html', form=form, title='Editar Produto')

@main_bp.route('/products/<int:pid>/delete', methods=['POST'])
@login_required
def product_delete(pid):
    if not admin_required():
        flash('Apenas administradores podem excluir produtos.', 'warning')
        return redirect(url_for('main.products'))
    p = Product.query.get_or_404(pid)
    db.session.delete(p)
    db.session.commit()
    flash('Produto excluído.', 'info')
    return redirect(url_for('main.products'))

@main_bp.route('/movements')
@login_required
def movements():
    records = Movement.query.order_by(Movement.timestamp.desc()).limit(200).all()
    return render_template('movements.html', records=records)

@main_bp.route('/movements/new', methods=['GET','POST'])
@login_required
def movement_new():
    form = MovementForm()
    form.product_id.choices = [(p.id, f"{p.name} (QTD: {p.quantity})") for p in Product.query.order_by(Product.name.asc()).all()]
    if not form.product_id.choices:
        flash('Cadastre um produto antes de registrar movimentações.', 'warning')
        return redirect(url_for('main.products'))
    if form.validate_on_submit():
        product = Product.query.get(form.product_id.data)
        qty = form.quantity.data
        if form.type.data == 'out' and product.quantity < qty:
            flash('Estoque insuficiente para saída.', 'danger')
            return render_template('movement_form.html', form=form)
        product.quantity = product.quantity + qty if form.type.data == 'in' else product.quantity - qty
        m = Movement(product_id=product.id, user_id=getattr(current_user, 'id', None), type=form.type.data, quantity=qty, note=form.note.data)
        db.session.add(m)
        db.session.commit()
        flash('Movimentação registrada.', 'success')
        return redirect(url_for('main.movements'))
    return render_template('movement_form.html', form=form)

@main_bp.route('/users', methods=['GET','POST'])
@login_required
def users():
    if not admin_required():
        flash('Apenas administradores podem gerenciar usuários.', 'warning')
        return redirect(url_for('main.dashboard'))
    form = UserForm()
    if form.validate_on_submit():
        if User.query.filter_by(username=form.username.data.strip()).first():
            flash('Usuário já existe.', 'danger')
        else:
            u = User(username=form.username.data.strip(), role=form.role.data)
            u.set_password(form.password.data)
            db.session.add(u)
            db.session.commit()
            flash('Usuário criado.', 'success')
            return redirect(url_for('main.users'))
    all_users = User.query.order_by(User.created_at.desc()).all()
    return render_template('users.html', form=form, all_users=all_users)
