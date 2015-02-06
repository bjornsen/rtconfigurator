import logging
import rtconfigurator
import inspect

logging.basicConfig(level=logging.DEBUG)

rtconfigurator.register("ticket_types.yaml")

incident = rtconfigurator.Incident()

logging.debug(incident.f)

incident.f = 100

logging.debug(incident.f)

logging.debug(str(rtconfigurator.Ticket))
logging.debug(str(rtconfigurator.TicketRegistry))