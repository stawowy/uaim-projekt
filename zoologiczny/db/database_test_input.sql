-- Sample Data for the `users` Table
INSERT INTO users (username, email, password, first_name, last_name, address, phone_number, role) 
VALUES
('john_doe', 'john.doe@example.com', 'hashed_password_123', 'John', 'Doe', '123 Elm Street', '1234567890', 'customer'),
('jane_smith', 'jane.smith@example.com', 'hashed_password_456', 'Jane', 'Smith', '456 Oak Avenue', '9876543210', 'admin');

-- Sample Data for the `products` Table
INSERT INTO products (name, description, price, category, stock_quantity) 
VALUES
('Dog Food', 'Premium quality dog food for all breeds', 19.99, 'Food', 100),
('Cat Toy', 'Interactive toy for cats', 5.49, 'Toys', 50),
('Fish Tank', '20-gallon aquarium for fish', 45.99, 'Aquarium', 30),
('Bird Cage', 'Spacious cage for small birds', 39.99, 'Birds', 20),
('Dog Leash', 'Durable leather leash for dogs', 15.99, 'Accessories', 150);

-- Sample Data for the `orders` Table
INSERT INTO orders (user_id, total_amount, status, order_date)
VALUES
(1, 45.47, 'completed', '2024-12-10'),
(2, 25.48, 'pending', '2024-12-15');

-- Sample Data for the `order_items` Table
INSERT INTO order_items (order_id, product_id, quantity, price)
VALUES
(1, 1, 2, 19.99),  -- 2 Dog Food items
(1, 3, 1, 45.99),  -- 1 Fish Tank
(2, 4, 1, 39.99);  -- 1 Bird Cage

-- Sample Data for the `animals` Table
INSERT INTO animals (species, breed, name, age, adoption_date)
VALUES
('Dog', 'Golden Retriever', 'Buddy', 3, '2024-12-01'),
('Cat', 'Siamese', 'Whiskers', 2, '2024-12-05'),
('Parrot', 'Macaw', 'Polly', 4, '2024-12-10');

-- Sample Data for the `plants` Table
INSERT INTO plants (name, species, price, stock_quantity)
VALUES
('Aloe Vera', 'Aloe', 15.99, 20),
('Cactus', 'Cactaceae', 9.99, 50),
('Fern', 'Nephrolepis exaltata', 8.49, 30),
('Succulent', 'Succulent', 12.99, 40);

-- Sample Data for the `reviews` Table
INSERT INTO reviews (product_id, user_id, rating, comment, review_date)
VALUES
(1, 1, 5, 'Great dog food! My dog loves it!', '2024-12-12'),
(3, 2, 4, 'The fish tank is good, but a bit expensive.', '2024-12-16'),
(4, 1, 5, 'The bird cage is spacious and very sturdy!', '2024-12-17');

-- Sample Data for the `shopping_cart` Table
INSERT INTO shopping_cart (user_id, product_id, quantity)
VALUES
(1, 2, 3),  -- 3 Cat Toys
(2, 5, 1);  -- 1 Dog Leash

-- Sample Data for the `transactions` Table
INSERT INTO transactions (order_id, transaction_date, amount, status, payment_method)
VALUES
(1, '2024-12-11', 45.47, 'successful', 'credit_card'),
(2, '2024-12-16', 25.48, 'pending', 'paypal');
