/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 10.4.27-MariaDB : Database - accessoriesshop
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/accessoriesshop /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE accessoriesshop;

/*Table structure for table card */

DROP TABLE IF EXISTS card;

CREATE TABLE card (
  card_id int(11) NOT NULL AUTO_INCREMENT,
  customer_id int(11) DEFAULT NULL,
  card_no varchar(50) DEFAULT NULL,
  card_name varchar(50) DEFAULT NULL,
  exp_date varchar(50) DEFAULT NULL,
  PRIMARY KEY (card_id)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table card */

insert  into card(card_id,customer_id,card_no,card_name,exp_date) values 
(1,1,'1232453543564675','dsafadsfsdf','01'),
(2,1,'1232453543564675','dsafadsfsdf','01'),
(3,1,'1232453543564675','dsafadsfsdf','01'),
(4,1,'2154635547687869','dnskskdnf','02');

/*Table structure for table category */

DROP TABLE IF EXISTS category;

CREATE TABLE category (
  cat_id int(11) NOT NULL AUTO_INCREMENT,
  cat_name varchar(50) DEFAULT NULL,
  cat_desc varchar(50) DEFAULT NULL,
  cat_status varchar(50) DEFAULT NULL,
  PRIMARY KEY (cat_id)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table category */

insert  into category(cat_id,cat_name,cat_desc,cat_status) values 
(1,'asdad','adssad','inactive');

/*Table structure for table courier */

DROP TABLE IF EXISTS courier;

CREATE TABLE courier (
  courier_id int(11) NOT NULL AUTO_INCREMENT,
  staff_id int(52) DEFAULT NULL,
  username varchar(50) DEFAULT NULL,
  cour_name varchar(50) DEFAULT NULL,
  cour_street varchar(50) DEFAULT NULL,
  cour_district varchar(50) DEFAULT NULL,
  cour_state varchar(50) DEFAULT NULL,
  cour_pincode varchar(50) DEFAULT NULL,
  cour_phone varchar(50) DEFAULT NULL,
  cour_email varchar(50) DEFAULT NULL,
  status varchar(50) DEFAULT NULL,
  PRIMARY KEY (courier_id)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table courier */

insert  into courier(courier_id,staff_id,username,cour_name,cour_street,cour_district,cour_state,cour_pincode,cour_phone,cour_email,status) values 
(1,NULL,'cour','bdss','jbsfsd','jbjsadcsaf','bjbfdsdf','68754','7896541230','jbcsdf@dsgfsg.jhg','inactive'),
(2,0,'harilal@gmail.com','dtdc','asdsd','eranakulam','kerala','555555','8564562516','pthalika8@gmail.com','active');

/*Table structure for table customer */

DROP TABLE IF EXISTS customer;

CREATE TABLE customer (
  customer_id int(11) NOT NULL AUTO_INCREMENT,
  username varchar(50) DEFAULT NULL,
  c_fname varchar(50) DEFAULT NULL,
  c_lname varchar(52) DEFAULT NULL,
  c_housename varchar(50) DEFAULT NULL,
  c_street varchar(60) DEFAULT NULL,
  c_district varchar(50) DEFAULT NULL,
  c_state varchar(50) DEFAULT NULL,
  c_pincode varchar(50) DEFAULT NULL,
  c_dob varchar(50) DEFAULT NULL,
  c_gender varchar(50) DEFAULT NULL,
  c_phone varchar(50) DEFAULT NULL,
  c_email varchar(50) DEFAULT NULL,
  c_status varchar(50) DEFAULT NULL,
  PRIMARY KEY (customer_id)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table customer */

insert  into customer(customer_id,username,c_fname,c_lname,c_housename,c_street,c_district,c_state,c_pincode,c_dob,c_gender,c_phone,c_email,c_status) values 
(1,'cus@gmail.com','amal','jhjh','v','b','jhb','jhbj','hbj','hb','jhb','hb','jhb','hb'),
(2,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);

/*Table structure for table delivery */

DROP TABLE IF EXISTS delivery;

CREATE TABLE delivery (
  delivery_id int(11) NOT NULL AUTO_INCREMENT,
  order_master_id int(11) DEFAULT NULL,
  courier_id int(11) DEFAULT NULL,
  delivery_date varchar(50) DEFAULT NULL,
  status varchar(50) DEFAULT NULL,
  PRIMARY KEY (delivery_id)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table delivery */

insert  into delivery(delivery_id,order_master_id,courier_id,delivery_date,status) values 
(1,1,1,'2023-02-18','Delivery Completed'),
(2,1,1,'2023-02-18','Delivery Completed');

/*Table structure for table login */

DROP TABLE IF EXISTS login;

CREATE TABLE login (
  username varchar(52) NOT NULL,
  password varchar(50) DEFAULT NULL,
  type varchar(50) DEFAULT NULL,
  status varchar(50) DEFAULT NULL,
  PRIMARY KEY (username)
) ENGINE=MyISAM DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table login */

insert  into login(username,password,type,status) values 
('admin@gmail.com','admin','admin','active'),
('staff@gmail.com','staff','staff','active'),
('cour','cour','courier','active'),
('cus@gmail.com','cus','customer','active'),
('asd@gmail.com','123132','staff','inactive'),
('harilal@gmail.com','sadfdf','courier','inactive');

/*Table structure for table order_details */

DROP TABLE IF EXISTS order_details;

CREATE TABLE order_details (
  order_details_id int(11) NOT NULL AUTO_INCREMENT,
  order_master_id int(11) DEFAULT NULL,
  product_id int(11) DEFAULT NULL,
  quantity int(50) DEFAULT NULL,
  total_price int(50) DEFAULT NULL,
  PRIMARY KEY (order_details_id)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table order_details */

insert  into order_details(order_details_id,order_master_id,product_id,quantity,total_price) values 
(1,1,1,1,1040),
(2,2,1,1,2300);

/*Table structure for table order_master */

DROP TABLE IF EXISTS order_master;

CREATE TABLE order_master (
  order_master_id int(11) NOT NULL AUTO_INCREMENT,
  customer_id int(11) DEFAULT NULL,
  total_amount varchar(50) DEFAULT NULL,
  date varchar(50) DEFAULT NULL,
  ostatus varchar(50) DEFAULT NULL,
  PRIMARY KEY (order_master_id)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table order_master */

insert  into order_master(order_master_id,customer_id,total_amount,date,ostatus) values 
(1,1,'1040','2023-02-18','Accepted by Courier'),
(2,1,'2300','2023-02-21','paid');

/*Table structure for table payment */

DROP TABLE IF EXISTS payment;

CREATE TABLE payment (
  payment_id int(11) NOT NULL AUTO_INCREMENT,
  card_id int(11) DEFAULT NULL,
  order_master_id int(11) DEFAULT NULL,
  amount varchar(50) DEFAULT NULL,
  payment_date varchar(50) DEFAULT NULL,
  PRIMARY KEY (payment_id)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table payment */

insert  into payment(payment_id,card_id,order_master_id,amount,payment_date) values 
(1,1,1,'1040','2023-02-18 15:21:03'),
(2,2,1,'1040','2023-02-18 15:22:28'),
(3,3,1,'1040','2023-02-18 15:44:57'),
(4,4,2,'2300','2023-02-21 13:33:10');

/*Table structure for table product */

DROP TABLE IF EXISTS product;

CREATE TABLE product (
  product_id int(11) NOT NULL AUTO_INCREMENT,
  cat_id int(11) DEFAULT NULL,
  subcat_id int(50) DEFAULT NULL,
  product_name varchar(50) DEFAULT NULL,
  product_desc varchar(50) DEFAULT NULL,
  product_img varchar(1500) DEFAULT NULL,
  product_rate varchar(50) DEFAULT NULL,
  stock varchar(50) DEFAULT NULL,
  status varchar(50) DEFAULT NULL,
  PRIMARY KEY (product_id)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table product */

insert  into product(product_id,cat_id,subcat_id,product_name,product_desc,product_img,product_rate,stock,status) values 
(1,1,1,'jewel','kkkk','static/uploads/5adda81e-36a3-44f8-95ef-400b8ade0e06cool-4k-wallpaper-2.jpg','0','0','inactive');

/*Table structure for table purchase_details */

DROP TABLE IF EXISTS purchase_details;

CREATE TABLE purchase_details (
  pdetails_id int(11) NOT NULL AUTO_INCREMENT,
  pmaster_id int(11) DEFAULT NULL,
  product_id int(11) DEFAULT NULL,
  cost_price int(50) DEFAULT NULL,
  selling_price int(50) DEFAULT NULL,
  quantity int(50) DEFAULT NULL,
  PRIMARY KEY (pdetails_id)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table purchase_details */

insert  into purchase_details(pdetails_id,pmaster_id,product_id,cost_price,selling_price,quantity) values 
(1,1,1,2000,2300,9),
(2,2,1,1000,1040,13);

/*Table structure for table purchase_master */

DROP TABLE IF EXISTS purchase_master;

CREATE TABLE purchase_master (
  pmaster_id int(11) NOT NULL AUTO_INCREMENT,
  vendor_id int(11) DEFAULT NULL,
  staff_id int(11) DEFAULT NULL,
  total_amount varchar(50) DEFAULT NULL,
  pstatus varchar(50) DEFAULT NULL,
  date_added varchar(50) DEFAULT NULL,
  PRIMARY KEY (pmaster_id)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table purchase_master */

insert  into purchase_master(pmaster_id,vendor_id,staff_id,total_amount,pstatus,date_added) values 
(1,1,0,'pending','20000','2023-02-18 12:35:03'),
(2,1,0,'15000','paid','2023-02-18 12:38:07');

/*Table structure for table purchased */

DROP TABLE IF EXISTS purchased;

CREATE TABLE purchased (
  purchased_id int(11) NOT NULL AUTO_INCREMENT,
  pdetails_id int(11) DEFAULT NULL,
  order_details_id int(11) DEFAULT NULL,
  qty_purchased varchar(50) DEFAULT NULL,
  PRIMARY KEY (purchased_id)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci; 

/*Data for the table purchased */

insert  into purchased(purchased_id,pdetails_id,order_details_id,qty_purchased) values 
(1,2,1,'1'),
(2,1,2,'1');

/*Table structure for table staff */

DROP TABLE IF EXISTS staff;

CREATE TABLE staff (
  staff_id int(11) NOT NULL AUTO_INCREMENT,
  username varchar(52) DEFAULT NULL,
  staff_fname varchar(50) DEFAULT NULL,
  staff_lname varchar(50) DEFAULT NULL,
  staff_gender varchar(50) DEFAULT NULL,
  staff_dob varchar(50) DEFAULT NULL,
  staff_housename varchar(50) DEFAULT NULL,
  staff_street varchar(50) DEFAULT NULL,
  staff_district varchar(50) DEFAULT NULL,
  staff_state varchar(50) DEFAULT NULL,
  staff_pincode varchar(50) DEFAULT NULL,
  staff_phone varchar(50) DEFAULT NULL,
  staff_email varchar(50) DEFAULT NULL,
  staff_date varchar(50) DEFAULT NULL,
  staff_status varchar(50) DEFAULT NULL,
  PRIMARY KEY (staff_id)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table staff */

insert  into staff(staff_id,username,staff_fname,staff_lname,staff_gender,staff_dob,staff_housename,staff_street,staff_district,staff_state,staff_pincode,staff_phone,staff_email,staff_date,staff_status) values 
(1,'staff@gmail.com','jhgjhj','bjbh','male','2023-02-10','bj','hbj','hbj','hbjh','bj','hbj','hbj','hbh','active'),
(2,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),
(3,'asd@gmail.com','amal','amal','male','2023-02-22','rerrr','azheekal','alappy','rrrrq','68754','7894561230','asd@gmail.com','2023-02-18','inactive');

/*Table structure for table subcategory */

DROP TABLE IF EXISTS subcategory;

CREATE TABLE subcategory (
  subcat_id int(11) NOT NULL AUTO_INCREMENT,
  subcat_name varchar(50) DEFAULT NULL,
  subcat_desc varchar(50) DEFAULT NULL,
  status varchar(50) DEFAULT NULL,
  PRIMARY KEY (subcat_id)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table subcategory */

insert  into subcategory(subcat_id,subcat_name,subcat_desc,status) values 
(1,'dsacsd','csadfsd','inactive'),
(2,'asdad','asda','active');

/*Table structure for table vendor */

DROP TABLE IF EXISTS vendor;

CREATE TABLE vendor (
  vendor_id int(11) NOT NULL AUTO_INCREMENT,
  staff_d varchar(50) DEFAULT NULL,
  v_name varchar(50) DEFAULT NULL,
  v_email varchar(50) DEFAULT NULL,
  v_building_name varchar(50) DEFAULT NULL,
  v_street varchar(50) DEFAULT NULL,
  v_district varchar(50) DEFAULT NULL,
  v_state varchar(50) DEFAULT NULL,
  v_pincode varchar(56) DEFAULT NULL,
  v_phone varchar(50) DEFAULT NULL,
  status varchar(60) DEFAULT NULL,
  PRIMARY KEY (vendor_id)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

/*Data for the table vendor */

insert  into vendor(vendor_id,staff_d,v_name,v_email,v_building_name,v_street,v_district,v_state,v_pincode,v_phone,status) values 
(1,'0','hubolt','pthalika8@gmail.com','lkdfhkvfhg','32nd street','eranakulam','cherthala','688532','9142449316','active');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
