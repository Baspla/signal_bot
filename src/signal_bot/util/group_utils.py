import base64


def groupContextFromId(group_id):  # Sollte diese Methode nicht mehr gehen so muss über v1/groups die id abgeglichen werden
    return f"group.{base64.b64encode(group_id.encode('ascii')).decode('ascii')}"