from zope.interface import Interface
from zope.interface import implements

class FileBackend(object):
  """Stores resumes and views on the filesystem as JSON."""

  implements(IResumeBackend)

  def persist(username, content=None, view=None):
    """Persist resume content and / or a view created for the resume that belongs to the given username."""
    return True

  def load(username):
    """Load the resume content and associated views for a given username."""
    return True

