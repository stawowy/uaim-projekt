-- Wstawianie przykładowych użytkowników
INSERT INTO users (username, password_hash, email, first_name, last_name, phone, address, role) VALUES
('admin_uzytkownik', 'hashedpassword1', 'admin@example.com', 'Admin', 'User', '123-456-7890', '123 Ulica Admina', 'admin'),
('jan_kowalski', 'hashedpassword2', 'jan.kowalski@example.com', 'Jan', 'Kowalski', '555-123-4567', '456 Ulica Główna', 'customer'),
('anna_nowak', 'hashedpassword3', 'anna.nowak@example.com', 'Anna', 'Nowak', '555-987-6543', '789 Broadway', 'employee'),
('paulina_zielinska', 'hashedpassword4', 'paulina.zielinska@example.com', 'Paulina', 'Zielinska', '555-567-8901', '12 Ulica Róż', 'customer'),
('mariusz_wisniewski', 'hashedpassword5', 'mariusz.wisniewski@example.com', 'Mariusz', 'Wiśniewski', '555-876-5432', '34 Ulica Nowa', 'customer'),
('krzysztof_adamski', 'hashedpassword6', 'krzysztof.adamski@example.com', 'Krzysztof', 'Adamski', '555-654-3210', '99 Ulica Stara', 'employee'),
('ewa_jakubowska', 'hashedpassword7', 'ewa.jakubowska@example.com', 'Ewa', 'Jakubowska', '555-432-9876', '67 Ulica Zielona', 'admin');

-- Wstawianie przykładowych produktów
INSERT INTO products (name, description, price, stock_quantity, category, subcategory, image_path,rating) VALUES
('Golden Retriever', 'Przyjazny pies, idealny dla rodzin', 1200.00, 5, 'animals', 'pies', '/images/products/golden_retriever.jpg',3.00),
('Papuga', 'Kolorowy i gadatliwy ptak', 300.00, 10, 'animals', 'ptak', '/images/products/parrot.jpg',4.50),
('Krzak Róż', 'Piękne czerwone róże', 25.00, 50, 'plants', 'roślina kwitnąca', '/images/products/rose_bush.jpg',4.00),
('Kaktus', 'Roślina o niskich wymaganiach pielęgnacyjnych', 15.00, 100, 'plants', 'succulent', '/images/products/cactus.jpg',5.00),
('Jedzenie dla psa', 'Pyszne jedzenie dla psa', 15.00, 20, 'others', 'jedzenie_dla_psa', '/images/products/dog_food.jpg',4.70),
('Zabawka dla psa', 'Zabawka do zabawy dla psa', 50.00, 15, 'others', 'zabawka', '/images/products/dog_toy.jpg',3.40),
('Karmnik dla ptaków', 'Karmnik drewniany dla ptaków', 40.00, 30, 'others', 'ptak', '/images/products/bird_feeder.jpg',2.69),
('Hamak dla kota', 'Hamak dla kota do odpoczynku', 80.00, 12, 'others', 'kot', '/images/products/cat_hammock.jpg',3.73);

-- Wstawianie przykładowych zamówień
INSERT INTO orders (user_id, total_amount, shipping_address, status) VALUES
(2, 1500.00, '456 Ulica Główna', 'pending'),
(2, 1200.00, '456 Ulica Główna', 'shipped'),
(3, 325.00, '789 Broadway', 'delivered'),
(4, 550.00, '12 Ulica Róż', 'pending'),
(5, 700.00, '34 Ulica Nowa', 'shipped'),
(6, 350.00, '99 Ulica Stara', 'delivered'),
(7, 400.00, '67 Ulica Zielona', 'pending');

-- Wstawianie przykładowych pozycji zamówienia
INSERT INTO order_items (order_id, product_id, quantity, price) VALUES
(1, 5, 2, 30.00),   -- Jedzenie dla psa
(1, 1, 1, 1200.00), -- Golden Retriever
(2, 3, 4, 25.00),   -- Krzak Róż
(2, 4, 2, 15.00),   -- Kaktus
(3, 2, 1, 300.00),  -- Papuga
(4, 6, 3, 50.00),   -- Zabawka dla psa
(5, 7, 1, 40.00),   -- Karmnik dla ptaków
(6, 8, 1, 80.00),   -- Hamak dla kota
(7, 5, 2, 30.00);   -- Jedzenie dla psa

-- Wstawianie przykładowych płatności
INSERT INTO payments (order_id, payment_method, payment_status, payment_amount) VALUES
(1, 'credit_card', 'completed', 1500.00),
(2, 'paypal', 'completed', 1200.00),
(3, 'bank_transfer', 'pending', 325.00),
(4, 'credit_card', 'completed', 550.00),
(5, 'paypal', 'completed', 700.00),
(6, 'bank_transfer', 'completed', 350.00),
(7, 'paypal', 'pending', 400.00);

-- Wstawianie przykładowych faktur
INSERT INTO invoices (order_id, invoice_number, total_amount, invoice_status) VALUES
(1, 'FV-1001', 1500.00, 'paid'),
(2, 'FV-1002', 1200.00, 'paid'),
(3, 'FV-1003', 325.00, 'pending'),
(4, 'FV-1004', 550.00, 'paid'),
(5, 'FV-1005', 700.00, 'paid'),
(6, 'FV-1006', 350.00, 'paid'),
(7, 'FV-1007', 400.00, 'pending');
