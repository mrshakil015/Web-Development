-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Mar 11, 2024 at 07:33 PM
-- Server version: 8.0.30
-- PHP Version: 8.1.10

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
  `id` int NOT NULL,
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `course_info`
--

INSERT INTO `course_info` (`id`, `courseid`, `course_name`, `month_duration`, `weekly`, `duration_hour`, `duration_minute`, `amount`, `image_name`, `aboutcourse`, `coursetopic`) VALUES
(3, '102', 'Digital Marketing', '১', '৩', '১', '৩০', '৫০০০', 'digitalmarketing.jpg', 'ব্যক্তিগত কাজ, একাডেমিক কিংবা ক্যারিয়ার -যেকোনো ক্ষেত্রে এগিয়ে থাকতে হলে যে বিষয়টি সম্পর্কে আপনাকে জানতেই হবে সেটি হলো মাইক্রোসফট অফিস। বিশ্বে ১২০ কোটি মাইক্রোসফট অফিস ইউজার রয়েছে। আর এই মাইক্রোসফট অফিসের সবচেয়ে গুরুত্বপূর্ণ ৩টি সফটওয়্যার - MS Word, MS Excel ও MS PowerPoint. বই, চিঠিপত্র, রিজিউমি, অ্যাপ্লিকেশন, বা অন্য ডকুমেন্টেশনের কাজ লেখার জন্য মাইক্রোসফট ওয়ার্ড ব্যবহৃত হয়। অন্যদিকে', 'মাইক্রোসফট অফিস সফটওয়্যারের ১০টিরও বেশি প্রজেক্ট ও এপ্লিকেশন\r\n\r\nMS Word-এ নিউজ ডকুমেন্টস, বিজনেস কার্ড, লেটার হেড ও 3D মডেল '),
(5, '103', 'Office Application Program', '৩', '৩/৫', '১', '৩০', '৩৮০০', 'msoffice.png', 'ব্যক্তিগত কাজ, একাডেমিক কিংবা ক্যারিয়ার -যেকোনো ক্ষেত্রে এগিয়ে থাকতে হলে যে বিষয়টি সম্পর্কে আপনাকে জানতেই হবে সেটি হলো মাইক্রোসফট অফিস। বিশ্বে ১২০ কোটি মাইক্রোসফট অফিস ইউজার রয়েছে। আর এই মাইক্রোসফট অফিসের সবচেয়ে গুরুত্বপূর্ণ ৩টি সফটওয়্যার - MS Word, MS Excel ও MS PowerPoint. বই, চিঠিপত্র, রিজিউমি, অ্যাপ্লিকেশন, বা অন্য ডকুমেন্টেশনের কাজ লেখার জন্য মাইক্রোসফট ওয়ার্ড ব্যবহৃত হয়। অন্যদিকে', 'মাইক্রোসফট অফিস সফটওয়্যারের ১০টিরও বেশি প্রজেক্ট ও এপ্লিকেশন\r\n\r\nMS Word-এ নিউজ ডকুমেন্টস, বিজনেস কার্ড, লেটার হেড ও 3D মডেল তৈরি'),
(9, '107', 'Graphic Designing', '৩', '৩', '১', '৩০', '৮০০০', 'graphic.jpg', 'প্রতিদিনের ব্যক্তিগত কিংবা অফিসিয়াল কাজে সবচেয়ে বেশি ব্যবহৃত সফটওয়্যারগুলোর মধ্যে Adobe Illustrator অন্যতম। আপনি যদি ডিজাইন সেক্টরে ক্যারিয়ার গড়তে চান তাহলে এডোবি ইলাস্ট্রেটরে অবশ্যই দক্ষতা অর্জন করতে হবে। Adobe Illustrator এ ', 'Color & Gradient color apply\r\n\r\nTransforming');

-- --------------------------------------------------------

--
-- Table structure for table `galleryimage_info`
--

