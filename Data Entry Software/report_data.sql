-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 05, 2023 at 04:33 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dataentry_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `report_data`
--

CREATE TABLE `report_data` (
  `data_id` int(11) NOT NULL,
  `operator_id` int(11) NOT NULL,
  `daily_complete_data` int(11) NOT NULL,
  `daily_working_data` int(11) NOT NULL,
  `remain_data` int(11) NOT NULL,
  `insert_date_time` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `report_data`
--

INSERT INTO `report_data` (`data_id`, `operator_id`, `daily_complete_data`, `daily_working_data`, `remain_data`, `insert_date_time`) VALUES
(16, 10002, 0, 140, 0, '2023-11-04'),
(17, 10002, 0, 145, 0, '2023-11-04'),
(18, 10002, 0, 150, 0, '2023-11-04'),
(19, 10002, 0, 152, 0, '2023-11-04'),
(20, 10002, 0, 157, 0, '2023-11-03'),
(21, 10002, 0, 162, 0, '2023-11-04'),
(22, 10002, 0, 166, 0, '2023-11-04'),
(23, 10002, 0, 172, 0, '2023-11-04'),
(24, 10002, 0, 175, 0, '2023-11-05'),
(25, 10002, 0, 179, 0, '2023-11-05'),
(26, 10002, 0, 183, 0, '2023-11-05'),
(27, 10002, 0, 186, 0, '2023-11-05'),
(28, 10002, 0, 189, 0, '2023-11-05');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `report_data`
--
ALTER TABLE `report_data`
  ADD PRIMARY KEY (`data_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `report_data`
--
ALTER TABLE `report_data`
  MODIFY `data_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
