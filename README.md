# awspass
Access keys management for AWS. 

I had issue while dealing with different access credentials, for some accounts.
So I've putted things like:
* switching
* rolling
* listing
* security
into small Python script. 

# how it works?
In short - pass tool is used to have data encrypted, and ~/.aws/credenitals has current data.

Pass gives security, and having credentials in file, instead of variable in environment means same settings everywhere.
