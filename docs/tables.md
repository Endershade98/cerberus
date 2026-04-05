# Tables

This document defines the **canonical status codes, transitions, and workflow semantics** used across the Cerberus system.

All codes are designed to be:

* machine-readable
* human-readable
* traceable across logs, workflows, and diagrams

---

# Global Status

Generic statuses reusable across multiple domains.

| Code        | Label       | Description                      |
| ----------- | ----------- | -------------------------------- |
| GEN-INIT    | Initialized | Object created but not processed |
| GEN-PENDING | Pending     | Waiting for processing           |
| GEN-PROC    | Processing  | Currently in execution           |
| GEN-COMP    | Completed   | Successfully completed           |
| GEN-FAIL    | Failed      | Generic failure                  |
| GEN-RETRY   | Retry       | Scheduled for retry              |
| GEN-CANCEL  | Cancelled   | Process cancelled                |

---

# Energy Processing Status

Represents the lifecycle of energy data processing aligned with GSE rules.

| Code           | Label                    | Description                       |
| -------------- | ------------------------ | --------------------------------- |
| ENG-REC-RCV    | Data Received            | Raw energy data received          |
| ENG-VAL-START  | Validation Started       | Validation in progress            |
| ENG-VAL-OK     | Validated                | Data is valid                     |
| ENG-VAL-ERR    | Validation Failed        | Data is invalid                   |
| ENG-AGG-START  | Aggregation Started      | Aggregation in progress           |
| ENG-AGG-DONE   | Aggregated               | Data aggregated per timeslot      |
| ENG-CALC-START | Calculation Started      | Shared energy calculation started |
| ENG-CALC-DONE  | Shared Energy Calculated | Shared energy computed            |
| ENG-COMP       | Completed                | Full process completed            |
| ENG-FAIL       | Processing Failed        | Error during processing           |

---

# Energy Processing Phases

Logical grouping of energy processing steps.

| Phase        | Codes               |
| ------------ | ------------------- |
| RECEIVING    | ENG-REC-RCV         |
| VALIDATION   | ENG-VAL-*           |
| AGGREGATION  | ENG-AGG-*           |
| CALCULATION  | ENG-CALC-*          |
| FINALIZATION | ENG-COMP / ENG-FAIL |

---

# Incentive Status

Represents the lifecycle of incentive calculation and distribution.

| Code            | Label               | Description                   |
| --------------- | ------------------- | ----------------------------- |
| INC-INIT        | Initialized         | Incentive created             |
| INC-DATA        | Data Loaded         | Input data collected          |
| INC-CALC-START  | Calculation Started | Incentive calculation running |
| INC-CALC-DONE   | Calculated          | Total incentive computed      |
| INC-ALLOC-START | Allocation Started  | Distribution process started  |
| INC-ALLOC-DONE  | Allocated           | Allocation completed          |
| INC-COMP        | Completed           | Fully processed               |
| INC-FAIL        | Failed              | Error occurred                |

---

# Member Lifecycle Status

Represents the lifecycle of a community member.

| Code        | Label            | Description            |
| ----------- | ---------------- | ---------------------- |
| MEM-REG     | Registered       | Member created         |
| MEM-PENDING | Pending Approval | Awaiting validation    |
| MEM-VALID   | Validated        | Requirements satisfied |
| MEM-ACTIVE  | Active           | Fully active member    |
| MEM-SUSP    | Suspended        | Temporarily disabled   |
| MEM-REJ     | Rejected         | Registration rejected  |
| MEM-EXIT    | Exited           | Left the community     |

---

# Energy Transition Rules

Defines allowed transitions between energy processing states.

| From           | To             | Condition             |
| -------------- | -------------- | --------------------- |
| ENG-REC-RCV    | ENG-VAL-START  | Data received         |
| ENG-VAL-START  | ENG-VAL-OK     | Valid data            |
| ENG-VAL-START  | ENG-VAL-ERR    | Invalid data          |
| ENG-VAL-OK     | ENG-AGG-START  | Validation success    |
| ENG-AGG-START  | ENG-AGG-DONE   | Aggregation complete  |
| ENG-AGG-DONE   | ENG-CALC-START | Ready for calculation |
| ENG-CALC-START | ENG-CALC-DONE  | Calculation done      |
| ENG-CALC-DONE  | ENG-COMP       | Success               |
| ANY            | ENG-FAIL       | Error                 |

---

# Processing Tracking Tables

## ProcessingJob

Represents a full processing workflow instance.

| Field        | Description         |
| ------------ | ------------------- |
| id           | Job ID              |
| type         | ENERGY / INCENTIVE  |
| status       | Current status code |
| started_at   | Start time          |
| completed_at | End time            |

---

## ProcessingStep

Represents a single step in a workflow.

| Field         | Description                      |
| ------------- | -------------------------------- |
| id            | Step ID                          |
| job_id        | Reference to job                 |
| step_code     | Status code (e.g. ENG-VAL-START) |
| status        | SUCCESS / FAILED                 |
| timestamp     | Execution time                   |
| error_message | Optional error details           |

---

# Diagram Legend (Miro / UML)

| Element  | Representation    |
| -------- | ----------------- |
| Process  | Rectangle (blue)  |
| Event    | Circle (orange)   |
| Status   | Label under shape |
| Decision | Diamond           |
| Database | Gray cylinder     |

---

# Testing Strategy

Defines how tests are distributed across layers.

| Layer          | Test Type              |
| -------------- | ---------------------- |
| domain         | Unit tests (no Django) |
| application    | Unit + integration     |
| infrastructure | Integration tests      |
| interfaces     | End-to-end tests       |

---

# Notes

* All status codes must be used consistently across:

  * Domain logic
  * Logs
  * Database
  * Flowcharts

* Status transitions should always be validated through state machines.
