

from __future__ import print_function

import logging

import grpc
from dotenv import load_dotenv
import os
import users_pb2
import users_pb2_grpc

load_dotenv()


def run():
    response = []
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to get these human beings ...")

    server_url = os.environ.get('SERVER_URL')
    with grpc.insecure_channel(server_url) as channel:
        stub = users_pb2_grpc.UserStub(channel)
        response = stub.GetUsers(users_pb2.GetUsersRequest())
    print(response.users)


if __name__ == "__main__":
    logging.basicConfig()
    run()
