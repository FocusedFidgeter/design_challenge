## Add extra functionality to the events api

Using the ORM improved code we will add some extra functionality to the API.

## Challenge

For this challenge you will need to add some extra functionality to the api. The extra functionality should
implement the following:

1. Add a feature to allow for ticket cancellation. That should be for a single ticket based on its id but also
   in case an event is deleted all the related tickets should be deleted as well.
2. Add a feature to be able to change the name on the ticket.

For both of these features, the api should make sure that the event for which the ticket is for hasn't started yet.

### Important

Remember to delete the database from the local directory after every time you test something to avoid errors.
