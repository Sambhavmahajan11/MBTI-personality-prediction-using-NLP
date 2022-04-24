from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    if self.drop.selected_value=="SVC Linear":
      type = anvil.server.call("SVC",self.text_box_1.text)
      self.result.text=f"Your personality type is {type}"
    elif self.drop.selected_value=="Catboost":
      type = anvil.server.call("CAT",self.text_box_1.text)
      self.result.text=f"Your personality type is {type}"
    else:
      alert("Please select a model")

  def handle_click(self, **event_args):
    """This method is called when the user presses the submit button"""
    if self.drop.selected_value=="SVC Linear":
      type = anvil.server.call("SVC",self.text_box_1.text)
      self.result.text=f"Your personality type is {type}"
    elif self.drop.selected_value=="Catboost":
      type = anvil.server.call("CAT",self.text_box_1.text)
      self.result.text=f"Your personality type is {type}"
    else:
      alert("Please select a model")
