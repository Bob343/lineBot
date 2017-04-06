from line import LineClient
token = "EfPdQCmYs1lLNDlN9dG5.Dlij+I0dlUkrGd52DXN8jq.G/QraQDoGoeeBxLbOoCelhGEHEveuNhrgHWv2fkklMw="

def main():
 client = LineClient(authToken = token)
 for op in client.longPoll():
  print op
  print op[0]
  print op[1]
  print op[2]
  print op[3]

main()
