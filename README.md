# 📦 OneStop Electronics E-Commerce Analysis

## Company Background  
Established in 2018, **OneStop Electronics** is a global e-commerce retailer specializing in high-demand consumer electronics. The company has capitalized on growing international interest by focusing on online sales and digital customer engagement. Its product lineup features top-tier brands such as **Apple, Samsung, and Bose**.

Through targeted marketing strategies such as email campaigns and affiliate partnerships, OneStop Electronics aims to deliver in-demand products while maintaining a strong commitment to customer satisfaction.

---

## Project Goals  
OneStop Electronics has been collecting data across multiple domains, including:

- Orders and order status  
- Product details  
- Geographic information  

However, this raw data is largely unprocessed and underutilized, limiting its ability to support strategic decisions.

### Objective  
The objective of this project is to design and implement a **scalable data pipeline** to automate:

- Ingestion  
- Cleaning  
- Transformation  
- Validation  

This will enable reliable access to refined data for analysis and reporting.

### Specific Analytical Goals

- Identify overall sales trends from **2019 to 2022**  
- Calculate **yearly and monthly growth rates**  
- Evaluate the performance and future viability of the **loyalty program**  
- Determine the company’s **average order value (AOV)**  

---

## Table of Contents  
1. [Executive Summary](#executive-summary)  
2. [Data-Driven Insights](#data-driven-insights)  
   - [Historical Trends](#historical-trends)  
   - [Product Trends](#product-trends)  
   - [Regional Trends](#regional-trends)  
   - [Loyalty Program](#loyalty-program)  
   - [Refund Rates](#refund-rates)  
3. [Recommendations](#recommendations)  
4. [Dashboard](#dashboard)

---

## Executive Summary  
From **2019 to 2022**, OneStop Electronics generated over **$28 million in sales revenue**, processing more than **108,000 orders**. The **average order value (AOV)** across all years stands at **$260 per order**.

In **2020**, the company saw significant year-over-year growth, with:

- **Sales revenue** increasing from **$2M to $10M**  
- Substantial increases in order volume and engagement across all tracked metrics

**March 2020** had the highest growth rates, with a **50% growth rate in sales** and a **46% increase in number of orders**.

Following 2020, sales dropped tremendously, with revenue steadily decreasing month by month. OneStop Electronics experienced a decline in YoY growth with revenue dropping by **10% in 2021** and by **45% in 2022**. **October 2022** was the worst month, with a **55% decrease in revenue**.

The loyalty program, introduced in 2019, shows promising growth potential. While non-loyalty members initially outperformed loyalty members, trends reversed post-2020. Loyalty members now show stronger performance across sales, order volume, and AOV.

---

## Data-Driven Insights

### Historical Trends  

<p align="center">
  <img src="graphs/sales%20rev%202%20graph.png" style="width:600px;"/>
</p>

**Sales Revenue**  
- **Growth in 2020**: Peaked in December 2020 with **$1.25M**  
- **Decline post-2020**: Bottomed in October 2022 at **$178K (-55%)**

---

<p align="center">
  <img src="graphs/aov%202%20graphs.png" style="width:600px;"/>
</p>

**Average Order Value (AOV)**  
- **Average**: $253 per month  
- **Peak**: October 2020 – $322  
- **Lowest**: October 2022 – $216  

---

<p align="center">
  <img src="graphs/num%20of%20order%202%20graphs.png" style="width:600px;"/>
</p>

**Order Count**  
- **Average monthly orders**: 2,276  
- **Peak**: December 2020 – 4,019 orders (+29%)  
- **Lowest**: October 2022 – 825 orders (-46%)

---


### 🧾 Product Trends  
<img src="/graphs/Product%20Trends.png" style="width:600px;"/>

- **Top 3 Revenue Products**:  
  - 24in 4k Gaming Monitor – **$9.85M**  
  - Apple Airpod Headphones – **$7.74M**  
  - Macbook Air Laptop – **$6.30M**  
  ➤ Combined, they account for **84% of total sales**

- **Highest AOV Products**:  
  - Macbook Air Laptop – **$1,588**  
  - ThinkPad Laptop – **$1,100**  
  - Apple iPhone – **$741**

- **Most Ordered Products**:  
  - Apple Airpod Headphones – **48,396** orders  
  - 24in 4k Gaming Monitor – **23,406** orders  
  - Samsung Charging Cable – **21,916** orders

- **Weakest Product**:  
  - **Bose Soundsport**  
    - 27 orders  
    - $124 AOV  
    - $3K in total revenue  

---

### Regional Trends  
<img src="/graphs/customer%20demographic.png" style="width:600px;"/>

- **66%** of customers are from **North America**, contributing to **51%** of global sales  
- The **top 10 countries** account for **77%** of total sales:  
  US, UK, Canada, Japan, Germany, Australia, Brazil, France, Spain, Netherlands  
- **Highest AOV by Country**:  
  - Japan – **$393**  
  - Netherlands – **$289**  
  - Germany – **$270**  
- **Lowest AOV** among top 10:  
  - Spain – **$223**

---

### Loyalty Program  

- **2019**:  
  - Loyalty members – **$415K in revenue**, **$207 AOV**  
  - Non-members – **$3.4M revenue**, **$233 AOV**  

- **2020**:  
  - Loyalty members – **$3M**, **$228 AOV**  
  - Non-members – **$7.1M**, **$345 AOV**

- **Post-2020**:  
  - Loyalty member AOV overtook non-loyalty in **2022**  
  - Loyalty members now perform better across most KPIs  

---

### Refund Rates
<img src="/graphs/refund%20metric.png" style="width:600px;"/>

- **Highest Refund Rate**:  
  - Macbook Air Laptop & ThinkPad Laptop – **11%**  

- **Most Refunds by Order Volume**:  
  - 24in 4k Gaming Monitor – **1,445** refunded orders  
  - Apple Airpod Headphones – **2,636** refunded orders  

- **Most Refund Revenue Lost**:  
  - Macbook Air Laptop – **$746,365**  
  - 24in 4k Gaming Monitor – **$642,719**  

---

## Recommendations  

1. **Remove Bose Soundsport**: Underperforms in all metrics, does not justify continued listing.  
2. **Implement targeted promotions**:  
   - Use **seasonal discounts** on essentials (chargers, headphones)  
   - Offer **free shipping** to encourage conversions  
   - **Bundle high-AOV items** (Macbook, ThinkPad) with accessories using a **“Buy More, Save More”** model  
3. **Investigate refund drivers**:  
   - High refund rates for premium items suggest product issues or customer dissatisfaction  
   - Coordinate with product/QA teams to resolve

---

## Dashboard  
Explore the full interactive Tableau dashboard here:  
[OneStop Electronics Dashboard](https://public.tableau.com/app/profile/jonathan.dang5972/viz/OneStopElectronicsDashboard/SalesDashboard?publish=yes)

<img src="/graphs/dashboard.png" style="width:1000px;"/>


