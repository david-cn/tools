#/use/bin/python
create_db_sql = {}

create_db_sql[0] = """
CREATE TABLE IF NOT EXISTS `game_behavior_log` (
`id` int(10) unsigned NOT NULL AUTO_INCREMENT,
`rand` int(10) unsigned DEFAULT NULL,
`server_init_time` int(10) unsigned DEFAULT NULL,
`increment_id` int(10) unsigned DEFAULT NULL,
`role_id` int(10) unsigned DEFAULT NULL,
`behavior` varchar(128) DEFAULT NULL,
`info` text,
`time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

"""

create_db_sql[1]=  """
CREATE TABLE IF NOT EXISTS `game_data_gem` (
`id` int(10) unsigned NOT NULL AUTO_INCREMENT,
`rand` int(10) unsigned DEFAULT NULL,
`server_init_time` int(10) unsigned DEFAULT NULL,
`increment_id` int(10) unsigned DEFAULT NULL,
`role_id` int(11) DEFAULT NULL,
`type` varchar(32) DEFAULT NULL,
`act` varchar(64) DEFAULT NULL,
`act_time` int(11) DEFAULT NULL,
`change_num` int(10) unsigned DEFAULT NULL,
`total_num` bigint(20) unsigned DEFAULT NULL,
`param` int(10) unsigned DEFAULT NULL,
PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

"""

create_db_sql[2]=  """
CREATE TABLE IF NOT EXISTS `game_data_gold` (
`id` int(10) unsigned NOT NULL AUTO_INCREMENT,
`rand` int(10) unsigned DEFAULT NULL,
`server_init_time` int(10) unsigned DEFAULT NULL,
`increment_id` int(10) unsigned DEFAULT NULL,
`role_id` int(11) DEFAULT NULL,
`type` varchar(32) DEFAULT NULL,
`act` varchar(64) DEFAULT NULL,
`act_time` int(11) DEFAULT NULL,
`change_num` int(10) unsigned DEFAULT NULL,
`total_num` bigint(20) unsigned DEFAULT NULL,
`param` int(10) unsigned DEFAULT NULL,
PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;


"""

create_db_sql[3]=  """
CREATE TABLE IF NOT EXISTS `game_data_item` (
`id` int(10) unsigned NOT NULL AUTO_INCREMENT,
`rand` int(10) unsigned DEFAULT NULL,
`server_init_time` int(10) unsigned DEFAULT NULL,
`increment_id` int(10) unsigned DEFAULT NULL,
`role_id` int(11) DEFAULT NULL,
`type` varchar(32) DEFAULT NULL,
`act` varchar(64) DEFAULT NULL,
`act_time` int(11) DEFAULT NULL,
`item_id`  int(11) DEFAULT NULL,
`unbinded_num`  int(11) DEFAULT NULL,
`binded_num` int(11) DEFAULT NULL,
`total_unbinded_num`  int(11) DEFAULT NULL,
`total_binded_num` int(11) DEFAULT NULL,
`param` int(11) DEFAULT NULL,
PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

"""

create_db_sql[4]=  """
CREATE TABLE IF NOT EXISTS `game_data_glory` (
`id` int(10) unsigned NOT NULL AUTO_INCREMENT,
`rand` int(10) unsigned DEFAULT NULL,
`server_init_time` int(10) unsigned DEFAULT NULL,
`increment_id` int(10) unsigned DEFAULT NULL,
`role_id` int(11) DEFAULT NULL,
`type` varchar(32) DEFAULT NULL,
`act` varchar(64) DEFAULT NULL,
`act_time` int(11) DEFAULT NULL,
`glory` int(11) DEFAULT NULL,
PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

"""

create_db_sql[5]=  """
CREATE TABLE IF NOT EXISTS `game_data_level`(
`id` int(10) unsigned NOT NULL AUTO_INCREMENT,
`rand` int(10) unsigned DEFAULT NULL,
`server_init_time` int(10) unsigned DEFAULT NULL,
`increment_id` int(10) unsigned DEFAULT NULL,
`role_id` int(11) DEFAULT NULL,
`level_up_time` int(11) DEFAULT NULL,
`level` int(11) DEFAULT NULL,
PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;


"""

create_db_sql[6]=  """
CREATE TABLE IF NOT EXISTS `game_world_chat` (
`id` int(10) unsigned NOT NULL AUTO_INCREMENT,
`rand` int(10) unsigned DEFAULT NULL,
`server_init_time` int(10) unsigned DEFAULT NULL,
`increment_id` int(10) unsigned DEFAULT NULL,
`role_id` int(11) DEFAULT NULL,
`msg` varchar(512) DEFAULT NULL,
`time` int(11) DEFAULT NULL,
PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

"""

create_db_sql[7]=  """

CREATE TABLE IF NOT EXISTS `game_guild_chat` (
`id` int(10) unsigned NOT NULL AUTO_INCREMENT,
`rand` int(10) unsigned DEFAULT NULL,
`server_init_time` int(10) unsigned DEFAULT NULL,
`increment_id` int(10) unsigned DEFAULT NULL,
`role_id` int(11) DEFAULT NULL,
`guild_id` int(11) DEFAULT NULL,
`msg` varchar(512) DEFAULT NULL,
`time` int(11) DEFAULT NULL,
PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

"""
