# Decision Support System (DSS) for Selecting Small Satellite Launch Vehicle Provider
## Table of Contents
1. Introduction
2. Scope
3. Methodology
4. Understanding the Design Attributes and Alternatives
5. DSS Development Strategy
6. Results and Use
7. Overall Utility of the Results
8. Limitations
9. Conclusion
### Introduction
The provided document outlines a comprehensive research paper titled "DSS for Selecting Small Satellite Launch Vehicle Provider." Small satellites, also known as SmallSats, play a crucial role in various applications, including education, scientific research, Earth observation, communication, and navigation. The document emphasizes the importance of selecting an appropriate launch provider, considering factors such as cost, reliability, and sustainability.
### Scope
The Decision Support System (DSS) discussed in the paper serves as a tool to facilitate an informed decision-making process during the selection of a small satellite launch vehicle provider. The system aims to ensure the best fit between mission requirements and launch provider capabilities. Key aspects of the DSS scope include:
1.Data Collection and Integration
2.Criteria and Scoring System
3.User Interface Design and Development
4.Simulation and Optimization
5.Recommendation Engine
### Methodology
The methodology section details the step-by-step approach taken in developing the DSS:

Data Collection and Integration:

Gather data on available small satellite launch providers, including launch history, cost, reliability, and technical capabilities.
Integrate data into the DSS for analysis.
Criteria and Scoring System:

Develop a comprehensive set of criteria for evaluating launch providers (e.g., launch cost, payload capacity, launch success rate).
Create a scoring system for objective comparison.
User Interface Design and Development:

Design an intuitive user interface accessible to various stakeholders.
Ensure usability for multiple users, including satellite operators, mission planners, and project managers.
Simulation and Optimization:

Implement simulation algorithms for exploring different scenarios.
Optimize launch provider selection based on specific mission requirements and budget constraints using Monte Carlo simulation.
Recommendation Engine:

Develop a recommendation engine suggesting the most suitable launch providers based on user inputs and preferences.
### Understanding the Design Attributes and Alternatives
The section provides an overview of the dataset used, including information on various space launch vehicles. Key statistics are summarized, covering vehicle names, countries of origin, payload capacities, prices, reliability, and launch frequencies.

### DSS Development Strategy
-This section outlines the structure of the DSS development:
 Data Loading: Reads data from an Excel file into a DataFrame.
 Data Cleaning: Converts specific columns to numeric types, handling non-numeric values as errors.
 User Inputs: Prompts the user for satellite mass, preferred launch country, and orbit type.
 Data Compiling: Compiles the DataFrame based on user inputs.
 Launcher Selection Logic: Implements a Multi-Attribute Utility Theory (MAU) approach.
-Defines utility functions for attributes like price, reliability, and frequency.
-Calculates a combined utility score (MAU value) for each launcher.
-Selects the launcher with the highest MAU value.
-Risk Analysis: Performs risk analysis based on launcher reliability.
 Categorizes risk into 'Low,' 'Medium,' and 'High.'
-Results and Use: Provides launcher recommendations based on user criteria and risk assessments.
The results section is divided into two main components:

-Launcher Recommendation
Recommends the best launcher based on user input (satellite mass, preferred country, and orbit type).
Calculates Multi-Attribute Utility (MAU) values for each launcher.
Outputs the recommended launcher with the highest MAU value.
-Risk Assessment
Analyzes reliability-based risk for each launcher.
Categorizes risk into 'Low,' 'Medium,' or 'High.'
Provides risk assessment output for each launcher option.
### Overall Utility of the Results
The results of the DSS aim to enhance decision-making by providing users with:

-Decision Making:

Comprehensive view for more informed decisions.
Customization:

Tailored calculations based on user inputs and priorities.
-Insightful Analysis:

Deeper insights into strengths and weaknesses of launcher options.
Limitations
The README acknowledges certain limitations:

-Data Dependency:

Accuracy and relevance of results depend on data quality and timeliness.
-Model Assumptions: Utility functions and risk categorization are based on assumptions.
-User Knowledge: Users need a certain understanding of attributes for full appreciation.

### Conclusion
The development of a Decision Support System for selecting small satellite launch vehicle providers is crucial for enhancing the efficiency and effectiveness of satellite missions. The outlined project proposal emphasizes the objectives, methodology, and user-friendly features of the DSS, empowering users to make informed decisions while considering various criteria and constraints, ultimately leading to successful satellite missions and cost optimization.

#### Contributors
This project was made possible by the contributions of the following individuals:
Evangelia Gkaravela & Vivek Mansukhbhai Padsala
