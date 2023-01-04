-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: mess_management
-- ------------------------------------------------------
-- Server version	8.0.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cut`
--

DROP TABLE IF EXISTS `cut`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cut` (
  `adm_no` char(8) NOT NULL,
  `_1` tinyint(1) NOT NULL DEFAULT '1',
  `_2` tinyint(1) NOT NULL DEFAULT '1',
  `_3` tinyint(1) NOT NULL DEFAULT '1',
  `_4` tinyint(1) NOT NULL DEFAULT '1',
  `_5` tinyint(1) NOT NULL DEFAULT '1',
  `_6` tinyint(1) NOT NULL DEFAULT '1',
  `_7` tinyint(1) NOT NULL DEFAULT '1',
  `_8` tinyint(1) NOT NULL DEFAULT '1',
  `_9` tinyint(1) NOT NULL DEFAULT '1',
  `_10` tinyint(1) NOT NULL DEFAULT '1',
  `_11` tinyint(1) NOT NULL DEFAULT '1',
  `_12` tinyint(1) NOT NULL DEFAULT '1',
  `_13` tinyint(1) NOT NULL DEFAULT '1',
  `_14` tinyint(1) NOT NULL DEFAULT '1',
  `_15` tinyint(1) NOT NULL DEFAULT '1',
  `_16` tinyint(1) NOT NULL DEFAULT '1',
  `_17` tinyint(1) NOT NULL DEFAULT '1',
  `_18` tinyint(1) NOT NULL DEFAULT '1',
  `_19` tinyint(1) NOT NULL DEFAULT '1',
  `_20` tinyint(1) NOT NULL DEFAULT '1',
  `_21` tinyint(1) NOT NULL DEFAULT '1',
  `_22` tinyint(1) NOT NULL DEFAULT '1',
  `_23` tinyint(1) NOT NULL DEFAULT '1',
  `_24` tinyint(1) NOT NULL DEFAULT '1',
  `_25` tinyint(1) NOT NULL DEFAULT '1',
  `_26` tinyint(1) NOT NULL DEFAULT '1',
  `_27` tinyint(1) NOT NULL DEFAULT '1',
  `_28` tinyint(1) NOT NULL DEFAULT '1',
  `_29` tinyint(1) NOT NULL DEFAULT '1',
  `_30` tinyint(1) NOT NULL DEFAULT '1',
  `_31` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`adm_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cut`
--

LOCK TABLES `cut` WRITE;
/*!40000 ALTER TABLE `cut` DISABLE KEYS */;
INSERT INTO `cut` VALUES ('11111111',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('11112222',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('11122233',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('11223344',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1),('ELECTRA',1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1);
/*!40000 ALTER TABLE `cut` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `cut_AFTER_INSERT` AFTER INSERT ON `cut` FOR EACH ROW BEGIN
	declare eat int;
	set eat =(select _1+_2+_3+_4+_5+_6+_7+_8+_9+_10+_11+_12+_13+_14+_15+_16+_17+_18+_19+_20+_21+_22+_23+_24+_25+_26+_27+_28+_29+_30+_31
					from cut
					where adm_no=new.adm_no
                    );
	update student set eat_count=eat where adm_no=new.adm_no;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `cut_AFTER_UPDATE` AFTER UPDATE ON `cut` FOR EACH ROW BEGIN
	declare eat int;
	set eat =(select _1+_2+_3+_4+_5+_6+_7+_8+_9+_10+_11+_12+_13+_14+_15+_16+_17+_18+_19+_20+_21+_22+_23+_24+_25+_26+_27+_28+_29+_30+_31
					from cut
					where adm_no=new.adm_no
                    );
	update student set eat_count=eat where adm_no=new.adm_no;
    
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `hostel`
--

DROP TABLE IF EXISTS `hostel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hostel` (
  `id` int NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `rent` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hostel`
--

LOCK TABLES `hostel` WRITE;
/*!40000 ALTER TABLE `hostel` DISABLE KEYS */;
INSERT INTO `hostel` VALUES (1,'M B Hostel',500),(2,'HS-1 Hostel',600),(3,'HS-2 Hostel',600),(4,'Kennedy Hostel',1000),(5,'D J Hostel',2000);
/*!40000 ALTER TABLE `hostel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `log_cred`
--

DROP TABLE IF EXISTS `log_cred`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `log_cred` (
  `adm_no` char(8) NOT NULL,
  `pass` varchar(20) NOT NULL DEFAULT '1234',
  `admin` tinyint NOT NULL DEFAULT '0',
  PRIMARY KEY (`adm_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log_cred`
--

LOCK TABLES `log_cred` WRITE;
/*!40000 ALTER TABLE `log_cred` DISABLE KEYS */;
INSERT INTO `log_cred` VALUES ('11111111','1234',0),('11112222','1234',0),('11122233','1234',0),('11223344','1234',0),('admin','admin',1),('ELECTRA','1234',0);
/*!40000 ALTER TABLE `log_cred` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mess_cost`
--

DROP TABLE IF EXISTS `mess_cost`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mess_cost` (
  `date` date NOT NULL,
  `Month_bill` float NOT NULL DEFAULT '0',
  PRIMARY KEY (`date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mess_cost`
--

LOCK TABLES `mess_cost` WRITE;
/*!40000 ALTER TABLE `mess_cost` DISABLE KEYS */;
INSERT INTO `mess_cost` VALUES ('2022-01-01',10),('2023-01-01',1222),('2023-01-04',4000);
/*!40000 ALTER TABLE `mess_cost` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `adm_no` char(8) NOT NULL,
  `name` varchar(50) NOT NULL,
  `hostel_id` int NOT NULL,
  `mess_bill` float DEFAULT NULL,
  `hostel_bill` float DEFAULT NULL,
  `total_bill` float GENERATED ALWAYS AS ((`hostel_bill` + `mess_bill`)) VIRTUAL,
  `eat_count` int DEFAULT '0',
  PRIMARY KEY (`adm_no`),
  KEY `student_ibfk_1` (`hostel_id`),
  CONSTRAINT `student_ibfk_1` FOREIGN KEY (`hostel_id`) REFERENCES `hostel` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` (`adm_no`, `name`, `hostel_id`, `mess_bill`, `hostel_bill`, `eat_count`) VALUES ('11111111','ELECTRA',1,1000,500,31),('11112222','abdul',2,1000,600,31),('11122233','rahul',2,1000,600,31),('11223344','joel',1,1000,500,31);
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `hostel_bill_updater_insert` BEFORE INSERT ON `student` FOR EACH ROW BEGIN
	declare bill int;
    select hostel.rent into bill from hostel where id=new.hostel_id;
    set new.hostel_bill=bill;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `hostel_bill_updater_update` BEFORE UPDATE ON `student` FOR EACH ROW BEGIN
	declare bill int;
    if(new.hostel_id<>old.hostel_id) then
		select hostel.rent into bill from hostel where id=new.hostel_id;
		set new.hostel_bill=bill;
    end if;
    
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Dumping routines for database 'mess_management'
--
/*!50003 DROP PROCEDURE IF EXISTS `authenticate` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `authenticate`(IN inadm_no char(8),IN inpass varchar(20))
BEGIN
declare passw varchar(20);

set passw=(select pass from log_cred where adm_no=inadm_no);
if passw = inpass then
	select TRUE,admin from log_cred where adm_no=inadm_no;
else
	select FALSE,FALSE;
end if;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `calc_mess_bill` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `calc_mess_bill`()
BEGIN
	-- Calculate the value of mess_bill in student
    declare total_days int;
	declare per_day_cost float;
	declare admno char(8);
	
	declare done int default FALSE;
	declare cur cursor for select adm_no from student;
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

	select sum(eat_count) into total_days from student;
	set per_day_cost=(select month_bill/total_days 
						from mess_cost order by date desc
						limit 1
					 );


	open cur;
	main_loop:loop
		fetch cur into admno;
		if done then
			leave main_loop;
		end if;
		update student
		set mess_bill=eat_count*per_day_cost
		where adm_no=admno;
	end loop; 
	close cur;


END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `create_new_mess_cost` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `create_new_mess_cost`()
BEGIN
	-- Create new row for next month
    insert into mess_cost(date) values (now());
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_student` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_student`(IN stu_adm_no char(8),IN stu_name varchar(50),IN stu_hostel_id int)
BEGIN
	insert into student(adm_no,name,hostel_id) values(stu_adm_no,stu_name,stu_hostel_id);
    insert into cut(adm_no) values(stu_adm_no);
    insert into log_cred(adm_no) values(stu_adm_no);
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `reset_cut` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `reset_cut`()
begin
    -- Reset all cut values to 1
    declare days int default day(last_day(now()));
    
    update cut set _1=1,_2=1,_3=1,_4=1,_5=1,_6=1,_7=1,_8=1,_9=1,_10=1,_11=1,_12=1,_13=1,_14=1,_15=1,_16=1,_17=1,_18=1,_19=1,_20=1,_21=1,_22=1,_23=1,_24=1,_25=1,_26=1,_27=1,_28=1,_29=0,_30=0,_31=0;
    
	if days>28 then
			update cut set _29=1;
	end if;
    if days>29 then
			update cut set _30=1;
	end if;
	if days>30 then
			update cut set _31=1;
	end if;
        
    
    
    
    
    
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `set_mess_cost` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `set_mess_cost`(IN cost int)
BEGIN
	update mess_cost 
    set month_bill=cost
    order by date desc
    limit 1;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-01-04 20:50:11
