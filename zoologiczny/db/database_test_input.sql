-- Inserting sample users
INSERT INTO users (username, password_hash, email, first_name, last_name, phone) VALUES
('admin_uzytkownik', 'hashedpassword1', 'admin@example.com', 'Admin', 'User', '123-456-7890'),
('jan_kowalski', 'hashedpassword2', 'jan.kowalski@example.com', 'Jan', 'Kowalski', '555-123-4567'),
('anna_nowak', 'hashedpassword3', 'anna.nowak@example.com', 'Anna', 'Nowak', '555-987-6543'),
('paulina_zielinska', 'hashedpassword4', 'paulina.zielinska@example.com', 'Paulina', 'Zielinska', '555-567-8901'),
('mariusz_wisniewski', 'hashedpassword5', 'mariusz.wisniewski@example.com', 'Mariusz', 'Wiśniewski', '555-876-5432'),
('krzysztof_adamski', 'hashedpassword6', 'krzysztof.adamski@example.com', 'Krzysztof', 'Adamski', '555-654-3210'),
('ewa_jakubowska', 'hashedpassword7', 'ewa.jakubowska@example.com', 'Ewa', 'Jakubowska', '555-432-9876'),
('lukasz_witkowski', 'hashedpassword8', 'lukasz.witkowski@example.com', 'Łukasz', 'Witkowski', '555-321-6540'),
('karolina_mazur', 'hashedpassword9', 'karolina.mazur@example.com', 'Karolina', 'Mazur', '555-213-4568'),
('kamil_bernat', 'hashedpassword10', 'kamil.bernat@example.com', 'Kamil', 'Bernat', '555-654-9876'),
('daria_michalska', 'hashedpassword11', 'daria.michalska@example.com', 'Daria', 'Michalska', '555-423-7890'),
('patryk_borek', 'hashedpassword12', 'patryk.borek@example.com', 'Patryk', 'Borek', '555-432-1234'),
('agata_kwiatkowska', 'hashedpassword13', 'agata.kwiatkowska@example.com', 'Agata', 'Kwiatkowska', '555-876-5431'),
('mateusz_sienkiewicz', 'hashedpassword14', 'mateusz.sienkiewicz@example.com', 'Mateusz', 'Sienkiewicz', '555-321-9876'),
('magdalena_baginski', 'hashedpassword15', 'magdalena.baginski@example.com', 'Magdalena', 'Bagiński', '555-654-7890');

-- Inserting sample products
INSERT INTO products (name, description, price, stock_quantity, category, subcategory, image_path, rating) VALUES
('Golden Retriever', 'Przyjazny pies, idealny dla rodzin', 1200.00, 5, 'animals', 'pies', 'products/golden_retriever.jpg', 3.00),
('Papuga', 'Kolorowy i gadatliwy ptak', 300.00, 10, 'animals', 'ptak', 'products/parrot.jpg', 4.50),
('Anubias', 'Roślina akwariowa o mocnych liściach, idealna do akwarium, łatwa w pielęgnacji', 25.00, 50, 'plants', 'roślina akwariowa', 'products/anubias.jpg', 4.00),
('Kryptokoryna', 'Roślina akwariowa o długich, wąskich liściach, doskonała do zacienionych akwariów', 15.00, 100, 'plants', 'roślina akwariowa', 'products/cryptocoryne.jpg', 5.00),
('Jedzenie dla psa', 'Pyszne jedzenie dla psa', 15.00, 20, 'others', 'jedzenie_dla_psa', 'products/dog_food.jpg', 4.70),
('Zabawka dla psa', 'Zabawka do zabawy dla psa', 50.00, 15, 'others', 'zabawka', 'products/dog_toy.jpg', 3.40),
('Karmnik dla ptaków', 'Karmnik drewniany dla ptaków', 40.00, 30, 'others', 'ptak', 'products/bird_feeder.jpg', 2.69),
('Hamak dla kota', 'Hamak dla kota do odpoczynku', 80.00, 12, 'others', 'kot', 'products/cat_hammock.jpg', 3.73),
('Java Fern', 'Roślina akwariowa o długich liściach, doskonała do tworzenia podwodnych krajobrazów w akwarium', 30.00, 40, 'plants', 'roślina akwariowa', 'products/java_fern.jpg', 4.20),
('Java Moss', 'Roślina akwariowa, idealna do tworzenia naturalnych środowisk w akwarium', 35.00, 60, 'plants', 'roślina akwariowa', 'products/java_moss.jpg', 4.60),
('Kość dla psa', 'Kość do żucia dla psa', 20.00, 50, 'others', 'zabawka', 'products/dog_bone.jpg', 4.10),
('Anubias Nana', 'Mała, roślina akwariowa o gruboziarnistych liściach, łatwa w utrzymaniu', 25.00, 25, 'plants', 'roślina akwariowa', 'products/anubias_nana.jpg', 3.90),
('Neon rybka', 'Dekoracyjna rybka do akwarium', 10.00, 200, 'animals', 'ryba', 'products/neon_fish.jpg', 5.00),
('Karaś złocisty', 'Ryba akwariowa, znana z pięknego wyglądu', 15.00, 80, 'animals', 'ryba', 'products/goldfish.jpg', 4.50),
('Koliber', 'Koliber, idealny do obserwacji w ogrodzie', 200.00, 40, 'animals', 'ptak', 'products/hummingbird.jpg', 4.80);

