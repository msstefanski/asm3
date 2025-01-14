
def get_event_query(dbo):
    return "SELECT ev.*, owner.OwnerName AS EventOwnerName " \
           "FROM event ev " \
           "LEFT OUTER JOIN owner ON ev.EventOwnerID = owner.ID "

def get_event(dbo, eventid):
    """
    Returns a complete event row by id
    (int) eventid: The event to get
    """
    e = dbo.first_row(dbo.query(get_event_query(dbo) + " WHERE ev.ID = %d" % eventid))
    return e

