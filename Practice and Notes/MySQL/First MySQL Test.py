import MySQLdb as mdb
import sys

############################################################################

# Print database version

#try:
#    con = mdb.connect('localhost','matt','demo','testdb');   # connect to host, user, p/w and db
#    
#    cur = con.cursor()                                      # cursor iterates over db items
#    cur.execute("SELECT VERSION()")                         # send SQL command to db
#    ver = cur.fetchone()                                    # fetch single record from data
#    print "Database version : %s" % ver
#                     
##    con.query("SELECT VERSION()")
##    result = con.use_result()    
##    print("My SQL Version: %s" % result.fetch_row()[0])
#    
#except mdb.Error, e:
#    print("Error %d: %s" % (e.args[0], e.args[1]))
#    sys.exit(1)
#    
#finally:
#    if con:
#        con.close()
        
############################################################################

# Create and populate a table

#con = mdb.connect('localhost','root','demo','testdb');
#
#with con:
#    cur = con.cursor()
#    cur.execute("USE testdb")
#    cur.execute("DROP TABLE IF EXISTS cleeve")
#    cur.execute("CREATE TABLE cleeve(id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(25))") # create table with 2 cols where name has a max length of 25                  
#    cur.execute("INSERT INTO cleeve(name) VALUES('Matt Allen')")
#    cur.execute("INSERT INTO cleeve(name) VALUES('James Morgan')")
#    cur.execute("INSERT INTO cleeve(name) VALUES('Doug Thompson')")
#    cur.execute("INSERT INTO cleeve(name) VALUES('Sam Allen')")
    
############################################################################    

# Retrieve all data

#con = mdb.connect('localhost','matt','demo','testdb');
#
#with con:
#    cur = con.cursor()
#    cur.execute("USE testdb")
#    cur.execute("SELECT * FROM cleeve")
#    
#    rows = cur.fetchall()                 # returns a tuple of tuples, in this case, all records (not efficient)
#    
#    for row in rows:
#        print row
        
############################################################################

# Retrieve individual data

#con = mdb.connect('localhost','matt','demo','testdb');
#
#with con:
#    cur = con.cursor()
#    cur.execute("SELECT * FROM cleeve")
#    
#    for i in range(cur.rowcount):       # returns records from the cursor in order until none remaining
#        row = cur.fetchone()
#        print row[0], row[1]
#        
#    while True:                         # same as above, alternate method
#        row = cur.fetchone()
#        if row == None:
#            break
#        print(row)
#        
#    cur.fetchmany(2)                    # fetch first 2 records
#    
#    while True:                         # fetch sets of 2 records in cursor until none remaining
#        two_rows = cur.fetchmany(2)
#        if two_rows == ():
#            break
#        print(two_rows)

############################################################################

# Retrieve data in dictionaries

#con = mdb.connect('localhost','matt','demo','testdb');
#
#with con:
#    cur = con.cursor(mdb.cursors.DictCursor)            # use a dict cursor (prevents default tuple use)
#    cur.execute("SELECT * FROM cleeve LIMIT 4")         # limit results to 4 records
#    
#    rows = cur.fetchall()
#    
#    for row in rows:
#        print row["id"], row["name"]
        
############################################################################

# Return database column headers

#con = mdb.connect('localhost','matt','demo','testdb');
#
#with con:
#    cur = con.cursor()
#    cur.execute("SELECT * FROM cleeve LIMIT 5")
#    
#    rows = cur.fetchall()
#    desc = cur.description                               # returns information about each of the table columns
#
#    print "%s %3s" % (desc[0][0], desc[1][0])            # prints column 0 and 1 names (%3s sets to length of 3)
#    
#    for row in rows:
#        print "%2s %3s" % row                            # prints id and name for each row (extracts tuple info)
#        
#con.close()

############################################################################

# Prepared statements

#con = mdb.connect('localhost','root','demo','testdb')
#
#with con:
#    cur = con.cursor()
#    cur.execute("USE testdb")
#    cur.execute("UPDATE cleeve SET name = %s WHERE id = %s", ("Dom Allen","4"))
#    cur.execute("SELECT * FROM cleeve")
#    
#    rows = cur.fetchall()
#    for row in rows:
#        print row[0], row[1]

############################################################################

# Transactions

# So far I have been writing code which is handled by connection context
# managers. These automatically take care of the try, except and finally
# statements where you should type code to start and then commit or rollback.

#try:
#    con = mdb.connect('localhost','root','demo','testdb')
#    
#    cur = con.cursor()
#    cur.execute("USE testdb")
#    cur.execute("DROP TABLE IF EXISTS cleeve")
#    cur.execute("CREATE TABLE cleeve(id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(25)) ENGINE=INNODB") # create table with 2 cols where name has a max length of 25                  
#    cur.execute("INSERT INTO cleeve(name) VALUES('Matt Allen')")
#    cur.execute("INSERT INTO cleeve(name) VALUES('James Morgan')")
#    cur.execute("INSERT INTO cleeve(name) VALUES('Doug Thompson')")
#    cur.execute("INSERT INTO cleeve(name) VALUES('Sam Allen')")
#    
#    con.commit()
#    
#except mdb.Error, e:    
#    if con:
#        con.rollback()
#        
#    print "Error %d: %s" % (e.args[0],e.args[1])
#    sys.exit(1)
#    
#finally:
#    if con:
#        con.close()
        
# Here, the transaction is started when we create a cursor. Until we write
# commit, the table is created but the data is not sent. We must also specify
# the engine explicity here (INNODB is slower but more secure than others).

############################################################################
        
MySQL Python Tutorial: http://zetcode.com/db/mysqlpython/
HTML Scraping: http://python-docs.readthedocs.io/en/latest/scenarios/scrape.html