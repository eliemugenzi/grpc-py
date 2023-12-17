

from concurrent import futures
import logging
from dotenv import load_dotenv
import os


import grpc
import users_pb2
import users_pb2_grpc

load_dotenv()


class User(users_pb2_grpc.UserServicer):
    def GetUsers(self, request, context):
        common_password = os.environ.get('COMMON_USER_PASSWORD')
        return users_pb2.GetUsersResponse(users=[
            users_pb2.UserData(id="1",name="Thomas Siebel",email="siebel@c3.io",password=common_password)
        ])


def serve():
    port = os.environ.get('SERVER_PORT')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    users_pb2_grpc.add_UserServicer_to_server(User(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
