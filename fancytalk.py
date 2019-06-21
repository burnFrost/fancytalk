#!/usr/bin/env python3

from random import *

seed(1)

translation = ""

#terms

how = [" according unto what ", " after what precedent ", " by means of " , " by virtue of what " , " by what means ", " by what method ", " from what source ", " through what medium ", " unto what degree ", " whence ", " whereby ", " wherewith "]

who = [" whom "]

the = [" thee "]

them = [" those folk " ]

you = [" thou "]

your = [" thine ", " thy "]

yours = [" thines ", " thys "]

doing = [" accomplishing ", " achieving ", " acting "]

does = [" suffice ", " avail "]

do = [" transact ", " conclude "]

mean = [" imply", " express"]

hey = [" salutations ", " regards ", " compliments ", " hail "]

also = [" along with ", " as a consequence ", " furthermore ", " moreover ", " including ", " likewise "]

andw = [" along with ", " as a consequence ", " furthermore ", " moreover ", " including ", " likewise "]

some = [" part of "]

one = [" peculiar ", " particular ", " solitary "]

every = [" each one ", " without exception "]

notw = [" nay "]

no = [" nay "]

yes = [" beyond a doubt ", " by all means ", " naturally ", " indubitably "]

new = [" au courant ", " contemporary ", " neoteric "]

old = [" along in years ", " venerable ", " geriatric "]

skill = [" proficiency ", " adeptness "]

skilled = [" proficient ", " adept "]

had = [" included ", " embraced "]

correct = [" appropriate ", " proper "]

today = [" presently "]

know = [" fathom ", " discern ", " perceive "]

knowing = [" fathoming ", " discerning ", " perceiving "]

work = [" endeavor ", " perform ", " function "]

working = [" endeavoring ", " performing ", " functioning "]

want = [" desire", " covet", " long", " lust", " yearn"]

need = [" require "]

needs = [" requires "]

needing = [" requiring "]

so = [" thus ", " of which "]

going = [" ensueing ", " developing "]



good = [" valorous "]

fix = [" rectify ", " remedy "]

fixes = [" rectifications ", " remedies "]

fixed = [" rectified ", " remedied "]

saying = [" expressing ", " affirming ", " conveying "]

thing = [" means "]

fancy = [" elegant ", " lavish "]

talk = [" eloquent ", " orate "]

talking = [" eloquenting ", " orating "]

made = [" composed ", " formulated "]

make = [" compose ", " formulate "]

making = [" composing ", " formulating "]

bored = [" disinterested "]

boring = [" platitudinous ", " interminable "]

am = [" grow ", " inhabit ", " befall ", " occur ", " transpire " ]

happy = [" ecstatic ", " elated ", " jubilant "]

look = [" admire ", " peer ", " behold "]

looking = [" admiring ", " peering ", " beholding "]

think = [" contemplate ", " muse "]

new = [" contemporary ", " dissimilar ", " au courant "]

friend = [" familiar", " common"]

up = [" proceeding ", " a phenomenon ", " a milestone "]

more = [" amassed ", " bounteous ", " aggrandized "]

word = [" dialect"]

able = [" endowed ", " fitted ", " adequated "]

power = [" ascendancy ", " imperium ", " omnipotence " ]

sure = [" doubtless ", " incontrovertible ", " indubitable " ]

this = [" aforementioned ", " previously mentioned "]

cool = [" ostentatious ", " keen ", " sensational ", " a la mode "]

are = [" art "]

basic = [" essential"]

best = [" capital", " primo", " choice", " paramount"]

issue = [" matter", " contention"]

test = [" evaluation ", " inquiry ", " inspection " ]

testing = [" evaluating ", " inquiring ", " inspecting " ]

example = [" exemplification", " citation", " instance", " case in point"]

chat = [" prattle "]

chatting = [" prattling "]

very = [" profoundly ", " exceedingly ", " extraordinarily ", " astonishingly ", " emphatically "]

thank = [" be obliged unto "]

happen = [" eventuate ", " proceed ", " betide "]

happens = [" eventuates ", " proceeds ", " betides "]

happened = [" eventuated ", " proceeded ", " betided "]

happening = [" eventuating ", " proceeding ", " betiding "]

should = [ " entertain ", " suffer ", " fall on "]


