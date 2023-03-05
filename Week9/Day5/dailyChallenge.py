class Airline:
     def __init__(self, id, name, planes):
         self.id = id
         self.name = name
         self.planes = planes
class Airplane:
    def __init__(self, id, current_location, company, flights):
        self.id = id
        self.current_location = current_location
        self.company = company
        self.flights = flights
        self.next_flights = {}
        self.next_flights[self.flights.date] = self.flights.location
    def fly(self, fl_destination):
        if fl_destination.destination in self.next_flights:
            print(f"Next flight of {self.id} from {self.current_location} to {fl_destination.destination} at {fl_destination.date}")
    def location_on_date(self, fl_date):
        print(f"{fl_date.origin} the plane current position {fl_date.date}")
    def available_on_date(self, date, location):
        if self.next_flights[date] == date and self.next_flights.get(date) == location:
            return True

class Flight:
    def __init__(self, date, destination, origin, plane, id):
        self.date = date
        self.destination = destination
        self.origin = origin
        self.plane = plane
        self.id = id
    def take_off(self):
        self.origin = "Now flying"
    def land(self):
        self.origin = self.destination
class Airport:
    def __init__(self, city, planes, scheduled_departures, scheduled_arrivals):
        self.city = city
        self.planes = []
        self.scheduled_departures = []
        self.scheduled_arrivals = []
    def schedule_flight(self, destination, datetime):
        for plane in self.planes:
            if plane.available_on_date(date, location):
                self.scheduled_departures.append({"date": date, "location" location})
            else:
                self.scheduled_arrivals.append({"date": date, "location" location})

    def info(self, start_date, end_date):
        return  f"{self.city_id} - city {self.planes} - planes {self.scheduled_departures} - departures {self.scheduled_arrivals} - arrivals"

# = Airport("Dubai", planes_in_du, )
# planes_in_du = Airplane("du", dubai_air, )
# dubai_air = Airline("du", "Dubai Air", )
