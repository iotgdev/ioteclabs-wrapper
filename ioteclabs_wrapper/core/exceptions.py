try:
    from json.decoder import JSONDecodeError
except ImportError:
    JSONDecodeError = ValueError


class LabsException(Exception):
    """Base exception class"""
    pass


class LabsResourceNotFound(LabsException):
    """404 exception"""
    pass


class LabsAPIException(LabsException):
    """500 exception"""
    pass


class LabsNotAuthenticated(LabsException):
    """401 exception"""
    pass


class LabsPermissionDenied(LabsException):
    """403 exception"""
    pass


class LabsBadRequest(LabsException):
    """400 exception"""
    pass


def get_exception(response):
    """
    Gets the appropriate exception based on the requests.Response.status_code
    :type response: requests.Response
    :rtype: LabsException
    """
    exceptions = {
        404: LabsResourceNotFound, 500: LabsAPIException, 401: LabsNotAuthenticated, 403: LabsPermissionDenied,
        400: LabsBadRequest
    }

    # noinspection PyBroadException
    try:
        message = response.json()['detail']
    except (KeyError, JSONDecodeError):
        message = response.content

    return exceptions.get(response.status_code, LabsException)(message)
