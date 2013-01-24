import MySQLdb
import config
import json
import logging
import logging.handlers
import datetime

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


class LogDB:
    def __init__(self):
        self.conns={}
        self.table_info = {}
        self.tables={"gold_in":"game_data_gold","gold_out":"game_data_gold", "gem_in":"game_data_gem", "gem_out":"game_data_gem","item_in":"game_data_item",
        "item_out":"game_data_item","glory_in":"game_data_glory","glory_out":"game_data_glory","level_up":"game_data_level",
        "guild_chat":"game_guild_chat","world_chat":"game_world_chat"}



    def get_db_conn(self,server_id):
        if self.conns.has_key(server_id):
            return self.conns[server_id]
        
        db_name="kom_analysis_"        
        for c in server_id:
            if c.isalnum() == False:
                db_name += '_'
            else:
                db_name += c


        conn=MySQLdb.connect(host=config.dbip,port=config.dbport, user=config.dbuser,passwd=config.dbpassword,charset="utf8")
        cur = conn.cursor()
        sql ="create database if not exists %s DEFAULT CHARSET=utf8;"%db_name 
        cur.execute(sql)

        sql = "use %s;" % db_name
        cur.execute(sql)

        for sql in create_db_sql.values(): 
            cur.execute(sql)
        cur.execute("show tables;") 
        tables = cur.fetchall()
        for t in tables:
            print t
            self.deal_table_header(cur,t[0])
        cur.close()    
        
        self.conns[server_id] = conn
        return conn    
    def deal_table_header(self,cur,tablename):
        cur.execute("select * from %s" % tablename)
        desc = cur.description
        table_info = {}
        for col in desc:
            col_info={}            
            col_info["type_code"]=col[1]
            table_info[col[0]] = col_info
        self.table_info[tablename]= table_info
    def deal_record(self, server_id,log_increment_id, server_init_time,rand,data):
        conn = self.get_db_conn(server_id)
        cur = conn.cursor() 
        type = data["type"]
        data["rand"] = rand
        data["server_init_time"]=server_init_time
        data["increment_id"]=log_increment_id
        t = data.get("type") 

        table_name=self.tables[t]
        table_info = self.table_info[table_name]
        var = ""
        value=""
        for k,v in data.items():
            var = var+ "`%s`,"%k
            if table_info[k].get("type_code")==253:
                value=value + "'%s',"%v
            else:    
                value=value + "%s,"%v
        var = var[:-1]
        value = value[:-1]
        
        sql = "insert into %s(%s) values(%s) where not exists (select * from %s where rand=%d and server_init_time=%d and increment_id=%d )"% (table_name,var,value,table_name,rand,server_init_time,log_increment_id)
        cur.execute(sql)
        cur.close()
        conn.commit()
    def deal_error(self):
        pass
    def deal_logfile(self,file_name):
        try:
            f = open(file_name)
            line = f.readline()
            while line:
                try:
                
                    line = line[line.find('|') + 1:]
                    print line
                    line =  eval(line)
                    log_increment_id = line["increment_id"]
                    server_init_time = line["server_init_time"]
                    rand             =  line["rand"]
                    data = json.loads(line.get("info")) 
                    server_id = "1-1"
                    self.deal_record(server_id,log_increment_id, server_init_time,rand,data)
                except:
                    pass
                line = f.readline()
            f.close()    
        except:
            pass
if __name__=="__main__":
    log = LogDB()
    print log.get_db_conn("1-1")
    import sys
    if len(sys.argv) < 3:
        exit()
    file = sys.argv[2]    
    log.deal_logfile(file)

