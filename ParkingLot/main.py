# 1. Big parking lots 10k - 30k
# 2. 4 entrance & 4 exits
# 3. Ticket & spot attatched at entrance
# 4. Parking spot should be nearest to the entrance
# 5. Limit/Capacity 30k
# 6. Parking spots - HC, Compact, Large, Motorcycle
# 7 Hourly Rate
# 8. Cash & credit card
# 9. Monitoring system
# 10. Minimal change in code for change in requirements


# ACTORS:-

# 1. Parking lot System
# 2. Entry?Exit Terminals
#     - printers
#     - payment processor 
# 3. Parking spot 
# 4. Ticket 
# 5. Database
# 6. Monitoring system

from abc import ABC, abstractmethod


class ParkingSpot:
    @abstractmethod
    def __init__(self, id, reserve):
        pass

