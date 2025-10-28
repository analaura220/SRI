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
-- Table structure for table `artigos`
--

DROP TABLE IF EXISTS `artigos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `artigos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `titulo` varchar(500) NOT NULL,
  `filiacao` varchar(300) NOT NULL,
  `resumo` varchar(800) NOT NULL,
  `palavras_chaves` varchar(500) NOT NULL,
  `link` varchar(500) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artigos`
--

LOCK TABLES `artigos` WRITE;
/*!40000 ALTER TABLE `artigos` DISABLE KEYS */;
INSERT INTO `artigos` VALUES (1,'aprendizado de máquina em análise de dados','universidade federal de minas gerais','este artigo apresenta técnicas de aprendizado de máquina aplicadas à análise de grandes volumes de dados utilizando algoritmos de classificação e regressão','aprendizado, máquina, dados, algoritmos','http://artigos.com/ml-analise-dados'),(2,'redes neurais artificiais para reconhecimento de padrões','universidade de são paulo','estudo sobre redes neurais profundas aplicadas ao reconhecimento de padrões em imagens utilizando arquiteturas convolucionais','redes, neurais, padrões, imagens, convolucional','http://artigos.com/redes-neurais'),(3,'processamento de linguagem natural com transformers','universidade estadual de campinas','análise de modelos transformers para processamento de linguagem natural incluindo bert e gpt aplicados a tarefas de classificação de texto','linguagem, natural, transformers, bert, texto','http://artigos.com/pln-transformers'),(4,'algoritmos de busca e recuperação de informação','pontifícia universidade católica','revisão de algoritmos clássicos de recuperação de informação incluindo modelos booleanos e vetoriais para sistemas de busca','busca, recuperação, informação, booleano, vetorial','http://artigos.com/recuperacao-info'),(5,'análise de sentimentos em redes sociais','universidade federal do rio de janeiro','técnicas de análise de sentimentos aplicadas a dados de redes sociais utilizando aprendizado de máquina e processamento de linguagem natural','sentimentos, redes, sociais, análise, dados','http://artigos.com/analise-sentimentos');
/*!40000 ALTER TABLE `artigos` ENABLE KEYS */;
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
