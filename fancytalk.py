#!/usr/bin/env python3

from random import *

seed(1)

translation = ""

#terms

how = [" according unto what ", " after what precedent ", " by means of " , " by virtue of what " , " by what means ", " by what method ", " from what source ", " through what agency ", " through what medium ", " unto what degree ", " whence ", " whereby ", " wherewith "]

who = [" whom "]

the = [" thee "]

them = [" those folk " ]

you = [" thou "]

your = [" thine ", " thy "]

yours = [" thines ", " thys "]

doing = [" accomplishing ", " achieving ", " acting "]

does = [" suffice ", " avail ", " doest "]

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

fancy = [" elegant", " lavish"]

talk = [" eloquent ", " orate "]

talking = [" eloquenting ", " orating "]

made = [" composed ", " formulated "]

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

like = [" fancy ", " relish ", " delight in ", " revel in "]

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

method = [" modus operandi ", " apparatus "]

advanced = [" foremost "]

high = [" soaring ", " altitudinous "]

it = [" 't "]

other = [" divergent ", " dissimilar "]

base = [" essential ", " fundamental part ", " underpinning "]

did = [" satisfy "]

find = [" acquisition ", " procure ", " distinguish "]

found = [" acquisitioned ", " procured ", " distinguished "]

finding = [" acquisitioning ", " procuring ", " distinguishing "]

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

getting = [" procuring ", " appropriating ", " assimilating "]

infinite = [" interminably "]

choose = [" predestine ", " commit oneself "]

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
		translation = translation.replace(" skill" ,skill[randint(0 , len(skill)-1)])

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
		translation = translation.replace(" like " ,like[randint(0 , len(like)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" enjoy " ,like[randint(0 , len(like)-1)])

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
		translation = translation.replace(" application" ,thing[randint(0 , len(thing)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" program" ,thing[randint(0 , len(thing)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" fancy" ,fancy[randint(0 , len(fancy)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" talk " ,talk[randint(0 , len(talk)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" speak " ,talk[randint(0 , len(talk)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" talking " ,talking[randint(0 , len(talking)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" made " ,made[randint(0 , len(made)-1)])

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
		translation = translation.replace(" a lot " ,much[randint(0 , len(much)-1)])

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
		translation = translation.replace(" pick " ,choose[randint(0 , len(choose)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" select " ,choose[randint(0 , len(choose)-1)])

	for x in range(0, len(translation)):
		translation = translation.replace(" decide " ,choose[randint(0 , len(choose)-1)])

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

