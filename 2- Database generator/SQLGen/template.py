class schema:
    def __init__( self ):
        self.models = {}
        self.colors = {}
        self.shoes = {}
        self.casual_shoes = {}
        self.sport_shoes = {}
        self.dress_shoes = {}
        self.customers = {}
        self.reviews = {}
        self.items = {}
        self.credit_cards = {}
        self.shipments = {}
        self.invoices = {}
        self.purchases = {}

    def insertModel( self, model_id, gender, name, description, price ):
        pKey = '-'.join( [ str( model_id ), gender ] )
        self.models[ pKey ] = [ model_id, gender, name, description, price ]

        return "INSERT INTO models VALUES (%d, '%s', '%s', '%s', %.2f);" % ( model_id, gender, name, description, price )

    def insertColor( self, color_id, model_id, gender, media1, media2, media3 ):
        fKey = '-'.join( [ str( model_id ), gender ] )
        assert self.models.get( fKey )

        pKey = '-'.join( [ str( color_id ), str( model_id ), gender ] )
        self.colors[ pKey ] = [ color_id, model_id, gender, media1, media2, media3 ]
        
        return "INSERT INTO colors VALUES (%d, %d, '%s', '%s', '%s', '%s');" % ( color_id, model_id, gender, media1, media2, media3 )

    def insertShoe( self, product_id, model_id, gender, status, size_ ):
        fKey = '-'.join( [ str( model_id ), gender ] )
        assert self.models.get( fKey )

        pKey = product_id
        self.shoes[ pKey ] = [ product_id, model_id, gender, status, size_ ]

        return "INSERT INTO shoes VALUES (%d, %d, '%s', '%s', %.1f);" % ( product_id, model_id, gender, status, size_ )
    
    def insertCasualShoe( self, model_id, gender ):
        fKey = '-'.join( [ str( model_id ), gender ] )
        assert self.models.get( fKey )

        pKey = fKey
        self.casual_shoes[ pKey ] = [ model_id, gender ]

        return "INSERT INTO casual_shoes VALUES (%d, '%s');" % ( model_id, gender )

    def insertSportShoe( self, model_id, gender ):
        fKey = '-'.join( [ str( model_id ), gender ] )
        assert self.models.get( fKey )

        pKey = fKey
        self.sport_shoes[ pKey ] = [ model_id, gender ]

        return "INSERT INTO sport_shoes VALUES (%d, '%s');" % ( model_id, gender )

    def insertDressShoe( self, model_id, gender ):
        fKey = '-'.join( [ str( model_id ), gender ] )
        assert self.models.get( fKey )

        pKey = fKey
        self.dress_shoes[ pKey ] = [ model_id, gender ]

        return "INSERT INTO dress_shoes VALUES (%d, '%s');" % ( model_id, gender )
    
    def insertCustomer(self, email, username, password, gender, birthdate, address):
        pKey = email
        self.customers[ pKey ] = [ email, username, password, gender, birthdate, address ]

        return "INSERT INTO customers VALUES ('%s', '%s', '%s', '%s', '%s', '%s');" % ( email, username, password, gender, birthdate, address )

    def insertReview(self, email, model_id, gender, comment_, rating):
        fKey = email
        assert self.customers.get( fKey )
        fKey = '-'.join( [ str( model_id ), gender ] )
        assert self.models.get( fKey )

        pKey = '-'.join( [ email, str( model_id ), gender ] )
        self.reviews[ pKey ] = [ email, model_id, gender, comment_, rating ]

        return "INSERT INTO reviews VALUES ('%s', %d, '%s', '%s', %.1f);" % ( email, model_id, gender, comment_, rating )
    
    def insertItem( self, item_id, email, status, product_id ):
        fKey = email
        assert self.customers.get( fKey )
        fKey = product_id
        assert self.shoes.get( fKey )

        pKey = '-'.join( [ str( item_id ), email ] )
        self.items[ pKey ] = [ item_id, email, status, product_id ]

        return "INSERT INTO items VALUES (%d, '%s', '%s', %d);" % ( item_id, email, status, product_id )
    
    def insertCreditCard(self, card_number, email, name, address, cvv2, postal_code):
        fKey = email
        assert self.customers.get( fKey )

        pKey = '-'.join( [ card_number, email ] )
        self.credit_cards[ pKey ] = [ card_number, email, name, address, cvv2, postal_code ] 
        
        return "INSERT INTO credit_cards VALUES ('%s', '%s', '%s', '%s', %d, '%s');" % ( card_number, email, name, address, cvv2, postal_code )
    
    def insertShipment( self, shipment_id, departure, arrival, status ):
        pKey = shipment_id
        self.shipments[ pKey ] = [ shipment_id, departure, arrival, status ]

        return "INSERT INTO shipments VALUES (%d, '%s', '%s', '%s');" % ( shipment_id, departure, arrival, status )
    
    def insertInvoice(self, invoice_id, total, date_time, card_number, email, shipment_id):
        fKey = '-'.join( [ card_number, email ] )
        assert self.credit_cards.get( fKey )

        fKey = shipment_id
        assert self.shipments.get( fKey )

        pKey = invoice_id
        self.invoices[ pKey ] = [ invoice_id, total, date_time, card_number, email, shipment_id ]

        return "INSERT INTO invoices VALUES (%d, %.2f, '%s', '%s', '%s', %d);" % ( invoice_id, total, date_time, card_number, email, shipment_id )
    
    def insertPurchase(self, item_id, email, invoice_id):
        fKey = '-'.join( [ str( item_id ), email ] )
        assert self.items.get( fKey )

        fKey = invoice_id
        assert self.invoices.get( fKey )

        pKey = '-'.join( [ str( item_id ), email, str( invoice_id ) ] )
        self.purchases[ pKey ] = [ item_id, email, invoice_id ]

        return "INSERT INTO purchases VALUES (%d, '%s', %d);" % ( item_id, email, invoice_id )
