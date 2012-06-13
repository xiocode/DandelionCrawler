/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50041
Source Host           : localhost:3306
Source Database       : dandelion_crawler

Target Server Type    : MYSQL
Target Server Version : 50041
File Encoding         : 65001

Date: 2012-06-05 17:40:05
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `tb_account_info`
-- ----------------------------
DROP TABLE IF EXISTS `tb_account_info`;
CREATE TABLE `tb_account_info` (
  `id` int(11) NOT NULL auto_increment,
  `uid` bigint(20) default NULL,
  `username` varchar(255) default NULL,
  `password` varchar(255) default NULL,
  `access_token` varchar(255) default NULL,
  `refresh_token` varchar(255) default NULL,
  `is_valid` tinyint(4) default '1' COMMENT '0:无效 1:有效',
  `rate_limited` tinyint(4) default '0' COMMENT '0:未超限 1:超限',
  `expires_in` bigint(20) default NULL,
  `assign_counter` int(11) default NULL,
  `platform_id` int(11) default NULL,
  `create_date` timestamp NULL default CURRENT_TIMESTAMP,
  PRIMARY KEY  (`id`),
  UNIQUE KEY `uid` (`uid`),
  KEY `create_date` (`create_date`),
  KEY `platform_id` (`platform_id`),
  KEY `rate_limited` USING BTREE (`platform_id`,`rate_limited`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of tb_account_info
-- ----------------------------
