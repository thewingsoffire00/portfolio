/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - pest_control_rajagiri
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`pest_control` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `pest_control`;

/*Table structure for table `card` */

DROP TABLE IF EXISTS `card`;

CREATE TABLE `card` (
  `card_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `card_no` varchar(50) DEFAULT NULL,
  `card_name` varchar(50) DEFAULT NULL,
  `exp_date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`card_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `card` */

/*Table structure for table `category` */

DROP TABLE IF EXISTS `category`;

CREATE TABLE `category` (
  `cat_id` int(11) NOT NULL AUTO_INCREMENT,
  `image` varchar(100) DEFAULT NULL,
  `cat_name` varchar(50) DEFAULT NULL,
  `cat_desc` varchar(50) DEFAULT NULL,
  `cat_status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`cat_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `category` */

insert  into `category`(`cat_id`,`image`,`cat_name`,`cat_desc`,`cat_status`) values 
(1,'static/uploads/95e690c4-a182-4651-8e18-15de045d13b7a.jpg','ghj','gh','active');

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `complaint` varchar(100) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  `complaint_date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

/*Data for the table `complaint` */

/*Table structure for table `courier` */

DROP TABLE IF EXISTS `courier`;

CREATE TABLE `courier` (
  `courier_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(52) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  `cour_name` varchar(50) DEFAULT NULL,
  `cour_building_name` varchar(100) DEFAULT NULL,
  `cour_street` varchar(50) DEFAULT NULL,
  `cour_district` varchar(50) DEFAULT NULL,
  `cour_state` varchar(50) DEFAULT NULL,
  `cour_pincode` varchar(50) DEFAULT NULL,
  `cour_phone` varchar(50) DEFAULT NULL,
  `cour_email` varchar(50) DEFAULT NULL,
  `data_added` varchar(100) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`courier_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `courier` */

/*Table structure for table `customer` */

DROP TABLE IF EXISTS `customer`;

CREATE TABLE `customer` (
  `customer_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `c_fname` varchar(50) DEFAULT NULL,
  `c_lname` varchar(52) DEFAULT NULL,
  `c_housename` varchar(50) DEFAULT NULL,
  `c_street` varchar(60) DEFAULT NULL,
  `c_district` varchar(50) DEFAULT NULL,
  `c_state` varchar(50) DEFAULT NULL,
  `c_pincode` varchar(50) DEFAULT NULL,
  `c_phone` varchar(50) DEFAULT NULL,
  `c_email` varchar(50) DEFAULT NULL,
  `data_added` varchar(100) DEFAULT NULL,
  `c_status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `customer` */

/*Table structure for table `delivery` */

DROP TABLE IF EXISTS `delivery`;

CREATE TABLE `delivery` (
  `delivery_id` int(11) NOT NULL AUTO_INCREMENT,
  `order_master_id` int(11) DEFAULT NULL,
  `courier_id` int(11) DEFAULT NULL,
  `delivery_date` varchar(50) DEFAULT NULL,
  `delivery_expect` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`delivery_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `delivery` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `username` varchar(52) NOT NULL,
  `password` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`username`,`password`,`type`,`status`) values 
('admin@gmail.com','admin','admin','active');

/*Table structure for table `order_details` */

DROP TABLE IF EXISTS `order_details`;

CREATE TABLE `order_details` (
  `order_details_id` int(11) NOT NULL AUTO_INCREMENT,
  `order_master_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `quantity` int(50) DEFAULT NULL,
  `total_price` int(50) DEFAULT NULL,
  PRIMARY KEY (`order_details_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `order_details` */

/*Table structure for table `order_master` */

DROP TABLE IF EXISTS `order_master`;

CREATE TABLE `order_master` (
  `order_master_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `total_amount` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `ostatus` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`order_master_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `order_master` */

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `card_id` int(11) DEFAULT NULL,
  `order_master_id` int(11) DEFAULT NULL,
  `amount` varchar(50) DEFAULT NULL,
  `payment_date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `subcat_id` int(50) DEFAULT NULL,
  `product_name` varchar(50) DEFAULT NULL,
  `product_desc` varchar(50) DEFAULT NULL,
  `product_img` varchar(1500) DEFAULT NULL,
  `product_rate` varchar(50) DEFAULT NULL,
  `stock` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `product` */

/*Table structure for table `purchase_details` */

DROP TABLE IF EXISTS `purchase_details`;

CREATE TABLE `purchase_details` (
  `pdetails_id` int(11) NOT NULL AUTO_INCREMENT,
  `pmaster_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `cost_price` int(50) DEFAULT NULL,
  `selling_price` int(50) DEFAULT NULL,
  `quantity` int(50) DEFAULT NULL,
  PRIMARY KEY (`pdetails_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `purchase_details` */

/*Table structure for table `purchase_master` */

DROP TABLE IF EXISTS `purchase_master`;

CREATE TABLE `purchase_master` (
  `pmaster_id` int(11) NOT NULL AUTO_INCREMENT,
  `vendor_id` int(11) DEFAULT NULL,
  `staff_id` int(11) DEFAULT NULL,
  `total_amount` varchar(50) DEFAULT NULL,
  `pstatus` varchar(50) DEFAULT NULL,
  `date_added` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`pmaster_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `purchase_master` */

/*Table structure for table `purchased` */

DROP TABLE IF EXISTS `purchased`;

CREATE TABLE `purchased` (
  `purchased_id` int(11) NOT NULL AUTO_INCREMENT,
  `pdetails_id` int(11) DEFAULT NULL,
  `order_details_id` int(11) DEFAULT NULL,
  `qty_purchased` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`purchased_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `purchased` */

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `staff_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(52) DEFAULT NULL,
  `staff_fname` varchar(50) DEFAULT NULL,
  `staff_lname` varchar(50) DEFAULT NULL,
  `staff_housename` varchar(50) DEFAULT NULL,
  `staff_street` varchar(50) DEFAULT NULL,
  `staff_district` varchar(50) DEFAULT NULL,
  `staff_state` varchar(50) DEFAULT NULL,
  `staff_pincode` varchar(50) DEFAULT NULL,
  `staff_phone` varchar(50) DEFAULT NULL,
  `staff_email` varchar(50) DEFAULT NULL,
  `staff_salary` varchar(50) DEFAULT NULL,
  `staff_date` varchar(50) DEFAULT NULL,
  `staff_status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

/*Table structure for table `subcategory` */

DROP TABLE IF EXISTS `subcategory`;

CREATE TABLE `subcategory` (
  `subcat_id` int(11) NOT NULL AUTO_INCREMENT,
  `category_id` varchar(100) DEFAULT NULL,
  `subcat_name` varchar(50) DEFAULT NULL,
  `subcat_desc` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`subcat_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `subcategory` */

/*Table structure for table `vendor` */

DROP TABLE IF EXISTS `vendor`;

CREATE TABLE `vendor` (
  `vendor_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_d` varchar(50) DEFAULT NULL,
  `v_name` varchar(50) DEFAULT NULL,
  `v_email` varchar(50) DEFAULT NULL,
  `v_building_name` varchar(50) DEFAULT NULL,
  `v_street` varchar(50) DEFAULT NULL,
  `v_district` varchar(50) DEFAULT NULL,
  `v_state` varchar(50) DEFAULT NULL,
  `v_pincode` varchar(56) DEFAULT NULL,
  `v_phone` varchar(50) DEFAULT NULL,
  `status` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`vendor_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `vendor` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
