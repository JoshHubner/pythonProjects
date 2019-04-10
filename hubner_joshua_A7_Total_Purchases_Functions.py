# ====================================================================================================
# PROGRAMMER:               Josh Hubner
# PROGRAM NAME:             Assignment 7
# DATE WRITTEN:/REVISED:    3/21/2019
#
# PURPOSE:  To calculate total purchases and organize as functions
# ====================================================================================================
# Defining the main program as a function
def main():
	items = getPrice();
	makeSpace();
	makeLine();
	priceData(items);
	makeLine();
	subTotal = itemSum(items);
	makeLine();
	taxTotally = taxTotal(subTotal);
	makeLine();
	grandTotal(taxTotally);
# ====================================================================================================
# Defining getPrice function
def getPrice():
	prices = [];
	
	#Creating a loop-controlled variable.
	again = "y"
	
	#Get price values from user and add them to the list.
	while again == "y":
		price = float(input("Please enter the price of this item: $"));
		prices.append(price);
		print("");
		print("Do you have another item? ");
		again = input("Please enter y for yes... anything else will be no. ");
		print("");
	#Return the list.
	return prices;
# ====================================================================================================
# Defining priceData function
def priceData(items):
	for item in items:
		print("Item price:    $" + format(item, "14,.2f"));
	return items;
# ====================================================================================================
# Defining makeLine function
def makeLine():
	print("______________________________________");
# ====================================================================================================
# Defining makeSpace function
def makeSpace():
	print("");print("");print("");print("");print("");print("");print("");print("");print("");print("");print("");print("");print("");print("");print("");print("");print("");print("");print("");print("");
# ====================================================================================================	
# Defining itemSum function
def itemSum(items):
	itemSum = 0.00;
	itemSum = sum(items);
	print("Item subtotal: $ ",format(itemSum, "12,.2f"));
	return itemSum;
# ====================================================================================================
# Defining taxTotal function
def taxTotal(subTotal):
	taxTotal = 0.00;
	taxRate = 0.07;
	taxTotal = (subTotal * taxRate);
	print("Tax total:     $ ",format(taxTotal, "12,.2f"));
	return taxTotal;
# ====================================================================================================
# Defining grandTotal function
def grandTotal(taxTotally):
	taxRate = 0.07;
	total = (taxTotally / taxRate) + taxTotally;
	print("Grand total:   $ ",format(total, "12,.2f"));
# ====================================================================================================
# Call the Main function
main();

# ====================================================================================================
#I ADDED THIS TO SEE THE RESULTS OF MY PROGRAM LONGER
print("");
input("press any key to exit...");
# ====================================================================================================
#END PROGRAM