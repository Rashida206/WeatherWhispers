def scrape_weather():
    query=request.form['query']
    if request.method == 'POST':
        url = request.form['https://www.google.com/search?q=weather+{query}']  
        min_temp, max_temp = scrape_temperature_data(url)
        
        if min_temp is not None and max_temp is not None:
            return render_template('weather.html', min_temp=min_temp, max_temp=max_temp)
        else:
            return "Failed to scrape temperature data."
    
    return render_template('weather_form.html')
def scrape_temperature_data(url):
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Locate the elements containing minimum and maximum temperature data
        # You may need to inspect the HTML of the website to find the specific elements
        min_temp_element = soup.find("span", class_="min-temperature")
        max_temp_element = soup.find("span", class_="max-temperature")

        if min_temp_element and max_temp_element:
            # Extract the temperature values
            min_temp = min_temp_element.text
            max_temp = max_temp_element.text

            return min_temp, max_temp

    return None, None
