-- This script adds the `country` column to the `users` table
ALTER TABLE users 
ADD COLUMN country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US';
