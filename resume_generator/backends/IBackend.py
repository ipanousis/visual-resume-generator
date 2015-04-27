from zope.interface import Interface
from zope.interface import implements

class IResumeBackend(Interface):
  """Implementations will be able to store and retrieve resumes and associated views based on a given ID."""

  def persist(username, content=None, view=None):
    """Persist resume content and / or a view created for the resume that belongs to the given username."""

  def load(username):
    """Load the resume content and associated views for a given username."""

