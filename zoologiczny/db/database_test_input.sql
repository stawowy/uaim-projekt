-- Insert sample users
INSERT INTO users (username, password_hash, email, first_name, last_name, phone, address, role) VALUES
('admin_user', 'hashedpassword1', 'admin@example.com', 'Admin', 'User', '123-456-7890', '123 Admin St', 'admin'),
('john_doe', 'hashedpassword2', 'john.doe@example.com', 'John', 'Doe', '555-123-4567', '456 Main St', 'customer'),
('jane_smith', 'hashedpassword3', 'jane.smith@example.com', 'Jane', 'Smith', '555-987-6543', '789 Broadway', 'employee');

-- Insert sample products
INSERT INTO products (name, description, price, stock_quantity, category, subcategory, image_path) VALUES
('Golden Retriever', 'Friendly dog, great for families', 1200.00, 5, 'animal', 'dog', '/images/products/golden_retriever.jpg'),
('Parrot', 'Colorful and talkative bird', 300.00, 10, 'animal', 'bird', '/images/products/parrot.jpg'),
('Rose Bush', 'Beautiful red roses', 25.00, 50, 'plant', 'flowering plant', '/images/products/rose_bush.jpg'),
('Cactus', 'Low maintenance succulent plant', 15.00, 100, 'plant', 'succulent', '/images/products/cactus.jpg'),
('Dog food ', 'tasty dog foodM', 15.00, 20, 'food', 'dog_food', '/images/products/dog_food.jpg');

-- Insert sample orders
INSERT INTO orders (user_id, total_amount, shipping_address, status) VALUES
(2, 1500.00, '456 Main St', 'pending'),
(2, 1200.00, '456 Main St', 'shipped'),
(3, 325.00, '789 Broadway', 'delivered');

-- Insert sample order items
INSERT INTO order_items (order_id, product_id, quantity, price) VALUES
(1, 5, 1, 1500.00),  -- Laptop
(2, 1, 1, 1200.00),  -- Golden Retriever
(3, 4, 5, 15.00),    -- Cactus
(3, 3, 2, 25.00);    -- Rose Bush

-- Insert sample payments
INSERT INTO payments (order_id, payment_method, payment_status, payment_amount) VALUES
(1, 'credit_card', 'completed', 1500.00),
(2, 'paypal', 'completed', 1200.00),
(3, 'bank_transfer', 'pending', 325.00);

-- Insert sample invoices
INSERT INTO invoices (order_id, invoice_number, total_amount, invoice_status) VALUES
(1, 'INV-1001', 1500.00, 'paid'),
(2, 'INV-1002', 1200.00, 'paid'),
(3, 'INV-1003', 325.00, 'pending');
