class HistoryTracedAttribute:
    def __init__(self, trace_attribute_name: str) -> None:
        self.trace_attribute_name = trace_attribute_name  # [1] self._name = None

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        self._track_change_in_value_for_instance(instance, value)
        instance.__dict__[self._name] = value

    def _track_change_in_value_for_instance(self, instance, value):
        self._set_default(instance)  # [2]
        if self._needs_to_track_change(instance, value):
            instance.__dict__[self.trace_attribute_name].append(value)

    def _needs_to_track_change(self, instance, value) -> bool:
        try:
            current_value = instance.__dict__[self._name]
        except KeyError:  # [3]
            return True
        return value != current_value  # [4]

    def _set_default(self, instance):
        instance.__dict__.setdefault(self.trace_attribute_name, [])


class Traveler:

    current_city = HistoryTracedAttribute("cities_visited")

    def __init__(self, name: str, current_city: str) -> None:
        self.name = name
        self.current_city = current_city
