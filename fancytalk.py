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

hey = [" ciao ", " regards ", " compliments ", " hail "]

also = [" along with ", " as a consequence ", " furthermore ", " moreover ", " including ", " likewise "]

andw = [" along with ", " as a consequence ", " furthermore ", " moreover ", " including ", " likewise "]

some = [" part of "]

one = [" peculiarly ", " particularly ", " solitarily "]

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

work = [" endeavor", " perform", " function"]

want = [" desire", " covet", " long", " lust", " yearn"]

need = [" require "]

needs = [" requires "]

needing = [" requiring "]

so = [" thus ", " of which "]

going = [" ensueing ", " developing "]



good = [" optimal ", " valorous "]

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

fun = [" gratification ", " enchanting ", " pleasant "]

power = [" ascendancy ", " imperium ", " omnipotence " ]

sure = [" doubtless ", " incontrovertible ", " indubitable " ]

this = [" aforementioned ", " previously mentioned "]

cool = [" ostentatious ", " dapper ", " a la mode "]

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

much = [" exuberance ", " profuseness "]

quiet = [" reticent ", " whist "]

about = [ " apropos ", " in respect unto " ]

on = [" adjacent "]

be = [" abide ", " endure ", " beest "]

being = [" abiding ", " enduring "]

there = [" thither "]

smart = [" resourceful "]

sorry = [" contrite "]

hear = [" auscultate ", " heareth "]

enjoy = [" relish ", " delight in ", " revel in "]

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

people = [" multitude "]

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

can = [" may ", " could ", " be capable of ", " commit "]

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

accept = [" acquiesce "]

see = [" discern "]

event = [" conjuncture ", " ceremony "]

events = [" conjunctures ", " ceremonies "]

bad = [" inadequate "]

rude = [" peremptory "]

polite = [" affable "]

kin = [" kinsfolk ", " lineage ", " consanguinity ", " kindred "]

story = [" anecdote ", " spiel ", " fable ", " legend ", " apologue ", " allegory "]

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




#Main

while(True):
	translation = input(": ")

	translation = " "+translation+" "

