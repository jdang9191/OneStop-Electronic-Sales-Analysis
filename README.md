# 📦 OneStop Electronics E-commerce Analysis

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

---

## Executive Summary  
From **2019 to 2022**, OneStop Electronics generated over **$28 million in sales revenue**, processing more than **108,000 orders**. The **average order value (AOV)** across all years stands at **$260 per order**.

In **2020**, the company saw significant year-over-year growth, with:

- **Sales revenue** increasing from **$2M to $10M**  
- Substantial increases in order volume and engagement across all tracked metrics

March 2020 had the highest growth rates, with a 50% growth rate in sales and 46% increase in number of orders.

Following 2020, sales dropped tremendously, with revenue steadily decreasing month by month. OneStop Electronics experienced a decline in YoY (Year over Year) growth with revenue dropping by 10% in 2021 and decreasing even further to 45% the following year. October 2022 was the worst month with a 55% decrease in revenue.

The loyalty program, first introduced in 2019, shows room for promising growth. While customers not in the loyalty program initially outperformed loyalty members in sales, trends started to reverse in recent years. Through further improvement and optimization of the loyalty program, sales, number of orders, and AOV could increase and drive future growth.

---

## Data-Driven Insights

### Historical Trends

**Sales Revenue**  
/graphs/sales rev 2 graph.png 
- Growth in 2020: Sales revenue steadily increased until it peaked in December 2020, generating $1.25M in sales revenue in that month alone.  
- Post 2020: Following 2020, sales revenue started steadily decreasing, with the lowest drop occurring in October 2022 (-55%) with sales revenue of $178K.

**AOV**  
/graphs/aov 2 graphs.png 
- Average AOV: AOV on average was $253 per month.  
- Peak AOV: October 2020 with an AOV of $322  
- Lowest AOV: October 2022 with an AOV of $216

**Order Count**  
/graphs/num of orders 2 graphs.png 
- Average order count per month was 2,276 orders  
- Peak order count: December 2020 (29%) with 4,019 orders  
- Lowest order count: October 2022 (-46%) with 825 orders

---

### Product Trends
/graphs/Product Trends.png 
- The three products that generated the most sales revenue are:  
  - **24in 4k Gaming Monitor**: $9,850,744  
  - **Apple Airpod Headphones**: $7,739,617  
  - **Macbook Air Laptop**: $6,295,309  
  - ➤ Combined, they account for **84% of total sales**

- **AOV by Product**:  
  - **Macbook Air Laptop**: $1,588 (highest)  
  - **ThinkPad Laptop**: $1,100  
  - **Apple iPhone**: $741

- **Most Ordered Products**:  
  - **Apple Airpod Headphones**: 48,396 orders  
  - **24in 4k Gaming Monitor**: 23,406 orders  
  - **Samsung Charging Cable**: 21,916 orders

- **Weakest Product**:  
  - **Bose Soundsport**:  
    - 27 orders  
    - $124 AOV  
    - $3K in total sales revenue  
    - Underperforms in all key metrics

---

## Regional Trends
/graphs/customer demographic.png 
Most customers come from North America, **66%** of customers are from North America and account for **51%** of total sales.
The top 10 countries in sales revenue account for approximately **77%** of sales. Ranked by sales revenue, these countries are the United States, United Kingdom, Canada, Japan, Germany, Australia, Brazil, France, Spain, and the Netherlands.
From these top 10 countries, Japan leads with the highest AOV (**$393**), followed by the Netherlands (**$289**) and Germany (**$270**). Spain has the lowest AOV (**$223**) of these 10 countries.

## Loyalty Program
Initially, customers not in the loyalty program outperformed loyalty members in sales by a wide margin. In 2019, loyalty members generated a mere **$415k $207 AOV** in sales revenue compared to **$3.4M $233 AOV** from members not in the loyalty program. Additionally, in 2020, loyalty members generated approximately **$3M $228 AOV** in 2020 while customers not in the loyalty program generated **$7.1M $345 AOV**. 

However, trends have started to reverse following 2020, with the loyalty program doing better in all metrics compared to non-loyalty members. Loyalty member AOV has steadily risen and overtook non-loyalty AOV in 2022. 

## Refund Rates
/graphs/refund metric.png 
Macbook Air Laptop and Thinkpad Laptop lead the product lineup with an **11%** refund rate.
24in 4k Gaming Monitor (**1445**) and Apple Airpod Headphones (**2636**) had the most number of orders refunded.
Macbook Air Laptop (**$746,365**) and 24in 4k Gaming Monitor (**642,719**) had the highest amount of revenue from sales refunded.

## Recommendations
Based on the following analysis and insights, the following is suggested.

1. Remove Bose Soundsport from the product lineup. It does not generate enough sales and has performed poorly every year in every metric.
2. Implement discounts and promotions in months where metrics are down. Consider seasonal promotions such as:
      Discounting essentials (chargers, headphones, etc.) and using free shipping to boost order volume
      Incentivizing high-AOV purchases (Macbook Air Laptop, Thinkpad Laptop) by using bundled discounts with items like webcams and monitors. Use a "Buy More, Save More" strategy to increase AOV.
3. Investigate with the product team to determine why refund rates for the highest-AOV items(Macbook and Lenovo) are so high.

## Dashboard
To explore more trends use the interactive Tableau Dashboard here(embed link). (https://public.tableau.com/app/profile/jonathan.dang5972/viz/OneStopElectronicsDashboard/SalesDashboard?publish=yes)
insert image of dashboard
