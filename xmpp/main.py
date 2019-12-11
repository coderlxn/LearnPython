import logging
import uuid
from sleekxmpp import ClientXMPP, ET


class EchoBot(ClientXMPP):
    def __init__(self, jid, password):
        ClientXMPP.__init__(self, jid, password)

        self.add_event_handler("session_start", self.session_start)
        self.add_event_handler("message", self.message)

    def session_start(self, event):
        self.send_presence()
        # self.get_roster()

    def message(self, msg):
        # if msg["type"] in ("chat", "normal"):
        #     msg.reply("Thanks for sending\n%(body)s" % msg).send()
        message_sender = str(msg["from"])
        message_sender = message_sender.split('/')[0]
        logging.info("Recedived message from {}".format(message_sender))

        if message_sender == 'b20b5f4eb87af6b929977b3e4ad5ad86@joywok.com':
            message = self.make_message('a861550db2514d7182b384089aced349@joywok.com', msg['body'], mtype="chat")
            message["id"] = str(uuid.uuid4()).replace('-', '')
            message.send()



    def send_message_callback(self, uid, to, body, json_data=""):
        logging.info("{} # Send message to {} {}".format(uid, to, body))
        message = self.make_message(to, body, mtype="chat")
        message["id"] = str(uuid.uuid4()).replace('-', '')
        if json_data is not "":
            json_element = ET.Element("json")
            json_element.attrib = {"xmlns": "urn:xmpp:json:0", "jwtype": "assistant"}
            json_element.text = json_data
            message.append(json_element)
        message.send()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    bot_uuid = '55939f2bbd294ab7ea7b178c3861c2e8'
    xmpp_host = 'staging-im.joywok.com'
    xmpp_port = 5333

    while True:
        xmpp = EchoBot("%s@joywok.com" % bot_uuid, '98ona6am8dv4mbjngr3ngodof5')

        xmpp.register_plugin('xep_0030')  # Service Discovery
        xmpp.register_plugin('xep_0004')  # Data Forms
        xmpp.register_plugin('xep_0060')  # PubSub
        xmpp.register_plugin('xep_0198')  #
        xmpp.register_plugin('xep_0199', pconfig={
            'keepalive': True,
            'interval': 60,
            'timeout': 30
        })  # XMPP Ping

        xmpp['feature_mechanisms'].unencrypted_plain = True
        xmpp["xep_0199"].keepalive = True


        xmpp.boundjid.domain = "joywok.com"
        xmpp.boundjid.resource = "assistant"
        xmpp.requested_jid.resource = 'assistant'
        xmpp.boundjid.user = bot_uuid
        xmpp.connect(address=(xmpp_host, xmpp_port), reattempt=False, use_tls=False)
        try:
            xmpp.process(block=True)
        except (SystemExit, KeyboardInterrupt):
            raise
        except Exception as what:
            logging.error("Error occurs", exc_info=True)
        finally:
            receiver.stop_consuming()
            xmpp.disconnect()


