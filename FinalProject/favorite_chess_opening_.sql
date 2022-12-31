-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 01, 2023 at 12:28 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Chess`
--

-- --------------------------------------------------------

--
-- Table structure for table `favorite chess opening?`
--

CREATE TABLE `favorite chess opening?` (
  `ChessID` int(11) NOT NULL,
  `Name` varchar(25) NOT NULL,
  `Chess_answers` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `favorite chess opening?`
--

INSERT INTO `favorite chess opening?` (`ChessID`, `Name`, `Chess_answers`) VALUES
(30, 'Anshul Prabu', 'f'),
(40, 'Sheila', 'qwe');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `favorite chess opening?`
--
ALTER TABLE `favorite chess opening?`
  ADD PRIMARY KEY (`ChessID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `favorite chess opening?`
--
ALTER TABLE `favorite chess opening?`
  MODIFY `ChessID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
