import Controllers.scraper_data as data
import Controllers.scraper_daily as daily
import Controllers.create_report as report
import Controllers.send_mail as send_email

data.selic()
data.inflacao()
daily.variations()
report.daily_report()
send_email.sendmail()


