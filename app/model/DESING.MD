# Documentación de Diseño: Clase HotelService
## 1. Diseño de la Clase
Se ha propuesto la clase `HotelService` utilizando el decorador `@dataclass`.
**Justificación:** Esta clase actúa como un contenedor de información para servicios adicionales (Spa, lavandería, etc.). Al ser una entidad que no requiere lógica de estado interna compleja ni métodos privados de procesamiento, las `dataclasses` proporcionan una implementación limpia, eficiente y con métodos automáticos (`__init__`, `__repr__`) que facilitan su gestión.
## 2. Integración con el Modelo
La integración se basa en el principio de **Agregación** para mantener un modelo coherente con la realidad del negocio:
- **En la Clase Reservation:** Se añadió un atributo `services` que consiste en una lista de objetos `HotelService`. Esto permite que los cargos adicionales estén vinculados directamente a la estancia del cliente. Si una reserva se cancela o se liquida, sus servicios asociados permanecen vinculados a ese ID específico.
- **En la Clase Hotel:** Se implementó el método `add_service_to_reservation`. El hotel actúa como una fachada (Facade), centralizando la lógica para buscar la reserva y asignar el nuevo objeto de servicio.
## 3. Principios de Programación Orientada a Objetos (OOP)
- **Responsabilidad Única (SRP):** `HotelService` solo define el concepto de servicio. La lógica de cobro y almacenamiento recae en `Reservation`.
- **Encapsulamiento:** Aunque son dataclasses, el acceso a la lógica de negocio se hace a través de métodos definidos en la clase controladora (`Hotel`), evitando que la consola manipule directamente las listas internas.
- **Modularidad:** El sistema permite añadir nuevos tipos de servicios sin modificar la estructura básica de las habitaciones o los huéspedes.