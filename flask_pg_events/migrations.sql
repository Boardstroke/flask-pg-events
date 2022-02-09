-- Create table customers
CREATE TABLE IF NOT EXISTS customers (
  id uuid PRIMARY KEY,
  name varchar(255) NOT NULL,
  address varchar(255) NOT NULL
);

-- Create table of products
CREATE TABLE IF NOT EXISTS products (
  id uuid PRIMARY KEY,
  name varchar(255) NOT NULL,
  description text NOT NULL,
  price decimal(10, 2) NOT NULL
);

-- Create order status enum
CREATE TYPE order_status AS ENUM (
  'pending',
  'processing',
  'shipped',
  'delivered'
);

-- Create table of orders
CREATE TABLE IF NOT EXISTS orders (
  id uuid PRIMARY KEY,
  customer_id uuid NOT NULL,
  status order_status NOT NULL,
  CONSTRAINT customer_id_fk FOREIGN KEY (customer_id) REFERENCES customers (id) ON DELETE CASCADE
);

-- Create order_items table
CREATE TABLE IF NOT EXISTS order_items (
  id uuid DEFAULT uuid_generate_v4 () PRIMARY KEY,
  order_id uuid NOT NULL,
  product_id uuid NOT NULL,
  quantity int4 NOT NULL,
  CONSTRAINT order_id_fk FOREIGN KEY (order_id) REFERENCES orders (id) ON DELETE CASCADE,
  CONSTRAINT product_id_fk FOREIGN KEY (product_id) REFERENCES products (id)
);

