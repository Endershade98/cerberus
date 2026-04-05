# Flowcharts Specification

This document defines the **minimal workflow representations** of the core business processes in the Cerberus system.

Each flowchart:

* uses standardized **status codes**
* represents **data flow end-to-end**
* includes **decision branches**
* is aligned with domain logic and state machines

---

# Legend

| Element   | Representation    |
| --------- | ----------------- |
| Process   | Rectangle         |
| Decision  | Diamond           |
| Status    | Inline label      |
| Start/End | Rounded rectangle |

---

# 1. Member Lifecycle Flow

## Overview

Describes how a member enters, gets validated, and interacts with the system.

---

## Flow

```
(Start)
   ↓
[Register Member]
Status: MEM-REG
   ↓
[Pending Approval]
Status: MEM-PENDING
   ↓
◇ Approved?
 ├── No → [Reject Member]
 │         Status: MEM-REJ
 │         ↓
 │        (End)
 │
 └── Yes
        ↓
   [Validate Member]
   Status: MEM-VALID
        ↓
   [Activate Member]
   Status: MEM-ACTIVE
        ↓
   ◇ Issue?
     ├── Yes → [Suspend Member]
     │         Status: MEM-SUSP
     │         ↓
     │      ◇ Recover?
     │        ├── Yes → MEM-ACTIVE
     │        └── No  → MEM-EXIT
     │
     └── No
           ↓
      [Continue Activity]
           ↓
      [Exit Community]
      Status: MEM-EXIT
           ↓
          (End)
```

---

# 2. Energy Processing Flow

## Overview

Represents the lifecycle of energy data from ingestion to shared energy calculation.

---

## Flow

```
(Start)
   ↓
[Receive Energy Data]
Status: ENG-REC-RCV
   ↓
[Validate Data]
Status: ENG-VAL-START
   ↓
◇ Valid?
 ├── No → [Reject Data]
 │         Status: ENG-VAL-ERR
 │         ↓
 │        (End)
 │
 └── Yes
        ↓
   [Validation Completed]
   Status: ENG-VAL-OK
        ↓
   [Aggregate Data]
   Status: ENG-AGG-START
        ↓
   [Aggregation Completed]
   Status: ENG-AGG-DONE
        ↓
   [Calculate Shared Energy]
   Status: ENG-CALC-START
        ↓
   [Shared Energy Calculated]
   Status: ENG-CALC-DONE
        ↓
   [Finalize Processing]
   Status: ENG-COMP
        ↓
      (End)
```

---

## Error Handling Branch

```
ANY STEP
   ↓
[Processing Error]
Status: ENG-FAIL
   ↓
[Retry or Abort]
   ↓
◇ Retry?
 ├── Yes → Return to previous step
 └── No  → (End)
```

---

# 3. Incentive Distribution Flow

## Overview

Describes how incentives are calculated and distributed among members.

---

## Flow

```
(Start)
   ↓
[Initialize Incentive]
Status: INC-INIT
   ↓
[Load Input Data]
Status: INC-DATA
   ↓
[Calculate Incentive]
Status: INC-CALC-START
   ↓
[Calculation Completed]
Status: INC-CALC-DONE
   ↓
[Allocate Incentives]
Status: INC-ALLOC-START
   ↓
[Allocation Completed]
Status: INC-ALLOC-DONE
   ↓
[Finalize]
Status: INC-COMP
   ↓
(End)
```

---

## Error Branch

```
ANY STEP
   ↓
[Failure]
Status: INC-FAIL
   ↓
[Retry / Abort]
```

---

# Data Flow Summary

## Member

```
Input → Register → Validate → Activate → Manage Lifecycle → Exit
```

---

## Energy

```
Input Data → Validation → Aggregation → Shared Energy Calculation → Finalization
```

---

## Incentives

```
Energy Results → Incentive Calculation → Allocation → Distribution
```

---

# Integration with Code

Each block in the flowcharts corresponds to:

* a **Use Case** (application layer)
* a **Status Code** (domain layer)
* optionally a **Domain Event**

Example:

```
[Validate Data]
Status: ENG-VAL-START
```

→ maps to:

* Use Case: `ValidateEnergyData`
* State: `EnergyStatus.VALIDATING`
* Event: `EnergyValidationStarted`

---

# Notes

* All flows must be implemented using **state machines**
* All transitions must be:

  * validated
  * logged (ProcessingStep)
* All statuses must match `tables.md`

---

# Purpose

These flowcharts serve as:

* a **blueprint for implementation**
* a **reference for developers**
* a **bridge between business and code**
