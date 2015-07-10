#Created by Kin-Ho Lam 7/9/15 for the COF Helpdesk
import sys, os, datetime

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
			comma_file.write(entry[0].replace("'", "").replace(".fsl.orst.edu","").replace(".cof.orst.edu","").replace(".forestry.oregonstate.edu", "") + "\tComma Error");
	zone.close();
	comma_file.close();

def check_date(col_name, col, zone_path):
	file_path = col_name+ ".txt";
	if(os.path.exists(zone_path)):
		zone = open(zone_path, 'r');
	else:
		return; 
	file_error = open(file_path, 'w+'); 
	file_error.write(col_name + "\n");
	for line in zone: 
		entry = line.split(",'");
		row = entry[col].replace("'", "");
		date_len = len(row);
		if(row != ""):
			if( (row.find("\\") != -1) or (date_len != 8 and date_len != 10) ):
				file_error.write(entry[0].replace("'", "").replace(".fsl.orst.edu","").replace(".cof.orst.edu","").replace(".forestry.oregonstate.edu", "") + "\t");
				if(row.find("\\") != -1 ):
					file_error.write(" Contains Backslash");
				if( (row.find("\\") != -1) and (date_len != 8 and date_len != 10) ): 
					file_error.write(" and");
				if(date_len != 8 and date_len != 10):
					file_error.write(" Invalid Date Format");
				file_error.write("\t" + row);
				file_error.write('\n');
	zone.close();
	file_error.close();

def check_po(zone_path):
	if(os.path.exists(zone_path)):
		zone = open(zone_path, 'r');
	else:
		return; 
	po_error = open("P0_Errors.txt", 'w+'); 
	po_error.write("P0_Errors\n");
	for line in zone: 
		entry = line.split(",'");
		row = entry[13].replace("'", "");
		P0_len = len(row);
		if( (row == "") or (P0_len < 8 and (row.find("NoPO") == -1))):
			po_error.write(entry[0].replace("'", "").replace(".fsl.orst.edu","").replace(".cof.orst.edu","").replace(".forestry.oregonstate.edu", "") + "\t");
			if(row == ""):
				po_error.write("No P0 Entered");
			else:
				po_error.write("Invalid P0 Entry")

			po_error.write("\t" + row);
			po_error.write('\n');
	zone.close();
	po_error.close();

def main():
	zone_path = "zone.txt";
	check_commas(zone_path);
	check_date("Purchase_Date_Errors", 10, zone_path);
	check_date("Warranty_Date_Errors",12, zone_path);
	check_po(zone_path);
	
main(); #run main