now = [" at thee trice "]

time = [" instance of trice "]

pointless = [" frivolous", " inessential"]

read = [" unravel"]

go = [" ensue ", " progress ", " bid ", " pop "]

goes = [" ensues ", " progresses ", " bids ", " pops "]

lie = [" prevaricate ", " delude "]

cheat = [" beguile ", " swindle "]

learn = [" ascertain", " discern"]

much = [" exuberantly ", " profusely "]

quiet = [" reticent ", " whist "]

about = [ " apropos ", " in respect unto " ]

on = [" adjacent "]

be = [" abide ", " endure ", " beest "]

being = [" abiding ", " enduring "]

there = [" thither "]

smart = [" resourceful "]

sorry = [" contrite "]

hear = [" auscultate ", " heareth "]

enjoy = [" relish ", " delight in ", " revel in ", " gratify "]

enjoyable = [" gratifying ", " enchanting ", " pleasant "]

enjoyment = [" gratification "]

similar = [" akin "]

favorite = [" cherished ", " choice ", " revered "]

food = [" comestible ", " viand "]

having = [" being compelled unto ", " entertaining "]

tedious = [" enervating ", " soporific "]

forw = [" beneficial unto ", " concerning ", " conductive unto ", " in contemptation of ", " with regard unto ", " with respect unto "]

yesterday = [" foretime "]

confuse = [" perplex ", " perturb ",]

confused = [" perplexed ", " perturbed "]

confusing = [" perplexing ", " perturbing "]

use = [" utilize ", " employ ", " adopt ", " apply "]

using = [" utilizing ", " employing ", " applying "]

gratz = [" complimentations on thine achievement "]

likely = [" presumptively "]

my = [" mine own "]

that = [" yond "]

will = [" shall "]

only = [" merely "]

great = [" most wondrous ", " exceptional ", " superb "]

well = [" sufficiently ", " adequately ", " properly "]

quite = [" considerably ", " without reservation ", " in all respects "]

person = [" lowborn "]

people = [" lowborns "]

went = [" departed ", " decamped "]

to = [" unto "]

then = [" thus ", " therefore ", " hence "]

i = [" thines truly "]

why = [" wherefore "]

put = [" rivet ", " consign ", " subject "]

selfw = [" individuality "]

pants = [" britches "]

oh = [" alas ", " woe "]

always = [" at each moment ", " perpetually ", " everlastingly ", " forevermore ", " in perpetuum ", " unceasingly "]

method = [" modus operandi "]

advanced = [" foremost "]

high = [" soaring ", " altitudinous "]

it = [" 't "]

other = [" divergent ", " dissimilar "]

base = [" essential ", " fundamental part ", " underpinning "]

did = [" satisfy "]

find = [" acquisition ",  " distinguish "]

found = [" acquisitioned ", " distinguished "]

finding = [" acquisitioning ", " distinguishing "]

life = [" continuance "]

wait = [" interim ", " foresee ", " tarry ", " hold onto thine hat "]

waiting = [" interiming ", " foreseeing ", " tarrying ", " holding onto thine hat "]

move = [" persuade ", " inspire ", " excite "]

moving = [" persuading ", " inspiring ", " exciting "]

win = [" triumph "]

won = [" achieved "]

reward = [" endowment", " conferment", " guerdon", " spoil"]

almost = [" nigh ", " well-nigh "]

around = [" encompassing "]

clothes = [" raiments "]

getting = [" reaping ", " appropriating ", " assimilating "]

infinite = [" interminably "]

choose = [" predestine ", " commit oneself "]

choice = [" volition " ]

can = [" may ", " be capable of ", " commit "]

we = [" our own selves "]

tell = [" acquaint ", " apprise " ] 

meet = [" rendezvous ", " foregather ", " convene " ]

again = [" reiteratively "]

seems = [" occurs "]

too = [" exorbitantly "]

late = [" unpunctual "]

where = [" unto what venue "]

has = [" fall upon "]

rich = [" opulent "]

happened = [" befallen "]

place = [" venue "]

get = [ " reap ", " appropriate ", " assimilate " ] 

got = [ " reaped ", " appropriated ", " assimilated " ] 

but = [" nevertheless "]