#translate

	for x in range(0, len(translation)):
		translation = translation.replace(" mean" ,mean[randint(0 , len(mean)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" and " ,andw[randint(0 , len(andw)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" also " ,also[randint(0 , len(also)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" some " ,some[randint(0 , len(some)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" any " ,some[randint(0 , len(some)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" one " ,one[randint(0 , len(one)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" every " ,every[randint(0 , len(every)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" not " ,notw[randint(0 , len(notw)-1)])



	for x in range(0, len(translation)):
		translation = translation.replace(" yes " ,yes[randint(0 , len(yes)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" new " ,new[randint(0 , len(new)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" old " ,old[randint(0 , len(old)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" skill " ,skill[randint(0 , len(skill)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" skilled " ,skilled[randint(0 , len(skilled)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" had " ,had[randint(0 , len(had)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" correct " ,correct[randint(0 , len(correct)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" true " ,correct[randint(0 , len(correct)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" today " ,today[randint(0 , len(today)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" know " ,know[randint(0 , len(know)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" knowing " ,knowing[randint(0 , len(knowing)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" work" ,work[randint(0 , len(work)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" try" ,work[randint(0 , len(work)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" attempt" ,work[randint(0 , len(work)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" want" ,want[randint(0 , len(want)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" enjoy " ,enjoy[randint(0 , len(enjoy)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" like " ,enjoy[randint(0 , len(enjoy)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" would" ,want[randint(0 , len(want)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" need " ,need[randint(0 , len(need)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" needs " ,needs[randint(0 , len(needs)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" needing " ,needing[randint(0 , len(needing)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" no " ,no[randint(0 , len(no)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" so " ,so[randint(0 , len(so)-1)])


	for x in range(0, len(translation)):
		translation = translation.replace(" how " ,how[randint(0 , len(how)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" who " ,who[randint(0 , len(who)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" the " ,the[randint(0 , len(the)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" they " ,them[randint(0 , len(them)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" them " ,them[randint(0 , len(them)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" you " ,you[randint(0 , len(you)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" your " ,your[randint(0 , len(your)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" their " ,your[randint(0 , len(your)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" yours " ,yours[randint(0 , len(yours)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" theirs " ,yours[randint(0 , len(yours)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" doing " ,doing[randint(0 , len(doing)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" hey " ,hey[randint(0 , len(hey)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" hi " ,hey[randint(0 , len(hey)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" hello " ,hey[randint(0 , len(hey)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" good " ,good[randint(0 , len(good)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" nice " ,good[randint(0 , len(good)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" polite " ,polite[randint(0 , len(polite)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" going " ,going[randint(0 , len(going)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" fix " ,fix[randint(0 , len(fix)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" repair " ,fix[randint(0 , len(fix)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" fixes " ,fixes[randint(0 , len(fixes)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" repairs " ,fixes[randint(0 , len(fixes)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" fixed " ,fixed[randint(0 , len(fixed)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" repaired " ,fixed[randint(0 , len(fixed)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" saying " ,saying[randint(0 , len(saying)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" does " ,does[randint(0 , len(does)-1)])	

	for x in range(0, len(translation)):
		translation = translation.replace(" do " ,do[randint(0 , len(do)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" thing " ,thing[randint(0 , len(thing)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" application " ,thing[randint(0 , len(thing)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" program " ,thing[randint(0 , len(thing)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" fancy " ,fancy[randint(0 , len(fancy)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" talk " ,talk[randint(0 , len(talk)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" speak " ,talk[randint(0 , len(talk)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" talking " ,talking[randint(0 , len(talking)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" made " ,made[randint(0 , len(made)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" created " ,made[randint(0 , len(made)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" make " ,make[randint(0 , len(make)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" create " ,make[randint(0 , len(make)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" making " ,making[randint(0 , len(making)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" creating " ,making[randint(0 , len(making)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" bored " ,bored[randint(0 , len(bored)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" boring " ,boring[randint(0 , len(boring)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" am " ,am[randint(0 , len(am)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" happy " ,happy[randint(0 , len(happy)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" glad " ,happy[randint(0 , len(happy)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" look " ,look[randint(0 , len(look)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" looking " ,looking[randint(0 , len(looking)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" think " ,think[randint(0 , len(think)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" new " ,new[randint(0 , len(new)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" friend" ,friend[randint(0 , len(friend)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" up " ,up[randint(0 , len(up)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" more " ,more[randint(0 , len(more)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" word" ,word[randint(0 , len(word)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" language" ,word[randint(0 , len(word)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" able " ,able[randint(0 , len(able)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" fun " ,fun[randint(0 , len(fun)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" sure " ,sure[randint(0 , len(sure)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" this " ,this[randint(0 , len(this)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" cool " ,cool[randint(0 , len(cool)-1)])
	
	for x in range(0, len(translation)):
		translation = translation.replace(" are " ,are[randint(0 , len(are)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" is " ,are[randint(0 , len(are)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" basic" ,basic[randint(0 , len(basic)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" normal" ,basic[randint(0 , len(basic)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" best" ,best[randint(0 , len(best)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" issue" ,issue[randint(0 , len(issue)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" test " ,test[randint(0 , len(test)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" testing " ,testing[randint(0 , len(testing)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" example" ,example[randint(0 , len(example)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" chat " ,chat[randint(0 , len(chat)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" chatting " ,chatting[randint(0 , len(chatting)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" very " ,very[randint(0 , len(very)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" thank " ,thank[randint(0 , len(thank)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" happen " ,happen[randint(0 , len(happen)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" happening " ,happening[randint(0 , len(happening)-1)])


	for x in range(0, len(translation)):
		translation = translation.replace(" should " ,should[randint(0 , len(should)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" must " ,should[randint(0 , len(should)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" now " ,now[randint(0 , len(now)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" time " ,time[randint(0 , len(time)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" pointless" ,pointless[randint(0 , len(pointless)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" petty" ,pointless[randint(0 , len(pointless)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" read" ,read[randint(0 , len(read)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" go " ,go[randint(0 , len(go)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" goes " ,goes[randint(0 , len(goes)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" lie " ,lie[randint(0 , len(lie)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" cheat " ,cheat[randint(0 , len(cheat)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" learn" ,learn[randint(0 , len(learn)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" much " ,much[randint(0 , len(much)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" quiet " ,quiet[randint(0 , len(quiet)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" silent " ,quiet[randint(0 , len(quiet)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" about " ,about[randint(0 , len(about)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" on " ,on[randint(0 , len(on)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" be " ,be[randint(0 , len(be)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" being " ,being[randint(0 , len(being)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" there " ,there[randint(0 , len(there)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" smart " ,smart[randint(0 , len(smart)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" sorry " ,sorry[randint(0 , len(sorry)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" hear " ,hear[randint(0 , len(hear)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" favorite " ,favorite[randint(0 , len(favorite)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" food " ,food[randint(0 , len(food)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" having " ,having[randint(0 , len(having)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" tedious " ,tedious[randint(0 , len(tedious)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" repeatative " ,tedious[randint(0 , len(tedious)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" for " ,forw[randint(0 , len(forw)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" yesterday " ,yesterday[randint(0 , len(yesterday)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" confuse " ,confuse[randint(0 , len(confuse)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" confused " ,confused[randint(0 , len(confused)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" confusing " ,confusing[randint(0 , len(confusing)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" use " ,use[randint(0 , len(use)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" using " ,using[randint(0 , len(using)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" gratz " ,gratz[randint(0 , len(gratz)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" congratulations " ,gratz[randint(0 , len(gratz)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" likely " ,likely[randint(0 , len(likely)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" probably " ,likely[randint(0 , len(likely)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" my " ,my[randint(0 , len(my)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" that " ,that[randint(0 , len(that)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" will " ,will[randint(0 , len(will)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" only " ,only[randint(0 , len(only)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" just " ,only[randint(0 , len(only)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" great " ,great[randint(0 , len(great)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" well " ,well[randint(0 , len(well)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" alright " ,well[randint(0 , len(well)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" quite " ,quite[randint(0 , len(quite)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" people " ,people[randint(0 , len(people)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" went " ,went[randint(0 , len(went)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" gone " ,went[randint(0 , len(went)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" unto " ,to[randint(0 , len(to)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" then " ,then[randint(0 , len(then)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" i " ,i[randint(0 , len(i)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" me " ,i[randint(0 , len(i)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" why " ,why[randint(0 , len(why)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" put " ,put[randint(0 , len(put)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" self " ,selfw[randint(0 , len(selfw)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" pants " ,pants[randint(0 , len(pants)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" oh " ,oh[randint(0 , len(oh)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" always " ,always[randint(0 , len(always)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" method " ,method[randint(0 , len(method)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" way " ,method[randint(0 , len(method)-1)])


	for x in range(0, len(translation)):
		translation = translation.replace(" advanced " ,advanced[randint(0 , len(advanced)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" high " ,high[randint(0 , len(high)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" it " ,it[randint(0 , len(it)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" other " ,other[randint(0 , len(other)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" different " ,other[randint(0 , len(other)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" base " ,base[randint(0 , len(base)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" did " ,did[randint(0 , len(did)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" find " ,find[randint(0 , len(find)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" locate " ,find[randint(0 , len(find)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" found " ,found[randint(0 , len(found)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" finding " ,finding[randint(0 , len(finding)-1)])
	
	for x in range(0, len(translation)):
		translation = translation.replace(" discover " ,find[randint(0 , len(find)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" discovered " ,found[randint(0 , len(found)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" discovering " ,finding[randint(0 , len(finding)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" life " ,life[randint(0 , len(life)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" existance " ,life[randint(0 , len(life)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" wait " ,wait[randint(0 , len(wait)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" waiting " ,waiting[randint(0 , len(waiting)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" move " ,move[randint(0 , len(move)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" moving " ,moving[randint(0 , len(moving)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" win " ,win[randint(0 , len(win)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" won " ,won[randint(0 , len(won)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" reward " ,reward[randint(0 , len(reward)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" prize " ,reward[randint(0 , len(reward)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" almost " ,almost[randint(0 , len(almost)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" clothes " ,clothes[randint(0 , len(clothes)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" around " ,around[randint(0 , len(around)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" infinite " ,infinite[randint(0 , len(infinite)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" forever " ,infinite[randint(0 , len(infinite)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" choose " ,choose[randint(0 , len(choose)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" choice " ,choice[randint(0 , len(choice)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" pick " ,choose[randint(0 , len(choose)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" select " ,choose[randint(0 , len(choose)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" decide " ,choose[randint(0 , len(choose)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" decision " ,choice[randint(0 , len(choice)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" can " ,can[randint(0 , len(can)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" we " ,we[randint(0 , len(we)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" us " ,we[randint(0 , len(we)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" tell " ,tell[randint(0 , len(tell)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" meet " ,meet[randint(0 , len(meet)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" again " ,again[randint(0 , len(again)-1)])


	for x in range(0, len(translation)):
		translation = translation.replace(" seems " ,seems[randint(0 , len(seems)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" too " ,too[randint(0 , len(too)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" late " ,late[randint(0 , len(late)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" where " ,where[randint(0 , len(where)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" has " ,has[randint(0 , len(has)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" rich " ,rich[randint(0 , len(rich)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" wealthy " ,rich[randint(0 , len(rich)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" happened " ,happened[randint(0 , len(happened)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" place " ,place[randint(0 , len(place)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" location " ,place[randint(0 , len(place)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" get " ,get[randint(0 , len(get)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" gain " ,get[randint(0 , len(get)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" got " ,got[randint(0 , len(got)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" gained " ,got[randint(0 , len(got)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" but " ,but[randint(0 , len(but)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" quick " ,quick[randint(0 , len(quick)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" fast " ,quick[randint(0 , len(quick)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" quicker " ,quicker[randint(0 , len(quicker)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" quickly " ,quicker[randint(0 , len(quicker)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" faster " ,quicker[randint(0 , len(quicker)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" maybe " ,maybe[randint(0 , len(maybe)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" exactly " ,exactly[randint(0 , len(exactly)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" convert " ,convert[randint(0 , len(convert)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" translate " ,convert[randint(0 , len(convert)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" understand " ,know[randint(0 , len(know)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" comprehend " ,know[randint(0 , len(know)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" explain " ,explain[randint(0 , len(explain)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" explanation " ,explanation[randint(0 , len(explanation)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" suppose " ,suppose[randint(0 , len(suppose)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" supposed " ,supposed[randint(0 , len(supposed)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" getting " ,getting[randint(0 , len(getting)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" better " ,better[randint(0 , len(better)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" become " ,become[randint(0 , len(become)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" becoming " ,becoming[randint(0 , len(becoming)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" became " ,became[randint(0 , len(became)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" before " ,before[randint(0 , len(before)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" after " ,after[randint(0 , len(after)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" least " ,least[randint(0 , len(least)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" most " ,most[randint(0 , len(most)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" large " ,large[randint(0 , len(large)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" big " ,large[randint(0 , len(large)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" huge " ,large[randint(0 , len(large)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" small " ,small[randint(0 , len(small)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" little " ,small[randint(0 , len(small)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" tiny " ,small[randint(0 , len(small)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" upgrade " ,upgrade[randint(0 , len(upgrade)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" improve " ,upgrade[randint(0 , len(upgrade)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" improvement " ,upgrade[randint(0 , len(upgrade)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" upgrades " ,upgrades[randint(0 , len(upgrades)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" improvements " ,upgrades[randint(0 , len(upgrades)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" upgraded " ,upgraded[randint(0 , len(upgraded)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" improved " ,upgraded[randint(0 , len(upgraded)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" add " ,add[randint(0 , len(add)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" remove " ,remove[randint(0 , len(remove)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" subtract " ,remove[randint(0 , len(remove)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" similar " ,similar[randint(0 , len(similar)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" like2 " ,similar[randint(0 , len(similar)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" accept " ,accept[randint(0 , len(accept)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" admit " ,accept[randint(0 , len(accept)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" agree " ,accept[randint(0 , len(accept)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" see " ,see[randint(0 , len(see)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" event " ,event[randint(0 , len(event)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" events " ,events[randint(0 , len(events)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" bad " ,bad[randint(0 , len(bad)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" rude " ,rude[randint(0 , len(rude)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" polite " ,polite[randint(0 , len(polite)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" kin " ,kin[randint(0 , len(kin)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" family " ,kin[randint(0 , len(kin)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" story " ,story[randint(0 , len(story)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" wealth " ,wealth[randint(0 , len(wealth)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" amount " ,amount[randint(0 , len(amount)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" chunk " ,amount[randint(0 , len(amount)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" volume " ,amount[randint(0 , len(amount)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" lot " ,amount[randint(0 , len(amount)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" joke " ,joke[randint(0 , len(joke)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" joking " ,joking[randint(0 , len(joking)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" kidding " ,joking[randint(0 , len(joking)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" jokingly " ,jokingly[randint(0 , len(jokingly)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" kiddingly " ,jokingly[randint(0 , len(jokingly)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" quit " ,quit[randint(0 , len(quit)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" quiting " ,quiting[randint(0 , len(quiting)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" begin " ,begin[randint(0 , len(begin)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" start " ,begin[randint(0 , len(begin)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" beginning " ,beginning[randint(0 , len(beginning)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" starting " ,beginning[randint(0 , len(beginning)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" say " ,say[randint(0 , len(say)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" saying " ,saying[randint(0 , len(saying)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" said " ,said[randint(0 , len(said)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" tell " ,tell[randint(0 , len(tell)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" told " ,told[randint(0 , len(told)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" guess " ,guess[randint(0 , len(guess)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" guessing " ,guessing[randint(0 , len(guessing)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" here " ,here[randint(0 , len(here)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" lack " ,lack[randint(0 , len(lack)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" absence " ,lack[randint(0 , len(lack)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" lacking " ,lacking[randint(0 , len(lacking)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" absent " ,lacking[randint(0 , len(lacking)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" fair " ,fair[randint(0 , len(fair)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" honest " ,honest[randint(0 , len(honest)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" even " ,even[randint(0 , len(even)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" done " ,done[randint(0 , len(done)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" things " ,things[randint(0 , len(things)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" ask " ,ask[randint(0 , len(ask)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" asking " ,asking[randint(0 , len(asking)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" asked " ,asked[randint(0 , len(asked)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" full " ,full[randint(0 , len(full)-1)])














#punctuations

	for x in range(0, len(translation)):
		translation = translation.replace(" ." ,".")

	for x in range(0, len(translation)):
		translation = translation.replace(" ," ,",")

	for x in range(0, len(translation)):
		translation = translation.replace(" !" ,"!")

	for x in range(0, len(translation)):
		translation = translation.replace(" ?" ,"?")

	print("/ "+translation)

