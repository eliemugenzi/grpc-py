

from concurrent import futures
import logging

import grpc
import users_pb2
import users_pb2_grpc


class User(users_pb2_grpc.UserServicer):
    def GetUsers(self, request, context):
        return users_pb2.GetUsersResponse(users=[
            users_pb2.UserData(id="1",name="Thomas Siebel",email="siebel@c3.io",password="343434")
        ])


def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    users_pb2_grpc.add_UserServicer_to_server(User(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
