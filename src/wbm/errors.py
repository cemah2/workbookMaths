"""Exceptions shared by the wbm modules."""


class MymathNotFoundError(ImportError):
    """The requested mymath implementation does not exist yet."""


class MymathMissingError(AttributeError):
    """A mymath module (or the whole package) is not available yet.

    ``wbm.attempt`` turns it into a friendly "⏳ pas encore fait" message.
    """
