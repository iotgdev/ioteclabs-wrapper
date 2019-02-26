"""
python wrapper for the iotec labs API
Usage:
>>> from ioteclabs_wrapper import LabsAPI
>>> api = LabsAPI()
>>> # get account information for an id
>>> api.xcm.retrieve(id='X8tXcX5rSdaOMeF7Mj2g')

>>> # get a list of campaigns
>>> api.xcm.list()

>>> # delete a lineitem by id
>>> api.xcm.delete(id=62)

>>> # change user
>>> api.change_user('<username>', '<password>')
>>> # jwt tokens are added to the session
"""

from ioteclabs_wrapper.core.access import LabsAPI

__all__ = ['LabsAPI']