quick = [" expeditious ", " presto ", " in short order "]

quicker = [" expeditiously ", " hastily "]

maybe = [" perchance ", " conceivably ", " weather permitting "]

exactly = [" precisely "]

convert = [" appropriate "]

explain = [" convey ", " elucidate "]

explanation = [" elucidation "]

suppose = [" presume "]

supposed = [" presumed "]

getting = [" reaping ", " appropriating ", " assimilating "]

better = [" ameliorate ", " sophisticated ", " exceptional "]

become = [" metamorphose ", " harmonize ", " embellish "]

becoming = [" metamorphosing to ", " harmonizing to ", " embellishing to "]

became = [" metamorphosed to ", " harmonized to ", " embellished to "]

before = [" antecedent to ", " preceding "]

after = [" subsequently ", " ensuing "]

least = [" feeblest "]

most = [" utmost ", " highest degree "]

large = [" exorbitant ", " generous ", " considerable "]

small = [" inadequate ", " inconsequential ", " diminutive ", " humble "]

upgrade = [" enrich ", " ameliorate "]

upgrades = [" enrichments ", " ameliorates " ]

upgraded = [" enriched ", " ameliorated "]

add = [" append "]

remove = [" expel "]

bet = [" parlay "]

accept = [" acquiesce ", " sympathize "]

accepted = [" acquiesced ", " sympathized "]

see = [" discern "]

event = [" conjuncture ", " ceremony "]

events = [" conjunctures ", " ceremonies "]

bad = [" inadequate "]

rude = [" peremptory "]

polite = [" affable "]

kin = [" lineage ", " consanguinity ", " kindred "]

story = [" anecdote ", " spiel ", " apologue ", " allegory "]

wealth = [" luxuriance ", " affluence "]

amount = [" magnitude ", " expanse ", " passel "]

joke = [" quip "]

joking = [" facetious "]

jokingly = [" facetiously "]

quit = [" relinquish "]

quiting = [" relinquishing "]

begin = [" commence "]

beginning = [" commencement ", " genesis "]

say = [" express "]

saying = [" expressing "]

said = [" aforementioned "]

tell = [" apprise "]

told = [" apprised "]

guess = [" conjecture "]

guessing = [" conjecturing "]

here = [" hither "]

lack = [" exiguity "]

lacking = [" exiguous "]

fair = [" honorable "]

honest = [" virtuous "]

even = [" conceivably "]

done = [" concluded "]

things = [" occurrences "]

ask = [" inquire "]

asking = [" inquiring "]

asked = [" inquired "]

full = [" abounding "]

crystal = [" lucent "]

clean = [" limpid "]

check = [" audit "]

out = [" superficially "]

worker = [" peasant "]

workers = [" peasants "]

many = [" abounding "]

luck = [" fortune "]

over = [" aloft "]

dare = [" strife ", " contention "]

update = [" refurbish "]

updates = [" renovations "]

phrase = [" expression "]

phrases = [" verbiage "]

none = [" nil "]

allw = [" ensemble "]

morning = [" dawn ", " sunrise "]

noon = [" meridian ", " noontide "]

night = [" nightfall ", " dusk ", " twilight "]

effort = [" resolution "]

currently = [" in aforementioned juncture "]

moment = [" trice "]

suggest = [" propose "]

suggested = [ " proposed "]

suggestion = [" proposition "]

parent = [" antecedent "]

father = [" begetter "]

mother = [" forebearer "]

child = [" bairn "]

double = [" duple "]

triple = [" trine ", " treble "]

camera = [" daguerreotype "]

cup = [" chalice "]

nextw = [" subsequent "]


#functions




def change(text, words, translate):
	for x in range(0, len(translate)):
		translate = translate.replace(text ,words[randint(0 , len(words)-1)])
	return translate


#Main

while(True):
	translation = input(": ")

	translation = " "+translation+" "

#fix

	for x in range(0, len(translation)):
		translation = translation.replace("n't " ," nay ")

	for x in range(0, len(translation)):
		translation = translation.replace("'re " ," art ")

	for x in range(0, len(translation)):
		translation = translation.replace("'m " ," am ")

