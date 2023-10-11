import pandas as pd
import os

# file_path = os.getenv('FILE_PATH')
# file_tran = os.getenv('FILE_TRAN')

# if file_path is None:
#     print("FILE_PATH not provided in the .env file.")
#     exit()

def transform_data (file_path, file_tran):

    try:
        # df = pd.read_csv(file_path, low_memory=False)
        df = pd.read_csv(os.path.join("..", file_path), low_memory=False)
        df['payGrade.externalCode'] = df['payGrade.externalCode'].fillna('NA')
        df['effectiveStartDate'] = pd.to_datetime(df['effectiveStartDate'], errors='coerce')
        df.dropna(subset=['effectiveStartDate'], inplace=True) # drops the rows where date conversion failed
        df.sort_values(by=['code', 'effectiveStartDate'], ascending=[True, False], inplace=True)
        df['effectiveStartDate'] = df['effectiveStartDate'].dt.strftime('%m/%d/%Y')
        result = df.groupby('code').first().reset_index()
        headers = [
                    'Supported operators: Delimit, Clear and Delete',
                    'Position Code',
                    'Default Value',
                    'English (United Kingdom)',
                    'Thai (Thailand)',
                    'Vietnamese (Vietnam)',
                    'Status(Valid Values : A/I   A for Active  I for Inactive  )',
                    'Start Date',
                    'Comment',
                    'Picklist Value.External Code',
                    'Picklist Value.External Code',
                    'Description',
                    'Job Classification .Job Code',
                    'Job Name',
                    'Picklist Value.External Code',
                    'payGrade.externalCode',
                    'FTE',
                    'Vacant(Valid Values : TRUE/FALSE)',
                    'Company.Company Code',
                    'Function.Function Code',
                    'Business Unit.Business Unit Code',
                    'Cost Center.Cost Center Code',
                    'Organization.Organization Code',
                    'location.externalCode',
                    'Multiple Incumbents Allowed(Valid Values : TRUE/FALSE)',
                    'Position Controlled(Valid Values : TRUE/FALSE)',
                    'Standard Weekly Hours',
                    'Work Location.Location ID',
                    'Picklist Value.External Code',
                    'locationGroup.externalCode',
                    'Policy Profile.Code',
                    'Group.Group Code',
                    'Job Family / Sub-Family.Job Family Code',
                    'Work Schedule.External Code',
                    'Daily Working Hours',
                    'Working Days per Week',
                    'Picklist Value.External Code',
                    'Zone.Code',
                    'Brand.Brand Code',
                    'HR District.HR District Code',
                    'Position.Parent Position (solid)',
                ]
        df1 = pd.DataFrame([headers], columns=df.columns)
        
        df2 = pd.concat([df1, result],ignore_index=True)
        print(df2.head())
        
        if df2.iloc[-1, 1] == 'Position Code':
            df2.drop(df2.tail(1).index, inplace=True)

        print(df2.head())
        
        # df2.to_csv(file_tran, index=False, encoding='utf8')
        df2.to_csv(file_tran , index=False, encoding='utf-8-sig')
    except Exception as e:
        print(f"An error occurred: {e}")
