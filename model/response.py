from model import status

class Response(object):

  @staticmethod
  def success(**result):
    return Response(
      result=result,
      msg=status.SUCCESS_MSG,
      code=status.SUCCESS
    )
  
  def keys(self):
    return (
      'msg',
      'code',
      'result'
    )
  
  def __getitem__(self, item):
    return getattr(self, item)

  def __setattr__(self, name, value) -> None:
      return super().__setattr__(name, value)

  def __init__(self, result, msg='', code=0, ) -> None:
    self.msg = msg
    self.code = code
    self.result = result
  
  def dict(self):
    return dict(self)
