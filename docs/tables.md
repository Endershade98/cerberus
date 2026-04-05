# Tables

## Global Status
```
Code           | Label                     | Description
----------------------------------------------------------------------
GEN-INIT       | Initialized               | Object created but not processed
GEN-PENDING    | Pending                   | Waiting for processing
GEN-PROC       | Processing                | Currently in execution
GEN-COMP       | Completed                 | Successfully completed
GEN-FAIL       | Failed                    | Generic failure
GEN-RETRY      | Retry                     | Scheduled for retry
GEN-CANCEL     | Cancelled                 | Process cancelled

```
## Energy Status 
```
Code           | Label                     | Description
----------------------------------------------------------------------
ENG-REC-RCV    | Data Received             | Raw energy data received
ENG-VAL-START  | Validation Started        | Validation in progress
ENG-VAL-OK     | Validated                 | Data is valid
ENG-VAL-ERR    | Validation Failed         | Data is invalid
ENG-AGG-START  | Aggregation Started       | Aggregation in progress
ENG-AGG-DONE   | Aggregated                | Data aggregated per timeslot
ENG-CALC-START | Calculation Started       | Shared energy calculation started
ENG-CALC-DONE  | Shared Energy Calculated  | Shared energy computed
ENG-COMP       | Completed                 | Full process completed
ENG-FAIL       | Processing Failed         | Error during processing

```
## Fasi
```
Phase          | Codes
----------------------------------------
RECEIVING      | ENG-REC-RCV
VALIDATION     | ENG-VAL-*
AGGREGATION    | ENG-AGG-*
CALCULATION    | ENG-CALC-*
FINALIZATION   | ENG-COMP / ENG-FAIL
```
## Incentive Stauts
```
Code           | Label                        | Description
----------------------------------------------------------------------
INC-INIT       | Initialized                  | Incentive created
INC-DATA       | Data Loaded                  | Input data collected
INC-CALC-START | Calculation Started          | Incentive calculation running
INC-CALC-DONE  | Calculated                   | Total incentive computed
INC-ALLOC-START| Allocation Started           | Distribution process started
INC-ALLOC-DONE | Allocated                    | Allocation completed
INC-COMP       | Completed                    | Fully processed
INC-FAIL       | Failed                       | Error occurred
```
## Member Status
```
Code           | Label              | Description
----------------------------------------------------------------------
MEM-REG        | Registered         | Member created
MEM-PENDING    | Pending Approval   | Awaiting validation
MEM-VALID      | Validated          | Requirements satisfied
MEM-ACTIVE     | Active             | Fully active member
MEM-SUSP       | Suspended          | Temporarily disabled
MEM-REJ        | Rejected           | Registration rejected
MEM-EXIT       | Exited             | Left the community
```

## Energy Transition
```
From            → To                | Condition
-------------------------------------------------------------
ENG-REC-RCV     → ENG-VAL-START     | Data received
ENG-VAL-START   → ENG-VAL-OK        | Valid data
ENG-VAL-START   → ENG-VAL-ERR       | Invalid data
ENG-VAL-OK      → ENG-AGG-START     | Validation success
ENG-AGG-START   → ENG-AGG-DONE      | Aggregation complete
ENG-AGG-DONE    → ENG-CALC-START    | Ready for calculation
ENG-CALC-START  → ENG-CALC-DONE     | Calculation done
ENG-CALC-DONE   → ENG-COMP          | Success
ANY             → ENG-FAIL          | Error
```

## Step Processing Tables
### ProcessingStep
```
Field              | Description
----------------------------------------
id                 | Step ID
job_id             | Reference to job
step_code          | ENG-VAL-START
status             | SUCCESS / FAILED
timestamp          | When executed
error_message      | Optional error
```
### ProcessingJob
```
Field              | Description
----------------------------------------
id                 | Job ID
type               | ENERGY / INCENTIVE
status             | Current status code
started_at         | Start time
completed_at       | End time
```

## Shapes and Codes
```
Element            | Representation
--------------------------------------------------
Process            | Rectangle (blue)
Event              | Circle (orange)
Status             | Small label under shape
Decision           | Diamond
Database           | Gray cylinder
```
## Tests Strategy
```
Layer          | Tipo test
--------------------------------------
domain         | unit (NO Django)
application    | unit + integration
infrastructure | integration
interfaces     | e2e
```