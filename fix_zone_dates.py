#Created by Kin-Ho Lam 7/9/15 for the COF Helpdesk
import sys, os, datetime, re

def check_commas(zone_path):
	if(os.path.exists(zone_path)):
		zone = open(zone_path, 'r');
	else:
		return; 
	comma_file = open("Comma_Errors.txt", 'w+'); 
	comma_file.write("Comma_Errors\n");
	for line in zone:
		if(line.count(',') != 14):
			entry = line.split(",'");
			comma_file.write(entry[0].replace("'", "").replace(".fsl.orst.edu","").replace(".cof.orst.edu","").replace(".forestry.oregonstate.edu", "") + "\tComma Error\n");
	zone.close();
	comma_file.close();

def fix_date(name , col, zone_path):
	if(os.path.exists(zone_path)):
		zone = open(zone_path, 'r+');
	else:
		return; 
	file_error = open('zone_tmp.txt', 'w+');
	fix_log = open(name + 'fix_log.txt', 'w+');
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
				file_error.write(line.replace(row, fix));
				fix_log.write(entry[0].replace("'", "").replace(".fsl.orst.edu","").replace(".cof.orst.edu","").replace(".forestry.oregonstate.edu", "") + "\tReplaced "+ row + " with " + fix + "\n")
			else:
				file_error.write(line);
		else:
			file_error.write(line);
	zone.close();
	file_error.close();
	os.remove(zone_path);
	os.rename("zone_tmp.txt", "zone.txt");

def main():
	zone_path = "zone.txt";
	check_commas(zone_path);
	fix_date("purchase", 10, zone_path);
	fix_date("warranty", 12, zone_path);
main(); #run main
