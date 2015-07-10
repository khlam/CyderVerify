#Created by Kin-Ho Lam 7/9/15 for the COF Helpdesk
import sys, os, datetime


def check_entry():
	zone_path = "zone.txt";
	wolcmd_path = "missing.txt";
	if(os.path.exists(zone_path)):
		zone = open(zone_path, 'r');
	else:
		return; 
	wolcmd = open(wolcmd_path, 'w+'); 
	
	for line in zone: 
		entry = line.split(",'");
		purchase_date = entry[10].replace("'", "");
		if(purchase_date != ""):
			
			if(purchase_date.find("\\") != -1):
				wolcmd.write(entry[0].replace("'", "").replace(".fsl.orst.edu","").replace(".cof.orst.edu","").replace(".forestry.oregonstate.edu", "") + " contains a backslash."); #removes ', .fsl.orst.edu, .cof.orst.edu, and .forestry.oregonstate.edu from name
				wolcmd.write("\t" + purchase_date);
				wolcmd.write('\n');
			date_len = len(purchase_date);
			if(date_len != 8 and date_len != 10):
				wolcmd.write(entry[0].replace("'", "").replace(".fsl.orst.edu","").replace(".cof.orst.edu","").replace(".forestry.oregonstate.edu", "") + " does not have the correct date format."); #removes ', .fsl.orst.edu, .cof.orst.edu, and .forestry.oregonstate.edu from name
				wolcmd.write("\t" + purchase_date);
				wolcmd.write('\n');
	zone.close();
	wolcmd.close();
	
def main(): #main
	check_entry();
	
main(); #run main