-- Inserting sample orders
INSERT INTO orders (user_id, total_amount, shipping_address, status) VALUES
(2, 1500.00, '456 Ulica Główna', 'pending'),
(3, 325.00, '789 Broadway', 'delivered'),
(4, 550.00, '12 Ulica Róż', 'pending'),
(5, 700.00, '34 Ulica Nowa', 'shipped'),
(6, 350.00, '99 Ulica Stara', 'delivered'),
(7, 400.00, '67 Ulica Zielona', 'pending'),
(8, 450.00, '14 Ulica Krótka', 'shipped'),
(9, 500.00, '21 Ulica Ogrodowa', 'delivered'),
(10, 1000.00, '36 Ulica Leśna', 'pending'),
(11, 1200.00, '5 Ulica Wiosenna', 'shipped'),
(12, 750.00, '8 Ulica Górska', 'delivered'),
(13, 620.00, '2 Ulica Kwiatowa', 'pending'),
(14, 850.00, '22 Ulica Morska', 'delivered'),
(15, 900.00, '77 Ulica Wiatrów', 'shipped');

-- Inserting sample order items
INSERT INTO order_items (order_id, product_id, quantity, price) VALUES
(1, 5, 2, 30.00),
(1, 1, 1, 1200.00),
(2, 3, 4, 25.00),
(2, 4, 2, 15.00),
(3, 2, 1, 300.00),
(4, 6, 3, 50.00),
(5, 7, 1, 40.00),
(6, 8, 1, 80.00),
(7, 5, 2, 30.00),
(8, 6, 1, 50.00),
(9, 3, 5, 25.00),
(10, 7, 1, 40.00),
(11, 8, 2, 80.00),
(12, 5, 3, 30.00),
(13, 6, 4, 50.00);

-- Inserting sample invoices
INSERT INTO invoices (order_id, invoice_number, total_amount, invoice_status, invoice_date) VALUES
(1, 'INV-001', 1500.00, 'pending', CURRENT_TIMESTAMP),
(2, 'INV-002', 325.00, 'paid', CURRENT_TIMESTAMP),
(3, 'INV-003', 550.00, 'pending', CURRENT_TIMESTAMP),
(4, 'INV-004', 700.00, 'paid', CURRENT_TIMESTAMP),
(5, 'INV-005', 350.00, 'pending', CURRENT_TIMESTAMP),
(6, 'INV-006', 400.00, 'paid', CURRENT_TIMESTAMP),
(7, 'INV-007', 450.00, 'pending', CURRENT_TIMESTAMP),
(8, 'INV-008', 500.00, 'paid', CURRENT_TIMESTAMP),
(9, 'INV-009', 1000.00, 'pending', CURRENT_TIMESTAMP),
(10, 'INV-010', 1200.00, 'paid', CURRENT_TIMESTAMP),
(11, 'INV-011', 750.00, 'pending', CURRENT_TIMESTAMP),
(12, 'INV-012', 620.00, 'paid', CURRENT_TIMESTAMP),
(13, 'INV-013', 850.00, 'pending', CURRENT_TIMESTAMP),
(14, 'INV-014', 900.00, 'paid', CURRENT_TIMESTAMP);