print('Hello, JavaScript.');
# prints exactly what's within the quotes as a string
print(2001);
# prints integer as it appears
print("What","do","commas","do?");
# prints on one line with spaces where the commas are separating the individual strings indicated by quotation marks
print("Does", "adding",      "space", "matter?");
# adding pace doens't matter wihtin the print comman unless it's within the quotation marks of a string
print('Launch' + 'Code');
# this is concatenated with no spaces
print("LaunchCode was founded in", 2013);
# this prints the string within quotation marks and the comma is necessary because the 2013 is a different datatype. 
# print("LaunchCode was founded in" 2013);
# this throws a syntax error--it's looking for a comma
print("LaunchCode was founded in" "2013");
# this prints without a space between in and 2013 because there's no comma to indicate the need for sepration but same line within two sets of the same datatype
print(2010,2013)
# two integers can't print with a space between, but they can print with a comma with or without a space. 
print("Does", "adding\tspace", "matter?");
# using \t within a text string adds a tab amount of spaces between characters
