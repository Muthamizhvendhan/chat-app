#Message web controller
class message_web_controller(object):
  
  #Costructor
  def __init__(self):
    pass  

  # HTTP GET method processor.
  def get(self,*args,**kwargs):
    if self.request=="/message/create":
      return render_template('main.html',var=self.var)
    elif self.request=="/messages":
      return render_template('main.html',var=self.var)