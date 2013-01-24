import ConfigParser
config = ConfigParser.ConfigParser()
config.readfp(open('config.cfg'))
dbip = config.get("db","dbip")
dbport = int(config.get("db","dbport"))
dbuser=config.get("db","user")
dbpassword=config.get("db","password")

if __name__ == "__main__":
    print dbip
    print dbport
    print dbuser
    print dbpassword
