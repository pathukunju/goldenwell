# Generated by Django 4.1.7 on 2023-03-01 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_role_user_full_name_alter_coins_currency_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coins',
            name='currency_title',
            field=models.CharField(blank=True, choices=[('BHD', 'BHD'), ('UYW', 'UYW'), ('XOF', 'XOF'), ('GYD', 'GYD'), ('QAR', 'QAR'), ('TOP', 'TOP'), ('GEL', 'GEL'), ('NLG', 'NLG'), ('GBP', 'GBP'), ('BGN', 'BGN'), ('TJS', 'TJS'), ('MUR', 'MUR'), ('UYI', 'UYI'), ('SLE', 'SLE'), ('PES', 'PES'), ('CUP', 'CUP'), ('GEK', 'GEK'), ('AOA', 'AOA'), ('LBP', 'LBP'), ('GHC', 'GHC'), ('XTS', 'XTS'), ('SZL', 'SZL'), ('AOR', 'AOR'), ('KES', 'KES'), ('MNT', 'MNT'), ('DEM', 'DEM'), ('PEI', 'PEI'), ('XSU', 'XSU'), ('HTG', 'HTG'), ('OMR', 'OMR'), ('NOK', 'NOK'), ('SRD', 'SRD'), ('AED', 'AED'), ('TTD', 'TTD'), ('CRC', 'CRC'), ('RSD', 'RSD'), ('BUK', 'BUK'), ('ESP', 'ESP'), ('AOK', 'AOK'), ('HRD', 'HRD'), ('UYP', 'UYP'), ('VED', 'VED'), ('PKR', 'PKR'), ('MZM', 'MZM'), ('VNN', 'VNN'), ('TJR', 'TJR'), ('GWE', 'GWE'), ('STN', 'STN'), ('FIM', 'FIM'), ('CZK', 'CZK'), ('SRG', 'SRG'), ('USD', 'USD'), ('BAM', 'BAM'), ('XBA', 'XBA'), ('XBB', 'XBB'), ('XDR', 'XDR'), ('XPT', 'XPT'), ('YUD', 'YUD'), ('ZAR', 'ZAR'), ('BEC', 'BEC'), ('TMM', 'TMM'), ('PGK', 'PGK'), ('CHE', 'CHE'), ('LUL', 'LUL'), ('FKP', 'FKP'), ('MAD', 'MAD'), ('ANG', 'ANG'), ('CUC', 'CUC'), ('ISJ', 'ISJ'), ('PHP', 'PHP'), ('DOP', 'DOP'), ('AON', 'AON'), ('BEL', 'BEL'), ('BDT', 'BDT'), ('THB', 'THB'), ('CHW', 'CHW'), ('ERN', 'ERN'), ('FJD', 'FJD'), ('SAR', 'SAR'), ('CNY', 'CNY'), ('BYB', 'BYB'), ('ISK', 'ISK'), ('ECV', 'ECV'), ('ILS', 'ILS'), ('SHP', 'SHP'), ('MGF', 'MGF'), ('NIO', 'NIO'), ('PLZ', 'PLZ'), ('EGP', 'EGP'), ('RHD', 'RHD'), ('KRW', 'KRW'), ('YUN', 'YUN'), ('XBC', 'XBC'), ('BRR', 'BRR'), ('BOB', 'BOB'), ('NPR', 'NPR'), ('USS', 'USS'), ('BGL', 'BGL'), ('PTE', 'PTE'), ('SUR', 'SUR'), ('MYR', 'MYR'), ('KZT', 'KZT'), ('LTT', 'LTT'), ('CSD', 'CSD'), ('PYG', 'PYG'), ('KRO', 'KRO'), ('UAK', 'UAK'), ('SLL', 'SLL'), ('MGA', 'MGA'), ('ATS', 'ATS'), ('MCF', 'MCF'), ('DZD', 'DZD'), ('BOV', 'BOV'), ('ZWL', 'ZWL'), ('NAD', 'NAD'), ('LAK', 'LAK'), ('ESB', 'ESB'), ('ESA', 'ESA'), ('RWF', 'RWF'), ('IQD', 'IQD'), ('PAB', 'PAB'), ('MOP', 'MOP'), ('COU', 'COU'), ('ECS', 'ECS'), ('HNL', 'HNL'), ('ILP', 'ILP'), ('GNS', 'GNS'), ('MZN', 'MZN'), ('YDD', 'YDD'), ('UGX', 'UGX'), ('CVE', 'CVE'), ('SSP', 'SSP'), ('XFU', 'XFU'), ('CSK', 'CSK'), ('TPE', 'TPE'), ('XAG', 'XAG'), ('ARA', 'ARA'), ('AWG', 'AWG'), ('XAU', 'XAU'), ('YER', 'YER'), ('UZS', 'UZS'), ('MXP', 'MXP'), ('JMD', 'JMD'), ('XPD', 'XPD'), ('UGS', 'UGS'), ('LSL', 'LSL'), ('XCD', 'XCD'), ('AFA', 'AFA'), ('EUR', 'EUR'), ('KMF', 'KMF'), ('ARS', 'ARS'), ('ALL', 'ALL'), ('MRU', 'MRU'), ('LVL', 'LVL'), ('BRB', 'BRB'), ('GWP', 'GWP'), ('BOL', 'BOL'), ('LRD', 'LRD'), ('XRE', 'XRE'), ('JPY', 'JPY'), ('MVR', 'MVR'), ('KWD', 'KWD'), ('PEN', 'PEN'), ('BRC', 'BRC'), ('VEB', 'VEB'), ('SVC', 'SVC'), ('ARP', 'ARP'), ('SKK', 'SKK'), ('ITL', 'ITL'), ('ARL', 'ARL'), ('NZD', 'NZD'), ('RUR', 'RUR'), ('BOP', 'BOP'), ('GHS', 'GHS'), ('BAD', 'BAD'), ('CNH', 'CNH'), ('ILR', 'ILR'), ('DKK', 'DKK'), ('CLF', 'CLF'), ('UAH', 'UAH'), ('AMD', 'AMD'), ('MTP', 'MTP'), ('SOS', 'SOS'), ('MAF', 'MAF'), ('ROL', 'ROL'), ('STD', 'STD'), ('XEU', 'XEU'), ('AUD', 'AUD'), ('PLN', 'PLN'), ('LKR', 'LKR'), ('SYP', 'SYP'), ('DDM', 'DDM'), ('TRY', 'TRY'), ('GRD', 'GRD'), ('MTL', 'MTL'), ('ZMK', 'ZMK'), ('XPF', 'XPF'), ('MMK', 'MMK'), ('BRZ', 'BRZ'), ('TMT', 'TMT'), ('MKN', 'MKN'), ('XUA', 'XUA'), ('ZMW', 'ZMW'), ('LUC', 'LUC'), ('BRE', 'BRE'), ('BTN', 'BTN'), ('XXX', 'XXX'), ('AFN', 'AFN'), ('VES', 'VES'), ('XFO', 'XFO'), ('HKD', 'HKD'), ('YUM', 'YUM'), ('ZAL', 'ZAL'), ('SIT', 'SIT'), ('RUB', 'RUB'), ('TRL', 'TRL'), ('KGS', 'KGS'), ('KPW', 'KPW'), ('AZN', 'AZN'), ('LUF', 'LUF'), ('GIP', 'GIP'), ('HUF', 'HUF'), ('WST', 'WST'), ('SDD', 'SDD'), ('KRH', 'KRH'), ('LTL', 'LTL'), ('BND', 'BND'), ('NGN', 'NGN'), ('CAD', 'CAD'), ('LVR', 'LVR'), ('JOD', 'JOD'), ('MXV', 'MXV'), ('SGD', 'SGD'), ('ZRN', 'ZRN'), ('ETB', 'ETB'), ('GTQ', 'GTQ'), ('ZRZ', 'ZRZ'), ('MWK', 'MWK'), ('MKD', 'MKD'), ('VEF', 'VEF'), ('MVP', 'MVP'), ('NIC', 'NIC'), ('IRR', 'IRR'), ('ALK', 'ALK'), ('CDF', 'CDF'), ('CHF', 'CHF'), ('KHR', 'KHR'), ('BRN', 'BRN'), ('BRL', 'BRL'), ('CLE', 'CLE'), ('GMD', 'GMD'), ('MRO', 'MRO'), ('USN', 'USN'), ('TZS', 'TZS'), ('MZE', 'MZE'), ('XAF', 'XAF'), ('EEK', 'EEK'), ('MDL', 'MDL'), ('XBD', 'XBD'), ('SEK', 'SEK'), ('BIF', 'BIF'), ('BGM', 'BGM'), ('MXN', 'MXN'), ('TND', 'TND'), ('IDR', 'IDR'), ('MLF', 'MLF'), ('AZM', 'AZM'), ('CYP', 'CYP'), ('UYU', 'UYU'), ('GNF', 'GNF'), ('TWD', 'TWD'), ('FRF', 'FRF'), ('KYD', 'KYD'), ('BGO', 'BGO'), ('ARM', 'ARM'), ('SCR', 'SCR'), ('BSD', 'BSD'), ('BWP', 'BWP'), ('INR', 'INR'), ('RON', 'RON'), ('SDP', 'SDP'), ('CLP', 'CLP'), ('BBD', 'BBD'), ('SDG', 'SDG'), ('CNX', 'CNX'), ('ZWD', 'ZWD'), ('BAN', 'BAN'), ('MDC', 'MDC'), ('ZWR', 'ZWR'), ('YUR', 'YUR'), ('LYD', 'LYD'), ('BYN', 'BYN'), ('BZD', 'BZD'), ('BEF', 'BEF'), ('SBD', 'SBD'), ('VUV', 'VUV'), ('IEP', 'IEP'), ('DJF', 'DJF'), ('ADP', 'ADP'), ('HRK', 'HRK'), ('VND', 'VND'), ('BYR', 'BYR'), ('BMD', 'BMD'), ('COP', 'COP'), ('GQE', 'GQE')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='local',
            name='currency',
            field=models.CharField(blank=True, choices=[('BHD', 'BHD'), ('UYW', 'UYW'), ('XOF', 'XOF'), ('GYD', 'GYD'), ('QAR', 'QAR'), ('TOP', 'TOP'), ('GEL', 'GEL'), ('NLG', 'NLG'), ('GBP', 'GBP'), ('BGN', 'BGN'), ('TJS', 'TJS'), ('MUR', 'MUR'), ('UYI', 'UYI'), ('SLE', 'SLE'), ('PES', 'PES'), ('CUP', 'CUP'), ('GEK', 'GEK'), ('AOA', 'AOA'), ('LBP', 'LBP'), ('GHC', 'GHC'), ('XTS', 'XTS'), ('SZL', 'SZL'), ('AOR', 'AOR'), ('KES', 'KES'), ('MNT', 'MNT'), ('DEM', 'DEM'), ('PEI', 'PEI'), ('XSU', 'XSU'), ('HTG', 'HTG'), ('OMR', 'OMR'), ('NOK', 'NOK'), ('SRD', 'SRD'), ('AED', 'AED'), ('TTD', 'TTD'), ('CRC', 'CRC'), ('RSD', 'RSD'), ('BUK', 'BUK'), ('ESP', 'ESP'), ('AOK', 'AOK'), ('HRD', 'HRD'), ('UYP', 'UYP'), ('VED', 'VED'), ('PKR', 'PKR'), ('MZM', 'MZM'), ('VNN', 'VNN'), ('TJR', 'TJR'), ('GWE', 'GWE'), ('STN', 'STN'), ('FIM', 'FIM'), ('CZK', 'CZK'), ('SRG', 'SRG'), ('USD', 'USD'), ('BAM', 'BAM'), ('XBA', 'XBA'), ('XBB', 'XBB'), ('XDR', 'XDR'), ('XPT', 'XPT'), ('YUD', 'YUD'), ('ZAR', 'ZAR'), ('BEC', 'BEC'), ('TMM', 'TMM'), ('PGK', 'PGK'), ('CHE', 'CHE'), ('LUL', 'LUL'), ('FKP', 'FKP'), ('MAD', 'MAD'), ('ANG', 'ANG'), ('CUC', 'CUC'), ('ISJ', 'ISJ'), ('PHP', 'PHP'), ('DOP', 'DOP'), ('AON', 'AON'), ('BEL', 'BEL'), ('BDT', 'BDT'), ('THB', 'THB'), ('CHW', 'CHW'), ('ERN', 'ERN'), ('FJD', 'FJD'), ('SAR', 'SAR'), ('CNY', 'CNY'), ('BYB', 'BYB'), ('ISK', 'ISK'), ('ECV', 'ECV'), ('ILS', 'ILS'), ('SHP', 'SHP'), ('MGF', 'MGF'), ('NIO', 'NIO'), ('PLZ', 'PLZ'), ('EGP', 'EGP'), ('RHD', 'RHD'), ('KRW', 'KRW'), ('YUN', 'YUN'), ('XBC', 'XBC'), ('BRR', 'BRR'), ('BOB', 'BOB'), ('NPR', 'NPR'), ('USS', 'USS'), ('BGL', 'BGL'), ('PTE', 'PTE'), ('SUR', 'SUR'), ('MYR', 'MYR'), ('KZT', 'KZT'), ('LTT', 'LTT'), ('CSD', 'CSD'), ('PYG', 'PYG'), ('KRO', 'KRO'), ('UAK', 'UAK'), ('SLL', 'SLL'), ('MGA', 'MGA'), ('ATS', 'ATS'), ('MCF', 'MCF'), ('DZD', 'DZD'), ('BOV', 'BOV'), ('ZWL', 'ZWL'), ('NAD', 'NAD'), ('LAK', 'LAK'), ('ESB', 'ESB'), ('ESA', 'ESA'), ('RWF', 'RWF'), ('IQD', 'IQD'), ('PAB', 'PAB'), ('MOP', 'MOP'), ('COU', 'COU'), ('ECS', 'ECS'), ('HNL', 'HNL'), ('ILP', 'ILP'), ('GNS', 'GNS'), ('MZN', 'MZN'), ('YDD', 'YDD'), ('UGX', 'UGX'), ('CVE', 'CVE'), ('SSP', 'SSP'), ('XFU', 'XFU'), ('CSK', 'CSK'), ('TPE', 'TPE'), ('XAG', 'XAG'), ('ARA', 'ARA'), ('AWG', 'AWG'), ('XAU', 'XAU'), ('YER', 'YER'), ('UZS', 'UZS'), ('MXP', 'MXP'), ('JMD', 'JMD'), ('XPD', 'XPD'), ('UGS', 'UGS'), ('LSL', 'LSL'), ('XCD', 'XCD'), ('AFA', 'AFA'), ('EUR', 'EUR'), ('KMF', 'KMF'), ('ARS', 'ARS'), ('ALL', 'ALL'), ('MRU', 'MRU'), ('LVL', 'LVL'), ('BRB', 'BRB'), ('GWP', 'GWP'), ('BOL', 'BOL'), ('LRD', 'LRD'), ('XRE', 'XRE'), ('JPY', 'JPY'), ('MVR', 'MVR'), ('KWD', 'KWD'), ('PEN', 'PEN'), ('BRC', 'BRC'), ('VEB', 'VEB'), ('SVC', 'SVC'), ('ARP', 'ARP'), ('SKK', 'SKK'), ('ITL', 'ITL'), ('ARL', 'ARL'), ('NZD', 'NZD'), ('RUR', 'RUR'), ('BOP', 'BOP'), ('GHS', 'GHS'), ('BAD', 'BAD'), ('CNH', 'CNH'), ('ILR', 'ILR'), ('DKK', 'DKK'), ('CLF', 'CLF'), ('UAH', 'UAH'), ('AMD', 'AMD'), ('MTP', 'MTP'), ('SOS', 'SOS'), ('MAF', 'MAF'), ('ROL', 'ROL'), ('STD', 'STD'), ('XEU', 'XEU'), ('AUD', 'AUD'), ('PLN', 'PLN'), ('LKR', 'LKR'), ('SYP', 'SYP'), ('DDM', 'DDM'), ('TRY', 'TRY'), ('GRD', 'GRD'), ('MTL', 'MTL'), ('ZMK', 'ZMK'), ('XPF', 'XPF'), ('MMK', 'MMK'), ('BRZ', 'BRZ'), ('TMT', 'TMT'), ('MKN', 'MKN'), ('XUA', 'XUA'), ('ZMW', 'ZMW'), ('LUC', 'LUC'), ('BRE', 'BRE'), ('BTN', 'BTN'), ('XXX', 'XXX'), ('AFN', 'AFN'), ('VES', 'VES'), ('XFO', 'XFO'), ('HKD', 'HKD'), ('YUM', 'YUM'), ('ZAL', 'ZAL'), ('SIT', 'SIT'), ('RUB', 'RUB'), ('TRL', 'TRL'), ('KGS', 'KGS'), ('KPW', 'KPW'), ('AZN', 'AZN'), ('LUF', 'LUF'), ('GIP', 'GIP'), ('HUF', 'HUF'), ('WST', 'WST'), ('SDD', 'SDD'), ('KRH', 'KRH'), ('LTL', 'LTL'), ('BND', 'BND'), ('NGN', 'NGN'), ('CAD', 'CAD'), ('LVR', 'LVR'), ('JOD', 'JOD'), ('MXV', 'MXV'), ('SGD', 'SGD'), ('ZRN', 'ZRN'), ('ETB', 'ETB'), ('GTQ', 'GTQ'), ('ZRZ', 'ZRZ'), ('MWK', 'MWK'), ('MKD', 'MKD'), ('VEF', 'VEF'), ('MVP', 'MVP'), ('NIC', 'NIC'), ('IRR', 'IRR'), ('ALK', 'ALK'), ('CDF', 'CDF'), ('CHF', 'CHF'), ('KHR', 'KHR'), ('BRN', 'BRN'), ('BRL', 'BRL'), ('CLE', 'CLE'), ('GMD', 'GMD'), ('MRO', 'MRO'), ('USN', 'USN'), ('TZS', 'TZS'), ('MZE', 'MZE'), ('XAF', 'XAF'), ('EEK', 'EEK'), ('MDL', 'MDL'), ('XBD', 'XBD'), ('SEK', 'SEK'), ('BIF', 'BIF'), ('BGM', 'BGM'), ('MXN', 'MXN'), ('TND', 'TND'), ('IDR', 'IDR'), ('MLF', 'MLF'), ('AZM', 'AZM'), ('CYP', 'CYP'), ('UYU', 'UYU'), ('GNF', 'GNF'), ('TWD', 'TWD'), ('FRF', 'FRF'), ('KYD', 'KYD'), ('BGO', 'BGO'), ('ARM', 'ARM'), ('SCR', 'SCR'), ('BSD', 'BSD'), ('BWP', 'BWP'), ('INR', 'INR'), ('RON', 'RON'), ('SDP', 'SDP'), ('CLP', 'CLP'), ('BBD', 'BBD'), ('SDG', 'SDG'), ('CNX', 'CNX'), ('ZWD', 'ZWD'), ('BAN', 'BAN'), ('MDC', 'MDC'), ('ZWR', 'ZWR'), ('YUR', 'YUR'), ('LYD', 'LYD'), ('BYN', 'BYN'), ('BZD', 'BZD'), ('BEF', 'BEF'), ('SBD', 'SBD'), ('VUV', 'VUV'), ('IEP', 'IEP'), ('DJF', 'DJF'), ('ADP', 'ADP'), ('HRK', 'HRK'), ('VND', 'VND'), ('BYR', 'BYR'), ('BMD', 'BMD'), ('COP', 'COP'), ('GQE', 'GQE')], max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='local',
            name='currency_with_default',
            field=models.CharField(choices=[('BHD', 'BHD'), ('UYW', 'UYW'), ('XOF', 'XOF'), ('GYD', 'GYD'), ('QAR', 'QAR'), ('TOP', 'TOP'), ('GEL', 'GEL'), ('NLG', 'NLG'), ('GBP', 'GBP'), ('BGN', 'BGN'), ('TJS', 'TJS'), ('MUR', 'MUR'), ('UYI', 'UYI'), ('SLE', 'SLE'), ('PES', 'PES'), ('CUP', 'CUP'), ('GEK', 'GEK'), ('AOA', 'AOA'), ('LBP', 'LBP'), ('GHC', 'GHC'), ('XTS', 'XTS'), ('SZL', 'SZL'), ('AOR', 'AOR'), ('KES', 'KES'), ('MNT', 'MNT'), ('DEM', 'DEM'), ('PEI', 'PEI'), ('XSU', 'XSU'), ('HTG', 'HTG'), ('OMR', 'OMR'), ('NOK', 'NOK'), ('SRD', 'SRD'), ('AED', 'AED'), ('TTD', 'TTD'), ('CRC', 'CRC'), ('RSD', 'RSD'), ('BUK', 'BUK'), ('ESP', 'ESP'), ('AOK', 'AOK'), ('HRD', 'HRD'), ('UYP', 'UYP'), ('VED', 'VED'), ('PKR', 'PKR'), ('MZM', 'MZM'), ('VNN', 'VNN'), ('TJR', 'TJR'), ('GWE', 'GWE'), ('STN', 'STN'), ('FIM', 'FIM'), ('CZK', 'CZK'), ('SRG', 'SRG'), ('USD', 'USD'), ('BAM', 'BAM'), ('XBA', 'XBA'), ('XBB', 'XBB'), ('XDR', 'XDR'), ('XPT', 'XPT'), ('YUD', 'YUD'), ('ZAR', 'ZAR'), ('BEC', 'BEC'), ('TMM', 'TMM'), ('PGK', 'PGK'), ('CHE', 'CHE'), ('LUL', 'LUL'), ('FKP', 'FKP'), ('MAD', 'MAD'), ('ANG', 'ANG'), ('CUC', 'CUC'), ('ISJ', 'ISJ'), ('PHP', 'PHP'), ('DOP', 'DOP'), ('AON', 'AON'), ('BEL', 'BEL'), ('BDT', 'BDT'), ('THB', 'THB'), ('CHW', 'CHW'), ('ERN', 'ERN'), ('FJD', 'FJD'), ('SAR', 'SAR'), ('CNY', 'CNY'), ('BYB', 'BYB'), ('ISK', 'ISK'), ('ECV', 'ECV'), ('ILS', 'ILS'), ('SHP', 'SHP'), ('MGF', 'MGF'), ('NIO', 'NIO'), ('PLZ', 'PLZ'), ('EGP', 'EGP'), ('RHD', 'RHD'), ('KRW', 'KRW'), ('YUN', 'YUN'), ('XBC', 'XBC'), ('BRR', 'BRR'), ('BOB', 'BOB'), ('NPR', 'NPR'), ('USS', 'USS'), ('BGL', 'BGL'), ('PTE', 'PTE'), ('SUR', 'SUR'), ('MYR', 'MYR'), ('KZT', 'KZT'), ('LTT', 'LTT'), ('CSD', 'CSD'), ('PYG', 'PYG'), ('KRO', 'KRO'), ('UAK', 'UAK'), ('SLL', 'SLL'), ('MGA', 'MGA'), ('ATS', 'ATS'), ('MCF', 'MCF'), ('DZD', 'DZD'), ('BOV', 'BOV'), ('ZWL', 'ZWL'), ('NAD', 'NAD'), ('LAK', 'LAK'), ('ESB', 'ESB'), ('ESA', 'ESA'), ('RWF', 'RWF'), ('IQD', 'IQD'), ('PAB', 'PAB'), ('MOP', 'MOP'), ('COU', 'COU'), ('ECS', 'ECS'), ('HNL', 'HNL'), ('ILP', 'ILP'), ('GNS', 'GNS'), ('MZN', 'MZN'), ('YDD', 'YDD'), ('UGX', 'UGX'), ('CVE', 'CVE'), ('SSP', 'SSP'), ('XFU', 'XFU'), ('CSK', 'CSK'), ('TPE', 'TPE'), ('XAG', 'XAG'), ('ARA', 'ARA'), ('AWG', 'AWG'), ('XAU', 'XAU'), ('YER', 'YER'), ('UZS', 'UZS'), ('MXP', 'MXP'), ('JMD', 'JMD'), ('XPD', 'XPD'), ('UGS', 'UGS'), ('LSL', 'LSL'), ('XCD', 'XCD'), ('AFA', 'AFA'), ('EUR', 'EUR'), ('KMF', 'KMF'), ('ARS', 'ARS'), ('ALL', 'ALL'), ('MRU', 'MRU'), ('LVL', 'LVL'), ('BRB', 'BRB'), ('GWP', 'GWP'), ('BOL', 'BOL'), ('LRD', 'LRD'), ('XRE', 'XRE'), ('JPY', 'JPY'), ('MVR', 'MVR'), ('KWD', 'KWD'), ('PEN', 'PEN'), ('BRC', 'BRC'), ('VEB', 'VEB'), ('SVC', 'SVC'), ('ARP', 'ARP'), ('SKK', 'SKK'), ('ITL', 'ITL'), ('ARL', 'ARL'), ('NZD', 'NZD'), ('RUR', 'RUR'), ('BOP', 'BOP'), ('GHS', 'GHS'), ('BAD', 'BAD'), ('CNH', 'CNH'), ('ILR', 'ILR'), ('DKK', 'DKK'), ('CLF', 'CLF'), ('UAH', 'UAH'), ('AMD', 'AMD'), ('MTP', 'MTP'), ('SOS', 'SOS'), ('MAF', 'MAF'), ('ROL', 'ROL'), ('STD', 'STD'), ('XEU', 'XEU'), ('AUD', 'AUD'), ('PLN', 'PLN'), ('LKR', 'LKR'), ('SYP', 'SYP'), ('DDM', 'DDM'), ('TRY', 'TRY'), ('GRD', 'GRD'), ('MTL', 'MTL'), ('ZMK', 'ZMK'), ('XPF', 'XPF'), ('MMK', 'MMK'), ('BRZ', 'BRZ'), ('TMT', 'TMT'), ('MKN', 'MKN'), ('XUA', 'XUA'), ('ZMW', 'ZMW'), ('LUC', 'LUC'), ('BRE', 'BRE'), ('BTN', 'BTN'), ('XXX', 'XXX'), ('AFN', 'AFN'), ('VES', 'VES'), ('XFO', 'XFO'), ('HKD', 'HKD'), ('YUM', 'YUM'), ('ZAL', 'ZAL'), ('SIT', 'SIT'), ('RUB', 'RUB'), ('TRL', 'TRL'), ('KGS', 'KGS'), ('KPW', 'KPW'), ('AZN', 'AZN'), ('LUF', 'LUF'), ('GIP', 'GIP'), ('HUF', 'HUF'), ('WST', 'WST'), ('SDD', 'SDD'), ('KRH', 'KRH'), ('LTL', 'LTL'), ('BND', 'BND'), ('NGN', 'NGN'), ('CAD', 'CAD'), ('LVR', 'LVR'), ('JOD', 'JOD'), ('MXV', 'MXV'), ('SGD', 'SGD'), ('ZRN', 'ZRN'), ('ETB', 'ETB'), ('GTQ', 'GTQ'), ('ZRZ', 'ZRZ'), ('MWK', 'MWK'), ('MKD', 'MKD'), ('VEF', 'VEF'), ('MVP', 'MVP'), ('NIC', 'NIC'), ('IRR', 'IRR'), ('ALK', 'ALK'), ('CDF', 'CDF'), ('CHF', 'CHF'), ('KHR', 'KHR'), ('BRN', 'BRN'), ('BRL', 'BRL'), ('CLE', 'CLE'), ('GMD', 'GMD'), ('MRO', 'MRO'), ('USN', 'USN'), ('TZS', 'TZS'), ('MZE', 'MZE'), ('XAF', 'XAF'), ('EEK', 'EEK'), ('MDL', 'MDL'), ('XBD', 'XBD'), ('SEK', 'SEK'), ('BIF', 'BIF'), ('BGM', 'BGM'), ('MXN', 'MXN'), ('TND', 'TND'), ('IDR', 'IDR'), ('MLF', 'MLF'), ('AZM', 'AZM'), ('CYP', 'CYP'), ('UYU', 'UYU'), ('GNF', 'GNF'), ('TWD', 'TWD'), ('FRF', 'FRF'), ('KYD', 'KYD'), ('BGO', 'BGO'), ('ARM', 'ARM'), ('SCR', 'SCR'), ('BSD', 'BSD'), ('BWP', 'BWP'), ('INR', 'INR'), ('RON', 'RON'), ('SDP', 'SDP'), ('CLP', 'CLP'), ('BBD', 'BBD'), ('SDG', 'SDG'), ('CNX', 'CNX'), ('ZWD', 'ZWD'), ('BAN', 'BAN'), ('MDC', 'MDC'), ('ZWR', 'ZWR'), ('YUR', 'YUR'), ('LYD', 'LYD'), ('BYN', 'BYN'), ('BZD', 'BZD'), ('BEF', 'BEF'), ('SBD', 'SBD'), ('VUV', 'VUV'), ('IEP', 'IEP'), ('DJF', 'DJF'), ('ADP', 'ADP'), ('HRK', 'HRK'), ('VND', 'VND'), ('BYR', 'BYR'), ('BMD', 'BMD'), ('COP', 'COP'), ('GQE', 'GQE')], default='USD', max_length=3),
        ),
    ]
