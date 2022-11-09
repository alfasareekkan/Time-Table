/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - timetable
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`timetable` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `timetable`;

/*Table structure for table `allocate_subject` */

DROP TABLE IF EXISTS `allocate_subject`;

CREATE TABLE `allocate_subject` (
  `allocate_id` int(11) NOT NULL AUTO_INCREMENT,
  `subject_id` int(11) DEFAULT NULL,
  `staff_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`allocate_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `allocate_subject` */

insert  into `allocate_subject`(`allocate_id`,`subject_id`,`staff_id`) values 
(2,1,2),
(3,3,3);

/*Table structure for table `course` */

DROP TABLE IF EXISTS `course`;

CREATE TABLE `course` (
  `course_id` int(11) NOT NULL AUTO_INCREMENT,
  `course` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`course_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `course` */

insert  into `course`(`course_id`,`course`) values 
(1,'course1');

/*Table structure for table `doubtt` */

DROP TABLE IF EXISTS `doubtt`;

CREATE TABLE `doubtt` (
  `doubt_id` int(11) NOT NULL AUTO_INCREMENT,
  `doubt` varchar(500) DEFAULT NULL,
  `doubt_reply` varchar(500) DEFAULT NULL,
  `std_id` int(11) DEFAULT NULL,
  `staff_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`doubt_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `doubtt` */

insert  into `doubtt`(`doubt_id`,`doubt`,`doubt_reply`,`std_id`,`staff_id`) values 
(1,'h','pending',4,2);

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `feedback` varchar(300) DEFAULT NULL,
  `sid` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`feedback`,`sid`,`date`) values 
(1,'jrnrjr',4,'2022-04-14');

/*Table structure for table `free` */

DROP TABLE IF EXISTS `free`;

CREATE TABLE `free` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tid` int(11) DEFAULT NULL,
  `sid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `free` */

insert  into `free`(`id`,`tid`,`sid`) values 
(1,15,2);

/*Table structure for table `leave_approach` */

DROP TABLE IF EXISTS `leave_approach`;

CREATE TABLE `leave_approach` (
  `leave_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `leave_date` date DEFAULT NULL,
  `reason` varchar(300) DEFAULT NULL,
  `status` varchar(300) DEFAULT NULL,
  `day` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`leave_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `leave_approach` */

insert  into `leave_approach`(`leave_id`,`staff_id`,`date`,`leave_date`,`reason`,`status`,`day`) values 
(1,3,'2022-04-14','2022-04-14','reason','accept','MONDAY');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(25) DEFAULT NULL,
  `password` varchar(15) DEFAULT NULL,
  `user_type` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`login_id`),
  UNIQUE KEY `user_name` (`user_name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`user_name`,`password`,`user_type`) values 
(1,'admin','admin','admin'),
(2,'anu','123','staff'),
(3,'siva','123','staff'),
(4,'manu','123','student'),
(5,'kannan','123','student');

/*Table structure for table `note` */

DROP TABLE IF EXISTS `note`;

CREATE TABLE `note` (
  `note_id` int(11) NOT NULL AUTO_INCREMENT,
  `note` varchar(500) DEFAULT NULL,
  `subject_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`note_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `note` */

insert  into `note`(`note_id`,`note`,`subject_id`) values 
(2,'BREAK.docx',3);

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(20) DEFAULT NULL,
  `last_name` varchar(20) DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `phone_number` bigint(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `dept` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

insert  into `staff`(`sid`,`login_id`,`first_name`,`last_name`,`gender`,`phone_number`,`email`,`dept`) values 
(1,2,'anuraj','pp','male',9544379299,'anuraj@gmail.com','1'),
(2,3,'siva','k','male',9876567744,'asasjdaskl@gmail.com','1');

/*Table structure for table `staff_attendance` */

DROP TABLE IF EXISTS `staff_attendance`;

CREATE TABLE `staff_attendance` (
  `aid` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(11) DEFAULT NULL,
  `date` varchar(34) DEFAULT NULL,
  `attendance` int(11) DEFAULT NULL,
  PRIMARY KEY (`aid`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `staff_attendance` */

insert  into `staff_attendance`(`aid`,`staff_id`,`date`,`attendance`) values 
(2,2,'2022-04-14',0),
(3,3,'2022-04-14',0);

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `std_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `reg_no` varchar(56) DEFAULT NULL,
  `fname` varchar(20) DEFAULT NULL,
  `lname` varchar(20) DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL,
  `semester` varchar(90) DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `parent_phone` bigint(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`std_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `student` */

insert  into `student`(`std_id`,`login_id`,`reg_no`,`fname`,`lname`,`course_id`,`semester`,`gender`,`phone`,`parent_phone`,`email`) values 
(1,4,'VIAOECS890','manu','p',1,'s1','male',9876567788,9876567744,'asasjdaskl@gmail.com'),
(2,5,'VIAOECS777','kannan','p',1,'s1','male',9876567777,9876567700,'asasjdaskl@gmail.com');

/*Table structure for table `student_attendance` */

DROP TABLE IF EXISTS `student_attendance`;

CREATE TABLE `student_attendance` (
  `attendance_id` int(11) NOT NULL AUTO_INCREMENT,
  `std_id` int(11) DEFAULT NULL,
  `subject_id` int(11) DEFAULT NULL,
  `attendance` int(11) DEFAULT NULL,
  `date` varchar(68) DEFAULT NULL,
  PRIMARY KEY (`attendance_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `student_attendance` */

insert  into `student_attendance`(`attendance_id`,`std_id`,`subject_id`,`attendance`,`date`) values 
(5,4,3,0,'2022-04-14'),
(6,5,3,0,'2022-04-14');

/*Table structure for table `subject` */

DROP TABLE IF EXISTS `subject`;

CREATE TABLE `subject` (
  `subject_id` int(11) NOT NULL AUTO_INCREMENT,
  `course_id` int(11) DEFAULT NULL,
  `subject_code` varchar(20) DEFAULT NULL,
  `subject` varchar(20) DEFAULT NULL,
  `semester` varchar(11) DEFAULT NULL,
  PRIMARY KEY (`subject_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `subject` */

insert  into `subject`(`subject_id`,`course_id`,`subject_code`,`subject`,`semester`) values 
(1,1,'AC003','SUBJECTSS','s1'),
(3,1,'AC002','SUBJECT2','s1'),
(4,1,'AC003','SUBJECT3','s1'),
(5,1,'AC005','SUB6','s1'),
(6,1,'AC005','SUBB','s1');

/*Table structure for table `time_table` */

DROP TABLE IF EXISTS `time_table`;

CREATE TABLE `time_table` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `course_id` int(11) DEFAULT NULL,
  `semester` varchar(23) DEFAULT NULL,
  `day` varchar(20) DEFAULT NULL,
  `hour` int(11) DEFAULT NULL,
  `subject_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;

/*Data for the table `time_table` */

insert  into `time_table`(`id`,`course_id`,`semester`,`day`,`hour`,`subject_id`) values 
(1,1,'s1','MONDAY',1,1),
(2,1,'s1','MONDAY',2,3),
(3,1,'s1','MONDAY',3,4),
(4,1,'s1','MONDAY',4,5),
(5,1,'s1','MONDAY',5,6),
(6,1,'s1','TUESDAY',1,1),
(7,1,'s1','TUESDAY',2,6),
(8,1,'s1','TUESDAY',3,3),
(9,1,'s1','TUESDAY',4,4),
(10,1,'s1','TUESDAY',5,5),
(11,1,'s1','WEDNESDAY',1,1),
(12,1,'s1','WEDNESDAY',2,4),
(13,1,'s1','WEDNESDAY',3,1),
(14,1,'s1','WEDNESDAY',4,4),
(15,1,'s1','THURSDAY',1,3),
(16,1,'s1','THURSDAY',2,4),
(17,1,'s1','THURSDAY',3,5),
(18,1,'s1','THURSDAY',4,5),
(19,1,'s1','THURSDAY',5,6),
(20,1,'s1','FRIDAY',1,5),
(21,1,'s1','FRIDAY',2,5),
(22,1,'s1','FRIDAY',3,3),
(23,1,'s1','FRIDAY',4,4),
(24,1,'s1','FRIDAY',5,4);

/*Table structure for table `topic_covered` */

DROP TABLE IF EXISTS `topic_covered`;

CREATE TABLE `topic_covered` (
  `topic_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(11) DEFAULT NULL,
  `subject_id` int(11) DEFAULT NULL,
  `module` int(11) DEFAULT NULL,
  `topic_covered` int(11) DEFAULT NULL,
  PRIMARY KEY (`topic_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `topic_covered` */

insert  into `topic_covered`(`topic_id`,`staff_id`,`subject_id`,`module`,`topic_covered`) values 
(1,3,3,1,1),
(2,3,3,2,1);

/*Table structure for table `work` */

DROP TABLE IF EXISTS `work`;

CREATE TABLE `work` (
  `work_id` int(11) NOT NULL AUTO_INCREMENT,
  `work` varchar(300) DEFAULT NULL,
  `staff_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`work_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `work` */

insert  into `work`(`work_id`,`work`,`staff_id`) values 
(2,'BREAK.docx',3);

/*Table structure for table `work_report` */

DROP TABLE IF EXISTS `work_report`;

CREATE TABLE `work_report` (
  `work_report_id` int(11) NOT NULL AUTO_INCREMENT,
  `work_report` varchar(300) DEFAULT NULL,
  `work_id` int(11) DEFAULT NULL,
  `std_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`work_report_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `work_report` */

insert  into `work_report`(`work_report_id`,`work_report`,`work_id`,`std_id`) values 
(1,'storage_emulated_0_im.jpg',2,4);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
