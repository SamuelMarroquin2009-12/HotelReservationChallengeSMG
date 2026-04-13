from dataclasses import dataclass, field
from datetime import datetime, date, timedelta
from typing import ClassVar

from dataclasses import dataclass, field
from datetime import date, datetime, timedelta
from typing import ClassVar  # Importante para definir variables de clase puras

# Importación de utilidades según el requerimiento del ejercicio
from app.services.util import (
    generate_unique_id, guest_not_found_error, room_not_available_error,
    reservation_not_found_error, room_already_exists_error,
    date_lower_than_today_error, room_not_found_error
)


