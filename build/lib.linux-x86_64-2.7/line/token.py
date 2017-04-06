from line import LineClient


token = 'EfEUB3RYUyqhUjxWTlE5.KcN5VkYwUV1kbpbfZlSQrq.+zJjsypN8QJhQzoEZGRSh6/KIbH9xqvkJFS76leBuag='

def main():
 client = LineClient(authToken=token)
 print client.revision
 for op in client.longPoll():
  print op

main()
