# Planung
Loop alle X (1 Sekunde?) der mit /v1/receive die neuen Nachrichten abfragt.
Auflösen der Nachrichten in Objekte.

## Programmaufbau

### Core
Holt Updates vom Reciever und ruft Handler auf

### HandlerDecorators
Verschiedene @Decorator für Handler.
Jeder HandlerDecorators führt eine Eigene Liste an registrierten Handlern und hat eine Grundbedinung (z.B. Hat message) bei der er erst seine Handler überpüft

### Addons
Registriert seine Handler

### Sender
Hat verschiedene Methoden um Nachrichten zu senden.
Kann zum Testen gemocked werden.

### Reciever
Holt die Updates.
Kann zum Testen ersetzt werden.

## Gelerntes

- GroupId an die gesendet wird ist (bisher immer) "group." + BASE64(groupId aus update)
- Der REST API Wrapper kann keine Reciepts versenden (gelesen)
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


# Aufbau

## Envelope
    [deprecated] String source
    String sourceNumber
    String sourceUuid
    String sourceName
    Integer sourceDevice
    long timestamp
    [optional] DataMessage dataMessage
    [optional] SyncMessage syncMessage
    [optional] CallMessage callMessage
    [optional] ReceiptMessage receiptMessage
    [optional] TypingMessage typingMessage

---

##Messages

### DataMessage

    long timestamp
    [optional] String message
    Integer expiresInSeconds
    Boolean viewOnce
    [optional] Reaction reaction
    [optional] Quote quote
    [optional] Payment payment
    [optional] List<Mention> mentions
    [optional] List<Preview> previews
    [optional] List<Attachment> attachments
    [optional] Sticker sticker
    [optional] RemoteDelete remoteDelete
    [optional] List<SharedContact> contacts
    [optional] GroupInfo groupInfo

### SyncMessage

    [optional] SyncDataMessage sentMessage
    [optional] List<String> blockedNumbers
    [optional] List<String> blockedGroupIds
    [optional] List<SyncReadMessage> readMessages
    [optional] SyncMessageType type

### CallMessage

    [optional] Offer offerMessage
    [optional] Answer answerMessage
    [optional] Busy busyMessage
    [optional] Hangup hangupMessage
    [optional] List<IceUpdate> iceUpdateMessages

### ReceiptMessage

    long when
    boolean isDelivery
    boolean isRead
    boolean isViewed
    List<Long> timestamps

### TypingMessage

    String action
    long timestamp
    [optional] String groupId

---

## Daten

### Attachment

    String contentType
    String filename
    String id
    Long size

### ContactAddress

    String type
    String label
    String street
    String pobox
    String neighborhood
    String city
    String region
    String postcode
    String country

### ContactAvatar

    Attachment attachment
    boolean isProfile

### ContactEmail

    String value
    String type
    String label

### ContactName

    String display
    String given
    String family
    String prefix
    String suffix
    String middle

### ContactPhone

    String value
    String type
    String label

### GroupInfo

    String groupId
    String type

### Mention

    [deprecated] String name
    String number
    String uuid
    int start
    int length

### Payment

    String note
    byte[] receipt

### Quote

    long id
    [deprecated] String author
    String authorNumber
    String authorUuid
    String text
    [optional] List<Mention> mentions
    List<QuotedAttachment> attachments

### QuotedAttachment

    String contentType
    String filename
    [optional] Attachment thumbnail

### Reaction

    String emoji
    [deprecated] String targetAuthor
    String targetAuthorNumber
    String targetAuthorUuid
    long targetSentTimestamp
    boolean isRemove

### RemoteDelete

    long timestamp

### SharedContact

    ContactName name
    [optional] ContactAvatar avatar
    [optional] List<ContactPhone> phone
    [optional] List<ContactEmail> email
    [optional] List<ContactAddress> address
    [optional] String organization

### Sticker

    String packId
    String packKey
    int stickerId

##Sync

### SyncDataMessage

    [deprecated] String destination
    String destinationNumber
    String destinationUuid
    DataMessage dataMessage

### SyncReadMessage

    [deprecated] String sender
    String senderNumber
    String senderUuid
    long timestamp

### SyncMessageType

    Enum mit:
    CONTACTS_SYNC
    GROUPS_SYNC
    REQUEST_SYNC

## Call Stubs

### Offer

### Answer

### Busy

### Hangup

### IceUpdate

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