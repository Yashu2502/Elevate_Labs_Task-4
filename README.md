# Elevate_Labs_Task-4

*Data Cleaning & Transformation*

***Data Issues Identified***

The raw dataset contained imperfections, inconsistencies, and missing values. The following 
steps were taken to clean and transform the data:

***Handled Missing Values:*** 

1)Missing Instructor, Class Type, Facility, and Theme values were replaced with 
"Unknown".

2)Missing Duration (mins) values were filled using the median duration.

3)Missing Customer Email and Customer Phone were replaced with "Not 
Provided". 

***Removed Duplicates:*** 

1)Identified and removed duplicate records based on Booking ID. 

***Data Type Corrections:***

1)Booking Date was converted to the correct date format. 

2)Price and Duration (mins) were converted to numeric values. 

***Fixed Inconsistencies in Categorical Data:***

1)Standardized values for Status and Booking Type (capitalization and spelling 
inconsistencies corrected).


**Key Insights & Visualizations** 

***Total Bookings and Revenue*** 

• Total Unique Bookings:  Displayed via KPI Card in Power BI. 

• Total Revenue Generated: Displayed via KPI Card in Power BI. 

***Booking Trends Over Time*** 

• A line chart was used to show the number of bookings per month, revealing seasonal 
trends and peak periods.

***Booking Type Distribution*** 

• A bar chart visualized the distribution of different booking types, identifying which 
services were most popular.

***Booking Status Breakdown*** 

• A pie chart was used to illustrate the percentage of completed, pending, and 
cancelled bookings. 

***Revenue Breakdown by Booking Type*** 

• A bar chart displayed revenue contributions by different booking types, highlighting 
the highest revenue-generating services. 


**Challenges & Solutions**

***Challenges Encountered***

****1. Incomplete Data:**** Many records had missing information. 

****Solution:**** Used placeholder values like "Unknown" and filled missing numeric 
values using the median. 

****2. Data Inconsistencies:**** Variations in status and booking type names. 

****Solution:**** Standardized text formats for consistency. 

****3. Outliers in Price & Duration:**** Some records contained unrealistic values.

****Solution:**** Removed negative and zero values from analysis.


**Conclusion** 
1)The majority of bookings were class-based reservations, followed by facility rentals. 

2)Revenue peaked in certain months, indicating seasonal trends.

3)A significant number of bookings were marked as pending or cancelled, suggesting 
potential areas for improvement in customer retention. 

4)The interactive dashboard allows for real-time filtering of data, giving deeper 
insights into different booking types and trends. 

