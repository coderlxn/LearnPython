import random
from faker import Factory
import os
import uuid
from datetime import datetime, timedelta
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import sessionmaker

basedir = os.path.abspath(os.path.dirname(__file__))
engine = create_engine('sqlite:///' + os.path.join(basedir, 'YWdatabase.db'))
Base = declarative_base()


def create_uuid():
    uid = str(uuid.uuid4())
    uid = uid.replace('-', '')
    return uid


members = ['11830737f8a69ba83791a607ef4958ba',  # 1
           '910a17c5f195ee9fe1c74c4cc7f3160d',  # 2
           'a81857cecd1bb5739eb959d5519d2df7',  # 3
           '33a9f881e99da9eac4c34ed898ced4bf']  # 5

self_uuid = '11830737f8a69ba83791a607ef4958ba'  # 4

groups = ['34383bf8c2274e9487aed0854376e4e3',  # 1 4
          'fea54018f9e84567a02a37c1770b094a',  # 2 3
          'cf6cd4fb5bae4f8095043c487667b2d1',  # 3 4
          '5d5f9fe4286246b68577e3a17b7caaf2',  # 4 4
          'e7299aacc3d540c8bf0d21933b857ab5',  # 5 4
          'd5ce6dbc076541fe841679fe129368ae',  # 6 4
          '6d38cd2a921f4d8ba953df8d29a95268',  # 7 4
          '6c5ebfe2a0cb49a8abca24f44903850a',  # 8 4
          '9436a99539ac4f9dabdb4b69bda17d2f',  # 9 4
          'e3b4c7f2e9b44b90b53ddc049fe467cc',  # 10 4
          '084e47e478794d4ca9ef5e0141759d27',  # 11 1
          '8bf2e342ee7a46afb692defc50423f25',  # 12 1
          '7d52d6eea16c437a949db9bc885588ed',  # 13 1
          '1c480026640344ec9eb78b8f6042d9e9',  # 14 1
          '109a5dc8e9bd42bc913d94b0c22d5549',  # 15 1
          'ab56349fb80047b6ae0101e727c2321d',  # 16 1
          '42309878f40d465ca8a8667ec21d9d66',  # 17 1
          'a60f40de3af247b2977acc08b4b2ed79',  # 18 1
          '8dd6ebc6235849a4bf0d6db2de88767b',  # 19 1
          '02737e2b006648d1bc2505ed57585f0d',  # 20 1
          '83a7cd58c2d84001914a140a21900e04',  # 21 2
          '7f6f362fd92f4ed28c5467a7181b3908',  # 22 2
          '869779bb48a4411fa02f68045d3a392a',  # 23 2
          '6af8eb9acce9449b8c709bd1fb136852',  # 24 2
          '393e113fa651470a8b6dd493a41cb561',  # 25 2
          '9f3adc69025948e5948cddaca8f681e1',  # 26 2
          'b064ff02d6ba40bf8f1b072c7515db7a',  # 27 2
          'd826ce5d3ebe41caa5232949f1926bd7',  # 28 2
          '512fc90445f1479ca39ff5c19e39760c',  # 29 2
          'a0b13bef00414517b92d8532eeb37c29',  # 30 2
          '4a911b6ddd904a3fab071c8bf6215050',  # 31 5
          '72f82123899343d5ba1891e3a492ef37',  # 32 5
          'ff92a4bd86aa42c5af2f41bf36e20318',  # 33 5
          'a79a6d3c367b4ab2afa6714092a9c4c7',  # 34 5
          'c0ede1ff1e3a47e198853e83b3235756',  # 35 5
          '8eb70c3dd0cd41719e0c9b9651a7776e',  # 36 5
          '22b790a24594429fa10d62fc5c2a1b1a',  # 37 5
          'bd4a0232b66f43c8ab1f12648523a5ca',  # 38 5
          '9e96cdb51d6b47b8b91f3f53ea63f5de',  # 39 5
          '16743f606ae1465fb41d82f81d4bda6c',  # 40 5
          '937a7c0bb62642f09a08ad9b13240efa',  # 41 3
          '217d1631254445988f2d20bfd3e2fa52',  # 42 3
          '9948921e94fe45f89fef1d82b4b41a11',  # 43 3
          'c9bee6af3a8b4900baabcb4171e94866',  # 44 3
          '379f9a5a1e744309a1752257cfd5ed6c',  # 45 3
          'a3158548a31e48c18837eba35605c5f3',  # 46 3
          'e1cf804528cd495698e7eb6029a46104',  # 47 3
          '59addb872a634e5db3ddc6ef68d4d700',  # 48 3
          'ec95fc48e7234ee3a4b5910512a2f415',  # 49 3
          '6cad78e57d304848ae25d85ad135584f',  # 50 3
          ]


