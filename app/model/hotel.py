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
# --- PARTE 2: CLASE ADICIONAL ---
@dataclass
class HotelService:
    """
    Representa servicios extra (Spa, Minibar, etc.).
    Se usa dataclass por ser una entidad principalmente de datos.
    """
    name: str
    price: float
    description: str = "Sin descripción"
    def __str__(self) -> str:
        return f"{self.name} (${self.price})"
# --- PARTE 1: MODELO BASE ---
@dataclass
class Guest:
    # Usamos ClassVar para que no entren al constructor y no causen el TypeError
    REGULAR: ClassVar[str] = "regular"
    VIP: ClassVar[str] = "vip"

    name: str          # Obligatorio
    email: str         # Obligatorio
    type_: str = "regular"  # Opcional (con valor por defecto)

    def __str__(self) -> str:
        return f"Guest {self.name} ({self.email}) of type {self.type_}"


@dataclass
class Reservation:
    # Atributos obligatorios PRIMERO
    guest_name: str
    description: str
    check_in: date
    check_out: date

    # Atributos con default_factory o init=False SIEMPRE al final
    guests: list[Guest] = field(default_factory=list, init=False)
    services: list[HotelService] = field(default_factory=list, init=False)
    id: str = field(default_factory=generate_unique_id)

    def add_guest(self, name: str, email: str, type_: str = "regular"):
        nuevo_huesped = Guest(name, email, type_)
        self.guests.append(nuevo_huesped)

    def delete_guest(self, guest_index: int):
        if 0 <= guest_index < len(self.guests):
            self.guests.pop(guest_index)
        else:
            guest_not_found_error()

    def add_service(self, service: HotelService):
        """Añade un servicio consumido a esta reserva."""
        self.services.append(service)

    def __len__(self) -> int:
        return (self.check_out - self.check_in).days

    def __str__(self) -> str:
        return (f"ID: {self.id}\n"
                f"Guest: {self.guest_name}\n"
                f"Description: {self.description}\n"
                f"Dates: {self.check_in} - {self.check_out}")