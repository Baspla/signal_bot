# Planung
Loop alle X (1 Sekunde?) der mit /v1/receive die neuen Nachrichten abfragt.
Auflösen der Nachrichten in Objekte.

## TODOs

- Dekoratoren in Klassen auslagern

## Decorators

@every
def funktion(envelope):

@message
def funktion(envelope,message):

@message(regex)
def funktion(envelope,message):

@command(cmd)
def funktion(envelope,cmd,args):

@reaction
def funktion(envelope,emoji):

@reaction(isRemove)
def funktion(envelope,emoji):

@quote
def funktion(envelope):

@delete
def funktion(envelope):

@attatchment
def funktion(envelope):

@attatchment(contentType)
def funktion(envelope):


## Beispieldaten

`[{"envelope":{...},"account":"+49...25"}},...]`

### Attatchment Message

    "source":"+49...10",
    "sourceNumber":"+49...10",
    "sourceUuid":"3d89...ea65",
    "sourceName":"Tim Morgner",
    "sourceDevice":2,
    "timestamp":1659039939499,
    "dataMessage":{
        "timestamp":1659039939499,
        "message":"test",
        "expiresInSeconds":0,
        "viewOnce":false,
        "attachments":[
            {"contentType":"application/x-krita",
            "filename":"Signal-Logo.svg.kra",
            "id":"3174707558046123701","size":1445166}
        ]
    }

### Response

     "source":"+49...10",
     "sourceNumber":"+49...10",
     "sourceUuid":"3d89...ea65",
     "sourceName":"Tim Morgner",
     "sourceDevice":2,
     "timestamp":1659040106096,
     "dataMessage":{
        "timestamp":1659040106096,
        "message":"response",
        "expiresInSeconds":0,
        "viewOnce":false,
        "quote":{
           "id":1659035465304,
           "author":"+49...25",
           "authorNumber":"+49...25",
           "authorUuid":"47c6...8614",
           "text":"Hallo",
           "attachments":[
           ]
        }
     }

### Reaction

     "source":"+49...10",
     "sourceNumber":"+49...10",
     "sourceUuid":"3d89...ea65",
     "sourceName":"Tim Morgner",
     "sourceDevice":2,
     "timestamp":1659040110303,
     "dataMessage":{
        "timestamp":1659040110303,
        "message":null,
        "expiresInSeconds":0,
        "viewOnce":false,
        "reaction":{
           "emoji":"👍",
           "targetAuthor":"+49...25",
           "targetAuthorNumber":"+49...25",
           "targetAuthorUuid":"47c6...8614",
           "targetSentTimestamp":1659035465304,
           "isRemove":false
        }
     }

### Message

     "source":"+49...10",
     "sourceNumber":"+49...10",
     "sourceUuid":"3d89...ea65",
     "sourceName":"Tim Morgner",
     "sourceDevice":2,
     "timestamp":1659040118192,
     "dataMessage":{
        "timestamp":1659040118192,
        "message":"Hallo",
        "expiresInSeconds":0,
        "viewOnce":false
     }

### remoteDelete

     "source":"+49...10",
     "sourceNumber":"+49...10",
     "sourceUuid":"3d89...ea65",
     "sourceName":"Tim Morgner",
     "sourceDevice":2,
     "timestamp":1659040130536,
     "dataMessage":{
        "timestamp":1659040130536,
        "message":null,
        "expiresInSeconds":0,
        "viewOnce":false,
        "remoteDelete":{
           "timestamp":1659039431843
        }
     }