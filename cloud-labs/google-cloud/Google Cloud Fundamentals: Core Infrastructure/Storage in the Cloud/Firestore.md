Google Cloud’s fourth core storage option is Firestore.

Firestore is a flexible, horizontally scalable, NoSQL cloud database for mobile, web, and server development.

With Firestore, data is stored in documents and then organized into collections.

Documents can contain complex nested objects in addition to subcollections.

Each document contains a set of key-value pairs.

For example, a document to represent a user has the keys for the firstname and lastname with the associated values.

Firestore’s NoSQL queries can then be used to retrieve individual, specific documents or to retrieve all the documents in a collection that match your query parameters.

Queries can include multiple, chained filters and combine filtering and sorting options.

They're also indexed by default, so query performance is proportional to the size of the result set, not the dataset.

Firestore uses data synchronization to update data on any connected device.

However, it's also designed to make simple, one-time fetch queries efficiently.

It caches data that an app is actively using, so the app can write, read, listen to, and query data even if the device is offline.

When the device comes back online, Firestore synchronizes any local changes back to Firestore.

Firestore leverages Google Cloud’s powerful infrastructure: automatic multi-region data replication, strong consistency guarantees, atomic batch operations, and real transaction support.
