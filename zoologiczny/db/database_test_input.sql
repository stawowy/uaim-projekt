-- Create test users
INSERT INTO users (username, password_hash, email, first_name, last_name, role)
VALUES
    ('admin', 'hashedpassword', 'admin@example.com', 'Admin', 'User', 'admin'),
    ('john_doe', 'hashedpassword', 'john@example.com', 'John', 'Doe', 'customer'),
    ('jane_smith', 'hashedpassword', 'jane@example.com', 'Jane', 'Smith', 'customer');

-- Create test products
INSERT INTO products (name, description, price, stock_quantity)
VALUES
    ('Dog Food', 'Premium dog food', 15.99, 100),
    ('Cat Toy', 'Interactive cat toy', 5.99, 50),
    ('Pet Bed', 'Comfortable pet bed for pets of all sizes', 25.99, 30);

-- Create test animals
INSERT INTO animals (species, description, price, stock_quantity)
VALUES
    ('Dog', 'Loyal and friendly', 150.00, 10),
    ('Cat', 'Independent and playful', 120.00, 15),
    ('Parrot', 'Colorful and intelligent', 200.00, 5);

-- Create test plants
INSERT INTO plants (name, description, price, stock_quantity)
VALUES
    ('Fern', 'A beautiful house plant', 10.99, 20),
    ('Cactus', 'Low maintenance desert plant', 7.99, 15),
    ('Rose', 'A beautiful flowering plant', 12.99, 25);

-- Create test orders
INSERT INTO orders (user_id, total_amount, shipping_address, status)
VALUES
    (1, 100.99, '123 Admin St, Admin City, AC 12345', 'pending'),
    (2, 50.99, '456 John Ave, Doe City, DC 67890', 'shipped'),
    (3, 200.00, '789 Jane Blvd, Smith City, SC 11223', 'delivered');

-- Create test order items
-- For order_id 1
INSERT INTO order_items (order_id, product_id, quantity, price)
VALUES
    (1, 1, 2, 15.99),  -- Dog Food
    (1, 2, 1, 5.99);   -- Cat Toy

-- For order_id 2
INSERT INTO order_items (order_id, animal_id, quantity, price)
VALUES
    (2, 1, 1, 150.00); -- Dog

-- For order_id 3
INSERT INTO order_items (order_id, plant_id, quantity, price)
VALUES
    (3, 3, 2, 12.99); -- Rose

-- Create test payments
INSERT INTO payments (order_id, payment_method, payment_status, payment_amount)
VALUES
    (1, 'credit_card', 'completed', 100.99),
    (2, 'paypal', 'completed', 150.00),
    (3, 'bank_transfer', 'completed', 200.00);

-- Create test invoices
INSERT INTO invoices (order_id, invoice_number, total_amount, invoice_status)
VALUES
    (1, 'INV-0001', 100.99, 'paid'),
    (2, 'INV-0002', 150.00, 'paid'),
    (3, 'INV-0003', 200.00, 'paid');

SELECT * from invoices;