#get_gentrification_severity(!median_household_income!, !change_dwl!, !change_edu!):

#! Gentrification Measures:
#? Census Tract was deemed “Gentrifiable” (1) if 
    # Median Household income below MTL

#? Census Tract was deemed “Gentrified” (2) if all of the following are true
    # Meets the Gentrifiable Criteria
    # CT Median home value Increase > MTL Median home value increase
    # CT Proportion of university-educated residents increase > MTL Proportion of university-educated residents increase

#? Else, Non-Gentrifiable (0)

#! Has measure of “Gentrification Severity”
    # The Increase in housing values (YearA → YearB) for a Gentrified Census Tract is … 
    
# Weak (2) if the increase is <= the 25th percentile
# Moderate (3) if the increase is = the 25th - 75th percentile
# Intense (4) if increase is above the 75th percentile.





import arcpy
import statistics

input_data = "CT_2011_change"
median_household_income = "median_household_income"
median_value_dwellings_NEW = "median_value_dwellings"
median_value_dwellings_OLD = "average_value_dwellings_2006"
education_NEW = "education"
education_OLD = "education_2006"
population_NEW = "population"
population_OLD = "population_2006"

CHANGE_DWL = "change_dwl"

#! Calculates total MTL median
def get_mtl_median_income():
    values = []
    with arcpy.da.SearchCursor(input_data, [median_household_income]) as cursor:
        for row in cursor:
            if row[0] is not None:
                values.append(row[0])

    return statistics.median(values)
mtl_median_income = get_mtl_median_income()

#! Calculates total MTL total Median Value of Dwellings
def mtl_dwl_new():
    values = []
    with arcpy.da.SearchCursor(input_data, [median_value_dwellings_NEW]) as cursor:
        for row in cursor:
            if row[0] is not None:
                values.append(row[0])
    return statistics.median(values)
def mtl_dwl_old():
    values = []
    with arcpy.da.SearchCursor(input_data, [median_value_dwellings_OLD]) as cursor:
        for row in cursor:
            if row[0] is not None:
                values.append(row[0])
    return statistics.median(values)
mtl_change_dwl = (mtl_dwl_new() - mtl_dwl_old())/mtl_dwl_old()

#! Calculates total MTL change for education
def get_edu_proportion(edu_field, pop_field):
    edu_total = 0
    pop_total = 0
    with arcpy.da.SearchCursor(input_data, [edu_field, pop_field]) as cursor:
        for row in cursor:
            if row[0] is not None and row[1] is not None and row[1] != 0:
                edu_total += row[0]
                pop_total += row[1]
    return edu_total / pop_total if pop_total > 0 else 0
mtl_edu_old = get_edu_proportion(education_OLD, population_OLD)
mtl_edu_new = get_edu_proportion(education_NEW, population_NEW)
mtl_change_edu = (mtl_edu_new - mtl_edu_old)/mtl_edu_old if mtl_edu_old > 0 else 0


#! 25th, 75th percentile of CT-level dwelling change
def get_change_dwl_percentiles():
    values = []
    with arcpy.da.SearchCursor(input_data, [CHANGE_DWL]) as cursor:
        for row in cursor:
            if row[0] is not None:
                values.append(row[0])
    q = statistics.quantiles(values, n=4)
    return q[0], q[2] # 25th and 75th percentiles
p25, p75 = get_change_dwl_percentiles()


#! MAIN FUNCTIN
def get_gentrification_severity(income, change_dwl, change_edu):
    if income >= mtl_median_income:
        return 0 # Non-Gentrifiable
    
    
    if not (change_dwl > mtl_change_dwl and change_edu > mtl_change_edu):
        return 1 # Gentrifiable
    
    if change_dwl <= p25:
        return 2 # Weak
    elif change_dwl <= p75:
        return 3 # Moderate
    else:
        return 4 # Intense
