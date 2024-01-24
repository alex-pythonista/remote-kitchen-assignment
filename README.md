# remote-kitchen-assignment
The goal is to create a simple Django backend where users can manage restaurants and menus.

# Task list

**User and Auth**
- [ ] Extend the user model to include necessary fields for user profiles.
- [ ] Update permissions to allow owners and employees to manage orders and payments.

**Restaurant and menu**
- [ ] Allow owners to create a new restaurant.
- [ ] Allow owners to update the details of their restaurant.
- [ ] Provide a list of restaurants owned by the authenticated owner.
- [ ] Allow owners to create a new menu for their restaurant.
- [ ] Allow owners to update the details of a menu.
- [ ] Provide a list of menus for the specified restaurant owned by the authenticated owner.
- [ ] Allow owners to create new items for a menu.
- [ ] Allow owners to update the details of an item.

**User Roles and Permissions**
- [ ] Define user roles for owners and employees.
- [ ] Implement permission checks in your APIs to ensure that only authorized users (connected to a specific restaurant) can create, modify, or view the menu and place orders.

**Ordering and Payment**
- [ ] Integrate Stripe API for payment processing. You can use the stripe library or any other Django-friendly Stripe package.
- [ ] Create API endpoints for processing payments.
- [ ] Implement a secure and efficient way to handle payment information, such as using Stripe tokens.
- [ ] Create models for orders, including necessary fields such as items, quantity, price, etc.
- [ ] Implement APIs for creating and managing orders.
- [ ] Connect the ordering system to the menu, ensuring that users can create orders based on the available menu items.
