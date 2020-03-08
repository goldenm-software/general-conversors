"""
Helpers
"""

import json

class Convsersor:
  """
  Conversor
  Convert a python dict to flespi dict

  Since : 2020-03-08

  Notes
  -----
  Covnert method = convert()

  Attributes
  ----------
  _result : dict : private
    Final result after conversion
  _source : dict : private
    Source or original dict to convert

  Methods
  -------
  _validate_is_array_dict(value=any)  : private
    Validate if is an array or dict
  _scan_down(key=str, value=any)      : private
    Iterate values and append in result
  convert()                           : public
    Convert method
  """

  _result = {}
  _source = {}

  def __init__(self, source):
    """
    Constructor

    Parameters
    ----------
    source : dict
      Original dict to convert
    """

    self._source = source

  def _validate_is_array_dict(self, value):
    """
    Validate if is an array or a dict

    Parameters
    ----------
    value : any
      Value to compare

    Return
    ------
    bool
      If true when is a dict or list
    """

    return isinstance(value, (dict, list,))

  def _scan_down(self, key, value):
    """
    Convert to dictionary (Flespi)

    Parameters
    ----------
    key   : str
      Key to scan
    value : any
      Value to scan
    """

    iteration = None
    if isinstance(value, list):
      iteration = enumerate(value)
    else:
      iteration = value.items()

    for i, v in iteration:
      if self._validate_is_array_dict(v):
        self._scan_down(f'{key}.{i}', v)
      else:
        self._result[f'{key}.{i}'] = v

  def set_source(self, source):
    """
    Set a new source

    Parameters
    ----------
    source : dict
      New source
    """

    self._source = source
    self._result = {}

  def to_flespi(self):
    """
    Flespi result

    Return
    ------
    result : json
      JSON-converted dict
    """

    return json.loads(self.convert())

  def convert(self):
    """
    Conversor

    Return
    ------
    _result : dict
      Converted dictionary
    """

    for key, value in self._source.items():
      if self._validate_is_array_dict(value):
        self._scan_down(key, value)
      else:
        self._result[key] = value

    return self._result