#translate

	translation = change(" mean", mean, translation)

	translation = change(" and ", andw, translation)

	translation = change(" also ", also, translation)

	translation = change(" some ", some, translation)

	translation = change(" any ", some, translation)

	translation = change(" one ", one, translation)

	translation = change(" every ", every, translation)

	translation = change(" not ", notw, translation)

	translation = change(" yes ", yes, translation)

	translation = change(" new ", new, translation)

	translation = change(" old ", old, translation)

	translation = change(" skill ", skill, translation)

	translation = change(" skilled ", skilled, translation)

	translation = change(" had ", had, translation)

	translation = change(" correct ", correct, translation)

	translation = change(" true ", correct, translation)

	translation = change(" today ", today, translation)

	translation = change(" know ", know, translation)

	translation = change(" knowing ", knowing, translation)

	translation = change(" work ", work, translation)

	translation = change(" working ", working, translation)

	translation = change(" try ", work, translation)

	translation = change(" trying ", working, translation)

	translation = change(" attempt ", work, translation)

	translation = change(" attempting ", working, translation)

	translation = change(" want ", want, translation)

	translation = change(" would ", want, translation)

	translation = change(" like2 ", enjoy, translation)

	translation = change(" enjoy ", enjoy, translation)

	translation = change(" enjoyable ", enjoyable, translation)

	translation = change(" enjoyment ", enjoyment, translation)

	translation = change(" need ", need, translation)

	translation = change(" needs ", needs, translation)

	translation = change(" needing ", needing, translation)

	translation = change(" no ", no, translation)

	translation = change(" needing ", needing, translation)

	translation = change(" so ", so, translation)

	translation = change(" how ", how, translation)

	translation = change(" who ", who, translation)

	translation = change(" the ", the, translation)

	translation = change(" they ", them, translation)

	translation = change(" them ", them, translation)

	translation = change(" you ", you, translation)

	translation = change(" your ", your, translation)

	translation = change(" their ", your, translation)

	translation = change(" yours ", yours, translation)

	translation = change(" doing ", doing, translation)

	translation = change(" hey ", hey, translation)

	translation = change(" hi ", hey, translation)

	translation = change(" hello ", hey, translation)

	translation = change(" good ", good, translation)

	translation = change(" nice ", good, translation)

	translation = change(" polite ", polite, translation)

	translation = change(" going ", going, translation)

	translation = change(" fix ", fix, translation)

	translation = change(" repair ", fix, translation)

	translation = change(" fixes ", fixes, translation)

	translation = change(" repairs ", fixes, translation)

	translation = change(" fixed ", fixed, translation)

	translation = change(" repaired ", fixed, translation)

	translation = change(" saying ", saying, translation)

	translation = change(" does ", does, translation)

	translation = change(" do ", do, translation)

	translation = change(" thing ", thing, translation)

	translation = change(" application ", thing, translation)

	translation = change(" program ", thing, translation)

	translation = change(" fancy ", fancy, translation)

	translation = change(" talk ", talk, translation)

	translation = change(" speak ", talk, translation)

	translation = change(" talking ", talking, translation)

	translation = change(" speaking ", talking, translation)

	translation = change(" made ", made, translation)

	translation = change(" make ", make, translation)

	translation = change(" create ", make, translation)

	translation = change(" created ", made, translation)

	translation = change(" making ", making, translation)

	translation = change(" creating ", making, translation)

	translation = change(" bored ", bored, translation)

	translation = change(" boring ", boring, translation)

	translation = change(" am ", am, translation)

	translation = change(" happy ", happy, translation)

	translation = change(" glad ", happy, translation)

	translation = change(" look ", look, translation)

	translation = change(" looking ", looking, translation)

	translation = change(" think ", think, translation)

	translation = change(" new ", new, translation)

	translation = change(" friend", friend, translation)

	translation = change(" up ", up, translation)

	translation = change(" more ", more, translation)

	translation = change(" word", word, translation)

	translation = change(" language", word, translation)

	translation = change(" able ", able, translation)

	translation = change(" fun ", enjoyable, translation)

	translation = change(" sure ", sure, translation)

	translation = change(" this ", this, translation)

	translation = change(" cool ", cool, translation)

	translation = change(" are ", are, translation)

	translation = change(" is ", are, translation)

	translation = change(" basic", basic, translation)

	translation = change(" normal", basic, translation)

	translation = change(" best ", best, translation)

	translation = change(" issue", issue, translation)

	translation = change(" test ", test, translation)

	translation = change(" testing ", testing, translation)

	translation = change(" example ", example, translation)

	translation = change(" chat ", chat, translation)

	translation = change(" chatting ", chatting, translation)

	translation = change(" very ", very, translation)

	translation = change(" thank ", thank, translation)

	translation = change(" happen ", happen, translation)

	translation = change(" happens ", happens, translation)

	translation = change(" happened ", happened, translation)

	translation = change(" happening ", happening, translation)

	translation = change(" should ", should, translation)

	translation = change(" must ", should, translation)

	translation = change(" now ", now, translation)

	translation = change(" time ", time, translation)

	translation = change(" pointless ", pointless, translation)

	translation = change(" petty ", pointless, translation)

	translation = change(" go ", go, translation)

	translation = change(" goes ", goes, translation)

	translation = change(" lie ", lie, translation)

	translation = change(" cheat ", cheat, translation)

	translation = change(" learn ", learn, translation)

	translation = change(" much ", much, translation)

	translation = change(" really ", much, translation)

	translation = change(" quiet ", quiet, translation)

	translation = change(" silent ", quiet, translation)

	translation = change(" about ", about, translation)

	translation = change(" on ", on, translation)

	translation = change(" be ", be, translation)

	translation = change(" being ", being, translation)

	translation = change(" there ", there, translation)

	translation = change(" smart ", smart, translation)

	translation = change(" sorry ", sorry, translation)

	translation = change(" hear ", hear, translation)

	translation = change(" favorite ", favorite, translation)

	translation = change(" food ", food, translation)

	translation = change(" having ", having, translation)

	translation = change(" tedious ", tedious, translation)

	translation = change(" repeatative ", tedious, translation)

	translation = change(" for ", forw, translation)

	translation = change(" yesterday ", yesterday, translation)

	translation = change(" confuse ", confuse, translation)

	translation = change(" confused ", confused, translation)

	translation = change(" confusing ", confusing, translation)

	translation = change(" use ", use, translation)

	translation = change(" gratz ", gratz, translation)

	translation = change(" congratulations ", gratz, translation)

	translation = change(" likely ", likely, translation)

	translation = change(" probably ", likely, translation)

	translation = change(" my ", my, translation)

	translation = change(" that ", that, translation)

	translation = change(" will ", will, translation)

	translation = change(" only ", only, translation)

	translation = change(" just ", only, translation)

	translation = change(" great ", great, translation)

	translation = change(" well ", well, translation)

	translation = change(" alright ", well, translation)

	translation = change(" quite ", quite, translation)

	translation = change(" person ", person, translation)

	translation = change(" people ", people, translation)

	translation = change(" went ", went, translation)

	translation = change(" gone ", went, translation)

	translation = change(" unto ", to, translation)

	translation = change(" then ", then, translation)

	translation = change(" i ", i, translation)

	translation = change(" me ", i, translation)

	translation = change(" why ", why, translation)

	translation = change(" put ", put, translation)

	translation = change(" self ", selfw, translation)

	translation = change(" pants ", pants, translation)

	translation = change(" oh ", oh, translation)

	translation = change(" always ", always, translation)

	translation = change(" method ", method, translation)

	translation = change(" way ", method, translation)

	translation = change(" advanced ", advanced, translation)

	translation = change(" high ", high, translation)

	translation = change(" it ", it, translation)

	translation = change(" other ", other, translation)

	translation = change(" different ", other, translation)

	translation = change(" base ", base, translation)

	translation = change(" did ", did, translation)

	translation = change(" find ", find, translation)

	translation = change(" locate ", find, translation)

	translation = change(" found ", found, translation)

	translation = change(" finding ", finding, translation)

	translation = change(" discover ", find, translation)

	translation = change(" discovered ", found, translation)

	translation = change(" discovering ", finding, translation)

	translation = change(" life ", life, translation)

	translation = change(" existance ", life, translation)

	translation = change(" wait ", wait, translation)

	translation = change(" waiting ", waiting, translation)

	translation = change(" move ", move, translation)

	translation = change(" moving ", moving, translation)

	translation = change(" win ", win, translation)

	translation = change(" won ", won, translation)

	translation = change(" reward ", reward, translation)

	translation = change(" prize ", reward, translation)

	translation = change(" almost ", almost, translation)

	translation = change(" clothes ", clothes, translation)

	translation = change(" around ", around, translation)

	translation = change(" infinite ", infinite, translation)

	translation = change(" forever ", infinite, translation)

	translation = change(" choose ", choose, translation)

	translation = change(" choice ", choice, translation)

	translation = change(" pick ", choose, translation)

	translation = change(" select ", choose, translation)

	translation = change(" decide ", choose, translation)

	translation = change(" decision ", choice, translation)

	translation = change(" can ", can, translation)

	translation = change(" could ", can, translation)

	translation = change(" we ", we, translation)

	translation = change(" us ", we, translation)

	translation = change(" tell ", tell, translation)

	translation = change(" meet ", meet, translation)

	translation = change(" again ", again, translation)

	translation = change(" seems ", seems, translation)

	translation = change(" too ", too, translation)

	translation = change(" late ", late, translation)

	translation = change(" where ", where, translation)

	translation = change(" has ", has, translation)

	translation = change(" rich ", rich, translation)

	translation = change(" wealthy ", rich, translation)

	translation = change(" happened ", happened, translation)

	translation = change(" place ", place, translation)

	translation = change(" location ", place, translation)

	translation = change(" get ", get, translation)

	translation = change(" obtain ", get, translation)

	translation = change(" gain ", get, translation)

	translation = change(" got ", got, translation)

	translation = change(" obtained ", got, translation)

	translation = change(" gained ", got, translation)

	translation = change(" but ", but, translation)

	translation = change(" quick ", quick, translation)

	translation = change(" fast ", quick, translation)

	translation = change(" quicker ", quicker, translation)

	translation = change(" quickly ", quick, translation)

	translation = change(" faster ", quicker, translation)

	translation = change(" maybe ", maybe, translation)

	translation = change(" exactly ", exactly, translation)

	translation = change(" convert ", convert, translation)

	translation = change(" translate ", convert, translation)

	translation = change(" understand ", know, translation)

	translation = change(" comprehend ", know, translation)

	translation = change(" explain ", explain, translation)

	translation = change(" explanation ", explanation, translation)

	translation = change(" suppose ", suppose, translation)

	translation = change(" supposed ", supposed, translation)

	translation = change(" getting ", getting, translation)

	translation = change(" better ", better, translation)

	translation = change(" become ", become, translation)

	translation = change(" becoming ", becoming, translation)

	translation = change(" became ", became, translation)

	translation = change(" before ", before, translation)

	translation = change(" after ", after, translation)

	translation = change(" least ", least, translation)

	translation = change(" most ", most, translation)

	translation = change(" large ", large, translation)

	translation = change(" big ", large, translation)

	translation = change(" huge ", large, translation)

	translation = change(" small ", small, translation)

	translation = change(" little ", small, translation)

	translation = change(" tiny ", small, translation)

	translation = change(" upgrade ", upgrade, translation)

	translation = change(" improve ", upgrade, translation)

	translation = change(" upgrades ", upgrades, translation)

	translation = change(" improvements ", upgrades, translation)

	translation = change(" upgraded ", upgraded, translation)

	translation = change(" improved ", upgraded, translation)

	translation = change(" add ", add, translation)

	translation = change(" remove ", remove, translation)

	translation = change(" subtract ", remove, translation)

	translation = change(" similar ", similar, translation)

	translation = change(" like ", similar, translation)

	translation = change(" accept ", accept, translation)

	translation = change(" accepted ", accepted, translation)

	translation = change(" add ", add, translation)

	translation = change(" admit ", accept, translation)

	translation = change(" agree ", accept, translation)

	translation = change(" see ", see, translation)

	translation = change(" event ", event, translation)

	translation = change(" events ", events, translation)

	translation = change(" bad ", bad, translation)

	translation = change(" rude ", rude, translation)

	translation = change(" kin ", kin, translation)

	translation = change(" family ", kin, translation)

	translation = change(" brother ", kin, translation)

	translation = change(" bro ", kin, translation)

	translation = change(" sister ", kin, translation)

	translation = change(" sis ", kin, translation)

	translation = change(" story ", story, translation)

	translation = change(" wealth ", wealth, translation)

	translation = change(" amount ", amount, translation)

	translation = change(" chunk ", amount, translation)

	translation = change(" volume ", amount, translation)

	translation = change(" lot ", amount, translation)

	translation = change(" bunch ", amount, translation)

	translation = change(" joke ", joke, translation)

	translation = change(" joking ", joking, translation)

	translation = change(" kidding ", joking, translation)

	translation = change(" jokingly ", jokingly, translation)

	translation = change(" kiddingly ", jokingly, translation)

	translation = change(" quit ", quit, translation)

	translation = change(" quiting ", quiting, translation)

	translation = change(" begin ", begin, translation)

	translation = change(" start ", begin, translation)

	translation = change(" beginning ", beginning, translation)

	translation = change(" starting ", beginning, translation)

	translation = change(" say ", say, translation)

	translation = change(" saying ", saying, translation)

	translation = change(" said ", said, translation)

	translation = change(" tell ", tell, translation)

	translation = change(" told ", told, translation)

	translation = change(" guess ", guess, translation)

	translation = change(" guessing ", guessing, translation)

	translation = change(" here ", here, translation)

	translation = change(" lack ", lack, translation)

	translation = change(" absence ", lack, translation)

	translation = change(" absent ", lacking, translation)

	translation = change(" lacking ", lacking, translation)

	translation = change(" fair ", fair, translation)

	translation = change(" honest ", honest, translation)

	translation = change(" even ", even, translation)

	translation = change(" done ", done, translation)

	translation = change(" things ", things, translation)

	translation = change(" stuff ", things, translation)

	translation = change(" ask ", ask, translation)

	translation = change(" asking ", asking, translation)

	translation = change(" asked ", asked, translation)

	translation = change(" full ", full, translation)

	translation = change(" crystal ", crystal, translation)

	translation = change(" clean ", clean, translation)

	translation = change(" clear ", clean, translation)

	translation = change(" check ", check, translation)

	translation = change(" out ", out, translation)

	translation = change(" worker ", worker, translation)

	translation = change(" workers ", workers, translation)

	translation = change(" many ", many, translation)

	translation = change(" luck ", luck, translation)

	translation = change(" dare ", dare, translation)

	translation = change(" challenge ", dare, translation)

	translation = change(" update ", update, translation)

	translation = change(" updates ", updates, translation)

	translation = change(" phrase ", phrase, translation)

	translation = change(" sentence ", phrase, translation)

	translation = change(" phrases ", phrases, translation)

	translation = change(" sentences ", phrases, translation)

	translation = change(" none ", none, translation)

	translation = change(" all ", allw, translation)

	translation = change(" morning ", morning, translation)

	translation = change(" noon ", noon, translation)

	translation = change(" afternoon ", noon, translation)

	translation = change(" evening ", noon, translation)

	translation = change(" night ", night, translation)

	translation = change(" nite ", night, translation)

	translation = change(" effort ", effort, translation)

	translation = change(" currently ", currently, translation)

	translation = change(" moment ", moment, translation)

	translation = change(" suggest ", suggest, translation)

	translation = change(" suggested ", suggested, translation)

	translation = change(" suggestion ", suggestion, translation)

	translation = change(" parent ", parent, translation)

	translation = change(" father ", father, translation)

	translation = change(" dad ", father, translation)

	translation = change(" mother ", mother, translation)

	translation = change(" mom ", mother, translation)

	translation = change(" child ", child, translation)

	translation = change(" baby ", child, translation)

	translation = change(" double ", double, translation)

	translation = change(" triple ", triple, translation)

	translation = change(" camera ", camera, translation)

	translation = change(" cup ", cup, translation)

	translation = change(" next ", nextw, translation)



#punctuations


	for x in range(0, len(translation)):
		translation = translation.replace(" ." ,".")

	for x in range(0, len(translation)):
		translation = translation.replace(" ," ,",")

	for x in range(0, len(translation)):
		translation = translation.replace(" !" ,"!")

	for x in range(0, len(translation)):
		translation = translation.replace(" ?" ,"?")


	for x in range(0, len(translation)):
		translation = translation.replace(" a a" ," an a")



	print("/ "+translation)


