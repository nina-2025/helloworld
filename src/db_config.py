from sqlalchemy import create_engine  
def sql_engine():    
    return create_engine("mysql+mysqlconnector://neda:neda%40123@localhost/testdb")
