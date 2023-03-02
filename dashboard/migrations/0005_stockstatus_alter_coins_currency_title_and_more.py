# Generated by Django 4.1.7 on 2023-03-01 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_orderstatus_alter_coins_currency_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('SUCCESS', 'SUCCESS')], max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='coins',
            name='currency_title',
            field=models.CharField(blank=True, choices=[('GBP', 'GBP'), ('TPE', 'TPE'), ('UAH', 'UAH'), ('CDF', 'CDF'), ('SBD', 'SBD'), ('UGX', 'UGX'), ('ZWL', 'ZWL'), ('FJD', 'FJD'), ('UGS', 'UGS'), ('MVR', 'MVR'), ('ARL', 'ARL'), ('BRC', 'BRC'), ('BIF', 'BIF'), ('CSK', 'CSK'), ('TWD', 'TWD'), ('BAN', 'BAN'), ('QAR', 'QAR'), ('TND', 'TND'), ('CLE', 'CLE'), ('BUK', 'BUK'), ('GTQ', 'GTQ'), ('XBD', 'XBD'), ('BRZ', 'BRZ'), ('AZM', 'AZM'), ('CZK', 'CZK'), ('KPW', 'KPW'), ('ANG', 'ANG'), ('YUR', 'YUR'), ('HRK', 'HRK'), ('PAB', 'PAB'), ('UYP', 'UYP'), ('FIM', 'FIM'), ('BWP', 'BWP'), ('ZRZ', 'ZRZ'), ('GIP', 'GIP'), ('XBA', 'XBA'), ('PTE', 'PTE'), ('PKR', 'PKR'), ('NIC', 'NIC'), ('SDD', 'SDD'), ('ARM', 'ARM'), ('IRR', 'IRR'), ('SLL', 'SLL'), ('XSU', 'XSU'), ('AED', 'AED'), ('SRG', 'SRG'), ('KHR', 'KHR'), ('LUF', 'LUF'), ('SYP', 'SYP'), ('XFO', 'XFO'), ('PLN', 'PLN'), ('XPF', 'XPF'), ('LKR', 'LKR'), ('STN', 'STN'), ('ISK', 'ISK'), ('ILS', 'ILS'), ('ATS', 'ATS'), ('XAF', 'XAF'), ('BRR', 'BRR'), ('BOL', 'BOL'), ('MUR', 'MUR'), ('BOP', 'BOP'), ('DOP', 'DOP'), ('BND', 'BND'), ('COP', 'COP'), ('ARS', 'ARS'), ('ZRN', 'ZRN'), ('XUA', 'XUA'), ('ZWR', 'ZWR'), ('ESB', 'ESB'), ('LYD', 'LYD'), ('XEU', 'XEU'), ('ADP', 'ADP'), ('LVR', 'LVR'), ('BRE', 'BRE'), ('MGF', 'MGF'), ('ALK', 'ALK'), ('PEI', 'PEI'), ('ETB', 'ETB'), ('MCF', 'MCF'), ('XBC', 'XBC'), ('CUP', 'CUP'), ('TJR', 'TJR'), ('CHE', 'CHE'), ('NZD', 'NZD'), ('MZE', 'MZE'), ('XDR', 'XDR'), ('TRY', 'TRY'), ('BMD', 'BMD'), ('CNX', 'CNX'), ('PHP', 'PHP'), ('USD', 'USD'), ('YUM', 'YUM'), ('ZMK', 'ZMK'), ('DJF', 'DJF'), ('SDP', 'SDP'), ('VEB', 'VEB'), ('BGO', 'BGO'), ('BOV', 'BOV'), ('CSD', 'CSD'), ('SLE', 'SLE'), ('PGK', 'PGK'), ('TMT', 'TMT'), ('GYD', 'GYD'), ('MLF', 'MLF'), ('MOP', 'MOP'), ('MKD', 'MKD'), ('CAD', 'CAD'), ('KRH', 'KRH'), ('STD', 'STD'), ('WST', 'WST'), ('ESP', 'ESP'), ('IQD', 'IQD'), ('SDG', 'SDG'), ('NAD', 'NAD'), ('GMD', 'GMD'), ('BDT', 'BDT'), ('GEK', 'GEK'), ('BEL', 'BEL'), ('KES', 'KES'), ('ARA', 'ARA'), ('XPD', 'XPD'), ('MXV', 'MXV'), ('CHW', 'CHW'), ('XXX', 'XXX'), ('NIO', 'NIO'), ('MZN', 'MZN'), ('BGM', 'BGM'), ('DEM', 'DEM'), ('BYB', 'BYB'), ('UZS', 'UZS'), ('ESA', 'ESA'), ('BHD', 'BHD'), ('BGL', 'BGL'), ('MRU', 'MRU'), ('BRL', 'BRL'), ('LVL', 'LVL'), ('FRF', 'FRF'), ('BOB', 'BOB'), ('EGP', 'EGP'), ('HKD', 'HKD'), ('XRE', 'XRE'), ('ECV', 'ECV'), ('AUD', 'AUD'), ('GHC', 'GHC'), ('INR', 'INR'), ('SGD', 'SGD'), ('UAK', 'UAK'), ('CVE', 'CVE'), ('CLP', 'CLP'), ('JPY', 'JPY'), ('EEK', 'EEK'), ('AFA', 'AFA'), ('JOD', 'JOD'), ('SHP', 'SHP'), ('CUC', 'CUC'), ('DKK', 'DKK'), ('PLZ', 'PLZ'), ('BTN', 'BTN'), ('SVC', 'SVC'), ('GWP', 'GWP'), ('ISJ', 'ISJ'), ('XBB', 'XBB'), ('MZM', 'MZM'), ('UYW', 'UYW'), ('MXN', 'MXN'), ('CNH', 'CNH'), ('NGN', 'NGN'), ('CNY', 'CNY'), ('ECS', 'ECS'), ('YUN', 'YUN'), ('LTT', 'LTT'), ('BEC', 'BEC'), ('VUV', 'VUV'), ('RSD', 'RSD'), ('SZL', 'SZL'), ('CRC', 'CRC'), ('AOA', 'AOA'), ('KWD', 'KWD'), ('ROL', 'ROL'), ('RUB', 'RUB'), ('RUR', 'RUR'), ('ILP', 'ILP'), ('TTD', 'TTD'), ('BZD', 'BZD'), ('BEF', 'BEF'), ('SSP', 'SSP'), ('KRW', 'KRW'), ('VNN', 'VNN'), ('PEN', 'PEN'), ('MAF', 'MAF'), ('XCD', 'XCD'), ('NLG', 'NLG'), ('COU', 'COU'), ('MXP', 'MXP'), ('MNT', 'MNT'), ('BAM', 'BAM'), ('USN', 'USN'), ('SAR', 'SAR'), ('SOS', 'SOS'), ('RON', 'RON'), ('BSD', 'BSD'), ('XPT', 'XPT'), ('GHS', 'GHS'), ('RHD', 'RHD'), ('GNS', 'GNS'), ('HRD', 'HRD'), ('MTP', 'MTP'), ('MAD', 'MAD'), ('ZMW', 'ZMW'), ('ITL', 'ITL'), ('CHF', 'CHF'), ('SEK', 'SEK'), ('DDM', 'DDM'), ('IEP', 'IEP'), ('HUF', 'HUF'), ('MYR', 'MYR'), ('YDD', 'YDD'), ('MKN', 'MKN'), ('VEF', 'VEF'), ('MTL', 'MTL'), ('XOF', 'XOF'), ('DZD', 'DZD'), ('KZT', 'KZT'), ('LBP', 'LBP'), ('GNF', 'GNF'), ('LSL', 'LSL'), ('SRD', 'SRD'), ('TZS', 'TZS'), ('AMD', 'AMD'), ('TRL', 'TRL'), ('CYP', 'CYP'), ('USS', 'USS'), ('MRO', 'MRO'), ('XAU', 'XAU'), ('LUC', 'LUC'), ('YER', 'YER'), ('HNL', 'HNL'), ('BYR', 'BYR'), ('GWE', 'GWE'), ('KMF', 'KMF'), ('TJS', 'TJS'), ('PYG', 'PYG'), ('SCR', 'SCR'), ('GQE', 'GQE'), ('MVP', 'MVP'), ('LRD', 'LRD'), ('LUL', 'LUL'), ('XTS', 'XTS'), ('AFN', 'AFN'), ('SIT', 'SIT'), ('PES', 'PES'), ('MDL', 'MDL'), ('AZN', 'AZN'), ('BRB', 'BRB'), ('HTG', 'HTG'), ('LAK', 'LAK'), ('XAG', 'XAG'), ('TOP', 'TOP'), ('THB', 'THB'), ('UYU', 'UYU'), ('BRN', 'BRN'), ('VES', 'VES'), ('AOR', 'AOR'), ('VND', 'VND'), ('ZAL', 'ZAL'), ('CLF', 'CLF'), ('KRO', 'KRO'), ('NPR', 'NPR'), ('EUR', 'EUR'), ('YUD', 'YUD'), ('ALL', 'ALL'), ('RWF', 'RWF'), ('OMR', 'OMR'), ('GEL', 'GEL'), ('ZWD', 'ZWD'), ('UYI', 'UYI'), ('AOK', 'AOK'), ('SKK', 'SKK'), ('MWK', 'MWK'), ('IDR', 'IDR'), ('TMM', 'TMM'), ('ERN', 'ERN'), ('JMD', 'JMD'), ('VED', 'VED'), ('XFU', 'XFU'), ('BGN', 'BGN'), ('GRD', 'GRD'), ('NOK', 'NOK'), ('AWG', 'AWG'), ('BBD', 'BBD'), ('KYD', 'KYD'), ('SUR', 'SUR'), ('ARP', 'ARP'), ('KGS', 'KGS'), ('ZAR', 'ZAR'), ('AON', 'AON'), ('LTL', 'LTL'), ('FKP', 'FKP'), ('MDC', 'MDC'), ('BYN', 'BYN'), ('MGA', 'MGA'), ('BAD', 'BAD'), ('ILR', 'ILR'), ('MMK', 'MMK')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='local',
            name='currency',
            field=models.CharField(blank=True, choices=[('GBP', 'GBP'), ('TPE', 'TPE'), ('UAH', 'UAH'), ('CDF', 'CDF'), ('SBD', 'SBD'), ('UGX', 'UGX'), ('ZWL', 'ZWL'), ('FJD', 'FJD'), ('UGS', 'UGS'), ('MVR', 'MVR'), ('ARL', 'ARL'), ('BRC', 'BRC'), ('BIF', 'BIF'), ('CSK', 'CSK'), ('TWD', 'TWD'), ('BAN', 'BAN'), ('QAR', 'QAR'), ('TND', 'TND'), ('CLE', 'CLE'), ('BUK', 'BUK'), ('GTQ', 'GTQ'), ('XBD', 'XBD'), ('BRZ', 'BRZ'), ('AZM', 'AZM'), ('CZK', 'CZK'), ('KPW', 'KPW'), ('ANG', 'ANG'), ('YUR', 'YUR'), ('HRK', 'HRK'), ('PAB', 'PAB'), ('UYP', 'UYP'), ('FIM', 'FIM'), ('BWP', 'BWP'), ('ZRZ', 'ZRZ'), ('GIP', 'GIP'), ('XBA', 'XBA'), ('PTE', 'PTE'), ('PKR', 'PKR'), ('NIC', 'NIC'), ('SDD', 'SDD'), ('ARM', 'ARM'), ('IRR', 'IRR'), ('SLL', 'SLL'), ('XSU', 'XSU'), ('AED', 'AED'), ('SRG', 'SRG'), ('KHR', 'KHR'), ('LUF', 'LUF'), ('SYP', 'SYP'), ('XFO', 'XFO'), ('PLN', 'PLN'), ('XPF', 'XPF'), ('LKR', 'LKR'), ('STN', 'STN'), ('ISK', 'ISK'), ('ILS', 'ILS'), ('ATS', 'ATS'), ('XAF', 'XAF'), ('BRR', 'BRR'), ('BOL', 'BOL'), ('MUR', 'MUR'), ('BOP', 'BOP'), ('DOP', 'DOP'), ('BND', 'BND'), ('COP', 'COP'), ('ARS', 'ARS'), ('ZRN', 'ZRN'), ('XUA', 'XUA'), ('ZWR', 'ZWR'), ('ESB', 'ESB'), ('LYD', 'LYD'), ('XEU', 'XEU'), ('ADP', 'ADP'), ('LVR', 'LVR'), ('BRE', 'BRE'), ('MGF', 'MGF'), ('ALK', 'ALK'), ('PEI', 'PEI'), ('ETB', 'ETB'), ('MCF', 'MCF'), ('XBC', 'XBC'), ('CUP', 'CUP'), ('TJR', 'TJR'), ('CHE', 'CHE'), ('NZD', 'NZD'), ('MZE', 'MZE'), ('XDR', 'XDR'), ('TRY', 'TRY'), ('BMD', 'BMD'), ('CNX', 'CNX'), ('PHP', 'PHP'), ('USD', 'USD'), ('YUM', 'YUM'), ('ZMK', 'ZMK'), ('DJF', 'DJF'), ('SDP', 'SDP'), ('VEB', 'VEB'), ('BGO', 'BGO'), ('BOV', 'BOV'), ('CSD', 'CSD'), ('SLE', 'SLE'), ('PGK', 'PGK'), ('TMT', 'TMT'), ('GYD', 'GYD'), ('MLF', 'MLF'), ('MOP', 'MOP'), ('MKD', 'MKD'), ('CAD', 'CAD'), ('KRH', 'KRH'), ('STD', 'STD'), ('WST', 'WST'), ('ESP', 'ESP'), ('IQD', 'IQD'), ('SDG', 'SDG'), ('NAD', 'NAD'), ('GMD', 'GMD'), ('BDT', 'BDT'), ('GEK', 'GEK'), ('BEL', 'BEL'), ('KES', 'KES'), ('ARA', 'ARA'), ('XPD', 'XPD'), ('MXV', 'MXV'), ('CHW', 'CHW'), ('XXX', 'XXX'), ('NIO', 'NIO'), ('MZN', 'MZN'), ('BGM', 'BGM'), ('DEM', 'DEM'), ('BYB', 'BYB'), ('UZS', 'UZS'), ('ESA', 'ESA'), ('BHD', 'BHD'), ('BGL', 'BGL'), ('MRU', 'MRU'), ('BRL', 'BRL'), ('LVL', 'LVL'), ('FRF', 'FRF'), ('BOB', 'BOB'), ('EGP', 'EGP'), ('HKD', 'HKD'), ('XRE', 'XRE'), ('ECV', 'ECV'), ('AUD', 'AUD'), ('GHC', 'GHC'), ('INR', 'INR'), ('SGD', 'SGD'), ('UAK', 'UAK'), ('CVE', 'CVE'), ('CLP', 'CLP'), ('JPY', 'JPY'), ('EEK', 'EEK'), ('AFA', 'AFA'), ('JOD', 'JOD'), ('SHP', 'SHP'), ('CUC', 'CUC'), ('DKK', 'DKK'), ('PLZ', 'PLZ'), ('BTN', 'BTN'), ('SVC', 'SVC'), ('GWP', 'GWP'), ('ISJ', 'ISJ'), ('XBB', 'XBB'), ('MZM', 'MZM'), ('UYW', 'UYW'), ('MXN', 'MXN'), ('CNH', 'CNH'), ('NGN', 'NGN'), ('CNY', 'CNY'), ('ECS', 'ECS'), ('YUN', 'YUN'), ('LTT', 'LTT'), ('BEC', 'BEC'), ('VUV', 'VUV'), ('RSD', 'RSD'), ('SZL', 'SZL'), ('CRC', 'CRC'), ('AOA', 'AOA'), ('KWD', 'KWD'), ('ROL', 'ROL'), ('RUB', 'RUB'), ('RUR', 'RUR'), ('ILP', 'ILP'), ('TTD', 'TTD'), ('BZD', 'BZD'), ('BEF', 'BEF'), ('SSP', 'SSP'), ('KRW', 'KRW'), ('VNN', 'VNN'), ('PEN', 'PEN'), ('MAF', 'MAF'), ('XCD', 'XCD'), ('NLG', 'NLG'), ('COU', 'COU'), ('MXP', 'MXP'), ('MNT', 'MNT'), ('BAM', 'BAM'), ('USN', 'USN'), ('SAR', 'SAR'), ('SOS', 'SOS'), ('RON', 'RON'), ('BSD', 'BSD'), ('XPT', 'XPT'), ('GHS', 'GHS'), ('RHD', 'RHD'), ('GNS', 'GNS'), ('HRD', 'HRD'), ('MTP', 'MTP'), ('MAD', 'MAD'), ('ZMW', 'ZMW'), ('ITL', 'ITL'), ('CHF', 'CHF'), ('SEK', 'SEK'), ('DDM', 'DDM'), ('IEP', 'IEP'), ('HUF', 'HUF'), ('MYR', 'MYR'), ('YDD', 'YDD'), ('MKN', 'MKN'), ('VEF', 'VEF'), ('MTL', 'MTL'), ('XOF', 'XOF'), ('DZD', 'DZD'), ('KZT', 'KZT'), ('LBP', 'LBP'), ('GNF', 'GNF'), ('LSL', 'LSL'), ('SRD', 'SRD'), ('TZS', 'TZS'), ('AMD', 'AMD'), ('TRL', 'TRL'), ('CYP', 'CYP'), ('USS', 'USS'), ('MRO', 'MRO'), ('XAU', 'XAU'), ('LUC', 'LUC'), ('YER', 'YER'), ('HNL', 'HNL'), ('BYR', 'BYR'), ('GWE', 'GWE'), ('KMF', 'KMF'), ('TJS', 'TJS'), ('PYG', 'PYG'), ('SCR', 'SCR'), ('GQE', 'GQE'), ('MVP', 'MVP'), ('LRD', 'LRD'), ('LUL', 'LUL'), ('XTS', 'XTS'), ('AFN', 'AFN'), ('SIT', 'SIT'), ('PES', 'PES'), ('MDL', 'MDL'), ('AZN', 'AZN'), ('BRB', 'BRB'), ('HTG', 'HTG'), ('LAK', 'LAK'), ('XAG', 'XAG'), ('TOP', 'TOP'), ('THB', 'THB'), ('UYU', 'UYU'), ('BRN', 'BRN'), ('VES', 'VES'), ('AOR', 'AOR'), ('VND', 'VND'), ('ZAL', 'ZAL'), ('CLF', 'CLF'), ('KRO', 'KRO'), ('NPR', 'NPR'), ('EUR', 'EUR'), ('YUD', 'YUD'), ('ALL', 'ALL'), ('RWF', 'RWF'), ('OMR', 'OMR'), ('GEL', 'GEL'), ('ZWD', 'ZWD'), ('UYI', 'UYI'), ('AOK', 'AOK'), ('SKK', 'SKK'), ('MWK', 'MWK'), ('IDR', 'IDR'), ('TMM', 'TMM'), ('ERN', 'ERN'), ('JMD', 'JMD'), ('VED', 'VED'), ('XFU', 'XFU'), ('BGN', 'BGN'), ('GRD', 'GRD'), ('NOK', 'NOK'), ('AWG', 'AWG'), ('BBD', 'BBD'), ('KYD', 'KYD'), ('SUR', 'SUR'), ('ARP', 'ARP'), ('KGS', 'KGS'), ('ZAR', 'ZAR'), ('AON', 'AON'), ('LTL', 'LTL'), ('FKP', 'FKP'), ('MDC', 'MDC'), ('BYN', 'BYN'), ('MGA', 'MGA'), ('BAD', 'BAD'), ('ILR', 'ILR'), ('MMK', 'MMK')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='local',
            name='currency_with_default',
            field=models.CharField(choices=[('GBP', 'GBP'), ('TPE', 'TPE'), ('UAH', 'UAH'), ('CDF', 'CDF'), ('SBD', 'SBD'), ('UGX', 'UGX'), ('ZWL', 'ZWL'), ('FJD', 'FJD'), ('UGS', 'UGS'), ('MVR', 'MVR'), ('ARL', 'ARL'), ('BRC', 'BRC'), ('BIF', 'BIF'), ('CSK', 'CSK'), ('TWD', 'TWD'), ('BAN', 'BAN'), ('QAR', 'QAR'), ('TND', 'TND'), ('CLE', 'CLE'), ('BUK', 'BUK'), ('GTQ', 'GTQ'), ('XBD', 'XBD'), ('BRZ', 'BRZ'), ('AZM', 'AZM'), ('CZK', 'CZK'), ('KPW', 'KPW'), ('ANG', 'ANG'), ('YUR', 'YUR'), ('HRK', 'HRK'), ('PAB', 'PAB'), ('UYP', 'UYP'), ('FIM', 'FIM'), ('BWP', 'BWP'), ('ZRZ', 'ZRZ'), ('GIP', 'GIP'), ('XBA', 'XBA'), ('PTE', 'PTE'), ('PKR', 'PKR'), ('NIC', 'NIC'), ('SDD', 'SDD'), ('ARM', 'ARM'), ('IRR', 'IRR'), ('SLL', 'SLL'), ('XSU', 'XSU'), ('AED', 'AED'), ('SRG', 'SRG'), ('KHR', 'KHR'), ('LUF', 'LUF'), ('SYP', 'SYP'), ('XFO', 'XFO'), ('PLN', 'PLN'), ('XPF', 'XPF'), ('LKR', 'LKR'), ('STN', 'STN'), ('ISK', 'ISK'), ('ILS', 'ILS'), ('ATS', 'ATS'), ('XAF', 'XAF'), ('BRR', 'BRR'), ('BOL', 'BOL'), ('MUR', 'MUR'), ('BOP', 'BOP'), ('DOP', 'DOP'), ('BND', 'BND'), ('COP', 'COP'), ('ARS', 'ARS'), ('ZRN', 'ZRN'), ('XUA', 'XUA'), ('ZWR', 'ZWR'), ('ESB', 'ESB'), ('LYD', 'LYD'), ('XEU', 'XEU'), ('ADP', 'ADP'), ('LVR', 'LVR'), ('BRE', 'BRE'), ('MGF', 'MGF'), ('ALK', 'ALK'), ('PEI', 'PEI'), ('ETB', 'ETB'), ('MCF', 'MCF'), ('XBC', 'XBC'), ('CUP', 'CUP'), ('TJR', 'TJR'), ('CHE', 'CHE'), ('NZD', 'NZD'), ('MZE', 'MZE'), ('XDR', 'XDR'), ('TRY', 'TRY'), ('BMD', 'BMD'), ('CNX', 'CNX'), ('PHP', 'PHP'), ('USD', 'USD'), ('YUM', 'YUM'), ('ZMK', 'ZMK'), ('DJF', 'DJF'), ('SDP', 'SDP'), ('VEB', 'VEB'), ('BGO', 'BGO'), ('BOV', 'BOV'), ('CSD', 'CSD'), ('SLE', 'SLE'), ('PGK', 'PGK'), ('TMT', 'TMT'), ('GYD', 'GYD'), ('MLF', 'MLF'), ('MOP', 'MOP'), ('MKD', 'MKD'), ('CAD', 'CAD'), ('KRH', 'KRH'), ('STD', 'STD'), ('WST', 'WST'), ('ESP', 'ESP'), ('IQD', 'IQD'), ('SDG', 'SDG'), ('NAD', 'NAD'), ('GMD', 'GMD'), ('BDT', 'BDT'), ('GEK', 'GEK'), ('BEL', 'BEL'), ('KES', 'KES'), ('ARA', 'ARA'), ('XPD', 'XPD'), ('MXV', 'MXV'), ('CHW', 'CHW'), ('XXX', 'XXX'), ('NIO', 'NIO'), ('MZN', 'MZN'), ('BGM', 'BGM'), ('DEM', 'DEM'), ('BYB', 'BYB'), ('UZS', 'UZS'), ('ESA', 'ESA'), ('BHD', 'BHD'), ('BGL', 'BGL'), ('MRU', 'MRU'), ('BRL', 'BRL'), ('LVL', 'LVL'), ('FRF', 'FRF'), ('BOB', 'BOB'), ('EGP', 'EGP'), ('HKD', 'HKD'), ('XRE', 'XRE'), ('ECV', 'ECV'), ('AUD', 'AUD'), ('GHC', 'GHC'), ('INR', 'INR'), ('SGD', 'SGD'), ('UAK', 'UAK'), ('CVE', 'CVE'), ('CLP', 'CLP'), ('JPY', 'JPY'), ('EEK', 'EEK'), ('AFA', 'AFA'), ('JOD', 'JOD'), ('SHP', 'SHP'), ('CUC', 'CUC'), ('DKK', 'DKK'), ('PLZ', 'PLZ'), ('BTN', 'BTN'), ('SVC', 'SVC'), ('GWP', 'GWP'), ('ISJ', 'ISJ'), ('XBB', 'XBB'), ('MZM', 'MZM'), ('UYW', 'UYW'), ('MXN', 'MXN'), ('CNH', 'CNH'), ('NGN', 'NGN'), ('CNY', 'CNY'), ('ECS', 'ECS'), ('YUN', 'YUN'), ('LTT', 'LTT'), ('BEC', 'BEC'), ('VUV', 'VUV'), ('RSD', 'RSD'), ('SZL', 'SZL'), ('CRC', 'CRC'), ('AOA', 'AOA'), ('KWD', 'KWD'), ('ROL', 'ROL'), ('RUB', 'RUB'), ('RUR', 'RUR'), ('ILP', 'ILP'), ('TTD', 'TTD'), ('BZD', 'BZD'), ('BEF', 'BEF'), ('SSP', 'SSP'), ('KRW', 'KRW'), ('VNN', 'VNN'), ('PEN', 'PEN'), ('MAF', 'MAF'), ('XCD', 'XCD'), ('NLG', 'NLG'), ('COU', 'COU'), ('MXP', 'MXP'), ('MNT', 'MNT'), ('BAM', 'BAM'), ('USN', 'USN'), ('SAR', 'SAR'), ('SOS', 'SOS'), ('RON', 'RON'), ('BSD', 'BSD'), ('XPT', 'XPT'), ('GHS', 'GHS'), ('RHD', 'RHD'), ('GNS', 'GNS'), ('HRD', 'HRD'), ('MTP', 'MTP'), ('MAD', 'MAD'), ('ZMW', 'ZMW'), ('ITL', 'ITL'), ('CHF', 'CHF'), ('SEK', 'SEK'), ('DDM', 'DDM'), ('IEP', 'IEP'), ('HUF', 'HUF'), ('MYR', 'MYR'), ('YDD', 'YDD'), ('MKN', 'MKN'), ('VEF', 'VEF'), ('MTL', 'MTL'), ('XOF', 'XOF'), ('DZD', 'DZD'), ('KZT', 'KZT'), ('LBP', 'LBP'), ('GNF', 'GNF'), ('LSL', 'LSL'), ('SRD', 'SRD'), ('TZS', 'TZS'), ('AMD', 'AMD'), ('TRL', 'TRL'), ('CYP', 'CYP'), ('USS', 'USS'), ('MRO', 'MRO'), ('XAU', 'XAU'), ('LUC', 'LUC'), ('YER', 'YER'), ('HNL', 'HNL'), ('BYR', 'BYR'), ('GWE', 'GWE'), ('KMF', 'KMF'), ('TJS', 'TJS'), ('PYG', 'PYG'), ('SCR', 'SCR'), ('GQE', 'GQE'), ('MVP', 'MVP'), ('LRD', 'LRD'), ('LUL', 'LUL'), ('XTS', 'XTS'), ('AFN', 'AFN'), ('SIT', 'SIT'), ('PES', 'PES'), ('MDL', 'MDL'), ('AZN', 'AZN'), ('BRB', 'BRB'), ('HTG', 'HTG'), ('LAK', 'LAK'), ('XAG', 'XAG'), ('TOP', 'TOP'), ('THB', 'THB'), ('UYU', 'UYU'), ('BRN', 'BRN'), ('VES', 'VES'), ('AOR', 'AOR'), ('VND', 'VND'), ('ZAL', 'ZAL'), ('CLF', 'CLF'), ('KRO', 'KRO'), ('NPR', 'NPR'), ('EUR', 'EUR'), ('YUD', 'YUD'), ('ALL', 'ALL'), ('RWF', 'RWF'), ('OMR', 'OMR'), ('GEL', 'GEL'), ('ZWD', 'ZWD'), ('UYI', 'UYI'), ('AOK', 'AOK'), ('SKK', 'SKK'), ('MWK', 'MWK'), ('IDR', 'IDR'), ('TMM', 'TMM'), ('ERN', 'ERN'), ('JMD', 'JMD'), ('VED', 'VED'), ('XFU', 'XFU'), ('BGN', 'BGN'), ('GRD', 'GRD'), ('NOK', 'NOK'), ('AWG', 'AWG'), ('BBD', 'BBD'), ('KYD', 'KYD'), ('SUR', 'SUR'), ('ARP', 'ARP'), ('KGS', 'KGS'), ('ZAR', 'ZAR'), ('AON', 'AON'), ('LTL', 'LTL'), ('FKP', 'FKP'), ('MDC', 'MDC'), ('BYN', 'BYN'), ('MGA', 'MGA'), ('BAD', 'BAD'), ('ILR', 'ILR'), ('MMK', 'MMK')], default='USD', max_length=3),
        ),
    ]