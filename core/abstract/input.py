"""
General data input interfaces
"""


class Device:
    """
    Data gathering device abstraction
    """

    def __init__(self, manufacturer, model, serial_number):
        """
        :param manufacturer: Device Manufacturer
        :param model: Device model
        :param serial_number: Device Serial Number
        """
        self.manufacturer = manufacturer
        self.model = model
        self.serial_number = serial_number


class ExternalData:
    """
    Encapsulates collected data in a traceable fashion
    """

    def __init__(self, access_timestamp, raw):
        """
        :param access_timestamp: Time the external API was accessed
        :param raw: Raw data collected
        """
        self.access_timestamp = access_timestamp
        self.raw = raw


class ExternalDataSource:
    """
    Interface to enforce correct return type and standardized naming
    """

    def read_state(self) -> ExternalData:
        """
        Establishes a connection to the integration medium and returns the latest state
        :rtype: ExternalData
        """
        raise NotImplementedError


class EnergyData(ExternalData):
    """
    Standard for energy and power data used as input
    """

    def __init__(self, device, access_timestamp, raw, accumulated_power, measurement_timestamp):
        """
        Minimum set of data for power measurement logging.
        :param device: Metadata about the measurement device
        :param access_timestamp: Time the external API was accessed
        :param raw: Raw data collected
        :param accumulated_power: Registered in Mega Watts
        :param measurement_timestamp: Time of measurement at the source
        """
        self.device = device
        self.accumulated_power = accumulated_power
        self.measurement_timestamp = measurement_timestamp
        ExternalData.__init__(self, access_timestamp, raw)


class CarbonEmissionData(ExternalData):
    """
    Standard for carbon emission data used as input
    """

    def __init__(self, access_timestamp, raw, accumulated_co2, measurement_timestamp):
        """
        Minimum set of data for power measurement logging.
        :param access_timestamp: Time the external API was accessed
        :param raw: Raw data collected
        :param accumulated_co2: Registered in great britain pounds per carbon dioxide
        :param measurement_timestamp: Time of measurement at the source
        """
        self.accumulated_co2 = accumulated_co2
        self.measurement_timestamp = measurement_timestamp
        ExternalData.__init__(self, access_timestamp, raw)