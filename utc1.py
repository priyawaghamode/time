import pytz, datetime
def check_user_input(input):
    try:
        # Convert it into integer
        val = int(input)
        print(val)
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            print("No..Input is a float  number.It is not allowed Number = ", val)
        except ValueError:
            print("No.. input is not a number. It's a string")

year=int(input("enter year(YYYY): "))
check_user_input(year)

month=int(input("enter month(MM): "))
check_user_input(month)

date=int(input("enter date(DD): "))
check_user_input(date)

hour=int(input("enter hour(HH): "))
check_user_input(hour)

minute=int(input("enter minutes(MM): "))
check_user_input(minute)


#convert to the date
user_time=datetime.datetime(year,month,date,hour,minute)
print("\nOur given time is :",user_time.isoformat())

#convert user time into particular timezone
cairo_timezone=pytz.timezone('Africa/Cairo')
london_timezone=pytz.timezone('UTC')
delhi_timezone=pytz.timezone('Asia/Kolkata')
sydney_timezone=pytz.timezone('Australia/Sydney')
UnitedKingdom_timezone=pytz.timezone('Europe/London')
Switzerland_timezone=pytz.timezone('Europe/Zurich')
SriLanka_timezone=pytz.timezone('Asia/Colombo')
Nepal_timezone=pytz.timezone('Asia/Kathmandu')
Japan_timezone=pytz.timezone('Asia/Tokyo')
Italy_timezone=pytz.timezone('Europe/Rome')
Israel_timezone=pytz.timezone('Asia/Jerusalem')

cairo_time=pytz.utc.localize(user_time).astimezone(cairo_timezone)
london_time=pytz.utc.localize(user_time).astimezone(london_timezone)
delhi_time=pytz.utc.localize(user_time).astimezone(delhi_timezone)
sydney_time=pytz.utc.localize(user_time).astimezone(sydney_timezone)
UnitedKingdom_time=pytz.utc.localize(user_time).astimezone(UnitedKingdom_timezone)
Switzerland_time=pytz.utc.localize(user_time).astimezone(Switzerland_timezone)
SriLanka_time=pytz.utc.localize(user_time).astimezone(SriLanka_timezone)
Nepal_time=pytz.utc.localize(user_time).astimezone(Nepal_timezone)
Japan_time=pytz.utc.localize(user_time).astimezone(Japan_timezone)
Italy_time=pytz.utc.localize(user_time).astimezone(Italy_timezone)
Israel_time=pytz.utc.localize(user_time).astimezone(Israel_timezone)

#print all time zone
print("\nCairo time is", cairo_time.isoformat())
print("\nLondon time is", london_time.isoformat())
print("\nDelhi time is", delhi_time.isoformat())
print("\nSydney time is", sydney_time.isoformat())
print("\nUnitedKingdom time is", UnitedKingdom_time.isoformat())
print("\nSwitzerland time is", Switzerland_time.isoformat())
print("\nSriLanka time is", SriLanka_time.isoformat())
print("\nNepal time is", Nepal_time.isoformat())
print("\nJapan time is", Japan_time.isoformat())
print("\nItaly time is", Italy_time.isoformat())
print("\nIsrael time is", Israel_time.isoformat())
