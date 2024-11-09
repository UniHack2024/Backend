import requests
from bs4 import BeautifulSoup
import json
import datetime
from alerts import add_categories

url = "https://sesizari.primariatm.ro/toate"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
script_tag = soup.find("script", {"id" : "__NEXT_DATA__"})

if script_tag:
    json_data = json.loads(script_tag.string)
    pageProps = json_data["props"]["pageProps"]

    # Assuming `pageProps` contains multiple entries in a list (adjust if structure differs)
    for entry in pageProps["entries"]:  # Adjust "entries" based on actual JSON structure
        # Extract required fields from each entry
        title = entry.get("title", "Default Title")
        description = entry.get("description", "")
        location_lat = entry["location"]["lat"]
        location_lng = entry["location"]["lng"]

        #category_name = entry.get("category", "Default Category")
        category_aux = entry.get("category", "Default Category")

        if(category_aux in )
        

        user_name = entry.get("user", "Default User")
        timestamp = entry.get("timestamp", datetime.now().isoformat())

        # Look up or create the related objects for foreign key fields
        category, _ = Category.objects.get_or_create(name = category_name)
        user, _ = User.objects.get_or_create(username = user_name)

        # Create and save the model instance
        record = MyModel(
            title = title,
            description = description,
            location_lat = location_lat,
            location_lng = location_lng,
            category = category,
            user = user,
            timestamp = datetime.fromisoformat(timestamp)  # Adjust format if necessary
        )
        record.save()

    print("Records saved successfully.")
else:
    print("No JSON tag script found")