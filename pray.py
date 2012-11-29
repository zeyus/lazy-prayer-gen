#!/usr/bin/python
import argparse, yaml, random
from sys import exit

parser = argparse.ArgumentParser(description='Pray to your deity you insignificant creation')
parser.add_argument('-v','--verses', help='Number of verses, keep in mind too many will will make it repeat', default=3)
parser.add_argument('-i','--irreverent', help='do not use exif/raw metadata to calculate creation date', default=False, action='store_true')
parser.add_argument('-d', '--deity', help='Choose your deity', default='Yaweh')
parser.add_argument('-p', '--personal', help='Make it personal', default=False,action='store_true')


args = parser.parse_args()

try:
    f = open('well.yaml')
    prayer_well = dict(yaml.load(f))
    f.close()
except Exception:
    exit("Can't read or parse 'well.yaml' file")

if args.personal:
    address = random.choice(prayer_well['fixed']['open']['address']['neuteral']+prayer_well['fixed']['open']['address']['personal'])
    self_ref = 'I'
else:
    address = random.choice(prayer_well['fixed']['open']['address']['neuteral']+prayer_well['fixed']['open']['address']['group'])
    self_ref = 'We'



deity_prefix = random.choice(prayer_well['general']['deity_prefix'])

#if deity_prefix is None:
#    deity_prefix = ''

intro_prefix = random.choice(prayer_well['fixed']['open']['intro_prefix'])
#if intro_prefix is None:
#    intro_prefix = ''


intro_grovel = random.choice(prayer_well['fixed']['open']['intro_grovel'])
#if intro_grovel is None:
#    intro_grovel = ''

intro_grovel_suffix = random.choice(prayer_well['fixed']['open']['intro_grovel_suffix'])



intro_items = (address,deity_prefix,args.deity)
print('%s,\n'%' '.join(part for part in intro_items if part))

if random.randint(1,4) < 4:
    intro_items = (intro_prefix,self_ref,intro_grovel,intro_grovel_suffix)
    print('%s you.'%' '.join(part for part in intro_items if part))



