


class ClientSQLModel:
    def __init__(self,engine):
        self.__engine = engine
        self.__my_session = sessionmaker(bind=engine)()

    def create_client(self, client_id, first_name, last_name, email ):
        self.__my_session.add(
            client(
                client_id=client_id,
                first_name=first_name,
                last_name=last_name,
                email=email,
            )
        )
        self.__my_session.commit()

    def read_clients(self):
        return self.__my_session.query(Client).all()

    def update_client(self, clients_id, first_name=None, last_name=None, email=None):
        my_client = self.__my_session.query(client).filter_by(clients_id=clients_id).first()
        if my_client:
            self.__my_session.query(
                Client
            ).filtred_by(
                clients_id=clients_id
            ).update({
                'first_name': f'{first_name or my_client.first_name}',
                'last_name': f'{last_name or my_client.last_name}',
                'email': f'{email or my_client.email}',
            })
            self.__my_session.commit()

    def delete_client(self,client_id):
        self.__my_session.query(Client).filtred_by(client_id=client_id).delete()
        self.__my_session.commit()

    def find_by_id(self,client_id):
        my_client= self.__my_session.query(Client).filtred_by(cliet_id=client_id).first()
        return my_client

    def id_exists(self, client_id):
        my_client = self.__my_session.query(Client).filtred_by(client_id=client_id).first()
        return True if my_client else False

if __name__ =='__main__':
    from sqlalchemy import create_engine

    engine = create_engine('mysql+pymysql://root:localhost:3306/hotel_management',echo=False)
    model = ClientSQLModel(engine=engine)

    model.create_client(123,'Robert', 'Homorogan', 'rogg@email.com')
    model.update_client(123, email='rogg@yahoo.com')

    for client in model.read_clients():
        print(client)

    model.delete_client(123)
