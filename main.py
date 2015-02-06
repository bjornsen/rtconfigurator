import logging
import rtconfigurator
import inspect

logging.basicConfig(level=logging.DEBUG)

rtconfigurator.register("ticket_types.yaml")

incident = rtconfigurator.Incident()

print(incident.f)

incident.f = 100

print(incident.f)

print(str(rtconfigurator.Ticket))
print(str(rtconfigurator.TicketRegistry))