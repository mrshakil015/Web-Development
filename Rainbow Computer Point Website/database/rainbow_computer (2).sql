-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 07, 2024 at 05:55 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rainbow_computer`
--

-- --------------------------------------------------------

--
-- Table structure for table `course_info`
--

CREATE TABLE `course_info` (
  `id` int(11) NOT NULL,
  `courseid` varchar(50) NOT NULL,
  `course_name` varchar(200) NOT NULL,
  `month_duration` varchar(50) NOT NULL,
  `weekly` varchar(20) NOT NULL,
  `duration_hour` varchar(20) NOT NULL,
  `duration_minute` varchar(20) NOT NULL,
  `amount` varchar(11) NOT NULL,
  `image_name` varchar(200) NOT NULL,
  `aboutcourse` text NOT NULL,
  `coursetopic` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `course_info`
--

INSERT INTO `course_info` (`id`, `courseid`, `course_name`, `month_duration`, `weekly`, `duration_hour`, `duration_minute`, `amount`, `image_name`, `aboutcourse`, `coursetopic`) VALUES
(3, '102', 'Digital Marketing', '1', '৩', '১', '৩০', '8888', 'digitalmarketing.jpg', 'ব্যক্তিগত কাজ, একাডেমিক কিংবা ক্যারিয়ার -যেকোনো ক্ষেত্রে এগিয়ে থাকতে হলে যে বিষয়টি সম্পর্কে আপনাকে জানতেই হবে সেটি হলো মাইক্রোসফট অফিস। বিশ্বে ১২০ কোটি মাইক্রোসফট অফিস ইউজার রয়েছে। আর এই মাইক্রোসফট অফিসের সবচেয়ে গুরুত্বপূর্ণ ৩টি সফটওয়্যার - MS Word, MS Excel ও MS PowerPoint. বই, চিঠিপত্র, রিজিউমি, অ্যাপ্লিকেশন, বা অন্য ডকুমেন্টেশনের কাজ লেখার জন্য মাইক্রোসফট ওয়ার্ড ব্যবহৃত হয়। অন্যদিকে', 'মাইক্রোসফট অফিস সফটওয়্যারের ১০টিরও বেশি প্রজেক্ট ও এপ্লিকেশন\r\n\r\nMS Word-এ নিউজ ডকুমেন্টস, বিজনেস কার্ড, লেটার হেড ও 3D মডেল '),
(5, '103', 'Office Application Program', '4', '6', '2', '0', '6000', 'banner.png', 'ব্যক্তিগত কাজ, একাডেমিক কিংবা ক্যারিয়ার -যেকোনো ক্ষেত্রে এগিয়ে থাকতে হলে যে বিষয়টি সম্পর্কে আপনাকে জানতেই হবে সেটি হলো মাইক্রোসফট অফিস। বিশ্বে ১২০ কোটি মাইক্রোসফট অফিস ইউজার রয়েছে। আর এই মাইক্রোসফট অফিসের সবচেয়ে গুরুত্বপূর্ণ ৩টি সফটওয়্যার - MS Word, MS Excel ও MS PowerPoint. বই, চিঠিপত্র, রিজিউমি, অ্যাপ্লিকেশন, বা অন্য ডকুমেন্টেশনের কাজ লেখার জন্য মাইক্রোসফট ওয়ার্ড ব্যবহৃত হয়। অন্যদিকে', 'মাইক্রোসফট অফিস সফটওয়্যারের ১০টিরও বেশি প্রজেক্ট ও এপ্লিকেশন\r\n\r\nMS Word-এ নিউজ ডকুমেন্টস, বিজনেস কার্ড, লেটার হেড ও 3D মডেল তৈরি'),
(9, '107', 'Graphic Designing', '৩', '৩', '১', '৩০', '৮০০০', 'graphic.jpg', 'প্রতিদিনের ব্যক্তিগত কিংবা অফিসিয়াল কাজে সবচেয়ে বেশি ব্যবহৃত সফটওয়্যারগুলোর মধ্যে Adobe Illustrator অন্যতম। আপনি যদি ডিজাইন সেক্টরে ক্যারিয়ার গড়তে চান তাহলে এডোবি ইলাস্ট্রেটরে অবশ্যই দক্ষতা অর্জন করতে হবে। Adobe Illustrator এ ', 'Color & Gradient color apply\r\n\r\nTransforming'),
(10, '110', 'Other', '৩', '৩', '2', '৩০', '12000', 'rcblogo.png', 'MS Office Complete Course কোর্সটির মাধ্যমে স্কিল অর্জন করে একাডেমিক এবং প্রফেশনাল ক্ষেত্রে রিপোর্ট, অ্যাসাইনমেন্ট, প্রেজেন্টেশন স্লাইড তৈরি ', 'MS Office Complete Course কোর্সটির মাধ্যমে স্কিল অর্জন করে একাডেমিক এবং প্রফেশনাল ক্ষেত্রে রিপোর্ট, অ্যাসাইনমেন্ট, প্রেজেন্টেশন স্লাইড তৈরি ');

-- --------------------------------------------------------

--
-- Table structure for table `service_info`
--

CREATE TABLE `service_info` (
  `id` int(10) NOT NULL,
  `serviceid` varchar(50) NOT NULL,
  `servicename` varchar(100) NOT NULL,
  `aboutservice` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `service_info`
--

INSERT INTO `service_info` (`id`, `serviceid`, `servicename`, `aboutservice`) VALUES
(2, '11', 'কম্পিউটার প্রশিক্ষণ bfm', 'কম্পিউটার প্রশিক্ষণ কেন্দ্র'),
(3, '22', 'কম্পিউটার প্রশিক্ষণ', 'কম্পিউটার প্রশিক্ষণ কেন্দ্র'),
(4, '33', 'কম্পিউটার প্রশিক্ষণ', 'কম্পিউটার প্রশিক্ষণ কেন্দ্র');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `course_info`
--
ALTER TABLE `course_info`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `service_info`
--
ALTER TABLE `service_info`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `course_info`
--
ALTER TABLE `course_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `service_info`
--
ALTER TABLE `service_info`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
