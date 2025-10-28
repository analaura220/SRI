-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: localhost    Database: sri
-- ------------------------------------------------------
-- Server version	8.0.43

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `documentos`
--

DROP TABLE IF EXISTS `documentos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `documentos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_artigo` int NOT NULL,
  `id_termo` int NOT NULL,
  `frequencia_do_termo` float NOT NULL,
  `tf_logaritimo` float NOT NULL,
  `idf_logaritimo` float NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_artigo` (`id_artigo`),
  KEY `id_termo` (`id_termo`),
  CONSTRAINT `documentos_ibfk_1` FOREIGN KEY (`id_artigo`) REFERENCES `artigos` (`id`),
  CONSTRAINT `documentos_ibfk_2` FOREIGN KEY (`id_termo`) REFERENCES `dicionario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `documentos`
--

LOCK TABLES `documentos` WRITE;
/*!40000 ALTER TABLE `documentos` DISABLE KEYS */;
INSERT INTO `documentos` VALUES (1,1,1,5,1.699,0.398),(2,1,2,4,1.602,0.495),(3,1,3,6,1.778,0.222),(4,1,4,3,1.477,0.602),(5,1,22,4,1.602,0.398),(6,2,5,7,1.845,0.398),(7,2,6,6,1.778,0.477),(8,2,7,4,1.602,0.699),(9,2,8,3,1.477,0.845),(10,2,9,2,1.301,0.954),(11,3,10,5,1.699,0.398),(12,3,11,4,1.602,0.602),(13,3,12,4,1.602,0.699),(14,3,13,3,1.477,0.778),(15,3,14,3,1.477,0.544),(16,3,25,2,1.301,0.699),(17,4,4,4,1.602,0.602),(18,4,15,5,1.699,0.477),(19,4,16,5,1.699,0.544),(20,4,17,6,1.778,0.398),(21,4,18,2,1.301,0.954),(22,4,19,2,1.301,0.778),(23,5,22,5,1.699,0.398),(24,5,20,4,1.602,0.699),(25,5,5,3,1.477,0.398),(26,5,21,4,1.602,0.699),(27,5,3,4,1.602,0.222),(28,5,1,2,1.301,0.398),(29,5,10,2,1.301,0.398);
/*!40000 ALTER TABLE `documentos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-27 21:22:41
