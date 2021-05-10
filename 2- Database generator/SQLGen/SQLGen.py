import os
import csv

from template import schema

data_dir = os.getcwd() + r'/data'

schema = schema()

# models
with open( data_dir + '/Database - models.csv', 'r' ) as rf:
    f = csv.reader( rf, delimiter=',' )
    line_number = 0
    for row in f:
        line_number += 1
        if line_number < 2:
            continue

        model_id = int( row[0] )
        gender = row[1]
        name = row[2]
        description = row[3]
        price = float( row[4] )

        sql = schema.insertModel( model_id, gender, name, description, price )
        print( sql )

# colors
with open( data_dir + '/Database - colors.csv', 'r' ) as rf:
    f = csv.reader( rf, delimiter=',' )
    line_number = 0
    for row in f:
        line_number += 1
        if line_number < 2:
            continue

        color_id = int( row[0] )
        model_id = int (row[1] )
        gender = row[2]
        media1 = row[3]
        media2 = row[4]
        media3 = row[5]

        sql = schema.insertColor( color_id, model_id, gender, media1, media2, media3 )
        print( sql )

# shoes
with open( data_dir + '/Database - shoes.csv', 'r' ) as rf:
    f = csv.reader( rf, delimiter=',' )
    line_number = 0
    for row in f:
        line_number += 1
        if line_number < 2:
            continue

        product_id = int( row[0] )
        model_id = int (row[1] )
        gender = row[2]
        status = row[3]
        size_ = float( row[4] )

        sql = schema.insertShoe( product_id, model_id, gender, status, size_ )
        print( sql )

# casual_shoes
with open( data_dir + '/Database - casual_shoes.csv', 'r' ) as rf:
    f = csv.reader( rf, delimiter=',' )
    line_number = 0
    for row in f:
        line_number += 1
        if line_number < 2:
            continue
        
        model_id = int (row[0] )
        gender = row[1]

        sql = schema.insertCasualShoe( model_id, gender )
        print( sql )

# sport_shoes
with open( data_dir + '/Database - sport_shoes.csv', 'r' ) as rf:
    f = csv.reader( rf, delimiter=',' )
    line_number = 0
    for row in f:
        line_number += 1
        if line_number < 2:
            continue
        
        model_id = int (row[0] )
        gender = row[1]

        sql = schema.insertSportShoe( model_id, gender )
        print( sql )

# dress_shoes
with open( data_dir + '/Database - dress_shoes.csv', 'r' ) as rf:
    f = csv.reader( rf, delimiter=',' )
    line_number = 0
    for row in f:
        line_number += 1
        if line_number < 2:
            continue
        
        model_id = int (row[0] )
        gender = row[1]

        sql = schema.insertDressShoe( model_id, gender )
        print( sql )

# customers
with open( data_dir + '/Database - customers.csv', 'r' ) as rf:
    f = csv.reader( rf, delimiter=',' )
    line_number = 0
    for row in f:
        line_number += 1
        if line_number < 2:
            continue
        
        email = row[0]
        username = row[1]
        password = row[2]
        gender = row[3]
        birthdate = row[4]
        address = row[5]

        sql = schema.insertCustomer( email, username, password, gender, birthdate, address )
        print( sql )

# reviews
with open( data_dir + '/Database - reviews.csv', 'r' ) as rf:
    f = csv.reader( rf, delimiter=',' )
    line_number = 0
    for row in f:
        line_number += 1
        if line_number < 2:
            continue
        
        email = row[0]
        model_id = int( row[1] )
        gender = row[2]
        comment_ = row[3]
        rating = float( row[4] )

        sql = schema.insertReview( email, model_id, gender, comment_, rating )
        print( sql )

# items
with open( data_dir + '/Database - items.csv', 'r' ) as rf:
    f = csv.reader( rf, delimiter=',' )
    line_number = 0
    for row in f:
        line_number += 1
        if line_number < 2:
            continue
        
        item_id = int( row[0] )
        email = row[1]
        status = row[2]
        product_id = int( row[3] )

        sql = schema.insertItem( item_id, email, status, product_id )
        print( sql )

# credit_card
with open( data_dir + '/Database - credit_cards.csv', 'r' ) as rf:
    f = csv.reader( rf, delimiter=',' )
    line_number = 0
    for row in f:
        line_number += 1
        if line_number < 2:
            continue
        
        card_number = row[0]
        email = row[1]
        name = row[2]
        address = row[3]
        cvv2 = int( row[4] )
        postal_code = row[5]

        sql = schema.insertCreditCard( card_number, email, name, address, cvv2, postal_code )
        print( sql )

# shipments
with open( data_dir + '/Database - shipments.csv', 'r' ) as rf:
    f = csv.reader( rf, delimiter=',' )
    line_number = 0
    for row in f:
        line_number += 1
        if line_number < 2:
            continue

        shipment_id = int( row[0] )
        departure = row[1]
        arrival = row[2]
        status = row[3]

        sql = schema.insertShipment( shipment_id, departure, arrival, status )
        print( sql )

# invoices
with open( data_dir + '/Database - invoices.csv', 'r' ) as rf:
    f = csv.reader( rf, delimiter=',' )
    line_number = 0
    for row in f:
        line_number += 1
        if line_number < 2:
            continue

        invoice_id = int( row[0] )
        total = float( row[1] )
        date_time = row[2]
        card_number = row[3]
        email = row[4]
        shipment_id = int( row[5] )

        sql = schema.insertInvoice( invoice_id, total, date_time, card_number, email, shipment_id )
        print( sql )

# purchases
with open( data_dir + '/Database - purchases.csv', 'r' ) as rf:
    f = csv.reader( rf, delimiter=',' )
    line_number = 0
    for row in f:
        line_number += 1
        if line_number < 2:
            continue

        item_id = int( row[0] )
        email = row[1]
        invoice_id = int( row[2] )

        sql = schema.insertPurchase( item_id, email, invoice_id )
        print( sql )
