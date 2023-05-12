class MessageWrapper:
    def __init__(self, customer_contact, system_type, target_type, event_type, payload) -> None:
        self.customer_contact = customer_contact
        self.system_type = system_type
        self.target_type = target_type
        self.event_type = event_type
        self.payload = payload