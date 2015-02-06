import yaml
import logging

logger = logging.getLogger(__name__)

class TicketRegistry(type):
	def __init__(cls, name, bases, nmspc):
		super(TicketRegistry, cls).__init__(name, bases, nmspc)
		if not hasattr(cls, 'registry'):
			cls.registry = set()
		logger.debug("Registering class " + name)
		cls.registry.add(cls)
		g = globals()
		if name not in g:
			g[name] = cls
			logger.debug(name + " added successfully.")
		# Remove base classes
		cls.registry -= set(bases)
		
	def __iter__(cls):
		return iter(cls.registry)
	
	def __str__(cls):
		if cls in cls.registry:
			return cls.__name__
		return cls.__name__ + ":" + ",".join([sc.__name__ for sc in cls])

class Ticket(object, metaclass = TicketRegistry):
	pass

def register(config_file):
	with open(config_file) as f:
		ticket_types = yaml.load(f)
		
		for ticket in ticket_types:
			logger.debug("About to add " + str(ticket))
			ticket_name, ticket_dict = ticket
			type(ticket_name, (Ticket,), ticket_dict)