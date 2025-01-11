-- Wstawianie przykładowych użytkowników
INSERT INTO users (username, password_hash, email, first_name, last_name, phone, address, role) VALUES
('admin_uzytkownik', 'hashedpassword1', 'admin@example.com', 'Admin', 'User', '123-456-7890', '123 Ulica Admina', 'admin'),
('jan_kowalski', 'hashedpassword2', 'jan.kowalski@example.com', 'Jan', 'Kowalski', '555-123-4567', '456 Ulica Główna', 'customer'),
('anna_nowak', 'hashedpassword3', 'anna.nowak@example.com', 'Anna', 'Nowak', '555-987-6543', '789 Broadway', 'employee'),
('paulina_zielinska', 'hashedpassword4', 'paulina.zielinska@example.com', 'Paulina', 'Zielinska', '555-567-8901', '12 Ulica Róż', 'customer'),
('mariusz_wisniewski', 'hashedpassword5', 'mariusz.wisniewski@example.com', 'Mariusz', 'Wiśniewski', '555-876-5432', '34 Ulica Nowa', 'customer'),
('krzysztof_adamski', 'hashedpassword6', 'krzysztof.adamski@example.com', 'Krzysztof', 'Adamski', '555-654-3210', '99 Ulica Stara', 'employee'),
('ewa_jakubowska', 'hashedpassword7', 'ewa.jakubowska@example.com', 'Ewa', 'Jakubowska', '555-432-9876', '67 Ulica Zielona', 'admin'),
('lukasz_witkowski', 'hashedpassword8', 'lukasz.witkowski@example.com', 'Łukasz', 'Witkowski', '555-321-6540', '14 Ulica Krótka', 'customer'),
('karolina_mazur', 'hashedpassword9', 'karolina.mazur@example.com', 'Karolina', 'Mazur', '555-213-4568', '21 Ulica Ogrodowa', 'employee'),
('kamil_bernat', 'hashedpassword10', 'kamil.bernat@example.com', 'Kamil', 'Bernat', '555-654-9876', '36 Ulica Leśna', 'customer'),
('daria_michalska', 'hashedpassword11', 'daria.michalska@example.com', 'Daria', 'Michalska', '555-423-7890', '5 Ulica Wiosenna', 'admin'),
('patryk_borek', 'hashedpassword12', 'patryk.borek@example.com', 'Patryk', 'Borek', '555-432-1234', '8 Ulica Górska', 'customer'),
('agata_kwiatkowska', 'hashedpassword13', 'agata.kwiatkowska@example.com', 'Agata', 'Kwiatkowska', '555-876-5431', '2 Ulica Kwiatowa', 'employee'),
('mateusz_sienkiewicz', 'hashedpassword14', 'mateusz.sienkiewicz@example.com', 'Mateusz', 'Sienkiewicz', '555-321-9876', '22 Ulica Morska', 'customer'),
('magdalena_baginski', 'hashedpassword15', 'magdalena.baginski@example.com', 'Magdalena', 'Bagiński', '555-654-7890', '77 Ulica Wiatrów', 'admin');

-- Wstawianie przykładowych produktów
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



-- Wstawianie przykładowych zamówień
INSERT INTO orders (user_id, total_amount, shipping_address, status) VALUES
(2, 1500.00, '456 Ulica Główna', 'pending'),
(2, 1200.00, '456 Ulica Główna', 'shipped'),
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


-- Wstawianie przykładowych pozycji zamówienia
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

-- Wstawianie przykładowych płatności
INSERT INTO payments (order_id, payment_method, payment_status, payment_amount) VALUES
(1, 'credit_card', 'completed', 1500.00),
(2, 'paypal', 'completed', 1200.00),
(3, 'bank_transfer', 'pending', 325.00),
(4, 'credit_card', 'completed', 550.00),
(5, 'paypal', 'completed', 700.00),
(6, 'bank_transfer', 'completed', 350.00),
(7, 'paypal', 'pending', 400.00),
(8, 'credit_card', 'completed', 450.00),
(9, 'paypal', 'completed', 500.00),
(10, 'bank_transfer', 'completed', 1000.00),
(11, 'credit_card', 'completed', 1200.00),
(12, 'paypal', 'completed', 750.00),
(13, 'credit_card', 'completed', 620.00),
(14, 'paypal', 'completed', 850.00),
(15, 'bank_transfer', 'completed', 900.00);

-- Wstawianie przykładowych faktur
INSERT INTO invoices (order_id, invoice_number, total_amount, invoice_status) VALUES
(1, 'FV-1001', 1500.00, 'paid'),
(2, 'FV-1002', 1200.00, 'paid'),
(3, 'FV-1003', 325.00, 'pending'),
(4, 'FV-1004', 550.00, 'paid'),
(5, 'FV-1005', 700.00, 'paid'),
(6, 'FV-1006', 350.00, 'paid'),
(7, 'FV-1007', 400.00, 'pending'),
(8, 'FV-1008', 450.00, 'paid'),
(9, 'FV-1009', 500.00, 'paid'),
(10, 'FV-1010', 1000.00, 'paid'),
(11, 'FV-1011', 1200.00, 'paid'),
(12, 'FV-1012', 750.00, 'paid'),
(13, 'FV-1013', 620.00, 'paid'),
(14, 'FV-1014', 850.00, 'paid'),
(15, 'FV-1015', 900.00, 'paid');
