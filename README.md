# Cerberus

Cerberus is a backend platform designed for managing **Renewable Energy Communities (REC / CER)**, built using **Domain-Driven Design (DDD)** and **Clean Architecture** principles.

The project focuses on modeling complex energy-sharing logic, regulatory constraints, and financial distribution mechanisms in a scalable and maintainable way.

---

## Overview

Cerberus provides a structured backend system for:

* Member lifecycle management within an energy community
* Energy production and consumption tracking
* Shared energy calculation based on temporal matching
* Incentive calculation and distribution among members

The system is designed to reflect real-world regulatory requirements and industry practices.

---

## Architecture

The project strictly follows **Clean Architecture**:

* **Domain Layer**
  Contains core business logic, entities, value objects, and domain services.
  Completely framework-independent.

* **Application Layer**
  Implements use cases and orchestrates domain logic.

* **Infrastructure Layer**
  Handles persistence, ORM, and external integrations.

* **Interface Layer**
  Exposes REST APIs (Django REST Framework).

### Dependency Rule

```
Domain ← Application ← Infrastructure ← Interfaces
```

---

## Tech Stack

* Python 3.x
* Django
* Django REST Framework
* Pytest

---

## Domain Modeling

The domain is based on real-world Renewable Energy Community concepts:

* Member (consumer / producer / prosumer)
* Energy Asset (POD / plant)
* Energy Records (time-series data)
* Shared Energy (calculated per time slot)
* Incentives (economic redistribution)

Particular attention is given to **time-based aggregation** and **energy simultaneity**, which are critical in REC systems.

---

## Regulatory References

The domain logic and business rules are modeled according to official Italian and European regulations.

### Italian Authorities

* GSE (Gestore dei Servizi Energetici)
  https://www.gse.it/servizi-per-te/autoconsumo/comunita-energetiche-rinnovabili

* ARERA (Autorità di Regolazione per Energia Reti e Ambiente)
  https://www.arera.it/it/energia/comunita-energetiche.htm

### Key Documents

* GSE – Regole Operative per le Comunità Energetiche
* ARERA – Delibere sull’autoconsumo collettivo
* EU Directive 2018/2001 (RED II)

---

## Project Structure

```
cerberus/
├── domain/            # Core business logic
├── application/       # Use cases
├── infrastructure/    # ORM and external systems
├── interfaces/        # API layer
├── tests/             # Unit and integration tests
```

---

## Development Approach

The project follows a **test-first and domain-first approach**:

1. Model the domain
2. Write unit tests
3. Implement business logic
4. Add use cases
5. Integrate infrastructure
6. Expose APIs

---

## Current Status

* Architecture defined
* Initial domain modeling in progress

---

## Roadmap

* Domain modeling (members, energy, incentives)
* Application use cases
* Persistence layer implementation
* REST API
* Asynchronous processing (Celery)
* Monitoring and analytics

---

## Purpose

Cerberus is developed as an advanced backend engineering project to demonstrate:

* Domain-Driven Design in practice
* Clean Architecture implementation in Django
* Handling of complex, regulation-driven domains
* Scalable backend design for energy systems

---

## Author

Backend engineering project focused on advanced software architecture and domain modeling.
