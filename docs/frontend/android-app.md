# CERBERUS - Mobile App (React Native / Android)

## 1. Purpose

The Cerberus Mobile App is the **field companion application** for members of a Renewable Energy Community (CER / REC).

It is designed for:

- End users (members of the energy community)
- Light operational monitoring
- Energy awareness and consumption tracking
- Incentive visibility

The app is NOT an admin tool. It is a **consumer-grade energy insight application**, similar in spirit to:

- Tibber Mobile App
- Octopus Energy App
- Enel X Way Mobile Experience
- Sonnen App

---

## 2. Architectural Principles

### 2.1 Mobile-First Design

The mobile app is optimized for:

- Quick interactions
- Low cognitive load
- High-frequency energy checks
- Simple navigation

---

### 2.2 Backend-Driven Architecture

The app is a thin client:

- No business logic
- No domain rules
- No state derivation logic

All logic lives in backend services.

---

### 2.3 Microservice Integration

The app consumes APIs from:

- Member Service
- Energy Service
- Incentive Service

Future integrations:

- Notification Service (push)
- Identity Service (auth)
- Real-time Energy Service (WebSocket)

---

## 3. Technology Stack

- React Native (latest stable)
- TypeScript
- React Navigation
- React Query (server state)
- Zustand (light UI state only)
- Axios (API client)
- Expo (optional, recommended for speed)

---

## 4. Project Structure

```text
mobile-app/
├── src/
│   ├── app/
│   │   ├── App.tsx
│   │   └── providers/
│   │
│   ├── features/
│   │   ├── auth/
│   │   ├── dashboard/
│   │   ├── energy/
│   │   ├── incentives/
│   │   └── profile/
│   │
│   ├── shared/
│   │   ├── api/
│   │   ├── components/
│   │   ├── hooks/
│   │   ├── utils/
│   │   └── types/
│   │
│   ├── navigation/
│   │   ├── AppNavigator.tsx
│   │   ├── AuthNavigator.tsx
│   │   └── TabNavigator.tsx
│   │
│   ├── theme/
│   │   ├── colors.ts
│   │   ├── spacing.ts
│   │   └── typography.ts
│   │
│   └── services/
│       ├── storage.ts
│       └── secureStorage.ts
````

---

## 5. Core Modules

### 5.1 Dashboard Module

#### Purpose

Provide a quick overview of user energy behavior.

#### Features

* Daily energy consumption summary
* Weekly trends
* Incentive snapshot
* Personal KPIs

#### UI Components

* KPI cards
* Simple charts
* Progress indicators

---

### 5.2 Energy Module

#### Purpose

Allow users to view their consumption and production.

#### Features

* Daily / weekly / monthly consumption
* Historical charts
* Comparison trends

#### Screens

* Energy overview
* Energy detail view

---

### 5.3 Incentives Module

#### Purpose

Show financial/energy incentives earned.

#### Features

* Total incentives earned
* Monthly breakdown
* Historical list

#### Screens

* Incentive summary
* Incentive history

---

### 5.4 Profile Module

#### Purpose

User identity and membership info.

#### Features

* Member status
* Personal data
* CER participation details

---

## 6. Navigation Structure

### Tab Navigation

```text
Dashboard
Energy
Incentives
Profile
```

### Flow Navigation

* Auth flow (login/register)
* Main app (tabs)
* Detail screens

---

## 7. API Layer

### 7.1 Structure

```text
shared/api/
```

### 7.2 Example

```ts id="api-example"
import { httpClient } from "./httpClient";

export const getEnergySummary = async (memberId: string) => {
  const response = await httpClient.get(
    `/api/energy/summary/?member_id=${memberId}`
  );
  return response.data;
};
```

---

## 8. State Management Rules

### 8.1 Server State

Use React Query ONLY:

* caching
* synchronization
* fetching

---

### 8.2 UI State

Use Zustand ONLY for:

* modal states
* navigation UI states
* local toggles

---

### 8.3 Forbidden

* Redux
* Business logic in frontend
* Derived backend state

---

## 9. UX Design Principles

### 9.1 Design Style

Inspired by energy consumer apps:

* Tibber-like minimalism
* Enel X clarity
* Octopus Energy simplicity

---

### 9.2 UI Characteristics

* Mobile-first cards
* Large numeric KPIs
* Simple charts
* Bottom tab navigation

---

### 9.3 Interaction Patterns

* Swipe navigation (future)
* Pull-to-refresh
* Skeleton loading
* Toast notifications

---

## 10. Authentication (External)

The app does NOT implement authentication logic.

Expected external system:

* Identity Microservice (JWT-based)
* Token stored securely (SecureStore / Keychain)

Future:

* OAuth2 / Keycloak integration
* Biometric login (optional)

---

## 11. Offline Strategy (Future)

Planned improvements:

* Cached last state (React Query persistence)
* Offline energy view
* Sync on reconnect

---

## 12. Real-Time Features (Future)

* Push notifications (energy alerts, incentives)
* WebSocket live updates
* Live consumption tracking

---

## 13. Deployment

### Android

* Build via Gradle / Expo EAS
* APK / AAB distribution

### iOS (future)

* App Store release pipeline

---

## 14. Performance Requirements

* App launch < 2 seconds
* Smooth 60 FPS navigation
* Lazy loaded screens
* Minimal API payloads

---

## 15. Testing Strategy

### Unit Tests

* Components
* Hooks
* Utilities

---

### Integration Tests

* Feature flows
* API mocking

---

### E2E Tests (future)

* Detox (React Native)
* Full user journey

---

## 16. Domain Consistency Rule

Mobile app MUST reflect backend truth:

* Member status must match backend
* Energy data is read-only
* Incentives are computed server-side

No local computation allowed.

---

## 17. Long-Term Evolution

### Phase 1

* Basic dashboards
* Energy + incentives view
* API integration

### Phase 2

* Push notifications
* Real-time updates
* Improved charts

### Phase 3

* Smart insights (backend-driven)
* Predictive consumption
* Multi-CER support

---

## 18. Strategic Goal

The mobile app represents the **end-user layer of Cerberus ecosystem**, designed to:

* Increase energy awareness
* Encourage participation in CER communities
* Provide transparent incentive visibility

It must feel like a **real European energy utility app**, not a prototype.

