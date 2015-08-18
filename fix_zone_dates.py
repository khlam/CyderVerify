#Created by Kin-Ho Lam 7/9/15 for the COF Helpdesk
import sys, os, datetime, re

def backup_old_zone():
	old_zone = "\\errorchecker\\old_zone";
	zone_date = "\\errorchecker\\old_zone\\zone" + str(datetime.date.today()) + ".txt";
	if(os.path.exists(old_zone)):
		if not (os.path.exists(old_zone)):
			os.mkdir(old_zone);
		if (os.path.exists(zone_date)):
			os.remove(zone_date);
	os.rename("\\errorchecker\\zone.txt", zone_date);

def check_commas(zone_path):
	if(os.path.exists(zone_path)):
		zone = open(zone_path, 'r');
	else:
		return; 
	fix_log = open("fix_log" + str(datetime.date.today()) + ".txt", 'w+'); 
	fix_log.write("Comma Errors:\n");
	for line in zone:
		c_count = line.count(',');
		if(c_count != 14):
			entry = line.split(",'");
			fix_log.write(entry[0].replace("'", "").replace(".fsl.orst.edu","").replace(".cof.orst.edu","").replace(".forestry.oregonstate.edu", ""));
			if(c_count > 14):
				fix_log.write("\tExcess Commas ");
			else:
				fix_log.write("\tMissing Commas ");
			fix_log.write("(" + str(14 - c_count)+")\n");
	fix_log.write("\n");
	zone.close();
	fix_log.close();

def fix_date(name , col, zone_path):
	if(os.path.exists(zone_path)):
		zone = open(zone_path, 'r+');
	else:
		return; 
	zone_tmp = open('zone_tmp.txt', 'w+');
	fix_log = open("fix_log" + str(datetime.date.today()) + ".txt", 'a+');
	fix_log.write(name + ' Errors:\n');
	for line in zone: 
		entry = line.split(",'");
		row = entry[col].replace("'", "");
		if(row != ""):
			if(row.count("/") != 2):
				date = re.sub('[^0-9a-zA-Z]+', '/', row);
			else:
				date = row;
			date_len = len(date);
			if (date_len != 8 and date_len != 10):
				edit = date.split("/");
				if (len(edit[0]) != 2):
					edit[0] = "0"+edit[0];
				if (len(edit[1]) != 2):
					edit[1] = "0"+edit[1];
				if (len(edit[2]) != 2 and len(edit[2]) != 4):
					edit[2] = "0"+edit[2];
				fix = edit[0] +"/" + edit[1]+ "/" + edit[2];
				zone_tmp.write(line.replace(row, fix));
				fix_log.write(entry[0].replace("'", "").replace(".fsl.orst.edu","").replace(".cof.orst.edu","").replace(".forestry.oregonstate.edu", "") + "\t\t"+ row + " changed to " + fix + "\n")
			else:
				zone_tmp.write(line);
		else:
			zone_tmp.write(line);
	fix_log.write('\n');
	fix_log.close();
	zone.close();
	zone_tmp.close();
	#backup_old_zone();
	os.remove("zone.txt");
	os.rename("zone_tmp.txt", "zone.txt");

def main():
	zone_path = "zone.txt";
	check_commas(zone_path);
	fix_date("Purchase", 10, zone_path);
	fix_date("Warranty", 12, zone_path);
	
main(); #run main