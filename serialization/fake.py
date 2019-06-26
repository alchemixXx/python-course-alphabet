class Fake_json_hook():

    @staticmethod
    def json_hook(obj):
        if obj == "Car":
            return "Car deserialization has been run"
        elif obj == "Garage":
            return "Garage deserialization has been run"
        elif obj == "Cesar":
            return "Cesar deserialization has been run"
