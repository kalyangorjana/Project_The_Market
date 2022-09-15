import snowflake.connector as pm

con = pm.connect(user='root', password='Kalyan@123', account='ilb30847.us-east-1', warehouse='THEMARKET',
                 database='the_market_products', schema='product_data')
# import mysql.connector as pm
# con = pm.connect(host='localhost', port='3306', user='root', password='Kalyan@123', database='ProductManagementFlask')
print('Connected')

cur = con.cursor()


def create_table():
    sqlquery = 'create table if not exists product(productId int primary key autoincrement ,productName varchar (100) ' \
               'not null,productPrice double,productDescription varchar(5000)) '
    i = cur.execute(sqlquery)
    print(i, 'row affected')
    print('Table is Created')
    con.commit()


def insert(product_name, product_price, product_description):
    sqlQuery = f"insert into product (productName,productPrice,productDescription)values('{product_name}'," \
               f"{product_price},'{product_description}')"
    i = cur.execute(sqlQuery)
    print(i, 'row affected')
    print('Table is Created')
    con.commit()


def update(productId, productName, productPrice, productDescription):
    sqlQuery = f"update product set productName='{productName}',productPrice={productPrice},productDescription='" \
               f"{productDescription}' where productId={productId};"
    i = cur.execute(sqlQuery)
    print(i, 'row affected')
    print('Table is Created')
    con.commit()


def delete(productId):
    sqlQuery = f"delete from product where productId={productId};"
    i = cur.execute(sqlQuery)
    print(i, 'row affected')
    print('Table is Created')
    con.commit()


def getall():
    sqlQuery = "Select* from product"
    i = cur.execute(sqlQuery)
    print(i, 'row affected')
    rows = cur.fetchall()
    return rows


def getproductbyid(productId):
    sqlQuery = f"Select* from product where productId={productId}"
    i = cur.execute(sqlQuery)
    print(i, 'row affected')
    row = cur.fetchone()
    return row


def closeDB():
    con.close()
