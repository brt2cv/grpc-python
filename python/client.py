#!/usr/bin/env python3
# @Date    : 2021-12-20
# @Author  : Bright (brt2@qq.com)
# @Link    : https://gitee.com/brt2
# @Version : v0.0.1

# python -m grpc_tools.protoc -I ../helloworld --python_out=. --grpc_python_out=. ../helloworld/helloworld.proto

import grpc
import helloworld_pb2_grpc
import helloworld_pb2

if __name__ == '__main__':
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name="ahts"))
    print(f'msg:{response.message}')
