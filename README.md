# Serverless Trading Bot – AWS Architecture (README Summary)

## Overview
This project implements an **event‑driven, fully serverless trading bot** on AWS.  
Incoming strategy requests are processed, market data is fetched from Yahoo Finance, trading rules are evaluated, and orders are executed and logged—​all without managing servers.

## High‑Level Flow
1. **User → API Gateway** – HTTPS endpoint receives JSON payload (ticker, timeframe, indicators).  
2. **Lambda Trading Set Up** – Parses request, stores config, schedules periodic triggers in **CloudWatch Events**.  
3. **CloudWatch Events** – Fires on the defined schedule.  
4. **Lambda Hook Data** – Pulls latest market prices from Yahoo Finance.  
5. **Lambda Trading Rule** – Applies indicators (RSI, EMA, CCI, …) to generate buy/sell signals.  
6. **Lambda Order Core** – Places orders (or simulates), persists results to **Amazon RDS**.  
7. **SES/SNS Email** – Sends trade confirmation to the user.

## AWS Services Used
| Layer                | Service(s)              | Purpose                                  |
|----------------------|-------------------------|------------------------------------------|
| API Integration      | Amazon API Gateway      | Public REST endpoint                     |
| Compute              | AWS Lambda × 4          | Stateless business logic                 |
| Scheduling           | Amazon CloudWatch Events| Cron/Rate triggers                       |
| Data Source          | Yahoo Finance API       | Market prices                            |
| Persistence          | Amazon RDS              | Order & signal history                   |
| Notifications        | Amazon SES / SNS        | Email alerts                             |

## Key Benefits
* **Scalable & cost‑efficient** – Pay only per execution; auto‑scales with load.  
* **Event‑driven** – Clean separation between data fetch, rule evaluation, and order execution.  
* **Managed services** – No servers to patch; high availability out of the box.  
* **Audit‑ready** – All trades and signals stored in RDS for later analysis.

---
*Feel free to adapt table names, indicator logic, or notification channels to suit your trading requirements.*
