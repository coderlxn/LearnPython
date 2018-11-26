from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Text, DateTime

Base = declarative_base()
engine = create_engine('sqlite:///' + os.path.join(basedir, 'app.db'))

class ChatList(Base):
    __tablename__ = 'chatlist'
    uuid = Column(String(32), primary_key=True)
    sender_id = Column(String(32), nullable=False, index=True)
    group_id = Column(String(32))
    type = Column(Integer, nullable=False)
    code = Column(Integer)
    datetime_send = Column(DateTime)
    datetime_receive = Column(DateTime)
    message_body = Column(Text)
    message_status = Column(String(32))
    file_type = Column(Integer)
    file_info = Column(Text)
    read_flag = Column(Integer)
    extern = Column(Text)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.title)
