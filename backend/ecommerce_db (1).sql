-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jul 15, 2024 at 06:28 AM
-- Server version: 8.0.37
-- PHP Version: 8.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ecommerce_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `cart`
--

DROP TABLE IF EXISTS `cart`;
CREATE TABLE IF NOT EXISTS `cart` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `product_id` int DEFAULT NULL,
  `quantity` int DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `product_id` (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
CREATE TABLE IF NOT EXISTS `categories` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `parent_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `parent_id` (`parent_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `categories`
--

INSERT INTO `categories` (`id`, `name`, `parent_id`) VALUES
(1, 'Electronics', NULL),
(2, 'Clothing', NULL),
(3, 'Books', NULL),
(4, 'Home', NULL),
(5, 'Laptops', 1),
(6, 'Smartphones', 1),
(7, 'Men', 2),
(8, 'Women', 2),
(9, 'Fiction', 3),
(10, 'Non-Fiction', 3),
(11, 'Kitchen', 4),
(12, 'Furniture', 4),
(13, 'fdd', NULL),
(14, 'fdd', 1),
(15, 'fdd', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `categoriess`
--

DROP TABLE IF EXISTS `categoriess`;
CREATE TABLE IF NOT EXISTS `categoriess` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `parent_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `parent_id` (`parent_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
CREATE TABLE IF NOT EXISTS `product` (
  `id` int NOT NULL AUTO_INCREMENT,
  `category` varchar(80) NOT NULL,
  `product_code` varchar(80) NOT NULL,
  `product_title` varchar(120) NOT NULL,
  `product_price` float NOT NULL,
  `product_quantity` int NOT NULL,
  `track_quantity` tinyint(1) DEFAULT '0',
  `product_status` varchar(10) NOT NULL,
  `free_shipping` varchar(10) NOT NULL,
  `product_variant` varchar(10) NOT NULL,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`id`, `category`, `product_code`, `product_title`, `product_price`, `product_quantity`, `track_quantity`, `product_status`, `free_shipping`, `product_variant`, `name`) VALUES
(1, '', '', '', 0, 0, 0, '', '', '', 'Apple'),
(2, '', '', '', 0, 0, 0, '', '', '', 'Mango'),
(3, '', '', '', 0, 0, 0, '', '', '', 'Mango'),
(4, '', '', '', 0, 0, 0, '', '', '', 'Grapes'),
(5, '', '', '', 0, 0, 0, '', '', '', 'Grapes'),
(6, '', '', '', 0, 0, 0, '', '', '', 's'),
(7, '', '', '', 0, 0, 0, '', '', '', 'Orange'),
(8, '', '', '', 0, 0, 0, '', '', '', 'Strawberry'),
(9, 'wef', 'ew', 'th', 56, 3, 1, 'active', 'free', 'yes', 'ef');

-- --------------------------------------------------------

--
-- Table structure for table `resellers`
--

DROP TABLE IF EXISTS `resellers`;
CREATE TABLE IF NOT EXISTS `resellers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `reseller_code` varchar(50) NOT NULL,
  `reseller_name` varchar(100) NOT NULL,
  `available_wallet` decimal(10,2) DEFAULT '0.00',
  `membership` varchar(50) DEFAULT NULL,
  `total_credit_limit` decimal(10,2) DEFAULT '0.00',
  `mobile_number` varchar(20) DEFAULT NULL,
  `registration_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(80) NOT NULL,
  `password` varchar(200) NOT NULL,
  `is_admin` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `password`, `is_admin`) VALUES
(1, 'PSQ', 'pbkdf2:sha256:600000$qqNeRnnEbH7kEtna$647117a8c209a4471ea02c4bfbd112dbf0589bedacf841e6a35c2869537ef93b', 0),
(2, 'PC', 'pbkdf2:sha256:600000$nHWG1ETeabFxDQQT$bc45aea4614df5f8c6eac74e037f1ed2ba6d0cbd4b9d181379a438e91a8ca520', 0),
(3, 'PW', 'scrypt:32768:8:1$DHkY6jVV6P0kkGJE$5e97bfeea0d17a680b246afa588b8659ac9ecb1a021a1608f88112db97dd1b30147535251df45796f1d0bbd84eb3200349cb1aec7003d8c949f77af3d4e9d79d', 0),
(4, 'SDER', 'scrypt:32768:8:1$VYXONw0A7mEu89wI$67e38c421aa5f9b46487864dc1e7e902ea5e8b0a2d4612141341e14c5ada7793ad53e6f2c32c4a8a6756eb5c22ca08f11fde1cad33b04b8cefe60b7df54562a6', 0),
(5, 'PCDS', 'scrypt:32768:8:1$7Xs8ziZ1nVfWKOFa$1f4cb0ce855ce3cf6bee149a4570142bc5d74557e6f8840518c1f0f9b34cfb706fe03f0dfb9e949ca5608b859174baf2a9e6888a1a1db2c9c06bc670ed48e542', 0),
(6, 'AQ', 'scrypt:32768:8:1$o1RQhivAfMf7eCiv$a07123b5f08d0d622ef18ae5f9786bd04a70ee6a95df03ecbf1a3ce4f0b675a5c3f9109deb2a8575c8f3b068cc1b6ec579e94fa093463af7d4302f02b2ca4482', 0),
(7, 'FR', 'scrypt:32768:8:1$xfcVMbWfbHY7aAjK$e804d6f96ca180cc72e6a87a36a006faba9fd8078778cad2bd10254f03fb63af1aeae89332571b76b38495f7b1ef752021f8ed5c323d140e94cda318a1f8d8d1', 0);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `cart`
--
ALTER TABLE `cart`
  ADD CONSTRAINT `cart_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  ADD CONSTRAINT `cart_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`);

--
-- Constraints for table `categories`
--
ALTER TABLE `categories`
  ADD CONSTRAINT `categories_ibfk_1` FOREIGN KEY (`parent_id`) REFERENCES `categories` (`id`) ON DELETE SET NULL;

--
-- Constraints for table `categoriess`
--
ALTER TABLE `categoriess`
  ADD CONSTRAINT `categoriess_ibfk_1` FOREIGN KEY (`parent_id`) REFERENCES `categories` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
