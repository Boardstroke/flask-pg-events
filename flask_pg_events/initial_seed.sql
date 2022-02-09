-- Insert some customers
INSERT INTO customers (id, name, address)
    VALUES ('e3be5d5d-eee9-497c-9833-5a0e406e730f', 'John Doe', '123 Main St');

INSERT INTO customers (id, name, address)
    VALUES ('ba53a61a-a89c-4e4d-b137-fc1d1f3173c4', 'Jane Doe', '456 Main St');

INSERT INTO customers (id, name, address)
    VALUES ('9ffe95a8-68b8-41e9-a267-a9a8e107ad77', 'Joe Smith', '789 Main St');

-- Insert some products
INSERT INTO products (id, name, description, price)
    VALUES ('7826a29e-568d-44e1-9597-8593fd414b15', 'Product 1', 'Product 1 description', '10.00');

INSERT INTO products (id, name, description, price)
    VALUES ('124e0cf6-9b31-409d-b381-884f35f89468', 'Product 2', 'Product 2 description', '20.00');

INSERT INTO products (id, name, description, price)
    VALUES ('fe7bdfaa-8907-4a09-bcad-8322e8631fb1', 'Product 3', 'Product 3 description', '30.00');

INSERT INTO products (id, name, description, price)
    VALUES ('25ab14fd-d9af-4f25-84ab-7f1dee1a0d66', 'Product 4', 'Product 4 description', '40.00');

INSERT INTO products (id, name, description, price)
    VALUES ('e9f0504f-6446-41a0-a36b-dcdb72744bed', 'Product 5', 'Product 5 description', '50.00');

INSERT INTO products (id, name, description, price)
    VALUES ('8d80b891-7831-4832-9310-48bff03b4e27', 'Product 6', 'Product 6 description', '60.00');

INSERT INTO products (id, name, description, price)
    VALUES ('0e57e1e2-a20d-4836-b856-8278b7db5acc', 'Product 7', 'Product 7 description', '70.00');

-- Insert some orders
INSERT INTO orders (id, customer_id, status)
    VALUES ('05798f76-b836-4cb9-9f7c-59cb638167c7', 'e3be5d5d-eee9-497c-9833-5a0e406e730f', 'pending');

INSERT INTO orders (id, customer_id, status)
    VALUES ('499f89f0-5430-412a-9222-6fa62ac1e41e', 'ba53a61a-a89c-4e4d-b137-fc1d1f3173c4', 'pending');

INSERT INTO orders (id, customer_id, status)
    VALUES ('7b884459-b8a1-4b86-b0f2-c4b6ba187d0f', '9ffe95a8-68b8-41e9-a267-a9a8e107ad77', 'pending');

-- Insert some order items
INSERT INTO order_items (order_id, product_id, quantity)
    VALUES ('05798f76-b836-4cb9-9f7c-59cb638167c7', '7826a29e-568d-44e1-9597-8593fd414b15', 2);

INSERT INTO order_items (order_id, product_id, quantity)
    VALUES ('499f89f0-5430-412a-9222-6fa62ac1e41e', '25ab14fd-d9af-4f25-84ab-7f1dee1a0d66', 5);

INSERT INTO order_items (order_id, product_id, quantity)
    VALUES ('7b884459-b8a1-4b86-b0f2-c4b6ba187d0f', '25ab14fd-d9af-4f25-84ab-7f1dee1a0d66', 1);

INSERT INTO order_items (order_id, product_id, quantity)
    VALUES ('7b884459-b8a1-4b86-b0f2-c4b6ba187d0f', '124e0cf6-9b31-409d-b381-884f35f89468', 4);

