-- Enum for Order Status
CREATE TYPE order_status AS ENUM (
    'pending',     -- Order placed but not yet processed
    'shipped',     -- Order shipped
    'delivered',   -- Order delivered
    'canceled'     -- Order canceled
);

-- Enum for Payment Status
CREATE TYPE payment_status AS ENUM (
    'pending',     -- Payment not yet made
    'completed',   -- Payment successful
    'failed'       -- Payment failed
);

-- Enum for Payment Method
CREATE TYPE payment_method AS ENUM (
    'credit_card',  -- Payment via credit card
    'paypal',       -- Payment via PayPal
    'bank_transfer' -- Payment via bank transfer
);

-- Enum for Invoice Status
CREATE TYPE invoice_status AS ENUM (
    'pending',   -- Invoice not yet paid
    'paid'       -- Invoice paid
);

-- Enum for User Roles
CREATE TYPE user_role AS ENUM (
    'admin',
    'customer',
    'employee'
);

-- Enum for Product Category
CREATE TYPE product_category AS ENUM (
    'animal',       -- Category for animals
    'plant',        -- Category for plants
    'food',         -- Category for food products
    'accessory',    -- Category for accessories
    'other'         -- Category for miscellaneous products
);

-- Table for Users
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    phone VARCHAR(20),
    address TEXT,
    role user_role DEFAULT 'customer' NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Unified Table for Products
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT DEFAULT 0,
    category product_category NOT NULL,         -- Using enum for category
    subcategory VARCHAR(255),                   -- Subcategory for additional classification
    image_path VARCHAR(255),                    -- Path to product image
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for Orders
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    total_amount DECIMAL(10, 2) NOT NULL,
    shipping_address TEXT,
    status order_status DEFAULT 'pending',      -- Using enum for status
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for Order Items
CREATE TABLE order_items (
    order_item_id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(order_id) ON DELETE CASCADE,
    product_id INT REFERENCES products(product_id),
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

-- Table for Payments
CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(order_id) ON DELETE CASCADE,
    payment_method payment_method NOT NULL,     -- Using enum for payment method
    payment_status payment_status DEFAULT 'pending',  -- Using enum for payment status
    payment_amount DECIMAL(10, 2) NOT NULL,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for Invoices
CREATE TABLE invoices (
    invoice_id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(order_id) ON DELETE CASCADE,
    invoice_number VARCHAR(100) UNIQUE NOT NULL,
    invoice_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10, 2) NOT NULL,
    invoice_status invoice_status DEFAULT 'pending'  -- Using enum for invoice status
);
