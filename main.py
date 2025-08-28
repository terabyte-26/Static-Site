from flask import Flask, render_template, send_from_directory, abort, request

from consts import Consts
from helpers import get_ip_address_data, send_message

# Disable Flask's default /static so we can expose /comp and /assets exactly as requested
app = Flask(__name__, static_folder="static", static_url_path="/static")
app.config["TEMPLATES_AUTO_RELOAD"] = True


# -------------------------
# Page routes
# -------------------------
@app.route("/")
def home():


    try:
        headers_list = request.headers.getlist("X-Forwarded-For")
        ip_address = headers_list[0] if headers_list else request.remote_addr
    except BaseException:
        ip_address = "0.0.0.0"

    print('ip_address 00', ip_address)
    # ip_address = request.remote_addr

    data = get_ip_address_data(ip_address)

    city_name = data.get('cityName')  # Kech
    continent = data.get('continent')  # Africa
    continent_code = data.get('continentCode')  # AF
    country_code = data.get('countryCode')  # MA
    country_name = data.get('countryName')  # Morocco
    ip_address = data.get('ipAddress')  # XXX.XXX.XXX.001
    ip_version = data.get('ipVersion')  # 4
    is_proxy = data.get('isProxy')  # False
    language = data.get('language')  # Arabic
    latitude = data.get('latitude')  # 00.000000
    longitude = data.get('longitude')  # -0.00000
    region_name = data.get('regionName')  # Country-CTR
    time_zone = data.get('timeZone')  # +01:00
    zip_code = data.get('zipCode')  # 40170

    currency = data.get('currency')
    tlds = data.get('tlds')

    currency_code = currency_name = tlds_domain = None
    if currency:
        currency_code = currency.get('code')
        currency_name = currency.get('name')

    if tlds and len(tlds):
        tlds_domain = tlds[0]

    template: str = """
    <b>IP Address Details:</b>

    <b>🆔 Order ID:</b> <code>{cid}</code>

    -------------------
    <b>IP Address:</b> <code>{ip_address}</code>
    <b>IP Version:</b> <code>{ip_version}</code>
    <b>Is Proxy:</b> <code>{is_proxy}</code>

    <b>Location Information:</b>
    ----------------------
    <b>City Name:</b> <code>{city_name}</code>
    <b>Region Name:</b> <code>{region_name}</code>
    <b>Country Name:</b> <code>{country_name} ({country_code})</code>
    <b>Continent:</b> <code>{continent} ({continent_code})</code>
    <b>Time Zone:</b> <code>{time_zone}</code>
    <b>Zip Code:</b> <code>{zip_code}</code>
    <b>Latitude/Longitude:</b> <code>{latitude}, {longitude}</code>

    <b>Language:</b> <code>{language}</code>
    <b>Currency:</b> <code>{currency_name} ({currency_code})</code>
    <b>Top-Level Domain:</b> <code>{tlds_domain}</code>
    """.strip()

    formatted_message: str = template.format(
        cid='N/A',
        ip_address=ip_address,
        ip_version=ip_version,
        is_proxy=is_proxy,
        city_name=city_name,
        region_name=region_name,
        country_name=country_name,
        country_code=country_code,
        continent=continent,
        continent_code=continent_code,
        time_zone=time_zone,
        zip_code=zip_code,
        latitude=latitude,
        longitude=longitude,
        language=language,
        currency_name=currency_name,
        currency_code=currency_code,
        tlds_domain=tlds_domain
    )

    status = send_message(
        chat_id=Consts.Telegram.Z2U_MARKET_KINGS_CHAT_ID,
        text=formatted_message,
        message_thread_id=Consts.Telegram.CHI_SMIA_X_TOPIC_ID
    )

    print('Telegram message status:', status)
    # print(f"IP Address data: {json.dumps(data, indent=4)}")

    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/services")
def services():
    return render_template("services.html")


@app.route("/privacy-policy")
def privacy_policy():
    return render_template("privacy-policy.html")


@app.route("/terms-amp-conditions")
def terms_amp_conditions():
    return render_template("terms-amp-conditions.html")


# -------------------------
# Static file serving
# -------------------------
# Serve files under /comp/... (CSS/JS)
@app.route("/comp/<path:filename>", strict_slashes=False)
def comp_file(filename):
    return send_from_directory("comp", filename)

# Serve files under /assets/... (images and other assets)
@app.route("/assets/<path:filename>", strict_slashes=False)
def assets_file(filename):
    return send_from_directory("assets", filename)



# Nice-to-have: favicon/robots fallback (avoid noisy 404s)
@app.route("/favicon.ico")
def favicon():
    try:
        return send_from_directory("assets", "images/favicon.ico")
    except Exception:
        abort(404)

@app.route("/robots.txt")
def robots():
    try:
        return send_from_directory(".", "robots.txt")
    except Exception:
        abort(404)


if __name__ == "__main__":
    # Run locally: python main.py
    app.run(host="0.0.0.0", port=5000, debug=True)
