from sqlalchemy import *
engine = create_engine('sqlite:///calc.db')
metadata = MetaData()
con = engine.connect()
da = Table(
    'calc',metadata,
    Column('first_num',Integer),
    Column('second_num',Integer),
    Column('action',String),
    Column('result',Integer)
)
metadata.create_all(engine)

def add_result(first_num , second_num , action):
    res = eval(str(first_num)+action+str(second_num))
    con.execute(insert(da).values(
        first_num=first_num,
        second_num=second_num,
        action=action,
        result=res)
        )
    con.commit()
    
def get_results():
    return con.execute(select(da)).fetchall()
