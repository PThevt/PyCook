import json


class Recipe:

    def __init__(self, _id, _name, _description):
        self._id = _id
        self._name = _name
        self._description = _description

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, v):
        self._id = v

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, v):
        self._name = v

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, v):
        self._description = v

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True)
