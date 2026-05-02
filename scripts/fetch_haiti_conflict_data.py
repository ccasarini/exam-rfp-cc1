import requests
import os
import pandas as pd

def fetch_ucdp_haiti_data():
    """
    Fetches the UCDP GED dataset for Haiti from HDX by querying the HDX API.
    """
    hdx_api_url = "https://data.humdata.org/api/3/action/package_show?id=ucdp-data-for-haiti"
    output_path = "data/haiti_ucdp_conflict.csv"
    
    print(f"Querying HDX API for the latest UCDP Haiti data...")
    
    try:
        # Step 1: Get the package info from HDX
        response = requests.get(hdx_api_url)
        response.raise_for_status()
        package_info = response.json()
        
        if not package_info['success']:
            print("HDX API request failed.")
            return False
            
        # Step 2: Find the CSV resource
        resources = package_info['result']['resources']
        csv_url = None
        for resource in resources:
            if resource['format'].lower() == 'csv':
                csv_url = resource['url']
                break
        
        if not csv_url:
            print("Could not find a CSV resource in the HDX package.")
            return False
            
        print(f"Downloading from: {csv_url}")
        
        # Step 3: Download the file
        file_response = requests.get(csv_url)
        file_response.raise_for_status()
        
        os.makedirs("data", exist_ok=True)
        with open(output_path, "wb") as f:
            f.write(file_response.content)
            
        print(f"Successfully saved to {output_path}")
        
        # Validation
        df = pd.read_csv(output_path)
        # Filter out HXL tags (the first row often contains # tags in HDX data)
        first_cell = str(df.iloc[0, 0])
        if first_cell.startswith("#"):
            df = df.iloc[1:].reset_index(drop=True)
            df.to_csv(output_path, index=False)
            
        print(f"Loaded {len(df)} conflict events from UCDP.")
        return True
    except Exception as e:
        print(f"Error fetching UCDP data: {e}")
        return False

def fetch_acled_haiti_data(email, api_key):
    """
    Fetches the ACLED dataset for Haiti using their API.
    Requires an API Key and Email.
    """
    url = "https://api.acleddata.com/acled/read"
    params = {
        "email": email,
        "key": api_key,
        "country": "Haiti"
    }
    output_path = "data/haiti_acled_conflict.csv"
    
    print(f"Fetching ACLED Haiti data using API...")
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        if data['status'] != 200:
            print(f"ACLED API Error: {data['error']['message']}")
            return False
            
        events = data['data']
        df = pd.DataFrame(events)
        
        os.makedirs("data", exist_ok=True)
        df.to_csv(output_path, index=False)
        
        print(f"Successfully saved to {output_path}")
        print(f"Loaded {len(df)} conflict events from ACLED.")
        return True
    except Exception as e:
        print(f"Error fetching ACLED data: {e}")
        return False

if __name__ == "__main__":
    fetch_ucdp_haiti_data()
    print("\n--- ACLED Setup ---")
    print("To fetch ACLED data via this script, you need to provide your credentials.")
    print("Example usage: fetch_acled_haiti_data('your_email@example.com', 'your_api_key')")