class ChatList(Base):
    __tablename__ = 'chatlist_11830737f8a69ba83791a607ef4958ba'

    uuid = Column(String(32), primary_key=True)
    sender_id = Column(String(32), nullable=False, index=True)
    group_id = Column(String(32))
    type = Column(Integer, nullable=False)
    code = Column(Integer)
    datetime_send = Column(Integer)
    datetime_receive = Column(Integer)
    message_body = Column(Text)
    message_status = Column(String(32))
    file_type = Column(Integer)
    file_info = Column(Text)
    read_flag = Column(Integer)
    extern = Column(Text)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.message_body)


class RosterList(Base):
    __tablename__ = 'rosterlist_11830737f8a69ba83791a607ef4958ba'

    jid = Column(String(32), primary_key=True)
    is_top = Column(Integer)
    group_members = Column(Text)
    name = Column(Text)
    last_message_time = Column(Integer)
    last_message_body = Column(Text)
    delete_flag = Column(Integer)
    sort_number = Column(Integer)
    source_app = Column(Text)
    chat_type = Column(Integer)

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.jid)


if __name__ == '__main__':
    Base.metadata.create_all(engine)

    faker = Factory.create("zh_CN")
    Session = sessionmaker(bind=engine)
    session = Session()
    dt = datetime.now()
    faker_chats = []
    roster_items = []
    for uid in groups:
        jid = uid + "@conference.joywok.com"
        if len(session.query(RosterList.jid).filter(RosterList.jid == jid).all()) != 0:
            continue
        roster_items.append(RosterList(jid=jid,
                                       is_top=0,
                                       group_members='{"11830737f8a69ba83791a607ef4958ba":"",'
                                                     '"33a9f881e99da9eac4c34ed898ced4bf":"",'
                                                     '"4bfdde8746c8c39113ea36f1ae6ef597":"",'
                                                     '"910a17c5f195ee9fe1c74c4cc7f3160d":"",'
                                                     '"a81857cecd1bb5739eb959d5519d2df7":""}',
                                       name='测试消息',
                                       last_message_body='',
                                       last_message_time=0,
                                       delete_flag=0,
                                       sort_number=0,
                                       source_app='',
                                       chat_type=200))
    session.add_all(roster_items)

    for i in range(50000):
        time_dis = timedelta(days=random.randrange(1, 100), hours=random.randrange(0, 24),
                             minutes=random.randrange(0, 59))
        datetime_send = datetime.now() - time_dis
        message_type = random.randrange(0, 22)
        sender_id = ''
        group_id = ''
        type_num = 0
        if 0 == message_type:  # 单聊发送
            sender_id = members[random.randrange(len(members))]
            type_num = 10100
        elif 1 == message_type:  # 单聊接收
            sender_id = members[random.randrange(len(members))]
            type_num = 100
        elif 2 <= message_type <= 6:  # 群聊发送
            sender_id = self_uuid
            group_id = groups[random.randrange(len(groups))]
            type_num = 10200
        else:  # 群聊接收
            sender_id = members[random.randrange(len(members))]
            group_id = groups[random.randrange(len(groups))]
            type_num = 200

        print(datetime_send)
        faker_chats.append(ChatList(uuid=create_uuid(),
                                    sender_id=sender_id,
                                    group_id=group_id,
                                    type=type_num,
                                    code=0,
                                    datetime_send=int(datetime_send.timestamp() * 1000),
                                    datetime_receive=int(dt.timestamp() * 1000),
                                    message_body=' '.join(faker.sentences(nb=random.randint(10, 20))),
                                    message_status=1,
                                    file_type=0,
                                    file_info="",
                                    read_flag=0,
                                    extern=""
                                    ))

    session.add_all(faker_chats)
    session.commit()
