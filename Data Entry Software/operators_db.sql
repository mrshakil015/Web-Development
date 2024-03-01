-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 01, 2023 at 06:49 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

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
-- Table structure for table `operators_db`
--

CREATE TABLE `operators_db` (
  `id` int(50) NOT NULL,
  `operator_id` int(250) NOT NULL,
  `operatorname` varchar(250) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(250) NOT NULL,
  `emailaddress` varchar(250) NOT NULL,
  `contactnumber` varchar(20) NOT NULL,
  `assignday` int(250) NOT NULL,
  `remainday` int(50) NOT NULL,
  `sheetid` varchar(250) NOT NULL,
  `totaldata` int(50) NOT NULL,
  `dailydata` int(50) NOT NULL,
  `completedata` int(50) NOT NULL,
  `remaindata` int(50) NOT NULL,
  `totalhours` int(50) NOT NULL,
  `dailyhours` int(50) NOT NULL,
  `sheetname` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `operators_db`
--

INSERT INTO `operators_db` (`id`, `operator_id`, `operatorname`, `username`, `password`, `emailaddress`, `contactnumber`, `assignday`, `remainday`, `sheetid`, `totaldata`, `dailydata`, `completedata`, `remaindata`, `totalhours`, `dailyhours`, `sheetname`) VALUES
(7, 10000, 'Md Shakil', 'shakil.eub.cse@gmail.com', '123Shakil#', 'shakil.eub.cse@gmail.com', '01793299882', 34, 33, '1Cj2D9sVLR9a6NeQSfFZ8WI015aOyD6SvBCA_7F7WgMs', 372, 28, 17, 355, 5587, 0, 'Sheet1'),
(8, 10001, 'TechKnowGram Limited', 'mdallmamunridoy@gmail.com', 'Ridoy420@', 'mdallmamunridoy@gmail.com', '21221', 12, 11, '1Cj2D9sVLR9a6NeQSfFZ8WI015aOyD6SvBCA_7F7WgMs', 300, 12, 2, 298, 100, 0, 'Sheet2'),
(9, 10002, 'Lelin', 'lelin@gmail.com', '123Shakil#', 'lelin@gmail.com', '01793299882', 12, 11, '1Cj2D9sVLR9a6NeQSfFZ8WI015aOyD6SvBCA_7F7WgMs', 34, 12, 0, 34, 0, 0, 'Sheet1');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `operators_db`
--
ALTER TABLE `operators_db`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `operators_db`
--
ALTER TABLE `operators_db`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
