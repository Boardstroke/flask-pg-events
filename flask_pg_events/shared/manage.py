import click
from flask import Blueprint
from flask_pg_events import app, cursor
from datetime import datetime
manage = Blueprint('manage', __name__)


@manage.cli.command('migrate')
def run_migrations():
    migrations_file = open('/usr/app/flask_pg_events/migrations.sql', 'r')
    migrations_commands = migrations_file.read()
    try:
        cursor.execute(migrations_commands)
        app.logger.info('Migrations ran successfully')
    except Exception as e:
        app.logger.error('Migrations failed: {}'.format(e))
        raise e


@manage.cli.command('seed')
def run_seeds():
    seeds_file = open('/usr/app/flask_pg_events/seed/initial_seed.sql', 'r')
    seeds_commands = seeds_file.read()
    try:
        cursor.execute(seeds_commands)
        app.logger.info('Seeds ran successfully')
    except Exception as e:
        app.logger.error('Seeds failed: {}'.format(e))
        raise e


@manage.cli.command('create_new_order')
@click.argument('customer_id')
def create_new_order(customer_id):
    try:
        cursor.execute("""
            INSERT INTO orders (customer_id, created_at, updated_at)
            VALUES (%s, %s,)
        """, (customer_id, datetime.now(), datetime.now()))
        app.logger.info('New order created successfully')
    except Exception as e:
        app.logger.error('New order creation failed: {}'.format(e))
        raise e


@manage.cli.command('create_new_order_item')
@click.argument('order_id')
@click.argument('product_id')
@click.argument('quantity')
def create_new_order_item(order_id, product_id, quantity):
    try:
        cursor.execute("""
            INSERT INTO order_items (order_id, product_id, quantity, created_at, updated_at)
            VALUES (%s, %s, %s, %s, %s)
        """, (order_id, product_id, quantity, datetime.now(), datetime.now()))
    except Exception as e:
        app.logger.error('New order item creation failed: {}'.format(e))
        raise e