CREATE TABLE `galleryimage_info` (
  `id` int NOT NULL,
  `imageid` int NOT NULL,
  `imagename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `galleryimage_info`
--

INSERT INTO `galleryimage_info` (`id`, `imageid`, `imagename`) VALUES
(1, 110, 'hardware.jpg'),
(2, 123, 'banner2.jpg'),
(3, 124, 'graphic.jpg'),
(4, 154, 'banner.png');

-- --------------------------------------------------------

--
-- Table structure for table `pending_studentinfo`
--

CREATE TABLE `pending_studentinfo` (
  `id` int NOT NULL,
  `studentid` int NOT NULL,
  `coursename` varchar(50) NOT NULL,
  `studentname` varchar(50) NOT NULL,
  `fathername` varchar(50) NOT NULL,
  `mothername` varchar(50) NOT NULL,
  `dob` varchar(20) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `mobile` varchar(20) NOT NULL,
  `address` varchar(100) NOT NULL,
  `studentphoto` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `pending_studentinfo`
--

INSERT INTO `pending_studentinfo` (`id`, `studentid`, `coursename`, `studentname`, `fathername`, `mothername`, `dob`, `gender`, `email`, `mobile`, `address`, `studentphoto`) VALUES
(1, 2381, 'Office Application Program', 'Md. Shakil', 'Md. Bashir', 'Halima', '3/3/01', 'Male', 'shakil.eub.cse@gmail.com', '017889891283', 'Hemayetpur', 'instructor.JPG'),
(2, 2049, 'Office Application Program', 'Md. Shakil', 'Md. Bashir', 'Halima', '3/3/01', 'Male', 'shakil.eub.cse@gmail.com', '2323432', 'Hemayetpur', 'instructor.JPG'),
(3, 7379, 'Graphic Designing', 'Md. Shakil', 'Md. Bashir', 'Halima', '3/3/01', 'Male', 'shakil.eub.cse@gmail.com', '23432', 'Hemayetpur', 'instructor.JPG'),
(4, 6489, 'Digital Marketing', 'Md. Shakil', 'Md. Bashir', 'Halima', '3/3/01', 'Male', 'shakil.eub.cse@gmail.com', '234234', 'Hemayetpur', 'director.JPG'),
(5, 6248, 'Graphic Designing', 'Md. Shakil', 'Md. Bashir', 'Halima', '3/3/01', 'Male', 'shakil.eub.cse@gmail.com', '324', 'Hemayetpur', '6248_director.JPG'),
(6, 5404, 'Office Application Program', 'Md. Shakil', 'Md. Bashir', 'Halima', '2024-03-09', 'Male', 'shakil.eub.cse@gmail.com', '0187878', 'Hemayetpur', '5404_Python4.png');

-- --------------------------------------------------------

--
-- Table structure for table `service_info`
--

CREATE TABLE `service_info` (
  `id` int NOT NULL,
  `serviceid` varchar(50) NOT NULL,
  `servicename` varchar(100) NOT NULL,
  `aboutservice` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `service_info`
--

INSERT INTO `service_info` (`id`, `serviceid`, `servicename`, `aboutservice`) VALUES
(2, '11', 'কম্পিউটার প্রশিক্ষণ', 'আমাদের প্রতিষ্ঠানে আমরা দক্ষ জনবল তৈরী করতে কম্পিউটারের বিভিন্ন কোর্সের উপর শিক্ষার্থীদের প্রশিক্ষণ দিয়ে থাকি।'),
(3, '22', 'কম্পিউটার সেলস এবং সার্ভিস', 'আমরা গ্রাহকদের প্রয়োজনীয় সফটওয়্যার ও হার্ডওয়্যার পরামর্শ দিয়ে সঠিক সমাধান প্রদান করে থাকি এবং আমরা কম্পিউটার ও কম্পিউটারের যাবতীয় যন্ত্রপাতি বিক্রয় করে থাকি।'),
(4, '33', 'অনলাইনে ভর্তি এবং চাকুরীর আবেদন', '.'),
(6, '103', 'NID Card সংক্রান্ত কাজ', '.'),
(7, '104', 'ভিসা চেক ও পাসপোর্টের আবেদন', '.'),
(8, '105', 'খাজনার রশিদ ও টাকা জমা', '.'),
(9, '106', 'কম্পোজ, বায়না ও চুক্তিপত্র দলিল', '.'),
(10, '107', 'ছবি ও ডকুমেন্ট প্রিন্ট', '.');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `course_info`
--
ALTER TABLE `course_info`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `galleryimage_info`
--
ALTER TABLE `galleryimage_info`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `pending_studentinfo`
--
ALTER TABLE `pending_studentinfo`
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
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `galleryimage_info`
--
ALTER TABLE `galleryimage_info`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `pending_studentinfo`
--
ALTER TABLE `pending_studentinfo`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `service_info`
--
ALTER TABLE `service_info`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
