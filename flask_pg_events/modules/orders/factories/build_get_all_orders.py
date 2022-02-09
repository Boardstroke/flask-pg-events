def build_get_all_orders(order_repository):
    from flask_pg_events.modules.orders.presentantion import GetAllOrdersPresentantion
    from flask_pg_events.modules.orders.services import GetAllOrdersService

    get_all_orders_service = GetAllOrdersService(order_repository)
    get_all_orders_presentantion = GetAllOrdersPresentantion.as_view(
        'get_all_orders', service=get_all_orders_service)

    return get_all_orders_presentantion
