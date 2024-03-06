-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Gép: 127.0.0.1
-- Létrehozás ideje: 2024. Már 06. 11:02
-- Kiszolgáló verziója: 10.4.32-MariaDB
-- PHP verzió: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Adatbázis: `autoberles`
--

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `autok`
--

CREATE TABLE `autok` (
  `id` int(11) NOT NULL,
  `rendszam` varchar(6) NOT NULL,
  `tipus` varchar(100) NOT NULL,
  `evjarat` year(4) NOT NULL,
  `szin` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_hungarian_ci;

--
-- A tábla adatainak kiíratása `autok`
--

INSERT INTO `autok` (`id`, `rendszam`, `tipus`, `evjarat`, `szin`) VALUES
(1, 'ABC448', 'Wolkswagen Golf', '2012', 'Kék'),
(2, 'ABC456', 'Ford Ka', '2003', 'Pink'),
(3, 'ABC157', 'Ford Mondeo', '2015', 'Fekete'),
(4, 'ABC123', 'Volkswagen Golf', '2011', 'Fehér'),
(6, 'lol', 'lol', '0000', 'lol');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `berlok`
--

CREATE TABLE `berlok` (
  `id` int(11) NOT NULL,
  `nev` varchar(100) NOT NULL,
  `jogositvanyszama` varchar(15) NOT NULL,
  `telefonszam` varchar(20) NOT NULL,
  `szuletesiido` date NOT NULL,
  `lakcim` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_hungarian_ci;

--
-- A tábla adatainak kiíratása `berlok`
--

INSERT INTO `berlok` (`id`, `nev`, `jogositvanyszama`, `telefonszam`, `szuletesiido`, `lakcim`) VALUES
(1, 'Gipsz Jakab', 'VE445112', '0641555223', '0000-00-00', ''),
(2, 'Kandúr Károly', 'LR337157', '0641334112', '0000-00-00', '');

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `kolcsonzes`
--

CREATE TABLE `kolcsonzes` (
  `id` int(11) NOT NULL,
  `berloid` int(11) NOT NULL,
  `autoid` int(11) NOT NULL,
  `berletkezdete` datetime NOT NULL,
  `napokszama` int(11) NOT NULL,
  `napidij` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_hungarian_ci;

--
-- A tábla adatainak kiíratása `kolcsonzes`
--

INSERT INTO `kolcsonzes` (`id`, `berloid`, `autoid`, `berletkezdete`, `napokszama`, `napidij`) VALUES
(1, 2, 3, '2017-04-23 00:00:00', 6, 12500),
(2, 1, 4, '2017-04-25 00:00:00', 0, 9999);

--
-- Indexek a kiírt táblákhoz
--

--
-- A tábla indexei `autok`
--
ALTER TABLE `autok`
  ADD PRIMARY KEY (`id`);

--
-- A tábla indexei `berlok`
--
ALTER TABLE `berlok`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nev` (`nev`),
  ADD UNIQUE KEY `jogositvanyszama` (`jogositvanyszama`);

--
-- A tábla indexei `kolcsonzes`
--
ALTER TABLE `kolcsonzes`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `berletkezdete` (`berletkezdete`),
  ADD UNIQUE KEY `napidij` (`napidij`),
  ADD KEY `berloid` (`berloid`),
  ADD KEY `autoid` (`autoid`);

--
-- A kiírt táblák AUTO_INCREMENT értéke
--

--
-- AUTO_INCREMENT a táblához `autok`
--
ALTER TABLE `autok`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT a táblához `berlok`
--
ALTER TABLE `berlok`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT a táblához `kolcsonzes`
--
ALTER TABLE `kolcsonzes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Megkötések a kiírt táblákhoz
--

--
-- Megkötések a táblához `kolcsonzes`
--
ALTER TABLE `kolcsonzes`
  ADD CONSTRAINT `kolcsonzes_ibfk_2` FOREIGN KEY (`berloid`) REFERENCES `berlok` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
