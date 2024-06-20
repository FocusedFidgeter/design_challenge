## Add notification functionality using the observer pattern

The observer pattern is a design pattern in which an object, called the subject, maintains a list of its dependents, 
called observers, and notifies them automatically of any state changes, usually by calling one of their methods. 
This pattern is useful in situations where multiple objects need to be informed of changes to the state of another 
object, without tightly coupling them together. It allows for loosely coupled and highly cohesive code that is easily 
maintainable and extendable.


## Challenge

For this challenge you should add a feature to the ticket API to be able to send confirmations to the customer. You 
should design it in such a way that you can easily add different types of confirmation (email, SMS, or both). Switching 
between different confirmation methods should be modular and without changing the code, itself.











